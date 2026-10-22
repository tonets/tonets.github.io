# Masahito Ohue personal website

PukiWikiの公開ページをHugoへ移行した個人サイトである。PHP・データベースは不要であり、Markdownを編集するとGitHub ActionsがHTMLを生成してGitHub Pagesへ公開する。

## 移行した内容

- 旧サイトの公開コンテンツ43ページ。日本語・英語のプロフィール、研究成果、研究内容、ニュース、研究メモ、その他の公開ページを含む。
- ナビゲーションから到達しない旧ページも、全ページ一覧から閲覧できる。
- 本文内のページリンクを新URLへ変更し、元の見出しアンカーを保存した。
- 使用画像22点と本文で参照する添付画像1点を取り込み、画像表示の旧PukiWikiへの依存を解消した。
- 編集・ログイン画面、システムマニュアル、履歴・バックアップは移行対象外である。
- 本文は取得した旧サイトを基準とし、業績や所属の最新情報への更新は今回行っていない。

## 初回公開

1. GitHubで空の公開リポジトリを作成する。個人の標準URLを使う場合は `<username>.github.io`、プロジェクト用なら `personal-website` などとする。
2. このディレクトリのソースを `main` ブランチへpushする。`.github/workflows/pages.yml` も含める。
3. リポジトリの Settings → Pages → Build and deployment → Source を `GitHub Actions` にする。
4. Actionsの `Deploy Hugo site to GitHub Pages` を実行する。以後は `main` へのpushで自動公開される。
5. 公開URLを `hugo.toml` の `baseURL` に設定する。CIはPagesのURLを自動使用するため、プロジェクト配下のURLにも対応する。

既存の個人サイト用リポジトリがある場合は、その内容を確認してから利用する。履歴の上書きは行わない。

## 日英ページの管理

- 基本情報・所属・連絡先・CV・顔写真は `data/person.json` が共通の参照元である。
- トップページのニュースは `data/news.json` に日本語・英語の要約を対で登録する。
- 業績一覧は `content/publications.md` を一度だけ編集する。英語ページも同じ一覧を参照するため、項目の追加や削除は両言語に反映される。
- 研究内容・受賞の英語ページも、日本語の本文を共通の参照元とする。見出しや説明の英訳は `data/shared_translations.json` で管理する。日本語の新しい説明を追加した際は英訳も追加する。
- プロフィールの経歴・委員歴・教育歴などは日本語・英語それぞれの本文を更新する。
- 日英切替は対応する同じページへ移動する。研究メモや過去の記録など、日本語のみのページは英語メニューで明記している。
- 日本語の論文題名・講演題目などの書誌情報は、英語版でも原題を保持する。

## 画像の管理

`data/images.json` で画像の用途と説明を定義する。アイコン、バッジ、ロゴ、研究図、顔写真を区別し、縦横比を維持した表示サイズを共通CSSで設定する。研究図は最大幅680px・最大高さ420pxを基本とし、狭い画面では利用可能な幅に収める。ロゴは最大幅240px・最大高さ80px、バッジは最大高さ28px、アイコンは20pxの表示枠となる。画像を追加する際は、この定義も更新する。

## 更新方法

GitHubのWeb画面で対象のMarkdownを開き、編集してコミットすれば更新できる。

| 内容 | 編集ファイル |
| --- | --- |
| トップ・最近のニュース | `content/_index.md` |
| プロフィール | `content/profile.md` |
| 研究内容 | `content/research.md` |
| 研究成果 | `content/publications.md` |
| 受賞 | `content/awards.md` |
| 過去のニュース | `content/news.md` |
| 所属希望の方へ | `content/join.md` |
| 英語トップ | `content/en/_index.md` |
| 英語プロフィール | `content/en/profile.md` |
| 英語業績 | `content/en/publications.md` |
| 見た目 | `static/assets/site.css` |

新しい画像は `static/assets/` に置き、Markdownでは `![説明](/assets/filename.png)` と記述する。サイト内リンクは `[プロフィール](/profile/)` のように記述する。GitHub Pagesでサブディレクトリ配下へ公開する場合も、テンプレートがパスを調整する。

## ローカル確認

Hugo 0.168.0（通常版）を用いる。外部テーマ、Node.js、Ruby、Pythonの追加パッケージは不要である。

```sh
hugo server
```

配布ZIPには生成済みの `public/` も含む。Hugoを入れずに表示を確認する場合は、次を実行して `http://localhost:8000/` を開く。

```sh
python3 -m http.server 8000 --directory public
```

生成とリンク検証は次のとおりである。

```sh
hugo --cleanDestinationDir --baseURL https://example.org/
python3 scripts/check_site.py public
```

`baseURL` を `https://example.org/personal-website/` にした生成でも、同じ検証コマンドでサブディレクトリへの公開を確認できる。

## 移行時の留意点

- 元の2025年の顔写真は取得先がHTTP 503を返したため、旧英語ページの既存写真をトップページに使用した。新しい写真へ置換する場合はトップの `portrait` を変更する。
- 研究内容に含まれる旧ロゴ1点は取得先が応答せず、画像名をテキストとして残した。
- 「学生奨励賞」「音楽系雑記」ページにある計4点の画像は、旧サイト自体でFile not foundとなっていたため、取得できていない。
- 旧サイトで未作成のページへの編集用リンク18件は除去し、見えていた項目名は残した。
- 旧サイトの重複アンカー1件を一意に修正した。
- 外部サイト、DropboxのCV・論文ファイルなどは元のリンクを維持しており、その継続公開までは保証しない。
- 旧PukiWikiは変更していない。新サイトの公開後に旧環境の停止を別途実施する必要がある。

`data/migration.json` にページとURL、画像、取得できなかった画像の対応を記録している。本文中のすべての内部リンク・見出しアンカー・画像参照は `scripts/check_site.py` で検証する。

## 権利

移行元の文章・画像の権利は元の権利者に帰属する。サイト全体を一括でオープンソースライセンスに変更していない。
