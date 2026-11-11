# 第三方技能

模板的流程页会提到下面这些技能。它们不是本仓库的一部分，也没有复制进来，请到各自的来源安装，并遵守各自的许可证。没装也不影响库本身，只是对应的步骤要手工做或跳过。

| 技能 | 用在哪里 | 来源 | 备注 |
| --- | --- | --- | --- |
| `humanize-writing` | 英文正文润色，由 `coursework-writing` 调用 | <https://github.com/shir-danishyar/humanize> | MIT |
| `humanizer-zh` | 中文解释和笔记润色 | 作者署名 aizixun；正文提到参考了 <https://github.com/blader/humanizer> | MIT；仓库地址未核实 |
| `ai-text-detection` | 写作检测方面的参考资料，按需读 | 作者署名 nematbayat | MIT；仓库地址未核实 |
| `tdd`、`diagnosing-bugs`、`codebase-design`、`code-review` | 课程代码任务 | Matt Pocock 的技能集 | 地址和许可证未核实，请以上游为准 |
| `agent-reach` | 只读读取各平台内容，可选 | <https://github.com/Panniantong/Agent-Reach> | 许可证以上游为准 |

标了“未核实”的条目，是因为本仓库维护者手里的副本没有记录仓库地址或许可证文件。安装前请自己到上游确认。

## 仓库内包含的第三方内容

`skills/coursework-writing/references/a-reference-excerpt.md` 逐字摘录了 `ai-text-detection` 技能参考文档中的两节（原文为德语）。该技能以 MIT 许可证发布，许可证原文在同目录的 `LICENSE-ai-text-detection`。

## 暂未提供

`coursework-writing` 还会调用一个本地的写作信号统计技能 `ai-writing-signal-audit`，这一版没有随仓库提供。没有它时跳过信号审计那一步，并在核验表里写明没做。
