# 官公庁ニュース CSVアーカイブ / Public Agency News CSV Archive

ライブで検出した官公庁・公的機関の公式発表を、日付・地域別のCSVで公開する非公式アーカイブです。

## English

An independent, unofficial CSV archive of public-agency announcements collected during our livestreams, covering Japan, the United States and Europe.

- [Browse in English](https://NewMill-cmd.github.io/kankocho-news-archive/?lang=en) / [日本語](https://NewMill-cmd.github.io/kankocho-news-archive/?lang=ja)
- Select a date and region, or search filenames, then choose **Download CSV**. Downloads are free; CSV contents are not translated by the website.
- [Watch our livestreams](https://www.youtube.com/@kankocho_news/streams). The international stream uses English headlines and narration. Use `Research: NASA` or `Question: What does this mean?` to participate. Type `!japanese` for a Japanese explanation of the current announcement; English resumes afterwards. The Japan stream is in Japanese.
- Collection dates can differ from publication dates. Coverage is incomplete, and AI summaries or translations can contain errors. Check the official source URLs and each publisher’s reuse terms. We are not affiliated with any government or public agency.
- [Optional support via note (Japanese)](https://note.com/deep_whale2807/n/n5b1f9439e282) mainly helps cover the OpenAI API used for questions and translation. The archive remains free.

The interface supports 日本語 / English. A `?lang=` URL takes priority over the saved choice and browser language. Switching languages keeps your filters and does not alter CSV files. No external translation service or analytics is used by this website.

---

公開予定URL： https://NewMill-cmd.github.io/kankocho-news-archive/

## 初回の公開設定

1. Settings → Pages → Build and deployment → Source を **GitHub Actions** に変更。
2. Actions → **Publish CSV archive** → **Run workflow** → main を選択して実行。
3. 成功後、上記URLを開いて確認してください。

## CSVを追加

`data/jp/`（日本）、`data/us/`（米国）、`data/eu/`（欧州）、`data/other/` に `YYYY-MM-DD.csv` を保存。
UTF-8、1行目は列名。詳しくは [data/README.md](data/README.md) を参照。
mainへの更新後、一覧と公開ページは自動生成されます。CSV未登録時は公開準備中と表示します。

ニュース取得ライブのPCからの自動アップロードは、まだ連携していません。

## 公開前の確認

- CSVの内容と列を確認し、APIキー、個人情報、チャット履歴、内部ログを含めない。
- リポジトリ全体が公開されています。公開サイトに含まれないファイルもGitHubから閲覧できます。
- 認証情報を誤公開したら直ちに失効・再発行する。削除のみでは履歴から消えません。
- サイトは外部スクリプト・解析ツールを利用しません。表示には同一サイトの一覧JSONを使います。
- 自動取得のため網羅性を保証しません。要約・翻訳を含む場合は公式発表も確認してください。
- 第三者が再利用する際は、各発表元の利用条件を確認してください。

## ローカル確認

Python 3で `python3 scripts/build.py`、続けて `python3 -m http.server 8000 --directory _site`。
ブラウザーで http://localhost:8000/ を開きます。
