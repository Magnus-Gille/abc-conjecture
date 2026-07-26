# abc-conjecture collaboration protocol

Two AI agents share this folder. Mission (from Magnus): work together until
(a) the abc conjecture is proven, (b) it is disproven, or (c) both agents agree no
further progress is possible and co-sign a reasoned conclusion. Magnus is pinged via
ratatoskr when (a), (b) or (c) is reached.

## Participants

- **claude** — Claude Fable 5 running in Claude Code CLI. Maintains `STATUS.md`.
- **partner** — second agent (identify yourself in your first mailbox message and
  pick a short lowercase name to use as your file suffix, e.g. `codex`).

## Rules

1. **Mailbox.** All inter-agent communication goes through `mailbox/NNNN-<agent>.md`
   where NNNN is the next free zero-padded integer. Messages are append-only history:
   never edit or delete an existing message (yours or the other's).
2. **Workspaces.** `notes/<agent>/` is each agent's working area. Read the other's
   notes freely; write only under your own name.
3. **STATUS.md** reflects the *agreed* joint state; claude maintains it, partner
   requests corrections via mailbox.
4. **Rigor bar.** No proof-by-assertion. Every claimed lemma gets a proof the other
   agent independently verifies (including numerics). Challenge everything; a claim
   survives only after adversarial checking by both. Never present heuristics as
   theorems. LLM-generated "proofs" of famous conjectures are wrong by default —
   the burden of proof is on the prover.
5. **Termination (outcome c).** We declare (c) when BOTH hold:
   - every proposed attack line has either been refuted, shown circular/equivalent to
     abc itself, or reduced to a recognized open problem, with the obstruction
     documented; and
   - two consecutive exchange rounds produce no new viable line.
   Then either agent drafts `CONCLUSION.md`; both post explicit `SIGNED <date>`
   mailbox messages; claude pings Magnus via ratatoskr.
6. **Outcomes (a)/(b)** require a complete written proof/counterexample family in
   `CONCLUSION.md` that has survived line-by-line adversarial verification by the
   other agent, plus (for b) computational verification of the family. Only then
   ping Magnus.

## File map

- `firsttryabc.md` — prior attempt (read-only artifact, audited).
- `COORDINATION.md` — this protocol.
- `STATUS.md` — agreed joint state.
- `mailbox/` — numbered messages.
- `notes/claude/`, `notes/<partner>/` — per-agent working notes.
- `CONCLUSION.md` — final joint statement (end state).
