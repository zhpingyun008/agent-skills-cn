# 📦 安装指南

> 面向中国开发者的 Hermes Agent 技能安装说明

---

## 系统要求

- 操作系统：Linux / macOS / WSL2 (Windows)
- Python 版本：3.10 或更高
- Hermes Agent：已安装并运行

## 快速开始

### 步骤 1：克隆本仓库

```bash
git clone https://github.com/yourname/agent-skills-cn.git
cd agent-skills-cn
```

### 步骤 2：安装单个技能

```bash
# 方法一：直接复制
cp -r skills/<技能名称> ~/.hermes/skills/

# 方法二：使用提供的安装脚本
python install_skill.py <技能名称>
```

### 步骤 3：批量安装推荐技能

```bash
# 安装所有推荐技能
for dir in skills/*/; do
  cp -r "$dir" ~/.hermes/skills/
done
```

### 步骤 4：重启 Hermes Agent

```bash
# 重启后新技能自动生效
hermes restart
# 或直接重启终端/hermes会话
```

## 国内网络优化

### 使用国内镜像

如果 GitHub 访问不畅，可以使用以下方式：

```bash
# 通过 Gitee 镜像
git clone https://gitee.com/yourname/agent-skills-cn.git

# 或直接下载 Release 压缩包
wget https://github.com/yourname/agent-skills-cn/releases/latest/download/skills.tar.gz
tar -xzf skills.tar.gz -C ~/.hermes/skills/
```

### 配置代理

```bash
# 设置 Git 代理
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 设置环境变量
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
```

## 验证安装

```bash
# 检查技能目录
ls ~/.hermes/skills/

# 在对话中测试
# 输入："显示所有可用的技能"
# Hermes 应该能够列出已安装的技能
```

## 技能管理

### 查看已安装技能

```bash
ls ~/.hermes/skills/ | wc -l   # 统计技能数
ls ~/.hermes/skills/           # 列出技能
```

### 禁用技能

```bash
# 方式一：移出技能目录
mv ~/.hermes/skills/某技能 ~/backup/

# 方式二：标记禁用
touch ~/.hermes/skills/某技能/.disabled
```

### 卸载技能

```bash
rm -rf ~/.hermes/skills/某技能
```

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| 技能未触发 | 检查 SKILL.md 中的 triggers 描述是否匹配你的需求 |
| 技能报错 | 查看 Hermes 日志：`hermes logs --tail 50` |
| Python 依赖缺失 | `pip install -r skills/技能名/requirements.txt` |
| 权限不足 | `chmod +x skills/技能名/*.sh` |
| 网络问题 | 参考上方国内网络优化配置代理 |

## 参考链接

- [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/docs)
- [技能商店首页](README.md)
- [技能全量目录](Catalog.md)
- [Hermes Agent GitHub](https://github.com/NousResearch/hermes-agent)
