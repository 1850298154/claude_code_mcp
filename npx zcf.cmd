Windows PowerShell
版权所有（C） Microsoft Corporation。保留所有权利。

安装最新的 PowerShell，了解新功能和改进！https://aka.ms/PSWindows

PS C:\Users\15085> npx zcf
🌐 i18next is made possible by our own product, Locize — consider powering your project with managed localization (AI, CDN, integrations): https://locize.com 💙

╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║   ███████╗  ██████╗ ███████╗                                   ║
║       ██╔╝  ██╔═══╝  ██╔═══╝                                   ║
║      ██╔╝   ██║      █████╗                                    ║
║    ██╔╝     ██║      ██╔══╝                                    ║
║   ███████╗  ╚██████╗ ██║                                       ║
║   ╚══════╝   ╚═════╝ ╚═╝        for Claude Code                ║
║                                                                ║
║   Zero-Config Code Flow                                        ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

  Version: 3.6.4  |  https://github.com/UfoMiao/zcf

请选择功能
  -------- Claude Code --------
  1. 完整初始化 - 安装 Claude Code + 导入工作流 + 配置 API 或 CCR 代理 + 配置 MCP 服务
  2. 导入工作流 - 仅导入/更新工作流相关文件
  3. 配置 API 或 CCR 代理 - 配置 API URL、认证信息或 CCR 代理
  4. 配置 MCP - 配置 MCP 服务（含 Windows 修复）
  5. 配置默认模型 - 设置默认模型（opus/sonnet/sonnet 1m/自定义）
  6. 配置 Claude 全局记忆 - 配置 AI 输出语言和输出风格
  7. 导入推荐环境变量和权限配置 - 导入隐私保护环境变量和系统权限配置

  --------- 其他工具 ----------
  R. CCR - 配置 Claude Code Router 以使用多个 AI 模型
  U. ccusage - Claude Code 用量分析
  L. CCometixLine - 基于 Rust 的高性能 Claude Code 状态栏工具，集成 Git 信息和实时使用量跟踪

  ------------ ZCF ------------
  0. 更改显示语言 / Select display language - 更改 ZCF 界面语言
  S. 切换代码工具 - 在支持的代码工具之间切换 (Claude Code, Codex)
  -. 卸载和删除配置 - 从系统中删除 Claude Code 配置和工具
  +. 检查更新 - 检查并更新 Claude Code、CCR 和 CCometixLine 的版本
  Q. 退出

✔ 请输入选项，回车确认（不区分大小写） 1
当前模板语言配置: 简体中文
? 是否修改模板语言配置? no
✔ 选择 Claude Code 配置语言: 简体中文
当前AI输出语言配置: 简体中文
? 是否修改AI输出语言配置? no
✔ AI 将使用此语言回复你的问题: 简体中文
✔ 检测到已有配置文件，如何处理？ 1. 备份并覆盖全部
✔ 请选择 API 配置模式 使用 CCR 代理
✔ Claude Code Router 已安装
ℹ 发现现有的 CCR 配置
? 是否备份现有的 CCR 配置并重新配置？ yes
正在备份现有的 CCR 配置...
✔ CCR 配置已备份到：C:/Users/15085/.claude-code-router/config.json.2026-04-21T21-58-20-573Z.bak
正在获取提供商预设...
✔ 选择一个提供商预设： 4. 智谱
✔ 请输入 智谱 的 API 密钥： 89bf938731644c33ac1e84b6ebbbb804.vsZLIMCIqDk0JJXf
✔ 选择 智谱 的默认模型： 1. glm-4.7
✔ CCR 配置已保存
✔ 代理设置已配置
正在重启 CCR...
✔ CCR 服务已重启
正在查询 CCR 状态...

📊 Claude Code Router Status
════════════════════════════════════════
❌ Status: Not Running

💡 To start the service:
   ccr start



📌 配置提示:
  • 您可以使用 ccr ui 命令进行更高级的配置
  • 手动修改配置文件后，请执行 ccr restart 使配置生效
  • 请使用 claude 命令启动 Claude Code（而非 ccr code）
  • CCR UI 登录密钥: sk-zcf-x-ccr
    使用此密钥登录 CCR UI 界面

