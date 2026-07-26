# Kirti Joshi — Arithmetic Teichmüller Spaces: Verbatim Extracts for Audit

Extraction only. No correctness judgments are offered anywhere in this file.

## Method note / constraints (read first)

- The arXiv MCP tools (`search_papers`, `get_paper_latex_section`, etc.) were rate-limited
  (HTTP 429) and then explicitly taken off the table mid-task by the coordinator. All work
  below instead uses `WebFetch` against `arxiv.org` directly, plus one lucky break: a
  `WebFetch` of `https://arxiv.org/pdf/2401.13508` silently cached the full PDF locally
  (2.1MB), which was then converted with `pdftotext -layout` and grepped/sliced with `sed`.
  So the quoted text below is **verbatim from the PDF's text layer**, not from the original
  `.tex` source (the LaTeX-section MCP tool was unavailable under the rate-limit
  constraint). Mathematical content is verbatim as rendered; however `pdftotext`
  linearization can reorder stacked/tilde-accented symbols. In particular
  `\widetilde{\Theta}^{I}_{Mochizuki}`-type expressions frequently come out as glyph
  soup like `Θe IM ochizuki` or `e IM ochizuki` (the tilde-accent and superscript `I` get
  displaced). Treat that spacing/ordering as a rendering artifact of text extraction, not a
  discrepancy in the source. Page-number footer lines (bare numbers like `119`) that fell
  inside quoted ranges are left in place rather than silently deleted, since this is meant to
  be a verbatim capture.
- Hard time budget was imposed mid-task (~7 minutes) after the rate-limit pivot; see
  "Not done / caveats" at the end for exactly what was skipped as a result.

## 1. Paper inventory

Series title as used by Joshi: **"Construction of Arithmetic Teichmuller Spaces"**, parts I–IV,
plus a related but differently-titled "Final Report". Confirmation status is marked per row —
"CONFIRMED" means this session directly fetched the arXiv abs page (or, for III, the full PDF);
"via WebSearch snippet" means the title/ID come only from a search-engine result snippet quoted
back by WebSearch, not independently opened this session.

| Part | arXiv ID | Exact title | Versions / dates | Pages | Status |
|---|---|---|---|---|---|
| I | 2106.11452 | Not independently confirmed this session | Not confirmed | — | Identified only via a secondary citation inside a WebSearch answer ("builds on earlier papers arXiv:2106.11452, arXiv:2210.11635, arXiv:2303.01662, arXiv:2305.10398"); never fetched |
| II (v.1 of that slot) | 2111.04890 | "Construction of Arithmetic Teichmuller spaces II: Towards Diophantine Estimates" | Nov 2021 (not independently confirmed) | — | via WebSearch snippet; not fetched |
| II (later, different arXiv ID) | 2210.11635 | Not independently confirmed this session | Not confirmed | — | via WebSearch snippet only (mentioned as a citation, title not seen); relation to 2111.04890 / 2303.01662 not resolved |
| II (later still, different arXiv ID) | 2303.01662 | "Construction of Arithmetic Teichmuller spaces II: Proof of a local prototype of Mochizuki's Corollary 3.12" | Mar 2023 (not independently confirmed) | — | via WebSearch snippet; not fetched. Note: 2111.04890, 2210.11635, 2303.01662 are three *distinct* arXiv IDs all associated with "Part II" language — Joshi appears to have re-split/re-issued this slot rather than just posting new versions of one ID. Not resolved further this session. |
| II½ | 2305.10398 | "Construction of Arithmetic Teichmuller Spaces II½: Deformations of Number Fields" | May 2023 (not independently confirmed) | — | via WebSearch snippet; not fetched |
| **III** | **2401.13508** | **"Construction of Arithmetic Teichmuller Spaces III: A 'Rosetta Stone' and a proof of Mochizuki's Corollary 3.12"** | v1 24 Jan 2024, v2 15 Mar 2024, v3 27 Jun 2024, **v4 24 Feb 2025** | 163pp (v4) | **CONFIRMED** — abs page fetched directly; full text extracted from the PDF via pdftotext. `arxiv.org/pdf/2401.13508` (no version suffix) resolved to v4, the latest. |
| IV | 2403.10430 | "Construction of Arithmetic Teichmuller Spaces IV: Proof of the abc-conjecture" | v1 15 Mar 2024, v2 24 Feb 2025 | 80pp | CONFIRMED — abs page fetched directly. Comment field: "expanded and revised edition of my March 2024 submission and fixes the issues with the previous version." HTML render of v2 checked: only reaches **Section 7** ("Vojta's Inequality...") — no Section 9 found in the visible/fetched portion (see caveats: this fetch may have been truncated by fetch-tool length limits rather than proving absence). |
| Final Report | 2505.10568 | "Final Report on the Mochizuki-Scholze-Stix Controversy" | v1 29 Apr 2025 | 8pp | CONFIRMED — abs page fetched directly |

