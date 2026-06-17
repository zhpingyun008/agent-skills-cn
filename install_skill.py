#!/usr/bin/env python3
"""
install_skill.py — 安装单个或批量 Hermes Agent 技能

用法:
  python install_skill.py <技能名称>                    # 安装单个技能
  python install_skill.py --all                         # 安装此仓库中所有技能
  python install_skill.py --list                        # 列出可安装的技能
  python install_skill.py <技能1> <技能2>               # 安装多个技能

技能源目录: ~/.hermes/skills/
"""

import os
import sys
import shutil
import glob

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_SOURCE = os.path.join(REPO_DIR, "skills")
SKILL_TARGET = os.path.expanduser("~/.hermes/skills")


def get_available_skills():
    """获取仓库中所有可安装的技能。"""
    if not os.path.isdir(SKILL_SOURCE):
        return []
    skills = []
    for d in os.listdir(SKILL_SOURCE):
        skill_dir = os.path.join(SKILL_SOURCE, d)
        if os.path.isdir(skill_dir) and not d.startswith("."):
            if os.path.exists(os.path.join(skill_dir, "SKILL.md")):
                skills.append(d)
    return sorted(skills)


def install_skill(skill_name: str) -> bool:
    """安装指定技能。"""
    src = os.path.join(SKILL_SOURCE, skill_name)
    dst = os.path.join(SKILL_TARGET, skill_name)

    if not os.path.isdir(src):
        print(f"❌ 技能 '{skill_name}' 不存在于仓库中")
        return False

    if not os.path.exists(os.path.join(src, "SKILL.md")):
        print(f"❌ 技能 '{skill_name}' 缺少 SKILL.md，跳过")
        return False

    if os.path.exists(dst):
        print(f"ℹ️  技能 '{skill_name}' 已安装，将覆盖")
        shutil.rmtree(dst)

    try:
        shutil.copytree(src, dst)
        print(f"✅ 已安装技能: {skill_name}")
        return True
    except Exception as e:
        print(f"❌ 安装失败 '{skill_name}': {e}")
        return False


def main():
    if not os.path.isdir(SKILL_TARGET):
        print(f"📁 创建技能目录: {SKILL_TARGET}")
        os.makedirs(SKILL_TARGET, exist_ok=True)

    args = sys.argv[1:]

    if not args or "--help" in args or "-h" in args:
        print(__doc__)
        return

    if "--list" in args:
        skills = get_available_skills()
        if not skills:
            print("📭 仓库中暂无可用技能（skills/ 目录为空）")
            print("技能文件请放置在 skills/ 子目录下，每个技能一个文件夹，包含 SKILL.md")
        else:
            print(f"📦 可安装技能 ({len(skills)} 个):")
            for s in skills:
                print(f"  • {s}")
        return

    if "--all" in args:
        skills = get_available_skills()
        if not skills:
            print("📭 仓库中暂无可用技能")
            return
        print(f"📦 将安装 {len(skills)} 个技能...")
        ok = sum(1 for s in skills if install_skill(s))
        print(f"\n✅ 成功安装 {ok}/{len(skills)} 个技能")
        return

    # 安装指定技能
    ok = sum(1 for name in args if install_skill(name))
    print(f"\n✅ 成功安装 {ok}/{len(args)} 个技能")


if __name__ == "__main__":
    main()
