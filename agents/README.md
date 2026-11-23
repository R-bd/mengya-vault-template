# 子代理

两个只读子代理，主对话把一部分工作派给它们，结果交回主对话，由主对话按库内流程页写入。同一份定义分两种格式，内容一致，改一处要同步另一处。

| 子代理 | 做什么 | 由哪一页调用 |
| --- | --- | --- |
| `course-source-scout` | 课程来源侦察：每次只查一位学习者，核对收件箱、处理状态和课程页，交回“哪门课有什么新来源”的清单 | `vault/学习笔记/课程资料周检-Prompt.md` |
| `coursework-reviewer` | 作业独立复核：按题目、rubric 和来源核对成稿，只报告问题，不改稿 | `vault/学习笔记/作业与代码项目工作流.md` |

## 安装

1. 把文件里的占位符换成你自己的：
   - `<库根目录>`：你的 Obsidian 库的绝对路径。
   - `<技能目录>`：代理工具的技能目录，例如 Codex 的 `~/.codex/skills`。
2. 复制到代理工具的目录：
   - Claude Code：`agents/claude/*.md` 放进 `~/.claude/agents/`。
   - Codex：`agents/codex/*.toml` 放进 `~/.codex/agents/`。
3. 新开一个会话，子代理才会被识别。

## 用法

派子代理时直接说出名字，例如“派两个 course-source-scout，分别查学习者 A 和学习者 B”“用 coursework-reviewer 复核这份作业：成稿……题目……rubric……”。Codex 默认只在明确要求时才指定子代理角色。

## 边界

- Codex 版设了 `sandbox_mode = "read-only"`，写入会被系统拒绝；Claude Code 版只靠 `tools` 限制和说明约束。
- 不同学习者之间的隔离靠说明里的规则，不是技术上的目录权限。
- `coursework-reviewer` 的信号审计一步依赖 `ai-writing-signal-audit`，这一版没有随仓库提供，没装就跳过并在报告里写明。