Adjacent non-arXiv material seen on Joshi's site (`sites.arizona.edu/kirti-joshi/`,
`math.arizona.edu/~kirti/`) but out of scope (not arXiv papers): a "Questions and answers
regarding my preprints" PDF, a June 2024 provisional report PDF, and a November 2025 FAQ PDF
about the abc-conjecture proof. Not extracted from.

## 2. Extracted items

All four items below were located in **Construction III, arXiv:2401.13508, v4 (latest)** —
the only paper in which any of them were found. Location result up front:

| Item | Exists as literally labeled? | Where |
|---|---|---|
| Lemma 7.6.5.1 | **Yes**, matches description | §7.6.5, p.62–63 |
| Section 9.9 | Yes, but the map is embedded inside a proof, not a standalone definition | §9.9, p.118–120 |
| Section 9.10.3 | **Yes**, matches description | §9.10.3, p.123 |
| Theorem 9.11 | **No bare "Theorem 9.11"** — only "Theorem 9.11.1" under header "§9.11", and its content is a different result than described | §9.11 (p.126–127); best content-match is Lemma 9.10.7.1 + Prop. 9.10.8.1, §§9.10.7–9.10.8, p.125–126 |

---

### Item 1 — Lemma 7.6.5.1

**Provenance:** arXiv:2401.13508, v4 (latest), §7.6.5 "Another variant", pp.62–63 of the PDF.

**Assessment against the brief:** matches as described — the lemma and proof establish a
multiplicative norm on a tensor product of two Banach algebras by checking the
multiplicativity identity on pure tensors `b1 ⊗ b2`.

