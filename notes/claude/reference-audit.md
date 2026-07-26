# Reference audit — main-v2.tex ("Radicals in iterated quadratic abc-transfers")

Audit date: 2026-07-26. Method: WebFetch/WebSearch/curl on primary sources where
possible; where primary sources were paywalled or otherwise unfetchable, direct
`curl` download of the PDF followed by local text extraction (`pypdf`) and/or
vision-based reading, or independent secondary quotations. All quotes below are
transcribed verbatim from the source (OCR/extraction artifacts in bracketed
sources are noted where they affect legibility, e.g. Voutier 1996 numdam scan).

Grades used: **EXISTS+CONTENT-VERIFIED** / **EXISTS+CONTENT-PARTIAL** /
**METADATA-MISMATCH** / **NOT-FOUND**.

---

## 1. Baker–Wüstholz, "Logarithmic forms and group varieties" (1993) [CRITICAL]

**Grade: EXISTS+CONTENT-VERIFIED**

Metadata (Crossref DOI 10.1515/crll.1993.442.19): container-title "Journal für die
reine und angewandte Mathematik (Crelles Journal)", volume 1993, issue 442, pages
19–62, published 1993-09-01. Crossref's own author list is empty (a metadata gap
common to older Crelle records), but authorship "A. Baker and G. Wüstholz" is
confirmed by every secondary source below and is undisputed in the literature.

The original is paywalled (de Gruyter). Per instructions, I obtained **three**
independent secondary quotations of the theorem (exceeding the required two),
all restating it as "Theorem 4.2" / "Theorem 3" / "Theorem 2" in their own
numbering, all attributing it to Baker–Wüstholz [1993], and all giving **the
identical constant formula, height definition, and B-convention**:

**Source A** — K. C. Chim, PhD thesis, TU Graz, supervised by Gisbert Wüstholz
himself (`webfetch` saved copy, 167pp), p.92:
> "Theorem 4.2. If Λ = L(logα₁,...,logα_k) ≠ 0, then
> log|Λ| ≥ −C(k,d)h′(α₁)⋯h′(α_k)h′(L), where
> C(k,d) = 18(k+1)!k^(k+1)(32d)^(k+2)log(2kd)."

and p.91 for the height: "h′(α) = (1/d)max{h(α),|logα|,1}, where h(α)=d·h₀(α) is
the standard logarithmic Weil height of α" (h₀ being the *absolute* logarithmic
Weil height). And p.92: "If we write B = max{|b₁|,...,|b_k|,e}, then we get
h′(L) ≤ log B."

**Source B** — Chim & Ziegler, "On Diophantine equations involving sums of
Fibonacci numbers and powers of 2", arXiv:1705.06468, p.3–4, identical statement
verbatim as "Theorem 3", same constant, same h′, same B convention.

**Source C** — Chim, Pink & Ziegler, "On a variant of Pillai's problem",
arXiv:1604.04719, p.3, identical statement verbatim as "Theorem 2", same
constant, same h′, same B convention.

**Checking each element the paper claims:**
- Constant formula `C(n,d)=18(n+1)!·n^(n+1)·(32d)^(n+2)·log(2nd)` — **exact
  match** (sources use k in place of n).