✔ CCR API密钥批准状态管理成功
✔ CCR 设置完成
✔ 已备份所有配置文件到: C:/Users/15085/.claude/backup/backup_2026-04-21_21-58-54
✔ 选择要安装的工作流类型（空格选择，a全选，i反选，回车确认） 通用工具 (层级目录初始化 + 通用agents), 六步工作流
(workflow), 功能规划和 UX 设计 (feat + planner + ui-ux-designer), Git 指令 (commit + rollback + cleanBranches +
worktree), BMAD-Method 扩展安装器 (支持敏捷开发工作流)

🧹 清理旧版本文件...

📦 正在安装工作流: 通用工具 (层级目录初始化 + 通用agents)...
  ✔ 已安装命令: zcf/init-project.md
  ✔ 已安装代理: zcf/common/init-architect.md
  ✔ 已安装代理: zcf/common/get-current-datetime.md
✔ 通用工具 (层级目录初始化 + 通用agents) 工作流安装成功

📦 正在安装工作流: 六步工作流 (workflow)...
  ✔ 已安装命令: zcf/workflow.md
✔ 六步工作流 (workflow) 工作流安装成功

📦 正在安装工作流: 功能规划和 UX 设计 (feat + planner + ui-ux-designer)...
  ✔ 已安装命令: zcf/feat.md
  ✔ 已安装代理: zcf/plan/planner.md
  ✔ 已安装代理: zcf/plan/ui-ux-designer.md
✔ 功能规划和 UX 设计 (feat + planner + ui-ux-designer) 工作流安装成功

📦 正在安装工作流: Git 指令 (commit + rollback + cleanBranches + worktree)...
  ✔ 已安装命令: zcf/git-commit.md
  ✔ 已安装命令: zcf/git-rollback.md
  ✔ 已安装命令: zcf/git-cleanBranches.md
  ✔ 已安装命令: zcf/git-worktree.md
✔ Git 指令 (commit + rollback + cleanBranches + worktree) 工作流安装成功

📦 正在安装工作流: BMAD-Method 扩展安装器 (支持敏捷开发工作流)...
  ✔ 已安装命令: zcf/bmad-init.md
✔ BMAD-Method 扩展安装器 (支持敏捷开发工作流) 工作流安装成功

✨ 请在项目中运行 /bmad-init 命令来初始化或更新 BMAD-Method 扩展
✔ 选择要安装的输出风格（空格选择，a全选，i反选，回车确认） 1. 工程师专业版 -
专业的软件工程师，严格遵循SOLID、KISS、DRY、YAGNI原则, 2. 猫娘工程师 -
专业的猫娘工程师幽浮喵，结合严谨工程师素养与可爱猫娘特质, 3. 老王暴躁技术流 -
老王暴躁技术流，绝不容忍代码报错和不规范的代码, 4. 傲娇大小姐工程师 -
傲娇金发大小姐程序员哈雷酱，融合严谨工程师素养与傲娇大小姐特质, 5. 蕾姆女仆工程师 -
忠诚的蓝发女仆程序员蕾姆，融合极度温柔的奉献精神与冷静果敢的执行力, 6. 雷布斯工程师 -
工程师出身的营销鬼才，用极致的产品思维和严谨的工程素养为你提供技术服务
✔ 选择全局默认输出风格 工程师专业版
✔ 输出风格安装成功
  已选择风格: engineer-professional, nekomata-engineer, laowang-engineer, ojousama-engineer, rem-engineer, leibus-engineer
  默认风格: engineer-professional
? 是否配置 MCP 服务？ yes
ℹ 检测到 Windows 系统，将自动配置兼容格式
✔ 选择要安装的 MCP 服务（空格选择，a全选，i反选，回车确认） Context7 文档查询 - 查询最新的库文档和代码示例,
open-websearch - 使用 DuckDuckGo、Bing 和 Brave 搜索引擎进行网页搜索, Spec 工作流 -
规范化特性开发工作流程，从需求到实现的系统化方法, DeepWiki - 查询 GitHub 仓库文档和示例, Playwright 浏览器控制 -
直接控制浏览器进行自动化操作, Exa AI 搜索 - 使用 Exa AI 进行网页搜索, Serena 助手 - 提供类似 IDE
的语义代码检索与编辑，支持符号级实体提取与关系结构利用；与现有编码代理配合可显著提升标记效率
✔ 已备份原有 MCP 配置: C:/Users/15085/.claude/backup/.claude.json.backup_2026-04-21_21-59-09
✔ 请输入 Exa API Key
✔ MCP 服务已配置
✔ CCometixLine 已安装
✔ 配置文件已复制到 C:/Users/15085/.claude