```latex
B1 ⊗Qp B2 is equipped with a valuation i.e. a multiplicative norm |−|B1 ⊗B2 ;ρ1 ,ρ2 such that for
every b1 ∈ B1 and for every b2 ∈ B2 one has

  |b1 ⊗ b2 |B1 ⊗B2 ;ρ1 ,ρ2 = |(b1 ⊗ 1) · (1 ⊗ b2 )|B1 ⊗B2 ;ρ1 ,ρ2 =
                                = |(b1 ⊗ 1)|B1 ⊗B2 ;ρ1 ,ρ2 · |(1 ⊗ b2 )|B1 ⊗B2 ;ρ1 ,ρ2 = |b1 |B1 ;ρ1 |b2 |B2 ;ρ2 .

especially
                                 |b1 ⊗ b2 |B1 ⊗B2 ;ρ1 ,ρ2 = |b1 |B1 ;ρ1 |b2 |B2 ;ρ2 .

I will refer to |−|B1 ⊗B2 ;ρ1 ,ρ2 as the tensor product norm of (B1 , |−|B1 ;ρ1 ) and (B2 , |−|B2 ;ρ2 ).

§ 7.6.5 Another variant Here is a Banach theoretic version of the above lemma which I could
not find in existing literature and of which I will provide a proof.

Lemma 7.6.5.1. Let E1 , E2 be two p-adic fields, let ρ1 , ρ2 ∈ [0, 1] ⊂ R. Write B1 = BE1 , B2 =
BE2 and equip them with the multiplicative norms |−|Bi ;ρi for i = 1, 2. Then the algebra
B1 ⊗Qp B2 is equipped with a multiplicative norm |−|B1 ⊗B2 ;ρ1 ,ρ2 such that for every b1 ∈ B1
and for every b2 ∈ B2 one has

  |b1 ⊗ b2 |B1 ⊗B2 ;ρ1 ,ρ2 = |(b1 ⊗ 1) · (1 ⊗ b2 )|B1 ⊗B2 ;ρ1 ,ρ2 =
                                = |(b1 ⊗ 1)|B1 ⊗B2 ;ρ1 ,ρ2 · |(1 ⊗ b2 )|B1 ⊗B2 ;ρ1 ,ρ2 = |b1 |B1 ;ρ1 |b2 |B2 ;ρ2 .

especially
                                 |b1 ⊗ b2 |B1 ⊗B2 ;ρ1 ,ρ2 = |b1 |B1 ;ρ1 |b2 |B2 ;ρ2 .

Proof. By [Lang, 2002], there is a natural way to define an algebra structure on the tensor
product B1 ⊗Qp B2 compatible with the algebra structures of each of the factors, namely

                                 (b1 ⊗ b2 ) · (c1 ⊗ c2 ) = (b1 c1 ) ⊗ (b2 c2 ).

Then
                      |(b1 ⊗ b2 ) · (c1 ⊗ c2 )|B1 ⊗Qp B2 = |(b1 c1 ) ⊗ (b2 c2 )|B1 ⊗Qp B2
and by [Schneider, 2002, Chap 4, Proposition 17.4]

                                   |(b1 c1 ) ⊗ (b2 c2 )| = |b1 c1 |B1 |b2 c2 |B2

and as the norms on B1 , B2 are multiplicative, one gets

           |(b1 c1 ) ⊗ (b2 c2 )| = |b1 c1 |B1 |b2 c2 |B2 = |b1 | |c1 | |b2 | |c2 | = |b1 ⊗ c1 | |b2 ⊗ c2 |

and therefore
                                  |(b1 c1 ) ⊗ (b2 c2 )| = |b1 ⊗ c1 | |b2 ⊗ c2 | ,

                                                         63
and the assertion of the lemma is immediate from this formula by considering the special case
(b1 ⊗ 1)(1 ⊗ b2 ) = b1 ⊗ b2 . This proves the assertion.

§ 7.6.6 The lower bound lemma The proof of the following lemma is now self-evident:

Lemma 7.6.6.1. Suppose one is given a finite collection of Qp -Banach spaces {Vα }α and sup-
pose that one is also given an element mα ∈ Vα for each Vα . Then for the projective tensor
```

---

### Item 2 — Section 9.9

**Provenance:** arXiv:2401.13508, v4 (latest), §9.9 "Proof of the fundamental estimate for
Θ~^I_Mochizuki and Θ~^I_Joshi", pp.118–120 of the PDF.

**Assessment against the brief:** Section 9.9's primary content is "Theorem 9.9.1" (the
fundamental estimate) and its proof — it is not, itself, framed as a definition section. The
map `(a_w) ↦ ⊗_w a_w` the brief describes does appear, but embedded inside the proof of
Theorem 9.9.1 (used there to pass from a finite direct product of the `L'_w` to their tensor
product), rather than as a standalone boxed/numbered definition.

