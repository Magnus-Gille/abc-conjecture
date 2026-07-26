# abc Conjecture — Field Status & Citation Verification (as of 2026-07-25)

## Part A — Citation verification

**A1. Curtis Bright, arXiv:2301.11056 — CONFIRMED.**
Title "A New Lower Bound in the *abc* Conjecture"; published *Canadian Mathematical Bulletin* 67 (2024), 369–378. Abstract (fetched verbatim): proves infinitely many coprime a+b=c with c > rad(abc)·exp(6.563·√(log c)/log log c). Title, journal, and constant 6.563 all confirmed exactly as claimed.

**A2. Ghioca–Nguyen–Tucker, arXiv:1608.01361 — CONFIRMED.**
Title "Squarefree Doubly Primitive Divisors in Dynamical Sequences," authors Dragos Ghioca, Khoa D. Nguyen, Thomas J. Tucker. Abstract states the proof "assumes a conjecture of Vojta in the number field case and is unconditional in the function field case thanks to a deep theorem of Yamanoi" — matches the claim exactly.

**A3. Hector Pasten, arXiv:1705.09251 — CONFIRMED (full text).**
Title "Shimura curves and the abc conjecture," sole author Hector Pasten. Read Section 15 ("Linear forms in logarithms," pp. 62–65) of the full PDF directly. Proposition 15.1 states verbatim: for ν = ω(abc), d(abc)/(log d(abc))^ν < C_ε^ν·ν^(2ν²)·rad(abc)^(1+εν) — matching the claimed shape exactly (paper's ε ↔ claim's δ, C_ε ↔ C, rad(abc) ↔ R).

**A4. Project LANA statement, zen.ac.jp/news/zmcpostevent0717e — CONFIRMED.**
Fetched both the English page (zmcpostevent0717e) and its Japanese original (zmcpostevent0717, dated 17 July 2026, linked from each other). This is an official interim-report post from ZEN University's Zen Mathematics Center (ZMC). It confirms judgment on IUT/abc remains suspended, explicitly citing unresolved points "in the process of deriving Corollary 3.12 from Theorem 3.11 in the third IUT paper," centered on whether two q-pilot log-volume calculations are "tautologically equivalent." "Project LANA" = **"Lean for ANAbelian geometry"** (per ZMC's own announcement page, zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f): a Lean-proof-assistant formalization effort to (1) formalize anabelian geometry and (2) formally verify IUT theory "from a neutral point of view" to end the controversy. Activity began fall 2023, full launch Sept 2024, publicly announced 31 Mar 2026; led by Fumiharu Kato with core members Johan Commelin, Kiran Kedlaya, Yuichiro Hoshi, Adam Topaz plus ~7 younger researchers. Caveat: Mochizuki's own RIMS page separately posted an 8 Apr 2026 "Formalization of IUT" talk; unclear if this is the same effort or a distinct, parallel one.

**A5. Robert–Stewart–Tenenbaum, "A refinement of the abc conjecture" — CONFIRMED.**
Olivier Robert, Cameron L. Stewart, Gérald Tenenbaum, *Bulletin of the London Mathematical Society* 46(6) (2014), 1156–1166. Pulled the raw LaTeX source to avoid rendering ambiguity: c < k·exp(4√(3 log k/log log k)·(1 + (log log log k)/(2 log log k) + C₁/log log k)), k = rad(abc). I.e. log(c/R) ~ K√(log R/log log R) with **K = 4√3 ≈ 6.928** — just above Bright's proven lower-bound constant 6.563 (A1), as expected for a conjectured extremal order vs. a proven bound.

## Part B — Field status, July 2026

**Mochizuki/IUT.** No broad community acceptance; status unchanged since 2018–2021. Scholze–Stix's Aug 2018 objection to Corollary 3.12 (IUT-III) stands unretracted, still treated by most number theorists as unresolved (J. D. Boyd's Sept 2025 report, via Woit's blog: "most mathematicians view the ease with which an immediate contradiction can be derived from the setup as a sign to move on"). Mochizuki has issued no direct 2024–2026 rebuttal of Scholze–Stix specifically; his recent output targets Joshi (Mar 2024) and Boyd's "Kyoto echo chamber" framing (Oct 2025). Zen University's Inter-universal Geometry Center (IUGC, est. June 2023) runs two Kawakami-funded prizes: the $1M "Challenger Prize" for a peer-reviewed paper proving an essential IUT flaw (unclaimed as of Jul 2026), and the $20K–100K/yr "Innovator Prize" (1st awarded 2 Apr 2024 to Mochizuki, Fesenko [declined], Hoshi, Minamide, Porowski for "Explicit estimates in inter-universal Teichmüller theory," *Kodai Math. J.* 45 (2022) — no later-year winner found). Project LANA's 17 Jul 2026 interim report (A4) is the most concrete 2026 development and changes nothing substantive: judgment remains suspended.

**Kirti Joshi.** Series "Construction of Arithmetic Teichmuller Spaces" I–IV (2021–2024); IV = "...Proof of the abc-conjecture" (arXiv:2403.10430, rev. Feb 2025). His Apr 2025 "Final Report on the Mochizuki–Scholze–Stix Controversy" (arXiv:2505.10568) claims to refute Scholze–Stix and complete the proof, conditional on his own enhancements being accepted; further FAQ/status documents followed (Nov 2025, sites.arizona.edu/kirti-joshi). Mochizuki's Mar 2024 report calls Joshi "profoundly ignorant" of IUT's actual content and says the series has "no meaningful mathematical content whatsoever." Scholze and the wider community remain unconvinced (Woit, Sep 2025: "experts I've asked are all pessimistic that Joshi really has a proof"). No part of the series has peer-reviewed acceptance.

