# Priority/Novelty Search — (4ab,(a−b)²,c²) duplication orbit from (1,8,9)

Method note: arXiv API rate-limited one query (not retried); findings rest on WebSearch/WebFetch of arxiv.org, ams.org, and author pages. One extraction (flagged below) is unverified.

## 1. Browkin & Brzeziński, Math. Comp. 62 (1994), 931–939
**Verdict: NO OVERLAP FOUND.** Citation: Browkin, J.; Brzeziński, J., "Some remarks on the abc-conjecture," Math. Comp. 62 (1994), 931–939. https://www.ams.org/journals/mcom/1994-62-206/ (the specific article URL 403'd; bibliographic data cross-confirmed via Wikipedia "Jerzy Browkin" and multiple citing papers). Content is the **n-term generalization** of abc (the "n-conjecture"): a construction from the geometric-sum identity Σᵢ₌₀^{k-3} yⁱ=(y^{k-2}-1)/(y-1) (x:=y-1) producing n-tuples summing to 0 with largest limit point ≥ 2n−5. Unrelated to any quadratic duplication map. Nitaj's page separately credits Browkin & Brzeziński as contributors of individual high-quality abc-triple *examples* to standard tables — presumably computational finds, not from (4ab,(a−b)²,c²).

## 2. Nitaj's abc conjecture home page
**Verdict: NO OVERLAP FOUND.** https://nitaj.users.lmno.cnrs.fr/abc.html. Direct fetch confirms it catalogs known triples/tables (quality, size, merit) and lists three conjecture *generalizations* (n-term: Browkin–Brzeziński 1994; Baker's abc 1996; Hu–Yang k-term 2002). No duplication/doubling identity and no (1,8,9)-seeded orbit appear anywhere on the page.

## 3. abc triples via iteration/recurrence/dynamical systems
**Verdict: ADJACENT, with one important OVERLAP.**
- Martin & Miao, "abc triples," arXiv:1409.2974 (2014), §2.4, give a *different* quadratic self-map: if (a,b,c) is an abc triple then so is (a²,c(b−a),b²); iterated on (1,c−1,c) → (1,c²−2c,(c−1)²). Applied to (1,8,9) this yields (1,63,64) — not the target's (32,49,81); confirmed algebraically distinct. Nearest kin found; must be cited.
- Alvarez-Salazar, Barrios, Henaku, Soller, "On abc triples of the form (1,c−1,c)," arXiv:2301.01376 = Integers 23 (2023) #A64, studies exactly the (1,b,b+1) shape containing (1,8,9). Its bibliography documents the classical "ε can't be 0" lineage: **Jastrzębowski & Spielman** (communicated to Lang, Bull. AMS 23 (1990) 37–75) gave (1, 3^(2^k)−1, 3^(2^k)) — **c-values 9, 81, 6561,… identical to the target's c_n = 9^(2^n)**. This growth tower is the standard example since 1990, reused by Stewart [1984], Granville–Tucker ("It's as easy as abc," Notices AMS 49 (2002) 1224–1231), and Barrios (2023). **OVERLAPS: the c_n growth law is prior art**; the target's (aₙ,bₙ) split via 4ab/(a−b)² differs from the classical 1/(c^{2^k}−1) split, so the orbit itself differs, but this must be cited, not presented as new.
  - Caveat: one AI extraction over 1409.2974 additionally reported a "(1,8,9)-seeded c_{n+1}=c_n⁴−4c_n³+4c_n²" construction; repeating the same method on 2301.01376 did not reproduce it. **Unverified/possible hallucination** — confirm against the actual PDF before citing.
- Stewart–Tijdeman (1986) and van Frankenhuijsen's refinements build extremal-quality families via smooth/friable-number counting, not iterated squaring. NO OVERLAP on method, same goal.
- Idowu, "Symbolic Generation and Modular Embedding of High-Quality abc-Triples," arXiv:2506.10039 (2025): modular-inverse parametrization in ℤ/3^pℤ; lists (1,8,9) only as a table entry, not a seed; no Lucas/Wieferich/Baker content. ADJACENT (recent, same goal, unrelated method).