```latex
§ 9.9 Proof of the fundamental estimate for e ΘIM ochizuki and e
                                                               ΘIJ oshi . Now one is ready to
prove the fundamental estimate [Mochizuki, 2021c, Corollary 3.12].

Theorem 9.9.1. For X, C, L, L′ satisfying § 2.4, § 3.1, § 3.3, and for an odd prime ℓ ≫ 0 one
has                                            Y             ℓ∗
                             Θe IM ochizuki ≥          qw1/2ℓ ,
                                                            w∈Vodd,ss

and also                                                        Y                      ℓ∗
                                           e IJ oshi ≥
                                           Θ                              qw1/2ℓ            .
                                                                odd,ss
                                                         w∈V


Proof of Theorem 9.9.1. The strategy of the proof is the same as the local strategy of [Joshi,
2023b]. One exhibits an element, namely ξz = ξJzΘoshi (resp. ξz = ξ M                            ochizuki
                                                                                                          ), of Θ e I˜ ,
                                                                                               zΘ                   J oshi
e I˜
Θ            , eI , Θ
               Θ        eI            for which      the   absolute value can be  computed      and  one    shows    that
  M ochizuki     J oshi   M ochizuki

|ξz | exceeds the number on the right of the stated inequality. Since Θ               e IJ oshi (resp. Θ   e IM ochizuki )
on the left of the asserted inequality is a supremum, the inequality claimed in the theorem will
follow if the absolute value of this chosen element bounds above the quantity on the right of
the asserted inequality in the theorem.
     Since Θ  eI           e I˜
                          ,Θ              eI , Θ
                                         ,Θ          e I˜ as defined in § 9.8.1, Theorem-Definition 9.8.1.1
               M ochizuki     M ochizuki    J oshi     J oshi

are adelic, and Θ      eI            and   eI
                                           Θ           are   defined multiplicatively, one may work with com-
                        M ochizuki            J oshi


ponents ΘeI         ,ΘeI            for each w ∈ V. So it is enough to estimate Θ  eI            and then
           J oshi,w    M ochizuki,w                                                 M ochizuki,w

take product over all w ∈ V.
    First I will work with the product versions Θ      e I˜ and Θ  e I˜
                                                          J oshi     M ochizuki and then deduce the in-
                                               e I        e  I
equality for the tensor product versions ΘJ oshi and ΘM ochizuki from this.
    Note that these products are finite by Corollary 9.8.1.3. [As remarked earlier, by Lemma 9.8.2.7,
 logp (1 + p∗w ) L′ = |p∗ |L′w . So logBK (1 + p∗ ) contributes an element of unit norm in the prod-
                    w
uct.]
    So it suffices to establish the inequality (for w ∈ Vodd,ss )
                                                                                   ∗
                                             e IM ochizuki,w ≥ qw1/2ℓ ℓ .
                                             Θ

                                                            119
For this purpose it will be convenient to work with the Bloch-Kato logarithms § 9.7.2 of the
cohomological classes ξ y . Then Equation (9.7.2.1) asserts that the codomain of Bloch-Kato log-
arithm logBK is, for each w ∈ VL′ ,p , the field L′w considered as a Qpw -vector space. This means
that in the product setting i.e. in IeJQoshi and IeMQochizuki, each class ξ y contributes logBK (ξy ) in
                                                                             j                     j

L ′                                        e Q            eQ
       to the corresponding factor of IJ oshi (resp. IM ochizuki).
  w;yj
                                                                                               ˜
    Now let me say how one may deduce the inequality for e                   ΘIJ oshi (resp. e
                                                               ΘIJ oshi from e               ΘIM ochizuki
         ˜                                                         Q
from eΘIM ochizuki ). One may pass from the finite direct product w|p L′w (equivalently from the
finite direct sum) of Qp -vector spaces to the tensor product ⊗w|p L′w of Qp -vector spaces as
follows. Consider the mapping
                  Y                                        O
                        L′w ∋ (aw ) 7−→ ⊗w|p (aw ) ∈             L′w 7−→ ⊗ aw                  ∈ R,
                                                                              w|p   ⊗w|p L′w
                  w|p                                      w|p


where first mapping is the natural homomorphism of Qp -vector spaces:
                                              Y
                                                    L′w → ⊗w|p L′w ,
                                              w|p


and the second mapping is the tensor norm. In other words, one considers the image of the
theta-values locii in the tensor product (via the first mapping) and then takes supremum over
the tensor norms of all the images under the first homomorphism. This is where the cross-norm
property § 7.6.2 of the tensor product norms comes in to play. This property says one has
                                                               Y
                                         ⊗ aw              =         |aw |L′w .
                                        w|p     ⊗w|p L′w       w|p


Hence one may also work with suprema of absolute values of the images of the theta-locii in the
tensor products i.e. one can work with Θ  e IJ˜oshi instead of Θ                           e IM˜ochizuki, Θ
                                                                e IJ oshi (resp. work with Θ              e IM ochizuki)
and still arrive at the required estimates in the tensor product settings (i.e. for Θ       eI            (resp.
                                                                                               M ochizuki
e I                                                                                    ′
ΘJ oshi ) of [Mochizuki, 2021c]. Notably, since the tensor product ⊗w|p Lw is constructed us-
                  Q
ing the product w|p L′w (more precisely the tensor product is the quotient of a suitable free
Qp -module on the set underlying this product), one can expect that the theta-values locus in
the tensor product setting (i.e. ΘeI , Θ  eI            ) should provide tighter upper bounds than the
                                   J oshi    M ochizuki
                                                    e I˜
theta-values locus in the product setting i.e. ΘJ oshi , Θ  e I˜          .
                                                              M ochizuki
```

