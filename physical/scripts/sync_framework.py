#!/usr/bin/env python3
"""Build a print-oriented Markdown snapshot from Frameworks MDX sources."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path


DASHES = str.maketrans({
    "\u2010": "-",
    "\u2011": "-",
    "\u2012": "-",
    "\u2013": "-",
    "\u2014": "-",
    "\u2212": "-",
})


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout


def latex_escape(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    return text[4:end], text[end + 5 :]


def contributor_names(frontmatter: str) -> list[str]:
    names: list[str] = []
    in_wrote = False
    for raw in frontmatter.splitlines():
        line = raw.strip()
        if line == "- role: wrote":
            in_wrote = True
            continue
        if line.startswith("- role:") and line != "- role: wrote":
            in_wrote = False
        if in_wrote and line.startswith("users:"):
            match = re.search(r"\[([^]]*)\]", line)
            if match:
                names.extend(x.strip() for x in match.group(1).split(",") if x.strip())
    return names


def clean_mdx(text: str, base_url: str) -> str:
    _, body = split_frontmatter(text)
    body = re.sub(r"\{\/\*.*?\*\/\}", "", body, flags=re.S)
    body = re.sub(r"^import\s+.*$", "", body, flags=re.M)
    body = re.sub(r"^<\/?(?:TagList|AttributionList|ContributeFooter)[^>]*>\s*$", "", body, flags=re.M)
    body = re.sub(r"^<Checklist[^>]*>\s*$", "", body, flags=re.M)
    body = re.sub(r"^</Checklist>\s*$", "", body, flags=re.M)
    body = re.sub(r"^---\s*$", "", body, flags=re.M)
    body = re.sub(
        r"^## Table of Contents\s*$.*?(?=^## Related frameworks\s*$)",
        "",
        body,
        flags=re.M | re.S,
    )

    body = body.replace("> \u26a0\ufe0f Stub/in progress, help contribute/expand.",
                        "> **DOMAIN STATUS: IN PROGRESS.** The online framework currently defines scope only; this edition does not invent controls beyond the reviewed source.")
    body = body.replace("\U0001f511", "")
    body = re.sub(r">\s*\*\*Key Takeaway\*\*:\s*", "> **KEY TAKEAWAY.** ", body)
    body = re.sub(r">\s*\*\*Key Takeaway:\*\*\s*", "> **KEY TAKEAWAY.** ", body)
    body = body.replace("\u26a0\ufe0f", "WARNING:")

    body = re.sub(r"\]\(/", "](BASE_URL/", body)
    body = body.replace("BASE_URL", base_url.rstrip("/"))
    body = body.translate(DASHES)
    body = re.sub(r"- \[ \] ", "- ( ) ", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--ref", default="develop")
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--meta-output", required=True, type=Path)
    args = parser.parse_args()

    repo = args.repo.resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"Not a git checkout: {repo}")

    commit = git(repo, "rev-parse", args.ref).strip()
    commit_date = git(repo, "show", "-s", "--format=%cs", commit).strip()
    config = json.loads(args.config.read_text(encoding="utf-8"))

    output: list[str] = []
    credits: dict[str, set[str]] = {}
    source_paths: list[str] = []

    for part in config["parts"]:
        output.append(
            "\\partpage"
            f"{{{part['number']}}}"
            f"{{{latex_escape(part['title'])}}}"
            f"{{{latex_escape(part['tagline'])}}}\n"
        )
        for source_path in part["chapters"]:
            raw = git(repo, "show", f"{args.ref}:{source_path}")
            frontmatter, _ = split_frontmatter(raw)
            names = contributor_names(frontmatter)
            credits.setdefault(source_path, set()).update(names)
            source_paths.append(source_path)
            output.append(clean_mdx(raw, args.base_url))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(output), encoding="utf-8")

    credit_names = sorted({name for names in credits.values() for name in names})
    credit_text = ", ".join(credit_names) if credit_names else "See source repository"
    build_date = dt.date.today().isoformat()
    meta = f"""% Generated by scripts/sync_framework.py. Do not edit.
\\newcommand{{\\SourceRef}}{{{latex_escape(args.ref)}}}
\\newcommand{{\\SourceCommit}}{{\\texttt{{{latex_escape(commit[:12])}}}}}
\\newcommand{{\\SourceCommitFull}}{{\\nolinkurl{{{commit}}}}}
\\newcommand{{\\SourceCommitDate}}{{{latex_escape(commit_date)}}}
\\newcommand{{\\BuildDate}}{{{latex_escape(build_date)}}}
\\newcommand{{\\SourceBaseURL}}{{\\url{{{args.base_url.rstrip('/')}}}}}
\\newcommand{{\\FrameworkAuthors}}{{{latex_escape(credit_text)}}}
\\newcommand{{\\SourcePageCount}}{{{len(source_paths)}}}
"""
    args.meta_output.parent.mkdir(parents=True, exist_ok=True)
    args.meta_output.write_text(meta, encoding="utf-8")

    print(f"Synced {len(source_paths)} pages from {args.ref}@{commit[:12]}")


if __name__ == "__main__":
    main()
