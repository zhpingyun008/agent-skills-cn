# 🧠 AI Agent 技能商店 · Hermes Agent Skills

> 面向中国开发者的 AI Agent 技能精选集 — 共收录 **268** 个即用型 Hermes Agent 技能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📑 目录

- [什么是 AI Agent 技能？](#-什么是-ai-agent-技能)
- [快速安装与使用](#-快速安装与使用)
- [技能精选推荐（按分类）](#-技能精选推荐按分类)
- [实战案例](#-实战案例)
- [如何贡献技能](#-如何贡献技能)
- [常见问题](#-常见问题)
- [完整目录](Catalog.md)
- [安装指南](INSTALL.md)

## 🧩 什么是 AI Agent 技能？

**AI Agent 技能（Skills）** 是 Hermes Agent 的可插拔功能模块。每个技能是一个独立的目录，包含：

- `SKILL.md` — 技能描述、触发条件、分类信息
- 实现代码（Python / Shell / 配置文件）
- 测试用例与示例

当你向 Hermes 提出需求时，系统会自动匹配最合适的技能来响应。你可以把技能想象成 **AI 的 App Store**——
安装一个技能，就为你的 AI Agent 增加一项新能力。

### ✨ 技能核心特性

- **即插即用** — 无需修改配置文件，放入 skills 目录即可生效
- **语义触发** — 根据对话内容智能匹配，无需手动调用
- **自由组合** — 多个技能协同工作，完成复杂任务
- **开放生态** — 任何人都可以创建和分享新技能
- **268+ 技能** — 覆盖 DevOps、安全、工程、商业等 25+ 个分类

## ⚡ 快速安装与使用

### 前提条件

- 已安装 [Hermes Agent](https://hermes-agent.nousresearch.com)
- Python 3.10+

### 安装技能

```bash
# 方法一：手动安装（推荐）
# 将技能目录复制到技能目录
cp -r skill-name ~/.hermes/skills/

# 方法二：使用技能工厂（Meta Skill）
# 在对话中告诉 Hermes：
# "安装 [技能名称] 技能"

# 方法三：批量安装
git clone https://github.com/zhpingyun008/agent-skills-cn.git
cp -r hermes-zh-skills/skills/* ~/.hermes/skills/
```

### 验证安装

```bash
ls ~/.hermes/skills/ | wc -l
# 重启 Hermes Agent 即可生效
```

> 📖 详细安装说明请参阅 [INSTALL.md](INSTALL.md)

## 🏆 技能精选推荐（按分类）

从 268 个技能中精选 **50+** 个最实用的技能，覆盖 15+ 个分类：

### 📂 DevOps / 运维（共 39 个技能）

- **k8s-deployer** — Kubernetes 自动化部署与管理，K8s 运维必备
- **k8s-resource-manager** — K8s 资源管理与优化，集群稳定性的基石
- **docker-compose-manager** — Docker Compose 全生命周期管理
- **terraform-manager** — 基础设施即代码（IaC）的 Terraform 管理
- **terraform-generator** — 自动生成 Terraform 配置，加速云资源交付
- **incident-commander** — 自动化故障响应与告警处理，MTTR 降低利器
- **chaos-engineer** — 混沌工程实验，提前发现系统脆弱点
- **cloud-cost-optimizer** — 云成本分析与优化，省钱利器
- **browser-automation** — 浏览器自动化测试与操作
- **secrets-vault-manager** — 密钥与凭证安全管理
- **computer-use-linux** — Linux 桌面远程控制与自动化运维
- **system-activation** — 系统初始化与激活配置
- **system-cleanup** — 系统清理与资源回收
- **mcp-server-installer** — MCP 服务器一键安装与配置
- **dashboard-panel-builder** — 运维仪表盘面板构建

### 📂 软件工程（共 26 个技能）

- **code-review** — AI 驱动的代码审查，拦截隐患于合入之前
- **multi-file-refactor** — 多文件批量重构，大型项目重构利器
- **symbol-index** — 代码符号索引，提升跨文件导航与理解效率
- **improve-codebase-architecture** — 代码架构分析与改进建议
- **git-guardrails** — Git 操作安全护栏，防止误操作
- **worktree-isolation** — Git Worktree 隔离开发环境
- **agent-benchmark** — AI Agent 基准测试与性能评估
- **agent-monitor** — AI Agent 运行监控与诊断
- **diagnose** — 系统与代码问题自动诊断
- **execplan** — 执行计划生成与任务分解
- **litprog** — 文学编程（Literate Programming）支持
- **frontend-backend-api-alignment** — 前后端 API 对齐检查
- **third-party-ai-evaluation** — 第三方 AI 模型评测
- **zoom-out** — 代码整体架构鸟瞰分析
- **tool-benchmark-workflow** — 工具基准测试工作流

### 📂 安全（共 11 个技能）

- **sast-scanner** — 静态应用安全测试（SAST）
- **secret-scanner** — 密钥泄露扫描，防止敏感信息外泄
- **dependency-audit** — 依赖库安全审计
- **supply-chain-security** — 供应链安全分析与管控
- **container-security-scanner** — 容器镜像安全扫描
- **iac-security-scanner** — 基础设施即代码安全扫描
- **llm-security-auditor** — 大模型安全审计与对抗测试
- **threat-model** — 威胁建模与风险评估
- **compliance-checker** — 合规性自动检查
- **sandbox-exec** — 沙箱安全执行环境
- **agent-security-posture-audit** — Agent 安全态势审计

### 📂 商业 / 业务（共 9 个技能）

- **eve-scout** — 市场调研与竞争情报收集
- **eve-analyst** — 数据分析与商业洞察
- **eve-closer** — 销售赋能与客户转化支持
- **eve-product-manager** — AI 产品经理助手
- **eve-customer-success** — 客户成功与满意度分析
- **eve-qm** — 质量管理的 AI 驱动
- **eve-scribe** — 会议记录与文档自动化
- **ai-opc-builder** — AI 运营控制台构建
- **product-charter-engine** — 产品章程自动生成引擎

### 📂 生产力工具（共 10 个技能）

- **kanban-worker** — 看板任务管理自动化
- **api-tester** — API 测试自动化
- **batch-executor** — 批量任务执行器
- **sql-optimizer** — SQL 查询优化建议
- **regex-builder** — 正则表达式辅助构建
- **mermaid-render** — Mermaid 图表渲染支持
- **code-formatter** — 代码格式化与风格统一
- **caveman-mode** — 极简模式：最小化 AI 干扰
- **microsoft-workspace** — Microsoft 办公套件集成
- **evey-plugins** — EVE 插件扩展系统

### 📂 测试（共 5 个技能）

- **fuzz-tester** — 模糊测试，发现边界缺陷
- **snapshot-tester** — 快照测试，UI 回归检测
- **contract-test** — 契约测试，服务间接口验证
- **system-qa** — 端到端系统质量保证
- **specialized-testing** — 专项测试工具集

### 📂 质量保障（共 5 个技能）

- **accessibility-audit** — 无障碍（A11Y）审计
- **performance-profiler** — 性能分析与热点定位
- **performance-testing** — 性能测试与压测执行
- **load-test-generator** — 负载测试脚本生成
- **visual-regression** — 视觉回归测试

### 📂 数据工程（共 3 个技能）

- **anonymizer** — 数据脱敏与隐私保护
- **data-validator** — 数据质量验证
- **schema-evolution** — 数据 Schema 演化管理

### 📂 Agent 技能核心（共 31 个技能）

- **dynamic-router** — 动态路由：智能分发请求到最合适的技能
- **internet-perception** — 互联网感知：实时获取网络信息
- **git-workflow** — Git 工作流自动化
- **pr-automation** — Pull Request 自动化管理与合并
- **task-dag** — 任务依赖图编排与执行
- **lint-test-loop** — Lint-测试自动循环修复
- **mcp-gateway** — MCP 协议网关集成
- **collaborative-session** — 多 Agent 协作会话管理
- **role-agents** — 角色化 Agent 分工协作
- **multi-model-router** — 多模型路由：智能选择最优 LLM

### 📂 CMMI5 / 软件工程标准化（共 53 个技能）

- **srs-auto-generator** — SRS 需求规格说明书自动生成
- **srs-ai-review** — SRS 文档 AI 评审
- **tdd** — 测试驱动开发全流程支持
- **unit-test-auto-generator** — 单元测试自动生成
- **test-report-auto-generator** — 测试报告自动生成
- **fullstack-builder** — 全栈应用一键构建
- **multi-language-code-generator** — 多语言代码生成
- **architecture-highlevel-designer** — 系统架构高层设计
- **module-detailed-design-engine** — 模块详细设计引擎
- **refactor-assist** — 重构辅助工具
- **uml-fullchain-generator** — UML 全链路图生成
- **gantt-chart-scheduler** — 甘特图排期工具
- **change-impact-analyzer** — 变更影响分析
- **risk-identification-controller** — 风险识别与控制
- **online-fault-diagnosis-fixer** — 在线故障诊断与修复

### 📂 可观测性（共 7 个技能）

- **self-healer** — 自愈系统：自动发现并修复问题
- **log-aggregator** — 日志聚合与分析
- **alert-manager** — 告警管理与通知
- **agent-heartbeat** — Agent 心跳检测与健康监控
- **dashboard-builder** — 自定义仪表盘构建
- **observability-stack** — 可观测性全栈方案
- **agent-team-dashboard** — Agent 团队运行看板

### 📂 元技能 / Agent 自管理（共 19 个技能）

- **agent-self-audit** — Agent 自我审计与反思
- **agent-workflow** — Agent 工作流编排引擎
- **skill-factory** — 技能工厂：自动创建新技能
- **learning-cycle** — 持续学习循环
- **self-learning** — 自主学习机制
- **memory-engine** — 记忆引擎：持久化上下文记忆
- **system-health-report** — 系统健康度报告
- **curriculum-learning** — 课程学习路径规划

### 📂 MLOps / 机器学习运维（共 4 个技能）

- **model-registry** — 模型注册表与版本管理
- **experiment-tracker** — 实验追踪与对比分析
- **feature-store** — 特征存储与特征工程
- **data-pipeline** — 数据流水线编排

### 📂 进化与自学习（共 4 个技能）

- **super-hermes** — Hermes  Agent 自我进化升级
- **trajectory-distillation** — 轨迹蒸馏：知识迁移与优化
- **hermes-dojo** — Hermes 道场：Agent 训练与对战
- **gepa-evolution** — GEPA 进化算法驱动提升

### 📂 协作（共 4 个技能）

- **release-manager** — 发布管理自动化
- **release-notes-gen** — 发布说明自动生成
- **changelog-manager** — 变更日志管理
- **code-owner** — 代码责任人自动分配

> 📋 查看完整列表请参阅 [Catalog.md](Catalog.md)

## 🚀 实战案例

### 案例 1：K8s 集群自动化管理

```text
用户："检查所有命名空间的资源使用情况，找出 CPU 超限的 Pod"
Agent：自动匹配 k8s-resource-manager 技能 → 查询集群 → 返回分析报告 → 给出优化建议
```

**涉及的技能：** `k8s-deployer` + `k8s-resource-manager` + `cloud-cost-optimizer`

### 案例 2：代码安全审计流水线

```text
用户："扫描这个项目的最新代码，检查依赖漏洞和密钥泄露"
Agent：依次调用 dependency-audit → secret-scanner → sast-scanner
      → 合并报告 → 生成修复建议
```

**涉及的技能：** `dependency-audit` + `secret-scanner` + `sast-scanner` + `supply-chain-security`

### 案例 3：自动化 CI/CD + 发布

```text
用户："发布 v2.1.0 版本，生成变更日志和发布说明"
Agent：执行 changelog-manager → release-notes-gen → 合并 PR → 部署到生产环境
```

**涉及的技能：** `release-manager` + `release-notes-gen` + `changelog-manager` + `pr-automation`

### 案例 4：SRS 需求文档全流程

```text
用户："为这个 AI 客服系统生成完整的需求规格说明书"
Agent：调用 srs-auto-generator 生成文档 → srs-ai-review 评审 → 改进

      → 连接 code-review 技能确保代码与需求一致
```

**涉及的技能：** `srs-auto-generator` + `srs-ai-review` + `code-review` + `req-design-code-test-tracer`

### 案例 5：全栈应用一键构建

```text
用户："从需求到部署，帮我构建一个任务管理 Web 应用"
Agent：
  1. architecture-highlevel-designer → 架构设计
  2. module-detailed-design-engine → 详细设计
  3. fullstack-builder → 代码生成
  4. unit-test-auto-generator → 单元测试
  5. docker-compose-manager → 容器化部署
```

**涉及的技能：** CMMI5 全流程技能链

## 🤝 如何贡献技能

### 提交新技能

1. Fork 本仓库
2. 在 `skills/` 目录下创建新技能目录
3. 编写 `SKILL.md`（参考已有技能格式）
4. 提交 Pull Request

### 完善现有技能

- 提交 Issue 报告问题或建议
- 改进文档、增加示例
- 翻译技能描述为中文

> 建议使用 `skill-factory` 元技能快速创建新技能模板

## ❓ 常见问题

**Q: 安装技能会影响现有配置吗？**
A: 不会。技能目录彼此独立，新增技能不会影响已有技能。

**Q: 技能有优先级吗？**
A: Hermes Agent 根据对话上下文语义匹配技能，越精准的描述越容易被触发。

**Q: 如何禁用某个技能？**
A: 将技能目录移出 `~/.hermes/skills/` 或在技能目录中添加 `.disabled` 标记文件。

**Q: 技能会消耗大量 Token 吗？**
A: 大多数技能只会在被触发时运行，`smart-compress` 技能可以自动压缩上下文减少消耗。

**Q: 能在国内网络环境使用吗？**
A: 可以。Hermes Agent 支持本地模型（如通过 `local-model` 技能），也支持代理配置。

**Q: 技能数据安全吗？**
A: 所有技能在本地执行，代码可见可审计。请使用 `secrets-vault-manager` 管理敏感信息。

## 📊 统计

| 指标 | 数值 |
|------|------|
| 技能总数 | **268** |
| 分类数量 | **25** |
| 推荐技能 | **125** |
| 最新更新 | 2026-06-17 |

---

## 📜 许可证

[MIT License](LICENSE)

---

*用 AI Agent 技能武装你的 Hermes，让 AI 真正为你所用。*
