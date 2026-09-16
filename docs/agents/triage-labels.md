# Triage labels

5つの標準トリアージ役割を、ローカル Issue の `Status:` に記録する文字列へ対応付ける。

| スキル内の役割 | このリポジトリでの値 | 意味 |
| --- | --- | --- |
| `needs-triage` | `needs-triage` | メンテナーによる評価待ち |
| `needs-info` | `needs-info` | 報告者からの追加情報待ち |
| `ready-for-agent` | `ready-for-agent` | 仕様が整い、エージェントが実装できる |
| `ready-for-human` | `ready-for-human` | 人による実装が必要 |
| `wontfix` | `wontfix` | 対応しない |

スキルが役割を指定したら、この表の対応する値を使う。ラベル名を変更する場合は「このリポジトリでの値」を更新する。

Wayfinder の子チケットの状態は `issue-tracker.md` の「Wayfinder の操作」に従う。