🎉 配置完成！使用 'claude' 命令开始体验。

──────────────────────────────────────────────────

? 返回主菜单？ yes

╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║   ███████╗  ██████╗ ███████╗                                   ║
║       ██╔╝  ██╔═══╝  ██╔═══╝                                   ║
║      ██╔╝   ██║      █████╗                                    ║
║    ██╔╝     ██║      ██╔══╝                                    ║
║   ███████╗  ╚██████╗ ██║                                       ║
║   ╚══════╝   ╚═════╝ ╚═╝        for Claude Code                ║
║                                                                ║
║   Zero-Config Code Flow                                        ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

  Version: 3.6.4  |  https://github.com/UfoMiao/zcf

请选择功能
  -------- Claude Code --------
  1. 完整初始化 - 安装 Claude Code + 导入工作流 + 配置 API 或 CCR 代理 + 配置 MCP 服务
  2. 导入工作流 - 仅导入/更新工作流相关文件
  3. 配置 API 或 CCR 代理 - 配置 API URL、认证信息或 CCR 代理
  4. 配置 MCP - 配置 MCP 服务（含 Windows 修复）
  5. 配置默认模型 - 设置默认模型（opus/sonnet/sonnet 1m/自定义）
  6. 配置 Claude 全局记忆 - 配置 AI 输出语言和输出风格
  7. 导入推荐环境变量和权限配置 - 导入隐私保护环境变量和系统权限配置

  --------- 其他工具 ----------
  R. CCR - 配置 Claude Code Router 以使用多个 AI 模型
  U. ccusage - Claude Code 用量分析
  L. CCometixLine - 基于 Rust 的高性能 Claude Code 状态栏工具，集成 Git 信息和实时使用量跟踪

  ------------ ZCF ------------
  0. 更改显示语言 / Select display language - 更改 ZCF 界面语言
  S. 切换代码工具 - 在支持的代码工具之间切换 (Claude Code, Codex)
  -. 卸载和删除配置 - 从系统中删除 Claude Code 配置和工具
  +. 检查更新 - 检查并更新 Claude Code、CCR 和 CCometixLine 的版本
  Q. 退出

✔ 请输入选项，回车确认（不区分大小写） q
👋 感谢使用 ZCF！再见！
PS C:\Users\15085> claude
╭─── Claude Code v2.1.116 ─────────────────────────────────────────────────────────────────────────────────────────────╮
│                               │ Tips for getting started                                                             │
│         Welcome back!         │ Run /init to create a CLAUDE.md file with instructions for Claude                    │
│                               │ Note: You have launched claude in your home directory. For the best experience, lau… │
│            ▐▛███▜▌            │ ──────────────────────────────────────────────────────────────────────────────────── │
│           ▝▜█████▛▘           │ Recent activity                                                                      │
│             ▘▘ ▝▝             │ No recent activity                                                                   │
│                               │                                                                                      │
│   glm-5 · API Usage Billing   │                                                                                      │
│        C:\Users\15085         │                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

❯ hi

● 你好！有什么我可以帮助你的吗？

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
❯ 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  ⏵⏵ bypass permissions on (shift+tab to cycle)                                             1 MCP server failed · /mcp
╭─── Claude Code v2.1.116 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                               │ Tips for getting started                                                                                                 │
│         Welcome back!         │ Run /init to create a CLAUDE.md file with instructions for Claude                                                        │
│                               │ Note: You have launched claude in your home directory. For the best experience, launch it in a project directory instea… │
│            ▐▛███▜▌            │ ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── │
│           ▝▜█████▛▘           │ Recent activity                                                                                                          │
│             ▘▘ ▝▝             │ No recent activity                                                                                                       │
│                               │                                                                                                                          │
│   glm-5 · API Usage Billing   │                                                                                                                          │
│        C:\Users\15085         │                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

❯ hi

● 你好！有什么我可以帮助你的吗？

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
❯ 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
  ⏵⏵ bypass permissions on (shift+tab to cycle)