Note: "uses linearity" from the brief is not a verbatim phrase found adjacent to the map; the
closest textual anchor is the remark that the tensor product is "the quotient of a suitable free
`Qp`-module on the set underlying this product" (i.e., the map factors through the universal
multilinear/bilinear map defining the tensor product) — quoted above, last paragraph.

---

### Item 3 — Section 9.10.3

**Provenance:** arXiv:2401.13508, v4 (latest), §9.10.3 "Weighted volumes", p.123 of the PDF.

**Assessment against the brief:** matches as described — this is exactly a weighted /
lattice-volume definition on a tensor product of p-adic fields.

```latex
                               VolE (α + λ · OE ) = Vol(λOE ) = |λ|E ,
        and also

  (3)
                              Vol(λOE ) = sup{|s|E : s ∈ λOE } = |λ|E ,
        and, in particular,

  (4) for any s ∈ λ · OE (note that s ∈ S if and only if α = 0) one has the tautology

                                         |λ|E = VolE (S) ≥ |s|E .

Proof. The first equality is the translation invariance of Vol and the second equality is clear
from the definition of VolE . The remaining assertions are clear.

§ 9.10.3 Weighted volumes These considerations can be extended as follows. Let E1 , . . . , En
be finite extensions of Qp . The theory of volumes and log-volumes on E1 , . . . , En extends
to a theory of weighted volumes on the tensor product E = E1 ⊗Qp E2 ⊗Qp · · · ⊗Qp En .
Let Γ = {γ1 , γ2 , . . . , γn } ⊂ (0, 1] ⊂ R be a set of weights. Then the Γ-weighted volume


                                                123
VolΓE1 ⊗Qp ···⊗Qp En is a function on certain measuable subsets of the Qp -vector space E. This is
defined as follows.
    Recall from [Schneider, 2002], that E1 ⊗Qp E2 is equipped with topology which has a
fundamental system of neighborhoods of zero consisting of sets of the form V1 ⊗ V2 ⊗ · · · ⊗ Vn
where Vi ⊂ Ei is a Zp -lattice in each Ei .
    So it suffices to define

(9.10.3.1)           VolE1 ⊗Qp ···⊗Qp En (V1 ⊗Zp · · · ⊗Zp Vn ) = VolγE11 (V1 ) · · · VolγEnn (Vn ).

   This leads to the following version of Lemma 9.10.2.2:

Lemma 9.10.3.2. Let, for i = 1, . . . , n, Vi = αi + λi OEi ⊂ OEi with αi ∈ Ei and λi ∈ Ei∗ .
Then

  (1)
                                                                                n
                                                                                Y
                     VolΓE1 ⊗Qp ···⊗Qp En (V1 ⊗Zp V2 ⊗Zp · · · ⊗Zp Vn ) =             VolγEii (Vi ).
                                                                                i=1

  (2) Hence
                                                                       n
                                                                       Y                       n
                                                                                               Y
              VolΓE1 ⊗Qp ···⊗Qp En (V1 ⊗Zp V2 ⊗Zp · · · ⊗Zp Vn ) =           VolΓEi (Vi ) =          |λi |γEii ,
                                                                       i=1                     i=1


  (3) and hence if si ∈ λi OEi ∩ Ei∗ then
                                                                       n
                                                                       Y                       n
                                                                                               Y
              VolΓE1 ⊗Qp ···⊗Qp En (V1 ⊗Zp V2 ⊗Zp · · · ⊗Zp Vn ) =           VolγEii (Vi ) ≥           |si |γi .
                                                                       i=1                     i=1


§ 9.10.4 The sets of interest to us, arising in Theorem 7.7.3.1, contain tensor products of sets
of the form                               Y
                                             (λw · OL′w )
                                             w∈V
```

