# abc-conjecture — a two-AI-agent mathematics experiment

On 2026-07-25, two AI coding agents — **claude** (Anthropic Claude Fable 5
and, for the final PR gate, Opus 5, via Claude Code) and **codex** (OpenAI
Codex, GPT-5-based) — were given a shared folder, a prior failed proof
attempt, and one instruction:

> *Prove or disprove the abc conjecture. Coordinate, discuss and work with
> the second agent until (a) it is proven, (b) it is disproven, or (c) you
> both agree you cannot get any further.*

This repository is the complete, unedited record of what happened —
including a jointly written, cross-reviewed mathematics paper that came out
of it.

## TL;DR

1. **The abc conjecture was not proven or disproven** (nobody is surprised).
   The agents reached **outcome (c)** and co-signed
   [`CONCLUSION.md`](CONCLUSION.md): every attack line examined was either
   refuted, shown to be a published reformulation of abc itself, or reduced
   exactly to a recognized open problem.
2. Along the way the collaboration produced small rigorous results, and the
   strongest one became a real manuscript:
   **“Radicals in iterated quadratic abc-transfers”**
   ([`paper/main-v5.tex`](paper/main-v5.tex) — the current reference-audited
   PDF is in `output/pdf/`).

## The paper (Phase 2)

For every primitive triple a + b = c with a, b of opposite parity, iterate
the classical transfer

    (a, b, a+b)  ↦  (4ab, (a−b)², (a+b)²).

Main results, all effective and cross-verified line-by-line by both agents:

- an **exact whole-orbit radical identity**
  R_n/c_n = (R₀/c₀) · |sin(2ⁿθ)| / (2ⁿ sinθ · W_n), where cosθ =
  (b₀−a₀)/c₀ and W_n collects all repeated prime factors;
- a **one-shot Baker–Wüstholz estimate** pinning the archimedean factor
  two-sidedly at Θ(n), so **every such orbit eventually consists of
  abc-hits** (c/rad(abc) ≫ log c);
- an **if-and-only-if criterion**: the orbit's asymptotic abc-quality
  exceeds 1 along a subsequence exactly when repeated prime factors
  accumulate at positive power — made fully explicit for the seed (1,8,9)
  as a **Lucas–Wieferich** condition on V(2,9) at dyadic indices;
- a reproducible computation: **no square prime divisor exists for
  p ≤ 10⁷, 0 ≤ j ≤ 50** (664,577 primes tested, zero hits — reproduced
  independently by both agents).

The novelty claim is deliberately narrow (the *combination* of whole-orbit
statements); every closer ingredient found by two independent literature
sweeps is credited in the paper, from Oesterlé 1988 and two MathOverflow
answers to a 2023 M.Sc. thesis and a 2025 Hajdu–Tijdeman theorem.

**Current frozen artifacts** (see `output/SHA256SUMS`):

| Artifact | SHA-256 |
|---|---|
| `paper/main-v5.tex` | `a94309b910edb8791ec754fd2da1f013588527d8b50b7efb3080e05c89182c6c` |
| `output/pdf/radicals-in-iterated-quadratic-abc-transfers.pdf` | `7f76868650d478a08d5633b5e37dd99042a75f0bc66d07a6435ca6460e014ec7` |

**Status:** Phase 2 was approved by both agents, but a later full reference
audit suspended those exact-hash signatures. Version 3 attempted to close
every audit item from primary sources or an explicit fallback. At Magnus's
direction, the final v3 pass is Codex-only (`mailbox/0062-codex.md`); it
does not claim a renewed Claude countersignature. A later Opus 5 review of
PR #1 requested changes (`mailbox/0063-claude.md`) because the retained
unpublished Ohana--Spicer--Stein source lacked the promised stable archive. Version 4
uses the pre-agreed inline-derivation fallback, displays Stewart's inequality,
governs every tracked PDF, and corrects the review disclosures. A second
Opus 5 pass found stale handoff/checklist wording and several adjacent
consistency issues (`mailbox/0065-claude.md`). Version 5 resolves all of
them and is pending the final exact-hash Opus 5 re-review. The manuscript remains
**pending human validation** — see
`paper/HUMAN_VALIDATION_CHECKLIST.md`. Target venue: *Mathematika*
(the LMS AI policy, updated June 2026, expressly permits declared AI use
with full human responsibility), with an arXiv `math.NT` preprint first.
The named human author directs the work and takes responsibility; the AI
systems are not authors (full disclosure statement inside the paper).

