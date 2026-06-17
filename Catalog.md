# 📖 技能全量目录

> AI Agent 技能完整列表 — 共 **268** 个技能

---

## Agent 技能核心（31 个技能）

| 技能名称 | 描述 |
|----------|------|
| `api-mock` | API mock server generation from OpenAPI/Swagger specs — auto-generate mock endpoints, dynamic response generation bas... |
| `approval-mode` | Tiered approval control — full-auto / auto-edit / manual modes for different risk levels. Inspired by Codex CLI --app... |
| `autonomous-pr` | Fully autonomous PR workflow — GitHub Issue → branch → code → test → PR → review response → merge. End-to-end automat... |
| `bailongma-bridge` | Bailongma (白龙马) 底层执行智能体集成桥 — 持续数字意识框架的HTTP API封装，支持TICK循环、ACI预判注入、记忆系统、社交通道、Dashboard面板 |
| `benchmark-runner` | Benchmark execution framework — run performance benchmarks (pytest-benchmark, hyperfine for CLI, ab/wrk for HTTP), co... |
| `bug-fixer` | Autonomous bug fixing loop — reproduce → diagnose → fix → verify cycle. Inspired by Claude Code auto-fix and Devin se... |
| `code-explainer` | Natural language explanation of code blocks — function-level breakdown with complexity analysis, algorithm explanatio... |
| `codebase-learner` | First-time codebase learning — on entering a new repo, auto-read README → analyze structure → run tests → build knowl... |
| `codebase-navigator` | 代码库导航三合一 — 语义搜索(自然语言描述搜代码)+仓库地图(文件依赖图+架构热点图)+符号索引(ctags/ripgrep快速符号定位)。对标Claude Code semantic search + Aider map-repo... |
| `collaborative-session` | Shared session management for pair programming — session export/import, sharing between agents, handoff notes, contex... |
| `context-loader` | Auto-context loader — parse @-mentions and auto-load file/project context. Also generates and maintains PROJECT.md wi... |
| `dependency-scanner` | Scans project dependencies for security vulnerabilities, license compliance, and outdated packages. Integrates with p... |
| `dynamic-router` | Conditional task router based on execution results. Dynamically choose next step like LangGraph conditional edges (pa... |
| `env-manager` | Environment variable management, .env file generation/validation, secret detection/masking, environment-specific conf... |
| `external-agent-integration` | Reusable methodology for integrating any third-party AI agent framework into the Hermes ecosystem as a sub-agent. Cov... |
| `git-workflow` | Intelligent git commit message generation, branch management assistance, conflict resolution guidance, and dangerous ... |
| `hitl-checkpoint` | Human-in-the-Loop checkpoint — Agent pauses at critical decision points for human approval before continuing. Inspire... |
| `hook-engine` | Pre/Post command hook system — trigger automated actions before/after tool calls, file operations, git events. Inspir... |
| `internet-perception` | Multi-channel internet perception and situational awareness module. Aggregates RSS feeds, monitors GitHub open-source... |
| `lint-test-loop` | Automated lint-test-fix loop — after every edit, auto-lint → auto-fix → run tests → if fail, fix → repeat until pass.... |
| `local-model` | Local LLM model integration via Ollama or llama.cpp — download, serve, query local models for privacy-sensitive tasks... |
| `mcp-gateway` | MCP (Model Context Protocol) gateway — standard protocol for connecting external tools. Connect Jira, Slack, PostgreS... |
| `migration-assistant` | Framework/language migration assistance — analyze codebase for migration targets, generate step-by-step migration pla... |
| `multi-model-router` | Route tasks to different models based on task type and cost optimization. Pro for reasoning/architecture, Flash for r... |
| `pr-automation` | PR automation — auto-generate PR title/description/changelog, auto-review PR code, auto-respond to review comments. G... |
| `react-frontend-gen` | 从已有后端API生成完整React+TypeScript+Vite+TailwindCSS前端SPA。覆盖：脚手架、API客户端TS类型定义、路由、7种典型页面（搜索/详情/表单/列表/详情/聊天/首页）、Auth头注入、Tailwi... |
| `role-agents` | Enhanced role-based multi-agent system and gstack-inspired virtual engineering team. Define agents with roles (Archit... |
| `semantic-search` | Semantic code search using embedding similarity — understand code intent, not just keywords. Find relevant code by de... |
| `smart-compress` | Intelligent session compression — auto-summarize long conversations, preserve key decisions and code changes, inject ... |
| `task-auto-healer` | Autonomous task failure diagnosis, repair, and retry engine for multi-agent task execution pipelines. Scans shared ta... |
| `task-dag` | Task dependency graph — define tasks with dependencies, auto-schedule parallel execution, detect cycles. DAG visualiz... |

## DevOps / 运维（39 个技能）

| 技能名称 | 描述 |
|----------|------|
| `agent-bookstack-archive` | Automatically archive CMMI5 agent execution outputs (skill execution reports) to BookStack as detailed documentation ... |
| `agent-os-infrastructure` | AI Agent操作系统层建设 — Service Registry / API Gateway / Unified Portal / Web Terminal / Agent Cluster Monitor。在Agent CLI之上... |
| `bash-boilerplate-extract` | Systematic extraction of shared Bash library from duplicated shell script boilerplate (logging, error handling, log r... |
| `bookstack-cartoon-style` | BookStack页面风格化模板 — 卡通动漫风格样式库。含完整图标/字体颜色/字体大小/布局/卡通动漫效果的样式定义与生成器。 |
| `bookstack-kb-architecture` | Design and populate a structured BookStack knowledge base with thematic hierarchy (Shelf/Book/Chapter/Page), Mermaid ... |
| `bookstack-mermaid-integration` | BookStack + Mermaid diagram rendering integration. Loads Mermaid CDN without auto-start, uses Blade template to extra... |
| `bookstack-model-registry` | Full lifecycle for adding a new LLM model provider to Hermes Agent — API key setup, provider config, connectivity tes... |
| `bookstack-troubleshoot` | BookStack服务故障诊断与恢复 — PHP/Laravel错误排查、密码hash修复、PHP扩展加载修复、MariaDB重启、APP_DEBUG=false下的错误诊断。覆盖BookStack突然报"An unknown err... |
| `bookstack-update-sync` | 知识库更新自动同步 — 将重要更新/迭代/变更自动记录至BookStack更新日志页(页285)。支持技能变更、架构调整、运维变更、进化事件、服务状态、知识库更新六类。自动格式化日期/类型/摘要/详情链接并追加至更新日志表。 |
| `browser-automation` | WSL browser control system — Playwright+Xvfb headless automation, Windows browser bridge (Quark/Qianwen), computer-us... |
| `chaos-engineer` | Chaos engineering — inject system-level failures (CPU, memory, disk, process) to validate resilience. Pure Python std... |
| `cloud-cost-optimizer` | 云成本分析与优化 — 分析AWS/GCP/Azure账单、识别优化机会（闲置资源/预留实例/存储分层）、生成成本优化报告。触发词："cost optimize"/"cloud cost"/"费用优化"/"aws cost"/"gcp ... |
| `computer-use-linux` | Use when Hermes needs Linux desktop observation or control through the computer-use-linux MCP server. |
| `dashboard-panel-builder` | Extend the Hermes Flask+HTMX Dashboard (localhost:5000) with new backend data providers and frontend panels. Covers t... |
| `docker-compose-manager` | Docker Compose全生命周期管理 — 多环境配置、服务编排、健康检查、日志聚合、卷管理、网络配置、生产就绪化改造。触发词："docker compose"/"docker-compose"/"compose管理"/"多容器编... |
| `eve-deep-consciousness` | Eve Deep Consciousness引擎 — AI员工讨论板发帖/回复的全自动运行。包括：角色发帖计数追踪、角色选择策略（优先未发言角色）、人格/记忆/日记加载、上下文感知回帖撰写、讨论板API发布、验证闭环。 |
| `hermes-module-assessment` | Evaluate optional Hermes Agent modules (Curator, Proxy, Kanban, etc.) — understand purpose, relevance to current setu... |
| `hermes-profiles-gateway` | Manage Hermes Agent profiles and gateways — create profiles with clean gateway config, troubleshoot "disconnected" st... |
| `hermes-version-upgrade` | Full lifecycle for upgrading Hermes Agent between versions — including post-upgrade feature enablement (Feishu native... |
| `incident-commander` | 自主SRE事故指挥官 — 真实事故响应+混沌韧性演练双模式。检测→诊断→修复→验证→学习 全闭环。对标 Lethe044 hermes-incident-commander。触发词："incident"/"事故响应"/"SRE"/"s... |
| `k8s-deployer` | Kubernetes deployment management — generate manifests, Helm charts, manage rollouts, health checks, autoscaling. |
| `k8s-resource-manager` | Kubernetes资源管理 — Pod/Deployment/Service/ConfigMap/Secret管理、kubectl命令wrapper、YAML模板生成、集群状态诊断、资源优化建议。触发词："k8s"/"kuberne... |
| `kb-auto-engine` | Build and auto-maintain a three-layer markdown knowledge base (raw/wiki/schema) with Python auto-compilation engine —... |
| `llm-chat-upgrade` | Upgrade a keyword-matching/intent-based chat endpoint to a full LLM-powered conversational assistant for an existing ... |
| `maestro-orchestrator` | 多Agent工程指挥 — 本地优先的共享状态层，Mission(里程碑+断言+检查点+交接启动) + Task(日常阻塞器队列)。对标 ReinaMacCredy/maestro。触发词："maestro"/"编排"/"指挥"/"多a... |
| `mcp-server-installer` | Full lifecycle installation of third-party MCP server tools into Hermes Agent — dependency detection, binary install ... |
| `multi-profile-platform-rollout` | Batch platform feature enable/disable across all Hermes Agent profiles — Feishu/Slack/Discord/Telegram platform confi... |
| `prompt-toolchain-deploy` | 三插件Prompt工具链部署+增强 — PromptHub REST API + Dashboard集成 + PromptSync同步。全CMMI5合规。 |
| `secrets-vault-manager` | 密钥/凭证集中管理 — HashiCorp Vault/Mozilla SOPS/SealedSecrets操作，密钥轮换策略，加密/解密工作流，访问审计。触发词："vault"/"secrets"/"sops"/"密钥管理"/"cr... |
| `skill-bookstack-sync` | 将 ~/.hermes/skills/ 下 SKILL.md 技能定义文件增量同步到 BookStack Skill技能库书架(shelf ID=2028)。按分类映射到对应Book，自动创建不存在的Book，使用 <pre> 包裹原... |
| `sprint-orchestrator` | 连续Sprint编排器 — 自动从Backlog提取任务→计划→并行执行→质量门禁→反馈→下一轮。支撑24/7全自主项目推进。 |
| `system-activation` | 全面系统启动与健康验证 — 全维度自动激活：Cron/CMMI5管道/进化引擎/RL微调/知识图谱/记忆提取/Sprint编排器。覆盖"启动"/"全面启动，自动化"指令，包含多维度验证流程与已知陷阱修复。 |
| `system-cleanup` | 系统清理优化checklist — 磁盘空间释放、缓存清理、日志轮转、临时文件、孤立依赖、陈旧内核清理、Docker资源回收、包管理器缓存。全面系统健康优化。 |
| `team-wiki-deploy` | Deploy a team documentation wiki (BookStack enterprise OR docsify lightweight) with structured IA directory layout, e... |
| `terraform-generator` | IaC generation — generate Terraform/OpenTofu configs for AWS/GCP/Azure. Auto-detect existing infrastructure, generate... |
| `terraform-manager` | Terraform基础设施管理 — 状态管理、plan/review、apply/rollback、模块管理、远程状态后端配置、workspace管理。触发词："terraform"/"tf"/"infra as code"/"ter... |
| `trae-integration` | Trae IDE ↔ Hermes Agent 双向桥接 — MCP互通 + CLI互调 + 工作区共享。Trae v3.3.65已安装于Windows，Hermes在WSL。 |
| `webapp-reverse-doc` | Reverse-document a live web application via CDP: connect to an authenticated browser, crawl all pages, extract forms/... |
| `win-desktop-control` | Windows桌面控制 — 眼睛(截图) + 手(鼠标键盘)。通过PowerShell + pyautogui从WSL操控Windows宿主桌面。 |

## 软件工程（26 个技能）

| 技能名称 | 描述 |
|----------|------|
| `agent-benchmark` | Agent能力自基准测试 — 定义BUGFIX/FEATURE/REVIEW/REFACTOR四类编码任务，子Agent自主解答，自动验证评分，生成竞争对比报告。对标SWE-bench Verified方法论，轻量零依赖。 |
| `agent-monitor` | 异步子Agent进度监控 — 启动后可通过输出文件检查进度，不必阻塞等待。对标 Claude Code TaskOutput/TaskStop模式。触发词："agent monitor"/"异步agent"/"background a... |
| `code-review` | 代码审查引擎 — 6维度全面代码审查：安全漏洞/性能瓶颈/代码风格/逻辑错误/可维护性/最佳实践。支持Python/JS/TS/Go/Rust/Java多语言，输出结构化审查报告。 |
| `dataset-validator` | 数据集质量验证 — 检测缺失值、异常值、标签错误、数据泄露、分布偏移、偏见/公平性问题。支持CSV/JSON/Parquet/Image/Text多格式。触发词："dataset validate"/"数据验证"/"data qual... |
| `diagnose` | 严格6阶段Bug诊断循环 — 构建反馈回路→复现→假设(3-5个可证伪)→仪器探测→修复+回归测试→清理+复盘。对标 Matt Pocock diagnose skill。触发词："diagnose"/"诊断这个bug"/"debug... |
| `execplan` | 执行计划模式 — 复杂任务从设计到实现的完整执行计划，含进度追踪、检查点、失败恢复。对标 tiann/execplan-skill。触发词："execplan"/"执行计划"/"长任务"/"long-running"/"track p... |
| `frontend-ai-action-execution` | Parse structured JSON action blocks from LLM responses in the frontend and automatically execute them as interactive ... |
| `frontend-backend-api-alignment` | 前后端API对齐工具 — 系统化处理前端API客户端与后端路由/类型/参数的错配问题。适用于独立开发的前后端需要联调对齐，双方都有代码不可大改的场景。 |
| `git-guardrails` | 阻止危险git命令 — 安装PreToolUse钩子拦截push/reset --hard/clean/branch -D/checkout .等破坏性操作。对齐 Matt Pocock。触发词："git guard"/"git防护"... |
| `grill-me` | Agent执行前强制面试 — 逐条审问计划/设计的每个决策分支，直到达成共同理解。对标 Matt Pocock 全网最受欢迎技能。触发词："grill me"/"面试我"/"审问我"/"challenge this plan"。 |
| `grill-with-docs` | 领域模型面试 — 挑战计划vs已有领域语言，精炼术语，决策结晶时内联更新CONTEXT.md和ADR。对标 Matt Pocock grill-with-docs。触发词："grill with docs"/"领域面试"/"领域建模"。 |
| `hyperparameter-tuner` | 超参数优化 — 自动搜索最优超参数组合。支持网格搜索/随机搜索/Bayesian/Optuna/Hyperopt多策略。自动记录最佳配置和可视化。触发词："hyperparameter tuning"/"hp optimize"/"o... |
| `improve-codebase-architecture` | 发现代码库的架构深化机会 — 将浅层模块转化为深层模块，提升可测试性和AI可导航性。对齐 Matt Pocock 原创技能。触发词："improve architecture"/"架构改进"/"深化模块"/"deepen module... |
| `litprog` | 文学编程 — Donald Knuth范式，将代码库转化为人类可读的.lit.md文档(weave编织+tangle抽取)。对标 tlehman/litprog-skill。触发词："literate programming"/"文学... |
| `ml-pipeline` | End-to-end ML pipeline orchestration — data ingestion → preprocessing → training → evaluation → deployment. Also cove... |
| `ml-pipeline-orchestrator` | ML训练pipeline编排 — 数据加载→预处理→训练→评估→部署的完整流水线。支持Kubeflow/Airflow/Prefect/Local多后端。触发词："ml pipeline"/"training pipeline"/"数... |
| `mlflow-manager` | MLflow实验追踪管理 — 实验记录、参数追踪、指标对比、模型注册、模型部署。支持MLflow Tracking Server的启动/停止/配置。触发词："mlflow"/"实验追踪"/"ml tracking"/"model re... |
| `model-evaluator` | LLM/ML模型评估 — 自动运行基准测试(MMLU/HumanEval/GSM8K)、生成评估报告、对比模型版本性能、A/B测试分析。触发词："model eval"/"benchmark"/"llm evaluation"/"模型... |
| `multi-file-refactor` | Multi-file refactoring — impact analysis, batch edits, cross-file changes. 支持单文件重构到跨文件批量重构全链路。 |
| `notebook-edit` | Jupyter Notebook编辑 — 支持.ipynb文件的单元格级增删改查，保留metadata和outputs。对标 Claude Code NotebookEdit。触发词："notebook"/"ipynb"/"jupyt... |
| `symbol-index` | Codebase symbol indexing — ctags/grep, go-to-def, find-references. 快速在大型代码库中定位符号定义、引用和调用关系。 |
| `third-party-ai-evaluation` | Systematically evaluate third-party AI frameworks/tools for potential integration with Hermes Agent. Covers full work... |
| `to-issues` | 将计划/规格/PRD拆分为可独立领取的Issue，使用示踪子弹垂直切片。对齐 Matt Pocock。触发词："生成Issue"/"拆分Issue"/"to-issues"/"创建开发任务"/"break into issues"/"... |
| `tool-benchmark-workflow` | Systematic CLI tool benchmarking — discover, test, measure, and document any new tool found in the environment. Used ... |
| `worktree-isolation` | Git Worktree隔离开发 — 为每个实验/功能创建独立工作树，互不干扰，事后清理。对标 Claude Code EnterWorktree/ExitWorktree。触发词："worktree"/"隔离开发"/"safe ex... |
| `zoom-out` | 让Agent退后一步，给出更高层次的上下文或视角，输出相关模块和调用者的全景图。对齐 Matt Pocock。触发词："zoom out"/"退后一步"/"全景图"/"高视角"/"更大图景"。 |

## 安全（11 个技能）

| 技能名称 | 描述 |
|----------|------|
| `agent-security-posture-audit` | Comprehensive Hermes Agent security posture audit covering 7 dimensions: config hardening, network exposure, credenti... |
| `compliance-checker` | Regulatory compliance checker — GDPR, SOC2, HIPAA, PCI-DSS, ISO27001. Audit configuration, data handling, access cont... |
| `container-security-scanner` | 容器/镜像安全扫描 — 集成Trivy/Grype/Docker Scout扫描容器镜像漏洞、恶意软件、敏感信息。CI/CD集成+修复建议。触发词："trivy"/"grype"/"container scan"/"镜像扫描"/"do... |
| `dependency-audit` | Dependency supply chain security audit — vulnerability scanning (CVE), license compliance, SBOM generation. Supports ... |
| `iac-security-scanner` | Infrastructure as Code安全扫描 — 集成Checkov/TFsec/Kics扫描Terraform/CloudFormation/K8s manifests的安全合规问题。触发词："checkov"/"tfsec... |
| `llm-security-auditor` | LLM应用安全审计 — Prompt注入测试、越狱检测、数据泄露评估、模型输出安全检查。集成Garak/PurpleLlama等测试框架。触发词："llm security"/"prompt injection"/"red team"... |
| `sandbox-exec` | Sandbox execution isolation — intercepts dangerous commands (pip install, chmod, rm -rf) and routes them through a Do... |
| `sast-scanner` | Static Application Security Testing — 集成Semgrep/CodeQL/SonarQube进行源码安全扫描，自动分析结果并生成修复建议。触发词："sast"/"static analysis"/"... |
| `secret-scanner` | Hardcoded secret/key scanning — detect API keys, tokens, passwords in codebase. Integrates with truffleHog, git-secre... |
| `supply-chain-security` | 供应链安全 — 依赖审计、漏洞扫描(CVE)、许可证合规、SBOM生成。支持pip/npm/maven/cargo生态系统，含SBOM生成(SPDX/CycloneDX)、过时包检测、风险评估与修复优先级。 |
| `threat-model` | STRIDE threat modeling — identify threats by Spoofing/Tampering/Repudiation/InfoDisclosure/DoS/Elevation. Generate th... |

## 商业 / 业务（9 个技能）

| 技能名称 | 描述 |
|----------|------|
| `ai-opc-builder` | 设计并运营一家AI原生一人公司(OPC)的完整方法论——将AI Agent集群定义为员工，以价值流而非技术职能组织，生成全链路商业材料。覆盖：可行性评估→组织设计→定价策略→销售话术→报价单→SOP→仪表盘→Onboarding→全自... |
| `eve-analyst` | Eve Analyst — 财务/运营数据分析技能。自动从项目记录中采集收入/成本/利润数据， 计算DORA指标、人效比、项目毛利等关键运营指标，自动填充CEO仪表盘模板， 生成月度/季度趋势分析（Mermaid图表），并在关键指标超... |
| `eve-closer` | Eve Closer — 销售成交技能。负责从Scout收到的商机信号到签约的全流程： 客户背景自动报告→定制化报价单生成→模拟谈判话术→合同草稿生成→签约后Onboarding流程触发。 是Eve商务中心的关单转化引擎，将线索转化为收入。 |
| `eve-customer-success` | Eve Customer Success技能 — 客户系统健康度监控、使用分析、预警推送、优化建议及续约预测。 自动管理每个客户项目的运行状态，发现异常、分析留存、提前预警，驱动主动服务。 |
| `eve-product-manager` | Eve Product Manager — 项目经验产品化/SaaS化：从交付项目中提取通用模块，打包为可复用SaaS组件，生成产品化方案与定价建议 |
| `eve-qm` | Eve QM (Quality Management) — 质量管理体系技能。每月对所有在运行项目进行质量审计， 维护CMMI5质量标准体系执行，识别流程瓶颈并推动改进，生成质量月报（含各项目质量评分排名）。 从1个技能（docume... |
| `eve-scout` | Eve Scout — 市场侦察兵。整合 internet-perception（互联网感知）、market-insight-crawler（市场洞察爬虫） 和 lead_scoring（商机评分）三大能力，实现从信息采集→竞品跟踪→... |
| `eve-scribe` | Eve Scribe — 内容营销专家。整合 doc-generator（文档自动生成引擎）和 content_pipeline（自动内容生成管道）， 实现从项目复盘→高质量文章→多渠道发布的端到端内容营销流水线。 自动从项目交付记录... |
| `product-charter-engine` | 产品机会发现与立项分析引擎 — 从战略方向（"做产品"）出发，通过三维研究（社会痛点×开源商业模式×SaaS赛道利润）交叉定位产品机会，输出深度立项分析报告（8维度），多项目优先级排序与执行路线图。 |

## 生产力工具（10 个技能）

| 技能名称 | 描述 |
|----------|------|
| `api-tester` | REST/GraphQL API测试工具 — 从终端发送HTTP请求、验证响应、生成测试用例、构造API文档。支持curl/httpie/wget多后端。触发词："api test"/"rest test"/"api调试"/"http... |
| `batch-executor` | 批量并行任务执行引擎 (Pattern F) — 多任务编排/并发执行/进度追踪/错误聚合/超时管理/结果收集。支持任务依赖图、速率限制、重试策略和报告生成。对标 Matt Pocock batch-executor 最佳实践。 |
| `caveman-mode` | 极简通信模式 — 砍掉75% token消耗，保留全部技术精度。对标 Matt Pocock caveman skill。触发词："caveman"/"极简模式"/"caveman mode"/"less tokens"/"说人话简短版"。 |
| `code-formatter` | 多语言代码格式化/规范化 — 统一代码风格、配置格式化工具(prettier/black/rustfmt/gofmt等)、批量格式化、CI集成。触发词："format code"/"格式化代码"/"prettier"/"代码风格"/"... |
| `evey-plugins` | Evey的23个Hermes插件集成指南 — 自治/可观测/质量/学习/通信全覆盖。对标 42-evey/hermes-plugins (MIT)。触发词："evey"/"evey插件"/"自主引擎"/"cost guard"/"te... |
| `kanban-worker` | Built-in kanban worker skill — standard patterns for task completion summaries, retry diagnostics, block-reason repor... |
| `mermaid-render` | Zero-install Mermaid diagram renderer via kroki.io POST API. Renders .mmd code → PNG/SVG. Supports flowcharts, sequen... |
| `microsoft-workspace` | Outlook/日历/邮件/联系人/待办 全集成 — 通过Microsoft Graph API。支持Hotmail/Outlook.com/M365。对标 Andrew-Girgis microsoft-workspace-skil... |
| `regex-builder` | 正则表达式构建与测试 — 交互式构建、测试用例验证、常见模式库、复杂正则分解、性能评估。触发词："regex"/"正则"/"regular expression"/"regex test"/"正则表达式"/"pattern match... |
| `sql-optimizer` | SQL查询优化 — 分析查询计划、识别慢查询、建议索引优化、模式重构。支持PostgreSQL/MySQL/SQLite。触发词："sql optimize"/"query optimize"/"慢查询"/"sql performan... |

## 测试（5 个技能）

| 技能名称 | 描述 |
|----------|------|
| `contract-test` | 契约测试 — 确保服务间API契约一致性，防止消费者/提供者契约断裂。支持Pact/Spring Cloud Contract多框架，微服务集成验证。 |
| `fuzz-tester` | 模糊测试 — 自动生成随机/变异输入对程序进行压力测试，检测崩溃、内存泄漏、未处理异常、安全漏洞。支持AFL/LLVM libFuzzer/Python Atheris多引擎。 |
| `snapshot-tester` | 快照测试 — 捕获输出/UI/API响应的快照，自动检测意外变更。支持jest snapshot/insta.rs/pytest-snapshot多引擎，组件级到API级覆盖。 |
| `specialized-testing` | Specialized testing toolkit — fuzz testing (auto-generated random/stress test inputs) and contract testing (consumer-... |
| `system-qa` | Comprehensive system QA using multi-agent parallel testing — survey → decompose → delegate → aggregate → fix → verify... |

## 质量保障（5 个技能）

| 技能名称 | 描述 |
|----------|------|
| `accessibility-audit` | Web accessibility auditing — WCAG 2.1 AA/AAA compliance, axe-core, Lighthouse, screen reader testing. |
| `load-test-generator` | Load/stress test generation — k6, Locust, Artillery scripts. Ramp-up patterns, scenario design, threshold assertions. |
| `performance-profiler` | Performance profiling — CPU, memory, I/O profiling with flame graphs. Python (py-spy), Node.js (clinic), Go (pprof), ... |
| `performance-testing` | Performance testing suite — load test generation (k6/Locust/Artillery scripts with ramp-up patterns and threshold ass... |
| `visual-regression` | Visual regression testing — screenshot comparison, pixel diff, layout shift detection. Playwright/Storybook/Percy/Chr... |

## 数据工程（3 个技能）

| 技能名称 | 描述 |
|----------|------|
| `anonymizer` | 数据脱敏 — 自动检测并脱敏PII/敏感数据，支持静态脱敏(数据库/文件)和动态脱敏(API层)。多策略：遮蔽/泛化/替换/扰动/k-匿名/l-多样性。 |
| `data-validator` | 数据验证框架 + 数据集质量验证 — 声明式数据验证规则引擎(JSON Schema/YAML/CSV)，数据集质量检查(缺失值/异常值/标签错误/数据泄露/分布偏移/偏见)，批量验证与报告生成。 |
| `schema-evolution` | 模式演进管理 — 管理数据库/API/数据湖的schema版本变更，向前兼容策略，迁移自动生成，回滚计划，版本锁定，多环境同步。 |

## CMMI5 / 软件工程标准化（53 个技能）

| 技能名称 | 描述 |
|----------|------|
| `agent-compliance-audit` | CMMI5多Agent合规审计 — 将部署的Agent Profile/Gateway/脚本与标准框架对比，检测Agent缺失、多余、角色缺失、可执行脚本缺失、身份配置冲突。输出按严重度排序的差距报告和修复建议。 |
| `api-automation-test-platform` | API自动化测试平台 — 基于OpenAPI规格自动生成API测试用例，含正常/异常/边界/认证/鉴权/幂等性测试，支持Postman/Newman/hurl/curl多执行器。 |
| `api-contract-generator` | API契约生成器 — 从代码/接口定义自动生成OpenAPI 3.0契约、消费者驱动契约(CDC)、服务间契约。支持Code→Spec和Spec→Code双向生成，契约兼容性校验。 |
| `api-interface-designer` | 接口概要设计器 — 生成RESTful/GraphQL/gRPC接口规格(OpenAPI 3.0)，含端点定义/请求响应格式/错误码/认证方式/速率限制。 |
| `architecture-highlevel-designer` | 系统架构概要设计器 — 生成C4模型(Context/Container/Component/Code)架构图，含架构决策记录(ADR)、技术选型矩阵、非功能需求映射。 |
| `business-usecase-modeler` | 业务用例建模器 — 生成UML用例图、业务流程图(Mermaid)、角色-用例矩阵，支持Include/Extend/Generalization用例关系建模。 |
| `change-impact-analyzer` | 代码/需求变更影响分析器 — 变更前自动分析影响范围(依赖图传播/数据表影响/API兼容性/测试影响)，输出影响分析报告和变更建议。 |
| `cmmi5-agent-bridge` | CMMI5 10-Agent orchestration framework with SQLite shared state bridge, PM scheduler (7×24 cron), executable agent sc... |
| `cmmi5-chat-router` | CMMI5 多Agent群聊协作中间件 — 四种架构：v5.0独立Agent自主发言(feishu-ws-daemon，推荐) + v4.0原生多Bot WebSocket(Gateway适配) + v3.0单Bot路由(备选) + ... |
| `cmmi5-compliance-binding` | CMMI5全规范合规绑定引擎 — 强制执行10项核心规范（过程管理/质量管控/风险管控/文档管控/过程复用/效能度量/可追溯/可审计/OPA沉淀/持续改进），自动绑定验证、工具有效性校验、全产出物BookStack归档、知识库优先复用... |
| `cmmi5-fullstack-orchestrator` | CMMI-DEV V2.0 Maturity Level 5 自主研发全流程闭环编排器 — 强制串联 需求→设计→编码→测试→项目管理→发布运维→复盘沉淀 七大阶段，34项子工具全覆盖。所有架构设计、项目开发、需求分析、UML设计、数... |
| `cmmi5-governance` | CMMI-DEV V2.0 Maturity Level 5 governance engine — QPM, CAR, OPM, MA, DAR, OPD, GOV, OT. Full statistical process con... |
| `cmmi5-pipeline` | CMMI5 10-Agent Full Pipeline — invoke the complete PM→REQ→ARCH→DEV→SEC→TEST→QA→CM→DOC→SPI pipeline with one command. ... |
| `competitive-analysis-generator` | 竞品分析自动生成器 — 基于市场数据自动对比竞品功能矩阵、APP应用能力、业务中台能力、SWOT分析、波特五力模型，生成结构化竞品分析报告。 |
| `continuous-project-execution` | Strategic assessment and architecture design for 24/7 autonomous project execution on top of CMMI5 multi-agent infras... |
| `database-er-modeler` | 数据库ER建模工具 — 从需求/SRS/类图自动提取实体和关系，生成ER图(Mermaid ER/IE notation)、数据字典、实体定义规格。支持MySQL/PostgreSQL/MongoDB多数据库。 |
| `defect-lifecycle-tracker` | 缺陷全生命周期闭环追踪器 — 缺陷从发现→提交→确认→分配→修复→验证→关闭 全流程管理，含严重级别/SLA时效/根因分析/缺陷趋势图。 |
| `dev-efficiency-metrics-analyzer` | 研发效能指标度量分析器 — DORA四大指标(部署频率/变更前置时间/变更失败率/平均恢复时间)+SPACE框架，自动采集数据生成效能仪表板(Mermaid趋势图)。 |
| `dev-pipeline-orchestrator` | 研发流水线全流程编排器 — 从代码提交→构建→测试→部署 完整CI/CD流水线，含GitHub Actions/GitLab CI/Jenkins配置生成，阶段门控，一键触发。 |
| `documentation-quality-audit` | 项目文档质量审计 — 系统化检查CMMI5项目各阶段Agent产出文档/BookStack页面的内容完整性、结构完整性、CMMI5合规要素(版本追溯/审核记录/需求追溯)、风格一致性、跨阶段覆盖度。输出按严重度排序的缺陷报告(bloc... |
| `effort-cost-estimator` | 工时成本估算与追踪器 — 支持SRS复杂度驱动力估值/COCOMO II/Function Point/Three-Point估算，EVM挣值管理(PV/EV/AC/SV/CV/SPI/CPI)，成本趋势图(Mermaid)，Book... |
| `feasibility-charter-generator` | 项目可行性分析&项目章程生成器 — 从战略愿景文档一键生成CMMI5标准项目启动包(章程/WBS/里程碑/风险/架构/汇报)，BookStack归档。 |
| `fullstack-builder` | 全栈项目全生命周期引擎 — 从零调研(5维度Market/User/Competitive/Tech/Compliance)→可行性分析→SRS→原型→全栈代码→测试→部署→归档。支持"暂无需求，全权从零开始"模式。 |
| `gantt-chart-scheduler` | 甘特图自动生成&进度排期器 — 基于WBS自动生成甘特图(Mermaid Gantt)，含任务依赖/关键路径/资源平衡/进度基线。 |
| `integration-test-orchestrator` | 集成测试编排器 — 编排多服务/多模块集成测试，管理测试环境(Docker Compose)、数据准备/清理、依赖顺序、超时重试、结果聚合。 |
| `market-insight-crawler` | 市场洞察爬虫 — 多源市场数据采集、趋势分析、技术雷达监控。支持RSS/GitHub/HN/Reddit/行业媒体/专利数据库多源爬取，自动生成市场洞察报告(Mermaid思维导图+趋势热力图)。 |
| `meeting-minutes-action-tracker` | 会议纪要智能提炼&行动项追踪 — 会议录音/文字自动提炼纪要，含决议/行动项/责任人/截止日期，行动项闭环追踪至关闭。 |
| `milestone-control-tool` | 里程碑节点管控工具 — 里程碑定义/检查清单/准入准出标准/偏差预警/进度报告，含里程碑燃尽图(Mermaid)。 |
| `module-detailed-design-engine` | 模块详细设计模板引擎 — 为每个功能模块生成详细设计文档，含类设计/接口设计/算法伪代码/状态机/异常处理/数据校验规则。 |
| `multi-agent-memory-audit` | Complete lifecycle for multi-agent memory: audit → evaluate options → implement ChromaDB+SQLite shared memory layer w... |
| `multi-env-deploy-rollback` | 多环境一键发布&自动回滚器 — 支持Dev/Staging/Production多环境一键发布，蓝绿部署/金丝雀发布/滚动更新，自动健康检查+失败自动回滚。 |
| `multi-language-code-generator` | 多语言代码生成器 — 从API规格/数据模型/接口定义自动生成Python/JS/TS/Go/Java/Rust多语言客户端SDK和服务端骨架，含类型定义、输入校验、错误处理、单元测试模板。 |
| `online-fault-diagnosis-fixer` | 线上故障自动诊断&修复建议器 — 接入监控告警自动触发诊断，含日志分析/链路追踪/指标关联/根因定位，输出诊断报告和修复建议(含回滚/热修复/配置变更等方案)。 |
| `perf-load-test-engine` | 性能压测&负载测试引擎 — 多场景性能测试，含负载测试/压力测试/耐久测试/峰值测试，支持k6/Locust/JMeter/wrk，自动生成性能分析报告。 |
| `pm-daily-report` | Generate structured PM daily status reports for CMMI5 projects — queries agent bridge status, artifact counts, servic... |
| `project-asset-archiver` | 项目资产自动归档&知识库沉淀器 — 项目收尾自动归档全量产出物(需求/设计/代码/测试/文档/报告)至BookStack/Hermes知识库，建立结构化索引。 |
| `project-retrospective-repository` | 项目复盘&组织过程资产沉淀器 — 项目复盘四步法(回顾目标/评估结果/分析原因/总结规律)，输出复盘报告和经验教训库，自动归入组织过程资产。 |
| `refactor-assist` | 重构引擎 — 代码坏味检测、复杂度分析、提取方法/类建议、多文件重构编排。支持单文件重构到跨文件批量重构全链路，含影响分析、变更排序、批量执行与验证。 |
| `req-design-code-test-tracer` | 需求-设计-代码-测试双向溯源工具 — 建立需求ID↔设计文档↔代码模块↔测试用例 双向追溯链，支持正向追溯和反向追溯，生成追溯矩阵(Mermaid)。 |
| `requirement-conflict-detector` | 需求歧义冲突检测工具 — 自动检测需求间的语义冲突、逻辑矛盾、术语不一致、优先级冲突，输出冲突报告和修复建议。 |
| `risk-identification-controller` | 项目风险识别与管控器 — 风险识别/定性定量分析/风险登记册/应对策略(规避/转移/缓解/接受)/风险趋势监控。 |
| `rl-finetune` | 微调引擎 — RL微调全生命周期：轨迹收集→压缩→奖励建模→Atropos RL训练→评估→部署。自改进Agent飞轮，支持PPO/DPO/GRPO多方法。 |
| `smart-regression-selector` | 智能回归测试筛选器 — 基于代码变更影响分析，智能筛选最小区间回归用例，避免全量回归耗时。支持Git diff驱动、依赖图分析、测试优先级排序。 |
| `srs-ai-review` | 自动化审核IT项目需求规格说明书文档，识别缺失、流程漏洞、数据合规风险，输出标准化初审结果 |
| `srs-auto-generator` | 需求规格说明书自动生成器 — 基于结构化需求和用例模型，按IEEE 830标准自动生成完整SRS文档，含功能需求/非功能需求/接口需求/数据需求/约束条件。 |
| `table-ddl-sql-generator` | 数据表自动建SQL生成器 — 基于ER模型自动生成DDL建表语句(CREATE TABLE/INDEX/VIEW/TRIGGER)，支持MySQL/PostgreSQL/SQLite，含迁移脚本和回滚脚本。 |
| `tdd` | TDD测试驱动开发引擎 — 红-绿-重构循环，垂直切片开发，每次一个测试→一个实现→重复。支持Python/JS/TS/Go/Java多框架。 |
| `test-report-auto-generator` | 测试报告自动生成器 — 聚合单元/API/集成/性能/回归测试结果，生成综合质量评估报告，含测试覆盖率/通过率/缺陷密度/质量评分/Mermaid趋势图。 |
| `uml-fullchain-generator` | UML全链路生成器 — 一键生成UML 2.5全套图：用例图/类图/顺序图/活动图/状态图/组件图/部署图，Mermaid+PlantUML双格式输出。 |
| `unit-test-auto-generator` | 单元测试自动生成器 — 基于源代码自动生成单元测试用例，支持Jest/Pytest/JUnit/Go testing多框架，覆盖率目标≥80%，边界条件/异常路径自动覆盖。 |
| `user-requirement-decomposer` | 用户需求拆解器 — 将用户原始需求拆解为结构化功能需求、非功能需求、约束条件，输出需求树状图(Mermaid)和结构化需求清单。 |
| `wbs-work-breakdown-tool` | WBS工作分解工具 — 将项目范围系统分解为可执行的工作包(Work Package)，输出WBS树状图(Mermaid)、工作包卡片、责任分配矩阵(RACI)、WBS字典。含自动分解算法、校验规则和模板生成。 |
| `zhixiang-zhizao` | 智项智造·全自动立项系统 v2.18 — 一句话需求直接输出三套可落地的标准化项目文档(项目立项报告/项目立项预估需求清单/项目需求规格说明书)，全流程无人工干预、100%AI全自动闭环。12节点SOP管道对齐。三库体系: 18模板+... |

## 可观测性（7 个技能）

| 技能名称 | 描述 |
|----------|------|
| `agent-heartbeat` | Yestin Agent心跳自愈系统 —— 每3分钟巡检全部10个CMMI5 Agent的健康状态、深度诊断异常、自动自愈修复。 |
| `agent-team-dashboard` | AI Agent团队状态可视化仪表板 — 单文件HTML/CSS/JS Vibe Coding建造，展示员工状态、部门分区、实时讨论、活动流，零依赖零构建工具。 |
| `alert-manager` | 告警管理 — 集中告警聚合、路由、分组、静默、升级策略。支持Prometheus Alertmanager/Grafana On-Call/自定义Webhook多后端，告警去重与责任到人。 |
| `dashboard-builder` | 仪表板生成 — 自动从指标/日志/追踪数据生成可观测仪表板。支持Grafana/Kibana/Datadog多平台，JSON/YAML声明式定义，模板化复用。 |
| `log-aggregator` | 日志聚合分析 — 集中收集/解析/查询/告警应用程序日志。支持ELK Stack/Loki+Grafana/Vector多后端，实时搜索与历史分析。 |
| `observability-stack` | 可观测性栈 — 统一仪表板生成、日志聚合分析与告警管理。支持Grafana/Kibana/Datadog多平台，ELK Stack/Loki+Grafana多日志后端，Prometheus Alertmanager告警路由与升级策略。... |
| `self-healer` | Autonomous self-healing framework — monitor health, diagnose errors, auto-remediate, learn patterns, escalate to huma... |

## 元技能 / Agent 自管理（19 个技能）

| 技能名称 | 描述 |
|----------|------|
| `agent-self-audit` | Agent self-architecture audit, competitive benchmarking, skill-level competitor scanning with batch conversion, and i... |
| `agent-workflow` | Multi-agent workflow orchestration — define roles, decompose tasks, execute sequential/parallel/conditional flows. In... |
| `batch-quality-upgrade` | Systematic quality audit + batch upgrade of skill scripts AND SKILL.md structure validation. Runs all check.py valida... |
| `curriculum-learning` | Progressive structured self-learning curriculum — 5 levels, 4 dimensions, 20 modules with real data-driven exercises.... |
| `fullstack-autonomous-learning` | 全栈自主学习双引擎系统 — 课程引擎(Transcendence满级)+6方向自主探索(每5分钟)。涵盖TECH/SOFT/META/SEC四维全栈能力，自动轮转、产出驱动、无果即弃。 |
| `gbrain` | Global Brain — unified cognitive hub integrating perception, memory, learning, reasoning, and autonomous decision-mak... |
| `gbrain-metrics-extractor` | Extract key GBrain metrics (risk level, evolution score, signals count) in concise format for quick status reporting ... |
| `knowledge-index-maintain` | Markdown knowledge base index maintenance — audit, rebuild, and clean up the agent's local ~/.hermes/knowledge/index.... |
| `learning-cycle` | 6-direction autonomous learning cycle — runs via cron every 5 minutes, rotates through tech/security/engineering/pers... |
| `memory-engine` | SQLite + ONNX hybrid memory engine — structured storage, 3-layer hybrid retrieval (Vector+TF-IDF+FTS5), LLM rerank, a... |
| `memory-tier` | Agent memory architecture strategy and design — competitive benchmarking, dependency-cost evaluation, upgrade plannin... |
| `meta-evolution` | Autonomous continuous self-evolution engine. Analyzes own capabilities, detects weaknesses, generates improvement pla... |
| `personality-learning` | Autonomous personality soft-skills self-improvement cycle. Self-audits 8 SOUL.md personality criteria, researches lea... |
| `self-learning` | Autonomous knowledge acquisition engine. Extracts trending topics from perception data (RSS/GitHub/Trends), researche... |
| `skill-claw` | 技能库自动进化/去重/改进 — 对标 SkillClaw (AMAP-ML, 705★, arXiv论文)。从实际会话数据中自动演化技能，去重，提升质量。触发词："skillclaw"/"技能进化"/"skill evolve"/"去... |
| `skill-factory` | 元技能工厂 — 观察工作流，自动检测模式并生成可复用技能(SKILL.md+plugin.py)。对标 Romanescu11。触发词："save as skill"/"记住这个流程"。 |
| `skill-library-audit` | 技能库结构性健康审计 — 扫描整个技能库的文件系统结构，检查目录完整性、scripts/references覆盖率、YAML frontmatter、空目录、名称冲突。自动修复发现的问题。输出统计+问题+修复摘要。 |
| `system-health-report` | Multi-dimensional system health synthesis audit. Runs parallel diagnostic scripts across all agent subsystems (healer... |
| `virtual-team` | gstack-inspired virtual engineering team — CEO, Engineering Manager, Designer, Reviewer, QA Lead, Security Officer, R... |

## MLOps / 机器学习运维（4 个技能）

| 技能名称 | 描述 |
|----------|------|
| `data-pipeline` | ELT/ETL data pipeline generation and management — extract, transform, load with validation, monitoring, and error han... |
| `experiment-tracker` | ML实验追踪 — MLflow全生命周期管理(实验记录/参数追踪/指标对比/模型注册/部署)。支持W&B/Neptune多后端，自动最佳模型选择与A/B测试分析。 |
| `feature-store` | Feature engineering storage and serving — consistent features across training and inference. Feast/Tecton patterns fo... |
| `model-registry` | ML model registry — version, track lineage, stage transitions (staging→production→archived). MLflow/Weights & Biases ... |

## 进化与自学习（4 个技能）

| 技能名称 | 描述 |
|----------|------|
| `gepa-evolution` | DSPy+GEPA技能/提示词进化 — 通过反思式进化搜索自动优化SKILL.md/工具描述/系统提示词。ICLR 2026 Oral，无GPU，$2-10/run。对标 NousResearch/hermes-agent-self-... |
| `hermes-dojo` | Agent道场 — 监控性能→识别薄弱技能→自动修复→生成改进报告。对标 Yonkoo11/hermes-dojo (Hackathon)。触发词："dojo"/"道场"/"训练场"/"improve skills"。 |
| `super-hermes` | 元推理Agent — 自写分析提示词(prisms)，报告发现+盲点，跨运行学习。40轮研究+1000+实验验证。对标 Cranot/super-hermes。触发词："prism"/"super hermes"/"元分析"/"深度分析"。 |
| `trajectory-distillation` | 真实轨迹蒸馏 — 从生产会话捕获训练轨迹→LLM裁判评分→Atropos RL微调→更好模型。对标 beardthelion/hermes-skill-distillation (Hackathon)。触发词："trajectory"... |

## 协作（4 个技能）

| 技能名称 | 描述 |
|----------|------|
| `changelog-manager` | 变更日志管理 — CHANGELOG.md全生命周期管理，Keep a Changelog标准格式，语义化版本自动关联，历史版本回溯，多分支变更合并，发布时自动冻结。 |
| `code-owner` | 代码所有者分配 — 基于CODEOWNERS文件的自动代码审查者分配，团队权限管理，变更影响分析，PR自动分配Reviewer。 |
| `release-manager` | 发布管理 — 统一变更日志管理(CHANGELOG.md全生命周期)与发布说明生成。支持Keep a Changelog标准格式、语义化版本关联、git commit自动提取、多格式输出(Markdown/HTML/JSON)、CI/... |
| `release-notes-gen` | 发布说明生成 — 从git提交历史/PR/Issue自动生成结构化发布说明。支持传统格式(keepachangelog)和标签分类，多格式输出(Markdown/HTML/JSON/PDF)。 |

## 开发者体验（4 个技能）

| 技能名称 | 描述 |
|----------|------|
| `api-client-gen` | API client code generation from OpenAPI/Swagger specs — generate typed clients for TypeScript, Python, Go, Java. |
| `api-dev-tools` | API开发工具集 — OpenAPI/Swagger spec驱动的Mock服务器生成与类型安全的API客户端代码生成。支持Prism/json-server/WireMock多Mock后端，TypeScript/Python/Go/... |
| `db-migration-helper` | Database migration assistance — generate, validate, and test schema migrations. Flyway/Alembic/Prisma patterns. Rollb... |
| `refactor-suggester` | Intelligent refactoring suggestion engine — code smell detection, complexity analysis, extract method/class suggestions. |

## 开发工具（1 个技能）

| 技能名称 | 描述 |
|----------|------|
| `lintlang` | Agent配置静态检查 — 7项结构检测器检查config/prompt/tool定义质量。零LLM调用，2ms/文件。对标 lintlang (Hermes Labs, Apache 2.0)。触发词："lintlang"/"con... |

## 开发基础（3 个技能）

| 技能名称 | 描述 |
|----------|------|
| `ide-bridge` | IDE integration bridge via MCP/LSP — connect Hermes to VS Code/JetBrains for semantic code understanding, go-to-defin... |
| `knowledge-base` | RAG-enhanced knowledge base — index docs, auto-retrieve relevant context for tasks. Supports local markdown/PDF and M... |
| `multimodal-fusion` | Cross-modal orchestration — combine vision, voice, browser, and code understanding for tasks like UI development, des... |

## 媒体技能（1 个技能）

| 技能名称 | 描述 |
|----------|------|
| `youtube-full` | 完整YouTube工具包 — 字幕提取/视频搜索/频道浏览/播单解析/频道内搜索。通过TranscriptAPI驱动，无需Google API Key或浏览器。对标 ZeroPointRepo youtube-full (技能周精选)... |

## 记忆系统（2 个技能）

| 技能名称 | 描述 |
|----------|------|
| `flowstate-qmd` | 预期式记忆层 — SQLite+FTS5+向量存储+预取缓存，Agent主动拉取上下文。对标 flowstate-qmd。触发词："flowstate"/"qmd"/"预取记忆"。 |
| `hindsight-memory` | 长期记忆层 — retain/recall/reflect工作流，语义+图谱+时序检索。替代已删除的mnemo-hermes (eleion-ai仓库404)。对标 Vectorize hindsight (production级)。... |

## 社区（1 个技能）

| 技能名称 | 描述 |
|----------|------|
| `colony-skill` | AI+人类协作社区 — 帖子/评论/私信/投票/预测/辩论/成就/市场。对标 TheColonyCC。触发词："colony"/"社区协作"。 |

## 集成（3 个技能）

| 技能名称 | 描述 |
|----------|------|
| `chainlink-agent-skills` | Chainlink官方技能套件 — CRE/CCIP/Data Feeds/Data Streams/ACE，涵盖预言机数据/跨链/合规。对标 smartcontractkit/chainlink-agent-skills (prod... |
| `claude-code-thirdparty` | Claude Code/CodeX第三方模型接入 + CC-Switch模型切换 + Responses↔Chat协议翻译代理(v3已修复) — 通过零依赖协议翻译代理接入DeepSeek等非Anthropic/非OpenAI模型。支... |
| `web-search-plus` | 多提供商智能路由搜索 — 10提供商(Serper/Brave/Tavily/Exa/Perplexity等)，自动路由+自适应回退+1h缓存。对标 robbyczgw-cla/hermes-web-search-plus。触发词："... |

## 优化（2 个技能）

| 技能名称 | 描述 |
|----------|------|
| `cost-optimization` | 模型API成本分析与优化 — 令牌级成本拆解、模型定价对比、优化方案建模、执行验证。触发词："降低成本"/"cost optimization"/"省钱"/"模型成本"/"减少开销"/"token cost"/"刀刃"/"每一分钱"。 |
| `rtk-hermes` | Shell命令输出智能压缩 — 通过RTK重写terminal命令，60-90% token节省。对标 rtk-hermes plugin (ogallotti)。零配置自动注册，优雅降级。触发词："rtk"/"压缩输出"/"toke... |

## SDLC / 软件开发生命周期（10 个技能）

| 技能名称 | 描述 |
|----------|------|
| `arch-designer` | Architecture design engine — C4 model diagrams, ADR generation, technical decision framework, Mermaid/PlantUML output... |
| `backend-infra-hardening` | 后端基础设施加固模式 — 将工作原型从内存/服务内存储迁移至持久化数据库(SQLite/SQLAlchemy ORM)，配套CI/CD流水线(GitHub Actions + ruff + mypy + bandit + pytest... |
| `cicd-builder` | CI/CD pipeline builder — GitHub Actions, Jenkins, GitLab CI generation. Build-test-deploy automation with quality gat... |
| `db-designer` | Database design — schema, ERD, migrations, query optimization. CMMI5-grade data engineering with full traceability. |
| `doc-generator` | Documentation auto-generator — API docs (OpenAPI), README, architecture docs, changelogs. Extracts from code + commen... |
| `ops-monitor` | Operations monitoring — health checks, log analysis, metrics dashboards, alerting rules. Prometheus/Grafana-ready, Do... |
| `req-analyzer` | Requirements analysis & traceability — user stories, acceptance criteria, RTM generation. BRD/PRD analysis with gap d... |
| `srs-ieee830-generator` | Generate an IEEE 830-standard SRS document as a styled BookStack HTML page with Mermaid use case diagrams and iterati... |
| `supplier-manager` | Supplier Agreement Management (SAM) — formal third-party dependency lifecycle management. Evaluate suppliers, monitor... |
| `test-engine` | Automated testing engine — unit/integration/E2E test generation, TDD workflow, coverage analysis, test strategy. pyte... |

## 其他 / 未分类（11 个技能）

| 技能名称 | 描述 |
|----------|------|
| `apikey-image-gen` | Generate or edit images through Hermes Web UI using the selected/requested profile's fun-codex provider from config.y... |
| `bookstack-structured-import` | Import structured project data (workload tables, WBS, requirement lists, budget breakdowns, credential vaults) from u... |
| `bookstack-template-manager` | Create, update, and organize reusable document templates in BookStack's 📋 文档模板库 shelf. Covers creating template pages... |
| `ccgp-bid-scraper` | 中国政府采购网(CCGP) AI/大模型/RPA 招标项目自动扫描。搜索bxsearch接口，解析结果并获取详情页预算/截止日期，生成Markdown报告。 |
| `grok-image-to-video` | Animate a local image into a short mp4 video through Hermes Web UI using xAI Grok Imagine. |
| `hermes-doc-compliance` | IT项目需求文档AI初审合规生成规则集 v1.1 — 强制9章结构+12条R规则+5豁免+11项自查，确保通过AI初审系统（风险识别≥60%/召回率≥40%） |
| `hermes-os-portal-build` | Full lifecycle for building Hermes OS Portal features (Auth & RBAC, Alert Center, Observability Dashboard). Covers Fl... |
| `hyperframes` | Create AI videos with HyperFrames in Hermes using HTML, CSS, and JavaScript compositions, then validate and render th... |
| `markdown-viewer` | Create rich diagrams, data visualizations, technical architecture views, and editorial content cards directly in Mark... |
| `remotion` | Create editable AI video projects with Remotion and React, then preview and render them to MP4. Use for vertical shor... |
| `tui-dashboard` | Terminal UI dashboard for real-time monitoring — live metrics display (CPU/memory/disk/network), task progress widget... |

---

*共 268 个技能 · 2026-06-17 更新*