---

### Item 4 — "Theorem 9.11"

**Provenance:** arXiv:2401.13508, v4 (latest). There is no item literally labeled "Theorem
9.11" anywhere in the paper. What exists at that numeric position is a section header
"§ 9.11" followed by "**Theorem 9.11.1**" (p.126–127) — and its content is the *fundamental
volume estimate* feeding Mochizuki's Corollary 3.12, not a statement about inclusion of a
tensor-product lattice from pure tensors/convexity.

The content the brief actually describes — inferring inclusion of a lattice/hull built from a
full tensor product, from data on pure tensors, via convexity — is found one subsection
earlier, in **Lemma 9.10.7.1** (§9.10.7) and **Proposition 9.10.8.1** (§9.10.8), pp.125–126,
immediately preceding §9.11.

**(4a) §9.11 header + Theorem 9.11.1 (what is actually numbered "9.11.x"):**

```latex
§ 9.11 Proof of the fundamental estimate for Vol(Θ  eI                     eI
                                                      M ochizuki ) and Vol(ΘJ oshi ) Now one is

ready to prove the fundamental estimate [Mochizuki, 2021c, Corollary 3.12].

Theorem 9.11.1. For X, C, L, L′ satisfying § 2.4, § 3.1, § 3.3, and for an odd prime ℓ ≫ 0
one has                                         Y            ℓ∗
                          Vol( e
                               ΘIM ochizuki ) ≥        qw1/2ℓ ,
                                                      w∈Vodd,ss

and also                                              Y                    ℓ∗
                                       eI ) ≥
                                   Vol(Θ                          qw1/2ℓ        .
                                         J oshi
                                                         odd,ss
                                                    w∈V


Proof. By Proposition 9.10.8.1, one can work with Mochizuki’s holomorphic hulls or convex
closures (in Banach spaces). It will be enough to prove this for one of the two Θ      eI           eI .
                                                                                                   ,Θ
                                                                                        M ochizuki    J oshi

I will prove the assertion for Θe IM ochizuki. The proof of Theorem 9.9.1 will serve as a tem-
plate for this assertion. By the construction of these sets, Θ     eI          contains the classes Ξz
                                                                    M ochizuki

given by Theorem-Definition 9.8.1.1 obtained from each choice of Tate parameters obtained
using the standard point of the Σ e L′ and hence it contains a subset of the type considered in
Lemma 9.10.7.1
                      Y
                           (τ1 OL′w,1 ) ⊗Zp (τ2 OL′w,2 ) ⊗Zp · · · ⊗Zp (τℓ∗ OL′w,ℓ∗ ),
                    w∈Vodd,ss


with τj = logBK (Ξ0,zj ,w ) (for suitable j). So the volume of this set can be bounded by
Lemma 9.10.7.1.
    Since Θe IM ochizuki defined in § 9.8.1 is adelic, and weighted volumes are defined multiplica-
tively, one may work with components Θ       eI             for each w ∈ V. So it is enough to estimate
                                               M ochizuki,w
     e I
Vol(ΘM ochizuki,w ) and then take product over all w ∈ V. Note that the product is finite by Corol-
                                                                                          ℓ∗
                                                             eI
lary 9.8.1.3. So it suffices to establish the inequality Vol(Θ
                                                                                 1/2ℓ
                                                                            ) ≥ qw    . This in turn
                                                               M ochizuki,w

is clear from the construction of these sets: they contain the classes Ξz given by Theorem-
Definition 9.8.1.1 obtained from each choice of Tate parameters obtained using the standard
             e L′ and so contain a subset of the type Lemma 9.10.7.1 with τj = logBK (Ξ0,z ,w )
point of the Σ                                                                                   j

(for suitable j). Using this and the relationship between weighted volumes absolute values
established earlier and arguing as in the proof of Theorem 9.9.1, one obtains the assertion.

§ 9.11.1 Proof of Mochizuki’s Corollary 3.12 Mochizuki’s notational conventions [Mochizuki,
2021c, Page 420 and Page 608] sign conventions are a bit awkward to work with. The notation
convention of [Mochizuki, 2021c, Page 420 and Page 608] is designed so that the ration of the

                                                   127
LHS and RHS in [Mochizuki, 2021c, Corollary 3.12] is positive while both the LHS and RHS
are negative. I will define
                               X                                       X
   − LogVol( e
            ΘIM ochizuki ) =       − LogVol( e
                                            ΘM ochizuki,p ) = −              LogVol( e
                                                                                    ΘM ochizuki,p ) .
                               p                                         p


This is perfectly reasonable as the LogVol(Θe M ochizuki,p ) ≤ 0 and this notation convention is
compatible with the following standard properties of real numbers and logarithms: if 0 < x ≤ 1
is a real number then

      log(x) ≤ 0 and so |log(x)| = − log(x) ≥ 0 and hence − |log(x)| = log(x) ≤ 0.

Moreover if 0 < x, y ≤ 1 are real numbers then

                          − |log(x · y)| = log(x · y)
                                         = − |log(x)| + (− |log(y)|)
                                         = −(|log(x)| + |log(y)|).

    To provide a translation of Theorem 9.11.1 into [Mochizuki, 2021c, Corollary 3.12], one
must work with Mochizuki’s notational convention and the above observation regarding log-
arithms of real numbers. From Theorem 9.11.1 one obtains, using Mochizuki’s notational
conventions [Mochizuki, 2021c, Page 420 and Page 608], the assertion known as [Mochizuki,
2021c, Corollary 3.12]:
Corollary 9.11.1.1. With notations and assumptions of Theorem 9.11.1, and in Mochizuki’s
notational conventions [Mochizuki, 2021c, Page 420 and Page 608], one has

                     1                                   X
                              e IM ochizuki ) ≥ −
                   − ∗ LogVol(Θ                                       log qw1/2ℓ L′ .
                    ℓ                                                             w
                                                    p,w∈Vodd,ss
                                                         p      6=∅
```

