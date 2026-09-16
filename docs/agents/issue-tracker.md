# Issue tracker: Local Markdown

このリポジトリの Issue と仕様書は `.scratch/` 配下の Markdown ファイルで管理する。

## ファイル構成と更新規約

- 機能ごとに `.scratch/<feature-slug>/` を使用する。
- 仕様書は `.scratch/<feature-slug>/spec.md` に置く。
- 実装 Issue は `.scratch/<feature-slug>/issues/<NN>-<slug>.md` に1件ずつ作成し、`01` から採番する。
- トリアージの状態は Issue 上部の `Status:` 行に記録する。値は `docs/agents/triage-labels.md` に従う。
- コメントと会話履歴は Issue 末尾の `## Comments` に追記する。

## スキルからの操作

「Issue tracker に公開する」は、必要なディレクトリを作成して上記の配置にファイルを書き込むことを指す。

「関連チケットを取得する」は、指定されたパスのファイルを読むことを指す。番号だけの場合は対象機能の `issues/` 内で解決し、複数の候補がある場合は対象を確認する。

## Wayfinder の操作

`/wayfinder` は、作業全体を表す map と、その子チケットを使用する。

- Map: `.scratch/<effort>/map.md`。Notes / Decisions-so-far / Fog を記録する。
- 子チケット: `.scratch/<effort>/issues/<NN>-<slug>.md`。`01` から採番し、本文に調べる問いを書く。
- 種類: 上部の `Type:` 行に `research` / `prototype` / `grilling` / `task` を記録する。
- 状態: Wayfinder の子チケットでは `Status:` に `claimed` / `resolved` を使用する。
- 依存関係: 上部の `Blocked by: NN, NN` 行に依存先を書く。依存先がすべて `resolved` になったら着手可能とする。
- 次の作業: 対象の `issues/` から、未解決・依存関係が解消済み・未着手のチケットを番号順に選ぶ。
- 着手: 作業を始める前に `Status: claimed` を保存する。
- 解決: `## Answer` に回答を追記し、`Status: resolved` に更新する。その後、`map.md` の Decisions-so-far に要点とチケットへのリンクを追記する。
