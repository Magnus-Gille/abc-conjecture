# claude's draft sections for CONCLUSION.md (to merge with codex's technical body)

Status: DRAFT — status-seal section awaits agent results. For codex review.

## Draft: Preamble / verdict

> Two AI agents (claude — Claude Fable 5; codex — OpenAI Codex, GPT-5-based)
> worked adversarially and cooperatively in this repository on 2026-07-25 to
> prove or disprove the abc conjecture, starting from the prior attempt in
> `firsttryabc.md`. Outcome: **(c) — neither a proof nor a disproof.** Every
> line of attack examined was either refuted, shown to be a known published
> reformulation of abc itself, or reduced exactly to a recognized open
> problem. Both agents independently declared no viable remaining route
> (mailbox 0008, 0010) and co-sign this report. We emphasize what is genuinely
> established: several small rigorous results (an exact certificate-height
> lower bound; an exact minimal certificate for the Reyssat triple; a
> Baker–Wüstholz reduction of a transformation-orbit family to a dynamical
> Wieferich problem; a corrected reading of the prior attempt's §11) — and a
> precise map of why each path stops. Nothing here moves the conjecture.

## Draft: Equivalent reformulations not offering an independent attack
(literature-standard statements; qualitative on purpose; soft attributions
to be tightened only if the final text quotes them)

> Beyond the branches we worked, the standard reformulations were reviewed
> and deliberately not pursued, because each is known to re-encode abc rather
> than weaken it: (i) Szpiro-type conductor–discriminant bounds for Frey
> curves — modified Szpiro is equivalent to abc (Oesterlé, Szpiro, Frey);
> (ii) the modular-degree/congruence-number conjecture deg φ_E ≪ N^{2+ε},
> equivalent to abc-type statements (Frey; Mai–Murty) — modularity of
> elliptic curves (Wiles et al.) is proven, but the polynomial degree bound
> is exactly where abc's content reappears, which is why the FLT machinery
> does not yield abc; (iii) Vojta's height conjecture for P¹∖{0,1,∞} —
> equivalent to abc; its function-field and Nevanlinna analogues are
> THEOREMS (Mason–Stothers; Second Main Theorem), and the dictionary breaks
> precisely at the absence of an arithmetic derivative — which is the same
> obstruction our branch A quantifies via Pasten's equivalence; (iv) power
> of abc as an indicator of depth: abc implies effective Mordell (Elkies)
> and uniform abc over number fields implies no Siegel zeros
> (Granville–Stark); a short proof would effectivize large parts of
> diophantine geometry at once, which calibrates the prior improbability of
> the elementary routes examined here; (v) the unconditional frontier is
> exponential: Stewart–Yu log c ≪ R^{1/3}(log R)³ via linear forms in
> logarithms, and the "one more log" barrier of LFL is a recognized wall
> (our branch E documents its fixed-ω shadow).

## Draft: Heuristic summary (branch C, one paragraph)

> The powerful-skeleton counting model predicts T^{θ−1+o(1)} triples at
> height T with radical exponent θ, hence finitely many above any fixed
> quality 1+δ — abc is expected TRUE with polynomial room. This is evidence,
> not proof: the model assumes independence of additive structure from
> powerful-part structure, which is exactly what no one can prove. All
> unconditional constructions (LTE families, Stewart–Tijdeman/van
> Frankenhuijsen/Bright excess families, our Chebyshev orbit) guarantee only
> sub-polynomial excess; none is proven to sustain, or proven not to
> sustain, a fixed gap. Computation: records unchanged for decades
> [numbers per field-status note], consistent with the model.

## Draft: Status seal (SKELETON — fill from field-status agent + Joshi audit)

> The only claimed proofs are Mochizuki's IUT (published PRIMS 2021; the
> Scholze–Stix objection to IUT-III Cor 3.12 stands unresolved at community
> level; [LANA statement — pending verification]) and Joshi's arithmetic
> Teichmüller route ([reception; our source-level audit findings — pending]).
> Neither is community-accepted as of 2026-07-25. Our own bounded audit
> contributes: [outcomes of the four checker hypotheses]. We are not a
> referee committee; these are audit observations, not adjudication.

## Notification (mechanics)
[Redacted before publication: internal notification-infrastructure details.
The outcome-(c) notification was delivered to Magnus at conclusion time.]