## 4. Squarefree/powerful parts of Lucas sequences; Wieferich equivalence
**Verdict: NO OVERLAP on the exact equivalence; strong adjacent lineage that must be cited.**
- Stewart, Acta Math. 211 (2013) 291–314 (arXiv:1008.1274): lower bound for the greatest prime factor of Lucas/Lehmer terms (resolves Schinzel 1962, Erdős 1965). Prime-factor growth, not squarefree/powerful parts, not abc-linked.
- McDaniel & Ribenboim, "Square classes in Lucas sequences having odd parameters," J. Number Theory 73 (1998) 14–27: squarefree-part ("square-class") machinery for Lucas sequences — adjacent tool, not abc-linked.
- Ribenboim & Walsh, "The ABC conjecture and the powerful part of terms in binary recurring sequences," J. Number Theory 74 (1999) 134–147: abc ⇒ powerful parts of binary recurring sequence terms stay bounded. One-directional, general sequences.
- Murty & Wong, "The ABC conjecture and prime divisors of the Lucas and Lehmer sequences," Number Theory for the Millennium III (2002) 43–54: abc ⇒ P(aⁿ−bⁿ) ≫ n^(2−ε). One-directional, prime-factor flavor, not Wieferich-lift accumulation.
- Silverman, "Wieferich's criterion and the abc-conjecture," J. Number Theory 30 (1988) 226–237: abc ⇒ ≫log X non-Wieferich primes below X for any base a>1 — the "known adjacent" the brief flagged; confirmed.
- Anitha, Fathima & Vijayalakshmi, arXiv:2101.04901 (Funct. Approx. Comment. Math. 60(2)): abc-for-number-fields ⇒ ≫log x Lucas non-Wieferich primes p≡±1 (mod k). One-directional, general parameters.

All five are **one-directional** (abc, as a global hypothesis, ⇒ existence/density of non-Wieferich primes in a *general* family); none states a two-way equivalence between one orbit's abc-quality limit and Wieferich-lift accumulation in one companion sequence V_m(2,9). That equivalence appears genuinely new — this lineage is its direct ancestry and must be cited.

## 5. Anything else
No hit for Chebyshev-polynomial-based abc constructions in this sense (only an unrelated Markoff-equation paper). No hit for "duplication formula" as abc-conjecture terminology. No match for the specific two-log Baker setup (z=(7+4i√2)/9, non-root-of-unity argument). This sub-search was least exhaustive (arXiv API rate-limited mid-run); recommend one follow-up pass on Baker/linear-forms-in-logs applied to Lucas–Lehmer-type doubling recursions before submission.

## Addendum (coordinator follow-ups, time-boxed)
- **OEIS A025172** — CONFIRMED MATCH. Terms 1, 1, −7, −23, 17, 241, 329, −1511, −5983, 1633, 57113,… match exactly (signs included). OEIS states this sequence **equals (1/2)·V(n,2,9)**, i.e. exactly the Lucas sequence in the target's Baker step, with the closed form cos(nφ)=a(n)/3ⁿ for φ=arccos(1/3) (historically used for Hilbert's 3rd problem, scissors-congruence of the regular simplex). No mention of Wieferich primes or the abc conjecture on the visible OEIS record — direct fetch of oeis.org/A025172 403'd, so the full reference/comment list is **NOT CHECKED**; worth a manual look for any b-file/comment added post-indexing.
- **Ghioca–Nguyen–Tucker, Trans. AMS 370 (2018), 1119–1136** — **NOT CONFIRMED / NOT CHECKED** within the time budget. Could not locate this exact paper+venue+page combination; searches surfaced Ghioca–Nguyen–Ye, "The dynamical Manin–Mumford and dynamical Bogomolov conjectures for endomorphisms of (P¹)ⁿ," Compositio Math. 154 (2018) 1441–1472 (different venue/pages/coauthor), and Bombieri–Masser–Zannier, IMRN 1999, 1119–1140 (matching page range, wrong authors/year). Do not cite the Ghioca–Nguyen–Tucker reference until independently verified against MathSciNet/zbMATH.
- **Stewart, Acta Math. 211 (2013), 291–314** — CONFIRMED (see §4 above): bound shape is P(u(n)) ≳ n·exp(log n / (104 log log n)), resolving Schinzel (1962) and Erdős (1965); first general improvement on Bang (1886)/Carmichael (1912). arXiv:1008.1274.

## Overall verdict
- **Transformation (4ab,(a−b)²,c²):** not found verbatim anywhere searched; nearest kin is Martin–Miao's different map (a²,c(b−a),b²) (arXiv:1409.2974) — cite and distinguish explicitly.
- **(1,8,9) orbit / c_n=9^(2^n):** the c-value tower duplicates the classical Jastrzębowski–Spielman (1990) sequence — cite Lang 1990, Granville–Tucker 2002, Barrios et al. 2023; the (aₙ,bₙ) decomposition differs and is the actual new content here.
- **R_n<(2/3)c_n "abc hit" family:** same strength/genre as the 1990–2023 "ε≠0" lineage above, not a stronger result — must cite and position accordingly, not claim as a novel bound.
- **Baker elimination (two-log, z=(7+4i√2)/9):** no match found in this search; plausibly novel pending the recommended follow-up.
- **Wieferich equivalence:** the general paradigm (abc ⇔ Wieferich-type behavior in a recurrence) is well precedented (Silverman 1988; Murty–Wong 2002; Ribenboim–Walsh 1999; Anitha et al. 2021); the precise single-orbit two-way equivalence was not found and appears to be the paper's real contribution — frame it explicitly as sharpening/localizing this known paradigm, with full citations to all four.