- `h'(α) = max(h(α), |log α|/d, 1/d)` — mathematically **identical** to the
  sources' `h'(α)=(1/d)max{h(α)_source,|logα|,1}`, once one notes the sources'
  "h(α)_source" is d times the *absolute* height, i.e. `h(α)_source/d = h₀(α)`.
  Main-v2.tex's own "h(α)" is the absolute/normalized height throughout (its
  §3 computes `h(z)=½log c₀` directly via the Mahler-measure formula, which
  *is* the absolute height h₀) — so this is a labeling-convention difference,
  not a mathematical discrepancy.
- Strict vs. non-strict B: the source theorem **defines** B := max(|b₁|,...,
  |b_k|,e), a non-strict relation (B literally equals the max, with a floor of
  e ≈ 2.718). The theorem's conclusion remains valid for any B′ ≥ this value
  (since h′(L) ≤ log B ≤ log B′). Main-v2.tex's own use ("For n≥2, take the
  strict coefficient bound B=2N≥8") is the paper's own conservative choice of
  a value comfortably larger than the true coefficient bound N — this is a
  legitimate application, not a misstatement of the source's B-convention.
  There is no "strict <" requirement in the source theorem itself; the floor
  is B≥e, and B=2N≥8 (for n≥2, N≥4) comfortably satisfies it.

**Conclusion:** every element checked (constant, h′ definition, B floor and
convention) matches across three independent citing documents.

---

## 2. Z.-H. Sun, "Congruences concerning Lucas' law of repetition", arXiv:1312.3511 [CRITICAL]

**Grade: EXISTS+CONTENT-VERIFIED**

Downloaded the PDF directly (`arxiv.org/pdf/1312.3511`, 8pp; the arXiv MCP tool
could not convert this PDF-only paper — "PDF conversion requires the pdf
extra" — so I fetched and read it directly instead). Theorem 3, p.6:

> "**Theorem 3.** Let P,Q∈Z, PQ(P²−Q)(P²−4Q)≠0, (P,Q)=1, U_n=U_n(P,Q) and
> V_n=V_n(P,Q).
> (i) If p is an odd prime such that p|U_m (m≥1), then
> ord_p U_m = ord_p m + ord_p U_{p−(P²−4Q/p)}.
> (ii) If p is an odd prime such that p|V_m (m≥1), then
> ord_p V_m = ord_p m + ord_p U_{p−(P²−4Q/p)}."

This is **exactly** Theorem 3(ii) as the manuscript states it (ord_p = v_p,
(P²−4Q/p) = (D/p)). Hypothesis check for (P,Q)=(2,9): PQ=18≠0; P²−Q=4−9=−5≠0;
P²−4Q=4−36=−32≠0 (= D, matching the manuscript's stated D=−32 exactly);
gcd(P,Q)=gcd(2,9)=1. **All four hypotheses are satisfied.**

---

## 3. C. L. Stewart, "On divisors of Fermat, Fibonacci, Lucas and Lehmer numbers, III" (1983) [CRITICAL]

**Grade: EXISTS + CONTENT-PARTIAL**

Metadata (Crossref DOI 10.1112/jlms/s2-28.2.211): "On Divisors of Fermat,
Fibonacci, Lucas and Lehmer Numbers, III", J. London Math. Soc., vol s2-28,
issue 2, pp. 211–217, October 1983, author C. L. Stewart. **Exact match** to
the manuscript's citation.

The original is paywalled (Oxford Academic returned HTTP 403 on direct PDF
fetch, confirmed by `curl`). I made extensive attempts to find a secondary
verbatim quotation of Theorem 1 and could not fully succeed:
- Stewart's own conference-slide deck (carmamaths.org) does not contain the
  theorem text (checked via direct PDF read).
- Voutier, "Primitive divisors of Lucas and Lehmer sequences, II" (JTNB 8
  (1996), open numdam), p.252, quotes "Stewart [14, p.80]... Theorem 1" — but
  cross-checking Voutier's own bibliography (p.273) shows his ref. [14] is
  **a different Stewart paper**: "C. L. Stewart, *Primitive divisors of Lucas
  and Lehmer sequences*, Transcendence Theory: Advances and Applications
  (Baker & Masser, eds.), Academic Press, 1977" — not the JLMS 1983 "III"
  paper being audited here. (Voutier's ref. [15] is yet another Stewart paper:
  Proc. London Math. Soc. (3) 35 (1977), 425–447.) I flag this so the
  distinction is not lost: **this citation trail does not verify the target
  paper's Theorem 1**, it verifies a namesake theorem in a companion 1977
  paper by the same author.
- Ribenboim's 2002 Acta Arithmetica paper (§15 below, fully read) does not
  cite Stewart 1983 at all.
- I could not locate any source that reproduces the 1983 "III" paper's
  Theorem 1 verbatim (exact constant, exact hypothesis wording on
  (α+β)²/αβ, or the k²/log k-type growth rate).

**What I could not verify:** the exact inequality/constant in Theorem 1, the
precise hypothesis wording, and whether it directly yields the k²/log k
growth rate the manuscript claims in (4.7). The paper's *existence*, exact
bibliographic data, and general topic (effective bounds related to primitive
divisors / greatest square-free factors of Lucas–Lehmer-type sequences, a
running theme across Stewart's "I/II/III" series and follow-on literature by
Voutier, Bilu-Hanrot-Voutier, etc.) are well corroborated, but the specific
numerical content of *this* Theorem 1 remains unseen by me.

---

## 4. Bolvardizadeh, "On the quality of the ABC-solutions" (M.Sc. thesis, Lethbridge 2023) [CRITICAL]

**Grade: EXISTS+CONTENT-VERIFIED** (all four claims confirmed, plus bonus)

The bibliography's `hdl.handle.net/10133/6591` link and the OPUS item page
both work; the actual PDF lives at
`https://opus.uleth.ca/bitstreams/77f8e13b-4978-4b30-bcff-4364e26582e3/download`
(95 pp). Findings, with exact page numbers:

**Bonus (supervisor):** p.2 (title page): "Dr. Amir Akbary Professor Ph.D.
Thesis Supervisor." Confirmed again in Acknowledgments (p.4): "I would like to
express my gratitude to my supervisor Dr. Amir Akbary."

