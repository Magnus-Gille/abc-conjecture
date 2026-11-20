# An indexed certificate for the least paired-quartic squareclass

On the fixed elliptic slice at odd indices |n|≥3, define Jₙ=|F₊F₋|/512 and d=sf(Jₙ), the product of primes whose exponents are odd. The minimum is **2,671,321**, achieved at n=3. Two individual rank-zero descents show that each quartic contributes at least one distinct prime to d. Given those descents, the following independent finite proof uses just elliptic addition over prime fields, the Chinese remainder theorem and the Legendre symbol. [Individual square obstructions](abc_eisenstein_slice_squareclass_descent.md) · [Standalone verifier](abc_eisenstein_slice_squareclass_min.py) · [Verified counts](abc_eisenstein_slice_squareclass_min.txt)

Let (x,y) be the primitive odd pair at n, with 3 not dividing x. The quartics are both 1 modulo 3, are coprime away from 2,3, and their 2-adic valuations sum to 9. Write F₊F₋=±512d t². Reduction modulo 3 fixes the sign. On the 2-isogenous curve E′ defined by v²=u³−576u with Q=(−8,−64), put A(u)=u²+336u+576. The identity 4F₊F₋=(xy)⁴A(u(nQ)) implies that A(u(nQ)) has signed rational squareclass
\[
 c=\begin{cases}
  -2d,&d\equiv1\bmod3,\\
  +2d,&d\equiv2\bmod3.
 \end{cases}
\]
These statements can be checked without assigning a prime of d to a particular quartic. When a prime divides xy, the quartics themselves are units at that prime away from 2,3. [Isogeny and paired factor](abc_eisenstein_slice_paired_quartic.md)

Set L=1031·2591. Directly iterate the finite-field orbit of Q at all primes through 300. The three and only three good primes in this range at which an odd multiple hits A=0 are 167,191,263. If d≤L, its at least two distinct prime factors give the upper bound ⌊L/167⌋=15,995 on every one of them. Three different factors would give d≥167·191·263>L. Direct point addition at every prime through 15,995 finds 69 visiting primes, giving 218 unordered pairs with product at most L. For each p, enumerate all odd visiting classes h modulo lcm(2,ordₚ Q). For each pair intersect these classes by generalized CRT. Exactly 120 pairs give an intersection, comprising 444 classes n≡h mod M. The equality candidate accounts for four of them.

For each class and each auxiliary prime ℓ below, evaluate the Legendre symbol of A at the cyclic orbit of Q modulo ℓ. For the point at infinity enter +1, since A(u)/u² is then a unit reducing to 1. At an affine zero of A allow either sign. For a candidate c and a class n≡h mod M, the possible local indices are exactly the residue classes modulo ordₗ Q that equal h modulo gcd(M,ordₗ Q). Discard this class if every such index has the opposite sign from (c/ℓ). None of the six auxiliary primes divides a candidate d.

| Test | Order of Q | Surviving pairs with product strictly below L | Surviving CRT classes below L |
|---|---:|---:|---:|
| Initial CRT | | 119 | 440 |
| ℓ=5 | 4 | 60 | 222 |
| ℓ=7 | 4 | 28 | 104 |
| ℓ=23 | 6 | 7 | 20 |
| ℓ=37 | 6 | 4 | 14 |
| ℓ=43 | 11 | 3 | 10 |
| ℓ=47 | 6 | 0 | 0 |

The only surviving pair is (1031,2591), with necessary residue classes 3,1293,12639,13929 modulo 13932. Existence follows independently by substituting (x,y)=(11,3) at n=3: F₊=32·1031 and F₋=−16·2591. At n=±1 the parameters are (1,1), the normalized squareclass is 1, and the conic output is degenerate. Thus inclusion of those indices would change the answer.

## A gap to any further attaining index

For the equality candidate c=−2·1031·2591, the same orbit tests imply the necessary congruence
\[
 n\equiv\pm3\pmod{751025916841423597521007417808841718128000}.
\]
In particular n=3 is the only positive attaining index strictly below this modulus minus 3. This follows from finite arithmetic independently of an upper height bound for the associated rational points. It leaves open whether a further index attains the minimum.

First lift the four surviving classes to modulus 5·13932=69660. There are twenty candidates; the auxiliary primes 179 and 859 retain exactly ±3. Select the +3 branch; negating the elliptic point preserves its abscissa and hence all conditions, giving the other branch automatically. Independently for each
\[
 K\in\{32,25,49,11,169,289,23,29,31,37,41,47,53,61,73,89,97,101,109,113,137\},
\]
enumerate the K lifts 3+69660j modulo 69660K. At each multiplier two to six explicitly listed auxiliary primes suffice to eliminate every lift except 3. All those primes are below 10,000 and differ from 1031 and 2591. For example K=32 uses 6911,5503,6143. Taking the least common multiple of the resulting moduli gives the displayed integer. The verifier checks every asserted survivor directly and includes all the auxiliary primes for independent reproduction.

~~~sh
python abc_eisenstein_slice_squareclass_min.py
~~~