**(4b) Lemma 9.10.7.1 + Proposition 9.10.8.1 (the passage that actually matches "inclusion
of a full tensor-product lattice from pure tensors/convexity"):**

```latex
§ 9.10.7 Let
                                                            M
                               S ⊂ E1 ⊗Qp · · · ⊗Qp En =          Eα′ .
                                                              α

Then the hull of S, denoted here by hull(S), is the smallest subset hull(S) ⊂ E1 ⊗Qp · · ·⊗Qp En
of the tensor product such that hull(S) ⊃ S and whose image in the direct sum decomposition
on the right is of the form               M
                                               λα OEα′
                                             α

where 0 6= λα ∈ OEα′ .
   Properties of hulls are established in [Mochizuki, 2021c, Remark 3.9.5(ii)].
   The following lemma is now clear:

Lemma 9.10.7.1. Let S ′ ⊃ S = (τ1 OE1 ) ⊗Zp (τ2 OE2 ) ⊗Zp · · · ⊗Zp (τn OEn ) with τi ∈ OEi
for i = 1, . . . , n and suppose Γp are chosen as above and suppose that one has an element
s1 ⊗ s2 ⊗ · · · ⊗ sn ∈ S with si ∈ τi OEi for i = 1, . . . , n. Then
                                                                  n
                                                                  Y                   n
                                                                                      Y
                Γ        ′         Γp
             Vol (hull(S )) ≥ Vol (hull(S)) ≥ Vol (S) ≥Γp
                                                                        |si |γEii ≥         |si |Ei .
                                                                  i=1                 i=1

Proof. The first inequality is immediate from the properties of the hull in [Mochizuki, 2021c,
§ 3]. So the only point which needs to be checked is that 0 < γi ≤ 1, so the last inequality
follows from the fact that all the τi , and hence all the si have absolute values at most one.



                                                 125
§ 9.10.8 Mochizuki’s Hulls and Convex closures In this subsection I want to provide the fol-
lowing proposition which clarifies my usage of convex closures and Mochizuki’s holomorphic
hulls detailed in [Mochizuki, 2021c, Remark 3.9.5]. The notion of convex closure can be made
in any Banach space [Schneider, 2002]. Mochizuki’s notion of holomorphic hull is a bit more
specific. To establish the relationship assume, for notational simplicity, that E1 , E2 are two
p-adic fields considered as finite dimensional vector spaces over Qp .
    I work with the tensor product norm |−|E1 ⊗Qp E2 and the normed Qp -vector space

                                    (E1 ⊗Qp E2 , |−|E1 ⊗Qp E2 )

equipped with this tensor norm.
   On the other hand Mochizuki’s approach to holomorphic hulls detailed in [Mochizuki,
2021c, Remark 3.9.5] is based on the following decomposing the tensor product vector space
E1 ⊗Qp E2 :
                                                    M
                                f : E1 ⊗Qp E2 ≃ /      Fα
                                                           α

into a direct sum of p-adic fields Fα ⊃ Qp (obviously the set {α} is also finite) and work,
according to [Mochizuki, 2021c, Remark 3.9.5], relative to this decomposition. Since E1 ⊗Qp E2
is finite dimensional over Qp , f is an isomorphism of finite dimensional Banach spaces over
Qp .

Proposition 9.10.8.1. In the notation of this paragraph, suppose U ⊂ E1 ⊗Qp E2 is a relatively
compact subset. Let H = H(U) = hull(U) be the hull of U as defined by [Mochizuki, 2021c,
Remark 3.9.5, Page 543]. Then

  (1) H is a convex subset of ⊕α Fα containing f (U) and by [Mochizuki, 2021c, Properties P1,
      P2, P3, Page 534] it is the minimal convex subset containing f (U) with this property.

  (2) If V ⊂ E1 ⊗Qp E2 is a convex subset of this normed vector space then its image under f
      is also convex.

  (3) In particular, if P is a tensor product region of P ⊆ E1 ⊗Qp E2 in the sense of [Mochizuki,
      2021c, Remark 3.1.1], then H(P ) ⊆ ⊕α Fα is the image of the convex closure of P ⊆
      E1 ⊗Qp E2 .

Proof. By the definition of the hull given in [Mochizuki, 2021c, Remark 3.9.5] the hull is an
Zp -module. By the definition of convex subsets [Schneider, 2002, Chap I, § 2], the hull is a
convex subset as it is an Zp -module. By [Mochizuki, 2021c, Remark 3.9.5, Properties P1, P2,
P3] it is the smallest subset with the said properties. This proves (1). The assertion (2) is clear
from the definitions [Schneider, 2002]. The last assertion is a consequence of the fact that
holomorphic hull is the convex closure of f (P ).


                                               126
Remark 9.10.8.2. Because of Proposition 9.10.8.1, one can work with hulls and convex clo-
sures on an equal footing and this allows me to translate my results to Mochizuki’s context. •
```

## 3. Not done / caveats

- **arXiv MCP tools disabled mid-task** (429 rate-limiting, then explicit coordinator
  instruction to stop using them). All extraction above is from `pdftotext -layout` on a
  PDF, not the original `.tex` source — see the method note at the top for what that means
  for tilde/stacked-symbol glyphs.
- **Parts I, II (all three ID variants), and II½ were not independently fetched** — their
  titles/dates in the inventory table come only from WebSearch result snippets and are
  flagged "not independently confirmed" there. They were not searched for the four target
  items at all.
- **Part IV (2403.10430) was checked only via one WebFetch of its HTML rendering**, which
  reported content only up to Section 7 and no Section 9 — but that fetch may have been
  truncated by tool length limits on an 80-page paper rather than proving Section 9 is
  genuinely absent. Not independently re-verified against the PDF.
- **Earlier versions v1–v3 of Construction III were not checked.** v4's change log (from its
  arXiv comment field) states it is "substantially expanded" with new §§1.3/1.7/1.9, §4.6,
  §8.2.2, and a new §12 — meaning section/theorem numbering almost certainly shifted across
  versions. It is plausible that a "Theorem 9.11" existed under that exact label in an
  earlier version and was renumbered to 9.11.1 (or something else) by v4. This was not
  checked due to the time-boxed deadline.
- No correctness, validity, or gap-analysis judgment is made anywhere above on Joshi's
  mathematics — this file is extraction only, per the task instructions.