**§2.2 /4-normalized construction (p.20):** "2.2 ABC-solutions formed by (2.1)
and (2.2)... Define (a_m,b_m,c_m) = (v_m²,Du_m²,4Q^m) [gcd(v_m,u_m)=1], or
(v_m²/4,Du_m²/4,Q^m) [gcd(v_m,u_m)=2]." And Lemma 2.1 (p.20), formula (2.1):
"v_m² = Du_m² + 4Q^m." **Exact match** to the claimed V_m²=D·U_m²+4Q^m with a
/4-normalized version in §2.2.

**Theorem 2.6 assumes positive discriminant:** confirmed via Lemma 2.4 (p.22),
its load-bearing input, whose hypothesis is stated explicitly: "Let ε>0 and
D>0." Also confirmed retrospectively on p.73 (quoted next).

**pp.63–64 (§5.5) single out the missing archimedean limit for D<0:** found
verbatim, and the printed page numbers in the PDF are literally 63 and 64:

> (p.63–64, §5.5 "Future work"): "In Chapter 2, we studied two families of
> ABC-solutions... We only considered sequences with positive discriminants,
> as there are some obstacles when dealing with sequences with negative
> discriminants. For instance, consider the triple (a_m,b_m,c_m) defined in
> Section 2.1. If D = P²−4Q < 0, then Q > 0. Hence, max{a_m,b_m,c_m} = c_m. If
> we approach the problem similarly to Theorem 2.6, we need to determine the
> value of lim_{m→∞} log|u_m²|/log|Q^m|. **Observe that the argument used in
> Lemma 2.4 is not applicable in finding the value of this limit since
> |α/β| = 1 when D < 0.**"

This is a verbatim match, page numbers included, to every element of the
manuscript's claim about this thesis.