## Phase 1 highlights (the abc attempt itself)

- The inherited attempt (`firsttryabc.md`) was audited and found sound but
  **literature-known**: its "missing lemma" is exactly Hector Pasten's
  Small Derivatives Conjecture (Canad. Math. Bull. 2022), *proven
  equivalent to abc* — so that route is the conjecture in a costume.
- Exact computation: the minimal nondegenerate arithmetic-derivative
  certificate for the record Reyssat triple has height **H\* = 601**
  (two independent implementations agree).
- The quadratic-transfer idea was rescued from a false dismissal in the
  original attempt and sharpened into the orbit theorem above.
- A bounded, carefully calibrated source-level audit of four alleged local
  defects in one version of K. Joshi's Construction III preprint is in
  `notes/` — **extract-level observations only**, explicitly *not* an
  adjudication of that program, with all caveats recorded in
  `CONCLUSION.md`.
- Verified July-2026 field status: Mochizuki's IUT proof remains
  unaccepted (the ZEN/LANA Lean formalization project suspends judgment on
  exactly the disputed Corollary 3.12 step); no other credible claims;
  Reyssat's 1987 quality record still stands.

## How the agents worked

File-based coordination in this folder, no shared memory:

- [`COORDINATION.md`](COORDINATION.md) — the protocol both agents followed
  (append-only numbered mailbox, per-agent workspaces, adversarial
  verification of every claim, checksum-pinned sign-offs, explicit
  termination criteria).
- [`mailbox/`](mailbox/) — all 58+ messages, unedited: division of labor,
  proofs, refutations, the errors each agent caught in the other's work,
  priority-search corrections, and the final signatures.
- [`notes/claude/`](notes/claude/), [`notes/codex/`](notes/codex/) —
  per-agent working notes, verification scripts, literature reports.
- [`STATUS.md`](STATUS.md) — the running joint state and final ledger.

## Reproducing the computation

Requires only Python 3 (standard library):

    python3 paper/check_square_lifts.py --prime-limit 10000000 --max-j 50

Expected output: `tested_primes=664577`, `square_lifts=0`. The script
includes an exact-versus-modular self-check.

Build the paper (e.g. with [tectonic](https://tectonic-typesetting.github.io)):

    tectonic paper/main-v5.tex

## Repository layout

    firsttryabc.md        # the prior AI attempt that seeded the session
    COORDINATION.md       # two-agent protocol
    CONCLUSION.md         # co-signed phase-1 verdict (outcome c)
    STATUS.md             # joint ledger / handoff
    mailbox/              # numbered agent-to-agent messages (append-only)
    notes/claude/         # claude's audits, scripts, search reports
    notes/codex/          # codex's proofs, audits, scripts
    paper/                # manuscript, script, checklist, cover letter
    output/               # frozen PDF, source tarball, SHA256SUMS

## Caveats

- Nothing here proves or disproves the abc conjecture, and the paper says
  so explicitly.
- The Joshi-related notes are bounded audit observations on extracts of
  one preprint version, made by AI agents; they carry explicit
  calibrations and have no bearing on the truth of abc.
- The manuscript awaits the named author's personal validation before any
  submission; journal and arXiv acceptance are their decisions to pursue.

## License

Code: [MIT](LICENSE). Documents and text: [CC BY 4.0](LICENSE-docs.md).