**Other 2024–2026 claims.** None found credible. Patrick Letendre's "The abc Conjecture Revisited" (arXiv:2607.07641, 8 Jul 2026) proposes a *different*, new abc-type conjecture — not a proof or disproof of the original. Two self-published Zenodo items surfaced (L. S. Harris, 27 Jul 2025; C. Pompetzki, 8 Mar 2026, non-serious/meme-laden) with no peer review, minimal engagement, and no citations — not credible.

**Computational records.** Eric Reyssat's triple 2 + 3¹⁰·109 = 23⁵ (rad = 15,042, quality ≈1.6299) is still listed as the top-quality triple on Wikipedia's current abc-conjecture page. ABC@Home (BOINC/Leiden) exhaustively found all triples with c < 10¹⁸ by 2011, then non-exhaustively extended through 2012–2015 to roughly 23.8 million triples total before winding down (Wikipedia: "By 2015 the project had found 23.8 million triples ... and ceased operations soon after"). The commonly cited figure of 23,827,716 triples under c < 2⁶³ is consistent with this, though I could not independently confirm that exact integer from a primary source this session. No newer exhaustive enumeration was found.

**Best unconditional bounds.** Stewart–Yu (2001), log c ≪ R^(1/3)(log R)³, remains the standing *general-case* bound. Hector Pasten's "The largest prime factor of n²+1 and improvements on subexponential ABC" (arXiv:2312.03566, Dec 2023; *Inventiones Math.* 236 (2024)) combines Shimura-curve methods with Stewart–Yu transcendence theory to give "the first improvement on a result by Stewart and Yu dating back over two decades" — but only in a restricted subexponential regime, not the general exponent. Separately, Bernert–Browning–Lichtman–Teräväinen (arXiv:2410.12234, Oct 2024, rev. May 2026) obtain "a power-saving bound on the size of the exceptional set" of triples violating a fixed quality — a distinct counting/density question, not the same bound.

## Sources
- Bright, "A New Lower Bound in the abc Conjecture": https://arxiv.org/abs/2301.11056
- Ghioca, Nguyen, Tucker, "Squarefree Doubly Primitive Divisors in Dynamical Sequences": https://arxiv.org/abs/1608.01361
- Pasten, "Shimura curves and the abc conjecture": https://arxiv.org/abs/1705.09251 (full PDF: https://arxiv.org/pdf/1705.09251)
- Robert, Stewart, Tenenbaum, "A refinement of the abc conjecture," BLMS 46(6) 2014: https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/blms/bdu069 ; abstract mirror: https://academic.oup.com/blms/article-abstract/46/6/1156/2254710
- Wikipedia, abc conjecture (RST refined conjecture, raw source checked): https://en.wikipedia.org/wiki/Abc_conjecture ; raw wikitext: https://en.wikipedia.org/w/index.php?title=Abc_conjecture&action=raw
- Project LANA interim report (English): https://zen.ac.jp/news/zmcpostevent0717e ; (Japanese original): https://zen.ac.jp/news/zmcpostevent0717
- ZMC, Project LANA announcement: https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f
- Mochizuki news index (RIMS): https://www.kurims.kyoto-u.ac.jp/~motizuki/news-english.html
- Mochizuki, "Report on the recent series of preprints by K. Joshi" (Mar 2024): https://www.kurims.kyoto-u.ac.jp/~motizuki/Report%20on%20a%20certain%20series%20of%20preprints%20(2024-03).pdf
- Peter Woit, "Not Even Wrong" — abc category: https://www.math.columbia.edu/~woit/wordpress/?cat=33 ; "Two Number Theory Items (and Woody Allen)" (20 Sep 2025): https://www.math.columbia.edu/~woit/wordpress/?p=15277
- Zen University/IUGC, prize establishment: https://zen.ac.jp/news/0ul6zqed9-0 ; IUT Challenger Prize: https://zen.ac.jp/en/lp/icp
- Zen University/IUGC, 1st Innovator Prize announcement: https://zen.ac.jp/news/d-5ye560_l ; https://zen.ac.jp/en/iugc/topics/n7yb1b-ow0
- Joshi, "Construction of Arithmetic Teichmuller Spaces IV": https://arxiv.org/abs/2403.10430
- Joshi, "Final Report on the Mochizuki-Scholze-Stix Controversy": https://arxiv.org/abs/2505.10568
- Joshi, FAQ (Nov 2025): https://sites.arizona.edu/kirti-joshi
- Letendre, "The abc Conjecture Revisited": https://arxiv.org/abs/2607.07641
- Harris, Zenodo preprint (27 Jul 2025): https://zenodo.org/records/16505191
- Pompetzki, Zenodo preprint (8 Mar 2026): https://zenodo.org/records/18916301
- Pasten, "The largest prime factor of n^2+1 and improvements on subexponential ABC": https://arxiv.org/abs/2312.03566 ; journal version: https://link.springer.com/article/10.1007/s00222-024-01244-6
- Bernert, Browning, Lichtman, Teräväinen, "Bounds on the exceptional set in the abc conjecture": https://arxiv.org/abs/2410.12234
- Wikipedia, ABC@Home: https://en.wikipedia.org/wiki/ABC@Home
- Bart de Smit, ABC triples database (Leiden): https://pub.math.leidenuniv.nl/~smitbde/abc/
- Lifeboat News, "Effort to solve biggest controversy in mathematics has made no progress" (22 Jul 2026): https://lifeboat.com/blog/2026/07/effort-to-solve-biggest-controversy-in-mathematics-has-made-no-progress
