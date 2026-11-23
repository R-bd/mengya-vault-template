# 第三方技能

模板的流程页会提到下面这些技能。它们不是本仓库的一部分，也没有复制进来，请到各自的来源安装，并遵守各自的许可证。没装也不影响库本身，只是对应的步骤要手工做或跳过。

| 技能 | 用在哪里 | 来源 | 许可证 |
| --- | --- | --- | --- |
| `humanize-writing` | 英文正文润色，由 `coursework-writing` 调用 | <https://github.com/shir-danishyar/humanize> | MIT，Copyright (c) 2026 Shirhussain Danishyar |
| `humanizer-zh` | 中文解释和笔记润色，由 `coursework-writing` 和 `class-recording-to-obsidian` 调用 | <https://github.com/ai-zixun/humanizer-zh>（正文提到参考了 <https://github.com/blader/humanizer>） | MIT，Copyright (c) 2026 aizixun |
| `ai-text-detection` | 写作检测方面的参考资料，由 `coursework-writing` 按需读 | <https://github.com/nematbayat/ai-text-detection> | MIT，Copyright (c) 2026 nematbayat |
| `tdd`、`diagnosing-bugs`、`codebase-design`、`code-review` | 课程代码任务，见 `vault/学习笔记/作业与代码项目工作流.md` | <https://github.com/mattpocock/skills>（`skills/engineering/` 下） | MIT，Copyright (c) 2026 Matt Pocock |

以上来源和许可证于 2026-11-23 按各仓库根目录的 `LICENSE` 文件核对。上游以后可能改动，安装前请以当时的仓库为准。`ai-text-detection` 的 README 里许可证一节还是未填写的模板文字，以它的 `LICENSE` 文件为准。

## 仓库内包含的第三方内容

`skills/coursework-writing/references/a-reference-excerpt.md` 逐字摘录了 `ai-text-detection` 技能参考文档中的两节（原文为德语）。该技能以 MIT 许可证发布，许可证原文在同目录的 `LICENSE-ai-text-detection`。

## 暂未提供

`coursework-writing` 还会调用一个本地的写作信号统计技能 `ai-writing-signal-audit`，这一版没有随仓库提供。没有它时跳过信号审计那一步，并在核验表里写明没做。
