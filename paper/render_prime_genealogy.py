#!/usr/bin/env python3
"""Render the audited Markdown working draft as standalone LaTeX."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "prime-genealogy-draft.md"
TARGET = ROOT / "prime-genealogy-draft.tex"

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{geometry}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{hyperref}
\geometry{margin=1in}
\hypersetup{
  colorlinks=true,
  linkcolor=blue!45!black,
  urlcolor=blue!55!black,
  pdftitle={Prime genealogy in Chebyshev abc-orbits},
  pdfauthor={Magnus Gille}
}
\setlist{nosep,leftmargin=1.5em}
\setcounter{secnumdepth}{0}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\emergencystretch=2em
\title{Prime genealogy in Chebyshev \(abc\)-orbits:\\
interleaved Lucas atoms and exact radical telescopes}
\author{Magnus Gille\\Independent researcher}
\date{Research draft, July 2026}
\begin{document}
\maketitle
"""

POSTAMBLE = "\\end{document}\n"


def convert_inline(text: str) -> str:
    """Convert the small Markdown inline subset used by the manuscript."""
    text = re.sub(r"<(https?://[^>]+)>", r"\\url{\1}", text)
    text = re.sub(r"`([^`]+)`", r"\\texttt{\1}", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*([^*]+)\*", r"\\emph{\1}", text)
    return text


def heading(text: str) -> str:
    """Give hyperref a plain-text fallback for headings containing math."""
    converted = convert_inline(text)
    plain = re.sub(r"\\\((.*?)\\\)", r"\1", text)
    replacements = {
        r"\ell": "ell",
        r"\varepsilon": "epsilon",
        r"\mathbb": "",
        r"\operatorname": "",
    }

    for source, target in replacements.items():
        plain = plain.replace(source, target)

    plain = plain.replace("{", "").replace("}", "")
    plain = plain.replace("\\", "")
    plain = re.sub(r"\*\*|\*", "", plain)

    if converted == plain:
        return converted

    return f"\\texorpdfstring{{{converted}}}{{{plain}}}"


def convert() -> str:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    output: list[str] = [PREAMBLE]
    in_abstract = False
    in_items = False
    in_quote = False

    # The title, author, affiliation, and date are represented in PREAMBLE.
    cursor = 0
    while cursor < len(lines) and not lines[cursor].startswith("> Working-draft"):
        cursor += 1

    while cursor < len(lines):
        line = lines[cursor]
        stripped = line.strip()

        if stripped.startswith("> "):
            if not in_quote:
                output.append("\\begin{quote}\\small")
                in_quote = True
            output.append(convert_inline(stripped[2:]))
            cursor += 1
            continue

        if in_quote:
            output.append("\\end{quote}")
            in_quote = False

        if stripped.startswith("- "):
            if not in_items:
                output.append("\\begin{itemize}")
                in_items = True
            output.append(f"\\item {convert_inline(stripped[2:])}")
            cursor += 1
            continue

        if in_items:
            output.append("\\end{itemize}")
            in_items = False

        if stripped == "## Abstract":
            output.append("\\begin{abstract}")
            in_abstract = True
        elif stripped.startswith("## "):
            if in_abstract:
                output.append("\\end{abstract}")
                in_abstract = False
            output.append(f"\\section{{{heading(stripped[3:])}}}")
        elif stripped.startswith("### "):
            output.append(
                f"\\subsection{{{heading(stripped[4:])}}}"
            )
        elif stripped == "#### Proof":
            output.append("\\paragraph{Proof.}")
        else:
            output.append(convert_inline(line))

        cursor += 1

    if in_items:
        output.append("\\end{itemize}")
    if in_quote:
        output.append("\\end{quote}")
    if in_abstract:
        output.append("\\end{abstract}")

    output.append(POSTAMBLE)
    rendered = "\n".join(output)

    # Emphasis markers can span source line wraps in reference entries.
    return re.sub(r"\*([^*]+)\*", r"\\emph{\1}", rendered)


def main() -> int:
    TARGET.write_text(convert(), encoding="utf-8")
    print(TARGET)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
