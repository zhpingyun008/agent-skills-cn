#!/usr/bin/env python3
"""
setup_github.py — 在 GitHub 上自动创建 agent-skills-cn 仓库并上传文件。

使用方法：
  1. 设置环境变量 GITHUB_TOKEN（或传入 --token）
  2. 运行：python setup_github.py

要求：
  pip install PyGithub

该脚本将创建 GitHub 仓库（如果不存在），并将本地 repo 内容推送上去。
"""

import os
import sys
import argparse

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO_NAME = "agent-skills-cn"
REPO_DESCRIPTION = "🧠 AI Agent 技能商店 — Hermes Agent 中文技能精选集 | 面向中国开发者的 AI Agent 技能目录"
REPO_HOMEPAGE = "https://hermes-agent.nousresearch.com"
REPO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), REPO_NAME)


def check_prerequisites():
    """检查必要依赖和配置。"""
    missing = []
    if not GITHUB_TOKEN:
        missing.append("GITHUB_TOKEN 环境变量未设置")
    try:
        import github
    except ImportError:
        missing.append("缺少 PyGithub 库，请运行: pip install PyGithub")
    if not os.path.isdir(REPO_DIR):
        missing.append(f"本地仓库目录不存在: {REPO_DIR}")
    return missing


def create_repo():
    """使用 GitHub API 创建仓库并推送内容。"""
    from github import Github

    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    
    print(f"👤 已登录 GitHub: {user.login}")

    # 检查仓库是否已存在
    try:
        repo = user.get_repo(REPO_NAME)
        print(f"ℹ️  仓库 '{REPO_NAME}' 已存在，将更新内容")
    except Exception:
        repo = user.create_repo(
            REPO_NAME,
            description=REPO_DESCRIPTION,
            homepage=REPO_HOMEPAGE,
            private=False,
            has_issues=True,
            has_wiki=True,
            auto_init=False,
        )
        print(f"✅ 已创建新仓库: {repo.html_url}")

    # 上传文件
    print("\n📤 上传文件...")
    _upload_directory(repo, REPO_DIR, "")

    print(f"\n✅ 完成！仓库地址: {repo.html_url}")
    return repo.html_url


def _upload_directory(repo, local_dir, remote_path):
    """递归上传目录内容到 GitHub 仓库。"""
    import github

    # 获取已有文件的 SHA
    existing = {}
    try:
        contents = repo.get_contents(remote_path) if remote_path else repo.get_contents("")
        for c in contents:
            existing[c.path] = c.sha
    except Exception:
        pass

    for root, dirs, files in os.walk(local_dir):
        # 忽略隐藏文件和目录
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        files = [f for f in files if not f.startswith(".")]

        rel_root = os.path.relpath(root, local_dir)
        if rel_root == ".":
            rel_root = ""

        for fname in files:
            local_path = os.path.join(root, fname)
            remote_path = os.path.join(rel_root, fname).replace("\\", "/")

            if fname.endswith((".md", ".py", ".txt", ".json", ".yml", ".yaml", ".toml", ".sh")):
                with open(local_path, "rb") as f:
                    content = f.read()

                try:
                    if remote_path in existing:
                        repo.update_file(
                            remote_path,
                            f"更新 {remote_path}",
                            content,
                            existing[remote_path],
                        )
                        print(f"  ✏️  更新: {remote_path}")
                    else:
                        repo.create_file(
                            remote_path,
                            f"添加 {remote_path}",
                            content,
                        )
                        print(f"  ➕ 添加: {remote_path}")
                except Exception as e:
                    print(f"  ❌ 上传失败 {remote_path}: {e}")
            else:
                print(f"  ⏭️  跳过非文本文件: {remote_path}")


def main():
    parser = argparse.ArgumentParser(description="在 GitHub 上创建 agent-skills-cn 仓库")
    parser.add_argument("--token", help="GitHub Personal Access Token")
    parser.add_argument("--skip-checks", action="store_true", help="跳过前置检查")
    args = parser.parse_args()

    global GITHUB_TOKEN
    if args.token:
        GITHUB_TOKEN = args.token

    if not args.skip_checks:
        issues = check_prerequisites()
        if issues:
            print("❌ 前置检查未通过:")
            for i in issues:
                print(f"  • {i}")
            sys.exit(1)

    create_repo()


if __name__ == "__main__":
    main()