(Checked but not found: the thesis bibliography does **not** cite
Ohana–Spicer–Stein, so it could not be used as a secondary route to ref. #6.)

---

## 5. Hajdu–Tijdeman, "Integers represented by Lucas sequences" (2025) [CRITICAL]

**Grade: EXISTS+CONTENT-VERIFIED**

Metadata (Crossref DOI 10.1007/s11139-025-01041-6): "Integers represented by
Lucas sequences", The Ramanujan Journal, vol 66, issue 4, April 2025 — matches
"Ramanujan J. 66 (2025)". Fetched arXiv:2408.04982 directly (WebFetch on the
PDF failed to decode it; `curl` + local extraction succeeded, 24pp).

> **Theorem 2.1.** "For n≥2 we have in the real case |U_n|≥|α|^(n−2)/2 if B<0,
> |U_n|≥|α|^(n−1) if A²>4B>0, and in the non-real case
> |U_n| ≥ {¼e^(−250(log n)²)|α|^(n−2) if n>5·10⁸, ¼e^(−100000)|α|^(n−2) if
> n≤5·10⁸} for B≤535, and |U_n|≥{¼|α|^(n−2−88(log n)²) if n>2.1·10⁸,
> ¼|α|^(n−31710) if n≤2.1·10⁸} for B≥536."
>
> **Remark 1.** "We have in the real case |α|=(1+√5)/2 if (A,B)=±(1,−1),
> |α|≥2 if (A,B)≠±(1,−1), and in the non-real case, since B=1 is excluded,
> |α|=√B≥√2."

This is stated "for n≥2" (i.e. all indices, not just sufficiently large n) and
applies to every non-real (negative-discriminant) nondegenerate Lucas
sequence, matching the manuscript's characterization exactly ("growth
estimates ... valid for ALL indices"). It implies the archimedean limit: since
the exponent correction is O((log n)²) = o(n), log|U_n| = n·log|α| + o(n) for
every such sequence, so log|U_n²|/log Q^n → 1 in general — strictly more
general than the manuscript's own dyadic-only derivation, exactly as claimed
("implies that limit for every nondegenerate non-real Lucas sequence").

---

## 6. Ohana–Spicer–Stein, "The ABC data" (unpublished ms, Oct 2013)

**Grade: NOT-FOUND** (could not access the document; existence not independently corroborated)

The cited cocalc.com link (`/share/download/c1f4c5685b89bae0dfa24156574398b8c8172a3a/briefing/brief.pdf`)
redirects (302) to `cocalc.ai/share/download/...`, which returns only the
CoCalc web-app HTML shell (a JS single-page app, not the raw file) — confirmed
via `curl` on both the original and redirected URL, and via several
alternative CoCalc URL patterns (`/share/raw/...`, `/share/public_paths/...`,
`?viewer=share`), all of which return the same JS shell rather than file
bytes. The Wayback Machine has **no archived snapshot** of this URL at all
(`archive.org/wayback/available` returned an empty `archived_snapshots`).
WebSearch for the paper by title/authors turns up no independent citation of
this manuscript anywhere (only unrelated Ohana/Spicer/Stein co-authorships on
different papers), and Bolvardizadeh's 2023 thesis — which covers closely
related ABC-solution ground and would be a natural citer — does not cite it
either.

I was not able to verify the bibliographic details (13pp, October 2013) or
the claimed Proposition 1 content (the rad((b−a)²(4ab)c²) = rad(|b−a|)rad(abc)
formula) against any accessible copy of the source.

---

## 7. Martin–Miao, "abc triples" (2016)

**Grade: EXISTS+CONTENT-VERIFIED**

Metadata: Crossref (DOI 10.7169/facm/2016.55.2.2) gives "abc triples", Greg
Martin & Winnie Miao, Functiones et Approximatio Commentarii Mathematici, vol
55, issue 2, Dec 2016 (page range not populated by Crossref, but independently
confirmed as 145–176 by the Project Euclid listing title itself: "Functiones
et Approximatio 55.2 (2016), 145–176 doi: 10.7169/facm/2016.55.2.2", matching
the manuscript exactly). Downloaded `arxiv.org/pdf/1409.2974` (27pp) directly.

**§2.4 "Transfer method" (p.6)**, listing polynomial identities, ends with:
> "Some other examples of such polynomial transfers, which are all easily seen
> to be valid when c = a+b, include:
> **(b−a)² + 4ab = c²**,
> a³+b³=c(b²−ab+a²), a²(a+3b)+b²(3a+b)=c³, a³(a+2b)+c³(b−a)=b³(2a+b),
> 27c⁵(b−a)+a³(3a+5b)²(3a+2b)=b³(5a+3b)²(2a+3b)."

`(b−a)²+4ab=c²` is exactly the manuscript's identity (1.1). Confirmed §2.4
does catalogue it among "other" transfers (the section's main worked example
is the *different* transfer (a²,c(b−a),b²)).

**§3.1 "The transfer method again" (p.9)**, a genuinely different transfer
with one-sided bounds:
> "Recall from Section 2.4 that if (a,b,c) is an abc triple, then so is
> (a²,c(b−a),b²)... [§2.4, p.6:] if R(abc)<c, then
> R(a²·c(b−a)·b²) ≤ R(a)R(b)R(c)R(b−a) = (R(abc)/c)·c·R(b−a) < c(b−a) < b² ...
> if the quality q(a,b,c) is larger than 1, then... q(a²,c(b−a),b²) >
> 2q(a,b,c)/(q(a,b,c)+1) > 1."

Confirms both parts of the claim: §2.4 catalogues 4ab+(a−b)²=(a+b)² among
several transfers, and §3.1 iterates the *different* (a²,c(b−a),b²) transfer
with an explicit one-sided radical bound and quality bound.

---

## 8. Oesterlé, "Nouvelles approches du théorème de Fermat" (1988)

**Grade: EXISTS+CONTENT-VERIFIED**

Fetched the numdam PDF (`numdam.org/item/SB_1987-1988__30__165_0.pdf`, a
scanned document; WebFetch's text extraction failed on it, but the Read tool's
vision capability rendered the pages directly). Confirmed metadata on the
cover sheet: "Joseph Oesterlé, Nouvelles approches du «théorème» de Fermat,
Astérisque, tome 161-162 (1988), Séminaire Bourbaki, exp. n° 694, p. 165–186" —
**exact match**.

On printed **p.170** (verified by the page-footer numeral, in the middle of
§3 "La conjecture abc" → the Conjecture-3-implies-Conjecture-4 argument):

> "(14?) lorsque 16 divise abc par une démonstration analogue à celle de la
> prop. 1. Le cas où 4|abc, puis le cas général, s'en déduisent en choisissant
> b pair et **en écrivant l'inégalité (14?) pour le triplet
> (4ab, (a−b)², −(a+b)²).**"

This is the identity (up to the a+b+c=0 sign convention) written out
explicitly, in the abc-conjecture discussion, on p.170 exactly as claimed. A
closely related, more explicit form of the same construction (the recursive
counterexample sequence built from the identity) appears one page earlier, on
p.168, in the Szpiro-conjecture-sharpness discussion:

> "Considérons en effet les suites (aₙ), (bₙ), (cₙ) définies par a₀=16, b₀=1,
> c₀=−17, **aₙ₊₁=4aₙbₙ, bₙ₊₁=(aₙ−bₙ)², cₙ₊₁=−(aₙ+bₙ)²**."

Both appearances are consistent with the manuscript's characterization
("appears... in the abc–Szpiro discussion"); the p.170 citation specifically
is verified.

---

## 9. MathOverflow 263463, answer by Włodzimierz Holsztyński (2017)

**Grade: EXISTS+CONTENT-VERIFIED**

Fetched via the public StackExchange API (`api.stackexchange.com/2.3/questions/263463/answers`,
`site=mathoverflow`) since MathOverflow itself is on WebFetch's blocklist.
Confirmed: single answer, `owner.display_name = "Włodzimierz Holsztyński"`,
`creation_date` = 2017-03-15 20:00:44 UTC (matches "March 15, 2017" exactly).

Content, quoted from the answer body: starting from a reduced Pythagorean
triple (x,y,z) and a:=x², b:=y², c:=z² (a "squared Pythagorean triple"), the
answer defines A:=(x²−y²)²=(a−b)², B:=(2xy)²=4ab, C:=z⁴=c², and proves:

> "**THEOREM 1** L(A,B) > 1+S(a,b). Furthermore, if L(a,b) ≥ 1 then
> L(A,B) > 1."
> "**THEOREM 2** Every reduced Pythagorean triple (x,y,z) leads to an abc
> stream (A,B)↦(A′,B′)↦(A″,B″)↦... with Γ=1 ... appearing in a sharp way."

(Here L(a,b) is essentially the manuscript's quality function.) This matches
the claim exactly: iterates ((a−b)²,4ab,c²) from squared Pythagorean triples,
proves hit-preservation ("if L(a,b)≥1 then L(A,B)>1") and a one-step quality
inequality (Theorem 1).

---

## 10. MathOverflow 356295, answer attributed to Georgi Guninski (2020)

**Grade: EXISTS+CONTENT-VERIFIED, with one display-name caveat worth flagging**

Fetched via the StackExchange API. The question "How balanced can abc triples
be?" was asked by user **"Wolfgang"** on 2020-04-01. It has exactly one
answer, `answer_id 356345`, `owner.display_name = "joro"`,
`creation_date` = 2020-04-02 09:46:57 UTC (matches "April 2, 2020" exactly).

**The display name on the live site is "joro", not "Georgi Guninski."**
However, I confirmed this is the same real person: the "joro" account
(`mathoverflow.net/users/12481/joro`) lists `website_url: "https://www.guninski.com"`
in its public profile — Georgi Guninski's own domain — and two independent
WebSearch results state directly: "Georgi Guninski is an active contributor to
MathOverflow ... with the username 'joro'... profile can be found at
mathoverflow.net/users/12481/joro." So the manuscript's attribution is
substantively correct (right person, right date), just not the display name
currently shown on-site. Worth a footnote if a referee checks the live page.

Content, quoted verbatim:
> "Let a,b,c=a+b be good abc triple. Then A=4ab, B=(b−a)², C=(A+B)=(a+b)²=c²
> is good abc triple too, and it is twice bigger than the original... This
> construction is used in Bart de Smit high merit triples..."

This is exactly the transfer described in the manuscript's claim.

---

## 11. Alvarez-Salazar–Barrios–Henaku–Soller, "On abc triples of the form (1,c−1,c)" (2023)

**Grade: EXISTS+CONTENT-VERIFIED**

**Paper number**: confirmed **A64** (not A65) directly from the Integers
journal's own page title and PDF header: "#A64 INTEGERS 23 (2023) ON abc
TRIPLES OF THE FORM (1, c −1, c)" at `math.colgate.edu/~integers/x64/x64.pdf`
(fetched and read directly, 22pp; header confirms "INTEGERS: 23 (2023)").

**Zenodo DOI**: queried both the DataCite API and the Zenodo record API for
10.5281/zenodo.8283159 — resolves to title "On abc Triples of the Form
(1,c−1,c)", creators "Alvarez-Salazar, Elise; Barrios, Alexander J.; Henaku,
Calvin; Soller, Summer", publicationYear 2023. **Exact match** to the
manuscript's author list and title (this is a version-specific DOI; DataCite
shows it `IsVersionOf` the concept DOI 10.5281/zenodo.8283158, normal Zenodo
behaviour).

**Content claim** ("classical families include (1,9^k−1,9^k)"), p.2:
> "The 'simplistic abc conjecture' is false, as demonstrated by the triple
> (1, 3^(2k)−1, 3^(2k)), which is an abc triple for each positive integer k.
> This infinite sequence of abc triples is one of the first documented
> counterexamples to the simplistic abc conjecture and was communicated to
> Lang [7] by Jastrzębowski and Spielman."

3^(2k) = 9^k, so this is exactly the family (1,9^k−1,9^k), confirmed as prior
("classical") — matching the manuscript's own framing that this is prior art,
not a novelty claim of the cited paper.

---

## 12. OEIS A025172

**Grade: EXISTS+CONTENT-VERIFIED**

Fetched `oeis.org/A025172` directly. Confirmed:
- Terms: "1, 1, -7, -23, 17, 241, 329, -1511, -5983, 1633, 57113, ..." — exact
  match to the manuscript's list.
- Recurrence: "a(n) = 2*a(n-1) - 9*a(n-2)" for n≥2, with a(0)=a(1)=1 (FORMULA
  section) — exact match.
- Chebyshev/Lucas link: "Let phi = arccos(1/3)... cos(n*phi) = a(n)/3^n" (i.e.
  a(n) = 3^n·T_n(1/3)) and, from a comment by Peter Bala (Apr 01 2018): "This
  sequence is (1/2) * the Lucas sequence V(n,2,9)." — confirms
  3^m·T_m(1/3) = ½V_m(2,9) exactly as claimed.

---

## 13. Bajorska-Harapińska–Smoleń–Wituła, "quaternaccis" (2019)

**Grade: EXISTS (metadata confirmed) + CONTENT-UNVERIFIABLE (paywalled)**

Metadata (Crossref DOI 10.1007/s00006-019-0969-9): "On Quaternion Equivalents
for Quasi-Fibonacci Numbers, Shortly Quaternaccis", Advances in Applied
Clifford Algebras, vol 29, issue 3, July 2019 — matches the manuscript's
citation (Article 54; Crossref doesn't populate the article number field but
the title/journal/volume/year all match exactly).

The paper is fully paywalled: `link.springer.com` returns a 303 redirect to
Springer's login/IDP gateway with no visible abstract text reachable through
WebFetch. WebSearch turned up only the bibliographic record and a description
of the broader research programme ("newly defined families of associated
sequences of real polynomials and numbers that arose on a base of
quaternions"), not the specific claim about the Chebyshev-form sequence
3^m·T_m(1/3) or the A025172 recurrence. **I could not verify this content
claim; per instructions, I am saying so plainly rather than guessing.** This
is explicitly the manuscript's own "weakest link" citation, and my audit does
not strengthen it beyond confirming the paper exists with the stated metadata.

---

## 14. Ribenboim, "On square factors of terms of binary recurring sequences and the ABC conjecture" (2001)

**Grade: EXISTS (metadata confirmed) + CONTENT-PARTIAL**

Metadata (Crossref DOI 10.5486/PMD.2001.2559): "On square factors of terms of
binary recurring sequences and the $ABC$ Conjecture", Publicationes
Mathematicae Debrecen, vol 59, issue 3-4, pp. 459–469, published 2001-10-01,
author Paulo Ribenboim. **Exact match** to the manuscript's citation.

I could not obtain the PDF (no open-access route found for this journal for
this volume/year, unlike Acta Arithmetica). I therefore could not directly
confirm the existence of a numbered item "§2.13" with the specific
rank-divisibility criterion. The general topic (square factors / rank
criteria for binary recurring sequences) is entirely consistent with the
paper's title and with the closely-related, fully-verified Ribenboim 2002
paper (below), which uses the same style of apparatus, but I did not see the
specific item.

---

## 15. Ribenboim, "The square-free kernel of x^(2^n) − a^(2^n)" (2002)

**Grade: EXISTS+CONTENT-VERIFIED**

Full text obtained (Acta Arithmetica is open access; free PDF at
`impan.pl/shop/en/publication/transaction/download/product/83482`, CC-BY,
9pp). Confirmed masthead: "ACTA ARITHMETICA 101.2 (2002)... The square-free
kernel of x^(2^n) − a^(2^n), by Paulo Ribenboim (Kingston, Ont.)" pp.189-197 —
**exact match** to the manuscript's citation (journal, volume/issue, pages,
author, DOI 10.4064/aa101-2-9 confirmed on the same page).

Content is exactly as characterized ("dyadic Lucas factorizations/square-free
kernels"): the paper studies ν(x^(2^n)−a^(2^n)) (number of odd prime factors
of the square-free kernel) via the dyadic-doubling structure
u_n=x^(2^n)−a^(2^n)=u_{n−1}v_{n−1}, gcd(u_{n−1},v_{n−1})∈{1,2}, expressed
through binary linearly recurring (Lucas-type) sequences U_n(P,Q), V_n(P,Q)
with P=x+a, Q=xa — a direct structural cousin of the manuscript's own
disjoint-prime-support dyadic factorization (Lemma 2.1 of the manuscript).

---

## 16. Ribenboim–Walsh, "The ABC conjecture and the powerful part of terms in binary recurring sequences" (1999)

**Grade: EXISTS+CONTENT-VERIFIED**

Metadata (Crossref DOI 10.1006/jnth.1998.2315): "The ABC Conjecture and the
Powerful Part of Terms in Binary Recurring Sequences", Journal of Number
Theory, vol 74, issue 1, pp. 134–147, Jan 1999, authors Paulo Ribenboim & Gary
Walsh. **Exact match.**

Abstract thrust (ScienceDirect record): "The authors consider non-degenerate
binary recurring sequences with positive discriminant... Assuming the ABC
conjecture is true, they show that the powerful part of the terms of the
sequence remain 'small.' In particular, such sequences have only finitely
many terms which are powerful numbers." This is exactly the one-directional
(abc ⇒ non-Wieferich/non-powerful-type consequence) implication the
manuscript groups it under.

---

## 17. Silverman, "Wieferich's criterion and the abc-conjecture" (1988)

**Grade: EXISTS+CONTENT-VERIFIED**

Metadata (Crossref DOI 10.1016/0022-314X(88)90019-4): "Wieferich's criterion
and the abc-conjecture", Journal of Number Theory, vol 30, issue 2, pp.
226–237, Oct 1988, author Joseph H. Silverman. **Exact match.**

Abstract thrust (confirmed via WebSearch of the paper's abstract): "the
abc-conjecture ... implies that there are infinitely many primes for which
2^(p−1) ≡ 1 (mod p²) [i.e., non-Wieferich primes]... at least O(log X) such
primes less than X," plus an analogous elliptic-curve result. Exactly the
one-directional abc ⇒ non-Wieferich-primes implication the manuscript cites
it for.

---

## 18. Yabuta, "The ABC-conjecture and the powerful numbers in Lucas sequences" (2007)

**Grade: EXISTS+CONTENT-VERIFIED**

Fetched a MathSciNet-style review record directly (small PDF, single page)
giving: "Minoru Yabuta, *The ABC-conjecture and the powerful numbers in Lucas
sequences*, Fibonacci Quart. **45** (2007), no. 4, 362–365." — **exact match**
to the manuscript's citation (DOI 10.1080/00150517.2007.12428206 corroborated
separately via Crossref: same journal/volume/issue/pages/year/author).

Abstract, quoted in full: "P. Ribenboim and G. Walsh showed that if the
ABC-conjecture is true then every Lucas sequence has only finitely many
powerful terms in the case of positive discriminant. **We extend this result
into the case of negative discriminant.**" Confirms it belongs in the same
one-directional-implication family as refs. 16–17, extending Ribenboim–Walsh
specifically to negative discriminant — precisely the grouping in the
manuscript's sentence.

---

## 19. Bright, "A new lower bound in the abc conjecture" (2024)

**Grade: EXISTS+CONTENT-VERIFIED**

Downloaded the open-access Cambridge PDF directly (10pp, CC-BY) and read it.
Masthead: "Canad. Math. Bull. Vol. 67(2), 2024, pp. 369–378...
A new lower bound in the abc conjecture, Curtis Bright" — **exact match**
(DOI 10.4153/S0008439523000784 confirmed on the same page).

Abstract, quoted verbatim:
> "We prove that there exist infinitely many coprime numbers a, b, c with
> a+b=c and **c > rad(abc)exp(6.563√(log c)/log log c)**. These are the most
> extremal examples currently known in the abc conjecture... Our work builds
> on that of van Frankenhuysen (J. Number Theory 82 (2000), 91–95) who proved
> the existence of examples satisfying the above bound with the constant
> 6.068 in place of 6.563."

Exact match to the manuscript's claimed inequality and constant.

---

## 20. Bilu–Hanrot–Voutier, "Existence of primitive divisors of Lucas and Lehmer numbers" (2001)

**Grade: EXISTS+CONTENT-VERIFIED (metadata; classical result well-corroborated)**

Metadata (Crossref DOI 10.1515/crll.2001.080): "Existence of primitive
divisors of Lucas and Lehmer numbers", J. reine angew. Math. (Crelle's
Journal), volume "2001"/issue "539" (Crossref's quirky way of indexing this
journal — matches "539 (2001)"), authors Y. Bilu, G. Hanrot, P. M. Voutier.
Page range 75–122 is not populated by Crossref directly but is corroborated
independently and consistently by multiple sources (a zbMATH identifier
Zbl 0995.11010 was surfaced by WebSearch, plus multiple independent citing
bibliographies) — I could not get a direct fetch of the primary source or
zbMATH page itself (paywalled / bot-protected — HAL mirror returned an Anubis
challenge page). This is the well-known, standard reference establishing
existence of primitive divisors of Lucas/Lehmer numbers for n>30 (with a
completely explicit finite exception list, via an appendix by Mignotte) —
consistent with the manuscript's use ("the classical primitive-divisor
result").

