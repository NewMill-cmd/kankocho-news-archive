"""Build a static archive from explicitly public CSVs. Standard library only."""
import csv
import io
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
PATTERN = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2})(?:[_.-][A-Za-z0-9_.-]+)?\.csv\Z')


def spreadsheet_text(value):
    # Quoting CSV alone does not prevent spreadsheet formula interpretation.
    probe = value.lstrip(' \t\r\n\ufeff')
    if probe.startswith(('=', '+', '-', '@', '＝', '＋', '－', '＠')) or value.startswith(('\t', '\r', '\n')):
        return "'" + value
    return value


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copyfile(ROOT / 'index.html', OUT / 'index.html')
    files = []
    for region in ('jp', 'us', 'eu', 'other'):
        folder = ROOT / 'data' / region
        if not folder.exists():
            continue
        if folder.is_symlink():
            raise ValueError('Symlink folders are not allowed')
        for source in sorted(folder.glob('*.csv')):
            match = PATTERN.fullmatch(source.name)
            if source.is_symlink() or not match:
                raise ValueError('Use YYYY-MM-DD.csv or YYYY-MM-DD_suffix.csv; no symlinks')
            day = match['date']
            date.fromisoformat(day)
            if source.stat().st_size > 20 * 1024 * 1024:
                raise ValueError('CSV exceeds the 20 MiB archive limit')
            raw = source.read_text(encoding='utf-8-sig')
            rows = list(csv.reader(io.StringIO(raw), strict=True))
            if not rows or not rows[0] or any(len(r) != len(rows[0]) for r in rows):
                raise ValueError('CSV needs a header and consistent column counts')
            result = io.StringIO(newline='')
            writer = csv.writer(result)
            writer.writerows([spreadsheet_text(cell) for cell in row] for row in rows)
            payload = result.getvalue().encode('utf-8-sig')
            relative = Path('data') / region / source.name
            target = OUT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            files.append(dict(path=relative.as_posix(), region=region, date=day,
                              name=source.name, rows=len(rows)-1, bytes=len(payload)))
    files.sort(key=lambda f: (f['date'], f['region'], f['name']), reverse=True)
    (OUT / 'manifest.json').write_text(json.dumps({'files': files}, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT / '.nojekyll').touch()
    print(f'Built archive: {len(files)} CSV file(s)')


if __name__ == '__main__':
    build()
