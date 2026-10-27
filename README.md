# 官公庁ニュース CSVアーカイブ

ライブで検出した官公庁・公的機関の公式発表を、日付・地域別のCSVで公開する非公式アーカイブです。

公開予定URL： https://nnaoki498-cmd.github.io/kankocho-news-archive/

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
