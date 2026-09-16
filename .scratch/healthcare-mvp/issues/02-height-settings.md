# 02: 初期設定で身長を登録・変更する

Status: ready-for-agent

**Parent:** 個人向けヘルスケアアプリ初版 — 体重記録と振り返り（healthcare-mvp）

**What to build:** 初回に身長を登録し、後から設定画面で変更できるようにする。設定は Windows PC 内の DB に保存し、再起動後も利用できる。

**Blocked by:** 01: Windows で最小アプリを起動する

**対応する完成条件:** AC-02（設定）、AC-04（身長入力）

## 完了条件

- [ ] 身長を cm・小数第1位までで登録・変更できる。
- [ ] 空欄・非数値・非有限値・0以下・精度超過を拒否し、理由を表示する。入力を黙って丸めない。
- [ ] 身長は10倍した整数として保存し、接続を開き直しても同じ値を取得できる。
- [ ] キャンセル・保存失敗で保存済み設定が変わらない。
- [ ] SQLite DB を Windows ユーザーのアプリデータ領域に置き、実行ファイル・ソースから分離する。DB 形式の版を管理する。

## 共通の完了条件

- [ ] 画面操作から結果表示まで、この Issue の範囲を実際に動作確認し、確認結果を残す。
- [ ] 保存を伴う処理は Controller が呼ぶ共通の公開処理を境界として、一時 SQLite DB で保存・再読み込み・失敗時の保持を検証する。内部の呼び出し回数や SQL 文字列を合否の基準にしない。
- [ ] 変更内容・各部分の役割・コードを読む入口と順番・確認方法を短く文書化する。MVC と専用の保存処理の責任分担を守り、必要な機能だけを増やす。

## Comments

- 2026-09-16: 利用者が承認した13件の分割案に基づき作成。依存先の完了後に着手する。
- 2026-09-16: GitHub Issue 登録先: https://github.com/ypIwasaki/HealthCareAPP/issues/2
- GitHub 依存先: [#1](https://github.com/ypIwasaki/HealthCareAPP/issues/1)。
- GitHub 後続 Issue: [#3](https://github.com/ypIwasaki/HealthCareAPP/issues/3)。
