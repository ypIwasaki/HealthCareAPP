# 06: 項目別の折れ線グラフを表示する

Status: ready-for-agent

**Parent:** 個人向けヘルスケアアプリ初版 — 体重記録と振り返り（healthcare-mvp）

**What to build:** 項目を選んで折れ線グラフを切り替え、初期表示の直近28日で変化を振り返れるようにする。

**Blocked by:** 03: 体重記録を保存し、自動計算付きの一覧で確認する

**対応する完成条件:** AC-08（項目別・直近28日・欠測）

## 完了条件

- [ ] Matplotlib を Qt に埋め込み、体重・体脂肪率・骨格筋率・基礎代謝・BMI・体脂肪量・骨格筋量を切り替えて表示できる。
- [ ] Windows の当日を含む直近28日を表示し、項目名と単位を明示する。
- [ ] 未記録日をゼロ埋め・補間せず線を途切れさせ、記録がない期間でも表示できる。
- [ ] 最新の保存済み記録と有効な換算式から描画する。記録や設定を変更する機能が利用可能な場合、変更後は再取得して更新する。
- [ ] 当日を固定した確認で日付境界・期間外の除外・欠測を検証し、画面でも線の途切れと単位を確認する。

## 共通の完了条件

- [ ] 画面操作から結果表示まで、この Issue の範囲を実際に動作確認し、確認結果を残す。
- [ ] 保存を伴う処理は Controller が呼ぶ共通の公開処理を境界として、一時 SQLite DB で保存・再読み込み・失敗時の保持を検証する。内部の呼び出し回数や SQL 文字列を合否の基準にしない。
- [ ] 変更内容・各部分の役割・コードを読む入口と順番・確認方法を短く文書化する。MVC と専用の保存処理の責任分担を守り、必要な機能だけを増やす。

## Comments

- 2026-09-16: 利用者が承認した13件の分割案に基づき作成。依存先の完了後に着手する。
- 2026-09-16: GitHub Issue 登録先: https://github.com/ypIwasaki/HealthCareAPP/issues/6
- GitHub 依存先: [#3](https://github.com/ypIwasaki/HealthCareAPP/issues/3)。
- GitHub 後続 Issue: [#7](https://github.com/ypIwasaki/HealthCareAPP/issues/7)、[#8](https://github.com/ypIwasaki/HealthCareAPP/issues/8)。