---

## 21. van der Horst, "Finding ABC-triples using elliptic curves" (M.Sc. thesis, Leiden 2010)

**Grade: METADATA-MISMATCH (dead URL) + CONTENT-VERIFIED**

**URL problem:** the manuscript's cited URL,
`https://www.universiteitleiden.nl/binaries/content/assets/science/mi/scripties/vanderhorstmaster.pdf`,
returns **HTTP 404** (confirmed via `curl`, both as given and with corrected
capitalization). The thesis is real and currently hosted at a different
domain/path with different capitalization:
`https://math.leidenuniv.nl/scripties/vanderHorstMaster.pdf` (HTTP 200,
confirmed working, `Last-Modified: 2010-09-01`, matching the thesis's defence
date of 2010-08-27 found via WebSearch of Leiden's thesis listing). Discovered
via Leiden's own current thesis-listing page
(`math.leidenuniv.nl/scripties/master_theses.html`), which lists: "J.P. van
der Horst — Finding ABC-triples using Elliptic Curves (2010-08-27), supervised
by Dr. B. de Smit."

**Content (§2.3):** fetched the working PDF (57pp) and confirmed §2.3
"Transfer method" (pp.16–20) discusses exactly the claimed identity, p.19:

> "Another way to increase the expected quality is to find a prime factor
> which will occur often in the factorisation. For example, when we have an
> ABC-triple (A,B,C) with C an odd number, then A·B is even and we can use
> the transfer **((A−B)², 4AB, (A+B)²)**. Since A+B is odd, 4AB and (A+B)²
> are coprime and the necessary factor 2 is involved in the term 4AB."

Exact match to the polynomial transfer (1.1) the manuscript cites this
section for.

---

## Summary table

| # | Reference | Grade | Key finding |
|---|---|---|---|
| 1 | Baker–Wüstholz 1993 [CRITICAL] | EXISTS+VERIFIED | 3 independent secondary quotations, exact constant/height/B match |
| 2 | Sun 2013 (arXiv:1312.3511) [CRITICAL] | EXISTS+VERIFIED | Theorem 3(ii) verbatim match; (2,9) satisfies all hypotheses |
| 3 | Stewart 1983 JLMS [CRITICAL] | EXISTS+PARTIAL | Metadata exact; exact Theorem 1 text unreachable (paywalled); one promising secondary trail turned out to cite a *different* 1977 Stewart paper |
| 4 | Bolvardizadeh 2023 thesis [CRITICAL] | EXISTS+VERIFIED | All 4 claims verbatim-confirmed incl. exact pp.63–64; supervisor = Amir Akbary |
| 5 | Hajdu–Tijdeman 2025 [CRITICAL] | EXISTS+VERIFIED | Theorem 2.1 + Remark 1 verbatim, "for n≥2", non-real case, matches claim |
| 6 | Ohana–Spicer–Stein 2013 | NOT-FOUND | cocalc link unfetchable (JS shell); no Wayback snapshot; no external citation found anywhere |
| 7 | Martin–Miao 2016 | EXISTS+VERIFIED | §2.4 and §3.1 both verbatim-confirmed |
| 8 | Oesterlé 1988 | EXISTS+VERIFIED | Triple (4ab,(a−b)²,−(a+b)²) written out verbatim on p.170 exactly |
| 9 | MO 263463 (Holsztyński) | EXISTS+VERIFIED | Author/date/content all verbatim-confirmed via SE API |
| 10 | MO 356295 ("Guninski") | EXISTS+VERIFIED* | Content/date confirmed; *display name on-site is "joro", same person (verified via linked guninski.com) |
| 11 | Alvarez-Salazar et al. 2023 | EXISTS+VERIFIED | Paper A64 confirmed (not A65); zenodo DOI confirmed; (1,9^k−1,9^k) content confirmed |
| 12 | OEIS A025172 | EXISTS+VERIFIED | Terms, recurrence, and ½V_m(2,9) identity all confirmed |
| 13 | Bajorska et al. 2019 | EXISTS+UNVERIFIABLE | Metadata confirmed; content paywalled, stated plainly as unverified |
| 14 | Ribenboim 2001 | EXISTS+PARTIAL | Metadata exact; §2.13 item not directly seen (no open PDF found) |
| 15 | Ribenboim 2002 | EXISTS+VERIFIED | Full text read; metadata exact; content matches "dyadic square-free kernel" characterization |
| 16 | Ribenboim–Walsh 1999 | EXISTS+VERIFIED | Metadata exact; abstract confirms one-directional thrust |
| 17 | Silverman 1988 | EXISTS+VERIFIED | Metadata exact; abstract confirms non-Wieferich-primes thrust |
| 18 | Yabuta 2007 | EXISTS+VERIFIED | Metadata exact; full abstract confirms Ribenboim–Walsh extension |
| 19 | Bright 2024 | EXISTS+VERIFIED | Full abstract read; exact constant 6.563 confirmed verbatim |
| 20 | Bilu–Hanrot–Voutier 2001 | EXISTS+VERIFIED | Metadata strongly corroborated (Crossref + zbMATH ID + multiple citations); primary source paywalled/bot-blocked |
| 21 | van der Horst 2010 thesis | METADATA-MISMATCH+VERIFIED | Cited URL is dead (404); correct live URL found on different domain/path; §2.3 content verbatim-confirmed |
