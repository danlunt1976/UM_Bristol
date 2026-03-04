#!/usr/bin/env python3
"""Regenerate the 'Recent Updates' section of README.md from git history."""

import re
import subprocess
import sys


def get_recent_md_commits(count=10):
    """Return the most recent commits that added or modified .md files."""
    result = subprocess.run(
        [
            "git", "log", "--no-merges",
            "--diff-filter=AM",
            "--format=%ad\t%s",
            "--date=short",
            "--", "*.md",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    prefix_re = re.compile(
        r"^(feat|fix|docs|refactor|test|chore|perf|ci|build|style)(\(.+?\))?:\s*",
        re.IGNORECASE,
    )

    seen = set()
    entries = []
    for line in result.stdout.strip().splitlines():
        if not line or "[skip readme]" in line:
            continue
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        date, subject = parts
        subject = prefix_re.sub("", subject).strip()
        key = f"{date}\t{subject}"
        if key in seen:
            continue
        seen.add(key)
        entries.append(f"- **{date}** — {subject}")
        if len(entries) >= count:
            break

    return entries


def update_readme(entries):
    """Replace the Recent Updates block in README.md, write only if changed."""
    path = "README.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    block = "\n".join(entries)

    pattern = re.compile(r"(## Recent Updates\n).*?(\n---)", re.DOTALL)
    if not pattern.search(content):
        print("ERROR: Could not find Recent Updates section in README.md", file=sys.stderr)
        sys.exit(1)

    updated = pattern.sub(rf"\g<1>\n{block}\n\2", content)

    if updated == content:
        print("README.md is already up to date.")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("README.md updated with latest Recent Updates.")


def main():
    entries = get_recent_md_commits()
    if not entries:
        print("No qualifying commits found; leaving README.md unchanged.")
        return
    update_readme(entries)


if __name__ == "__main__":
    main()
