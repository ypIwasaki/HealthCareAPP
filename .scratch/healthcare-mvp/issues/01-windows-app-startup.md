# 01: Windows で最小アプリを起動する

Status: ready-for-agent

Completion: completed (2026-09-16)

**Parent:** 個人向けヘルスケアアプリ初版 — 体重記録と振り返り（healthcare-mvp）

**What to build:** 日本語の最小ウィンドウを Windows のアイコンから開いて終了できるようにし、配布用ビルドを再現する手順を残す。

**Blocked by:** None (can start immediately)

**対応する完成条件:** AC-01、AC-12（最小起動の範囲）

## 完了条件

- [x] Python・PySide6 の Qt Widgets を使った最小ウィンドウを日本語で表示できる。
- [x] Windows 上で PyInstaller により実行ファイルを作り、アイコンから起動・終了できる。
- [x] 日常利用時に WSL・開発用端末・別途インストールした Python を必要としない。
- [x] 必要なバージョンの互換性を確認して固定し、Windows でのビルド・起動確認手順と結果を残す。

## 共通の完了条件

- [x] 画面操作から結果表示まで、この Issue の範囲を実際に動作確認し、確認結果を残す。
- [x] 保存を伴う処理は Controller が呼ぶ共通の公開処理を境界として、一時 SQLite DB で保存・再読み込み・失敗時の保持を検証する。内部の呼び出し回数や SQL 文字列を合否の基準にしない。（本 Issue は保存処理なしのため対象外。）
- [x] 変更内容・各部分の役割・コードを読む入口と順番・確認方法を短く文書化する。MVC と専用の保存処理の責任分担を守り、必要な機能だけを増やす。

## Comments

- 2026-09-16: 利用者が承認した13件の分割案に基づき作成。依存先の完了後に着手する。
- 2026-09-16: GitHub Issue 登録先: https://github.com/ypIwasaki/HealthCareAPP/issues/1
- GitHub 依存先: なし。
- GitHub 後続 Issue: [#2](https://github.com/ypIwasaki/HealthCareAPP/issues/2)。
- 2026-09-16: 依存先なしを確認して実装。Python 3.12.14 / PySide6 6.11.2 / PyInstaller 6.22.3 を固定。起動境界の TDD、型チェック、全テスト、Windows ビルド、アイコン起動と終了の実画面確認を実施。手順・結果・コードの読む順番は [Windows 起動手順](../../../docs/windows-startup.md) を参照。保存処理は対象外。Status はトリアージ分類を保持し、完了は Completion とチェックリストで記録。変更はローカルのみ。
- 2026-09-16: 実装コミット `548c11e` を作業開始時点 `6b5232a` と比較して code-review を実施。Standards 0件、Spec 0件。外部への push・Issue 更新は行っていない。
