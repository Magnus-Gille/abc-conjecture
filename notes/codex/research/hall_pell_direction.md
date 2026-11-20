# A square-factor question on a Hall-type Pell family

Let $F_n,L_n$ be the Fibonacci and Lucas numbers with $F_0=0$, $F_1=1$, $L_0=2$, $L_1=1$. Both satisfy the recurrence $u_{n+2}=u_{n+1}+u_n$. For $n=7+12j$, $j\ge0$, set $t=L_n-11$ and $z=F_n$. Then $(t+11)^2-5z^2=-4$. Put

$$ A=t^2+10t+5,\qquad B=t^2+4t-1. $$

Expanding the fixed polynomials gives $A^3-(t^2+22t+125)B^2=1728t$. Substituting the Pell equation yields the integer triple

$$1728t + 5(zB)^2 = A^3.$$

These triples are primitive. The Lucas recurrence gives $(L_{12},L_{13})=(2,1)$ modulo 10, so $t\equiv8\pmod{10}$ throughout the progression. Thus $A$ is odd and $\gcd(A,t)=\gcd(5,t)=1$. Also $A\equiv t^2+t+2\pmod3$ has no zero modulo 3. Consequently $\gcd(1728t,A^3)=1$.

## Why measure repeated factors here

Put $M=t z A B$. The triple has radical $\operatorname{rad}(30M)$ and height $c=A^3$. As $j$ grows, both $M$ and $c$ are asymptotic to positive constants times $t^6$, while $\log t=n\log((1+\sqrt5)/2)+o(1)$. Thus a fixed exponent violation along this family occurs infinitely often exactly when $\limsup \log(M/\operatorname{rad}M)/n>0$. All primes common to two of $t,z,A,B$ are among 2, 3 and 5. For $t,A,B$ this follows from their pairwise resultants (5, −1, −144 in the order $t,A$; $t,B$; $A,B$). For a common prime involving $z$, use $5z^2=t^2+22t+125$ and the resultants of the latter polynomial with $t,A,B$, whose absolute values are 125, 720 and 6480.

## A recurring square and its first lift

The recurrence gives $L_{223}\equiv782\pmod{29^2}$ and $(L_{2436},L_{2437})\equiv(2,1)\pmod{29^2}$. For $n=223+2436j$ this gives $t\equiv-70\pmod{29^2}$ and $A(-70)=4205=5\cdot29^2$. These indices belong to the primitive progression above. In particular, this fixed square really survives in the radical calculation.

On the same progression, $A/29^2\equiv 8-4j\pmod{29}$. To check this first lift, the Fibonacci companion matrix $T$ has $T^{2436}\equiv I\pmod{29^2}$ (the recurrence gives $F_{2436}\equiv0$, $F_{2437}\equiv1$). Hence $T^{2436j}\equiv I+j(T^{2436}-I)\pmod{29^3}$, so $A/29^2$ is affine in $j$ modulo 29. At $j=0,1$ the values are 8 and 4. Thus the cube condition selects exactly $j\equiv2\pmod{29}$ within the square progression.

One fixed square saves only a constant factor in the radical. The research question is whether higher powers or several distinct square divisors can occur together often enough on individual indices to give a saving exponential in $n$. An initial tractable target is to characterize the index classes for the other primes dividing $A$ or $B$ twice and test the compatibility and sizes of their smallest simultaneous solutions. No estimate here establishes a positive limiting exponent.
