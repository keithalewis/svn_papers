#!/bin/sh

source functions.sh
./head.cgi

cat <<EoT
<h1>$(up Model)</h1>
<p>
Adam Smith didn't have much to say about models.  Only much later
did Bachelier start using Brownian motion to understand the pricing
of options.  </p>

<p>
I eschew the unrealistic continuous time models found in the literature
for a discrete time model. This avoids the doubling strategy Zeno style
paradox.  Trades can only occur at times t$(sub 0), t$(sub 1),..., t$(sub
n).  The set of all possible outcomes is &Omega;. At each time t$(sub
j) the model represents partial information about the eventual outcome,
&omega;&isin;&Omega;, by an algebra of subsets of &Omega; denoted F$(sub
j) that can be infinite, but are not assumed to be &sigma;-algebras. </p>

<p>
A model of market prices is a F$(sub j) measurable function X$(sub j)(q,
i, c, i', c'; &omega;) = x. If buyer c decides to exchange q units of
instrument i with seller c' in intrument i', then then the account entry
(t$(sub j), q, i, c, -xq, i', c') will result.  </p>

<p>
Buyers generally have more information available to them than sellers.
They know whether or not they are going to buy. At each time t$(sub j)
this information is represented by the algebra G$(sub j). Sometimes buyers
don't pay as much attention to the market as they should so to incorporate
this possibility I won't assume G$(sub j) &supe; F$(sub j).  </p>

<p>
The owner of an instrument gets certain cash flows. Stocks pay dividends.
Bonds have coupons. Foreign exchange transactions involve interest rate
rolls. American options can be exercised. This is modelled by a F$(sub j)
&or; G$(sub j) measurable function C$(sub j)(q, i, c; &omega;) = c.  </p>

EoT

./foot.cgi
