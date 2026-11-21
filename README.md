# experience-to-class-followup

馆校招募、课程开班、邀请授权及竞争去向。 其中人物代号、机构、交易及历史回执均为合成资料。

## 数据约定

`data/layout.json` 逐一解释业务表及 CSV 列顺序，`data/rules.json` 记录运营口径。CSV 使用 UTF-8、首行为列名；空白字段表示未提供或不适用，`+` 隔开多值字段。历史记录的业务时刻与送交时刻含义不同，按各表说明解释。

- `cohorts.csv`：事前分配、入口、候选课程和明示联络授权。
- `courses.csv`：课程开放日历与共享组。组内名额不是各课程相加，组容量另表规定。
- `quota.csv`：每个共享班型的总资源上限。
- `events.csv`：记录取得时刻晚于业务发生时刻；switched 行的 class 为目的课。
- `commitments.csv`：邀请通知和班位实际接受状态；有效期用自然日。
- `identity_candidates.csv`：两个入口发现的可匹配记录，同一个候选组必须共同求可相容身份；confirmed 优先。
- `opening_changes.csv`：课程规则可部分变更，场地再次开放不撤销学员的拒收意思。

## 本地检查

使用 Python 3.11 及标准库。`python3 inspect_inputs.py` 读取原始资料并列出记录数；`python3 -m unittest discover -s tests` 检查输入资料。检查不计算或发布业务结论。
