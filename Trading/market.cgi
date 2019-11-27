#!/bin/sh

source ./functions.sh
./head.cgi

cat <<EoT
<h1>$(up Market)</h1>
<p>
There are two kinds of markets. <em>Over-the-counter</em> markets enable
buyers to locate sellers that exchange instruments directly, while
<em>exchanges</em> match buyers and somewhat anonymous sellers.
When a buyer specifies a quantity and instrument, a <em>market</em>
A market, at any given time, determines the quantity a seller
will exchange a given instrument with a buyer that specifies
a quantity and
</p>

<h2>Over-the-counter</h2>
<p>
Instruments that are exchanged directly between two counterparties are
said to trade over-the-counter or <em>off-exchange</em>.  The sellers
are typically investment banks or mutual funds. The buyers are typically
businesses or individuals.  </p>

<p>
Other than puts, calls, and futures, most derivatives trade OTC.  </p>

<h2>Exchanges</h2>
<p>
Exchanges have agreements with <em>market makers</em>, or <em>liquidity
providers</em>, to provide two sided quotes on the instruments the
exchange trades. Customers of the exchange can place limit orders
or market orders. There are other types of orders, but they are all
essentially limit orders with additional conditions.  </p>

<!-- link to various order types -->

<h3>Limit Orders</h3>
<p>
A <em>limit order</em> for an instrument specifies a <em>price</em> and
a <em>quantity</em>.  The customer wishes to obtain the specified quantity
of the instrument at the specified price.
If the quantity is positive, it is a <em>buy order</em>. If the quantity
is negative, it is a <em>sell order</em>.
If the order is <em>filled</em>
or <em>executed</em>, the customer's wish is fullfilled.  The customer
can also <em>cancel</em> the order at any point before it is filled. </p>

<p>
The <em>order book</em> is the collection of all limit orders.
The order book for an instrument can be represented as a non-decreasing
function. If $(smath '{('p$(sub i), q$(sub i)')}')
is the collection of prices and
quantities of all limit orders, this function is

<blockquote>
&beta; = &sum;$(sub '{q<sub>i</sub> &gt; 0}') q$(sub i)
1$(sub '[p'$(sub i)',&infin;)')
&minus; &sum;$(sub '{q'$(sub i)' &lt; 0}') q$(sub i)
1$(sub '(&minus;&infin;,p'$(sub i)']')
= &sum; q$(sub i) L$(sub p$(sub i)),
</blockquote>
where L$(sub p) = 1$(sub '[p,&infin;)') if p &gt; 0 and
L$(sub p) = &minus;1$(sub '(&minus;&infin;,p]')
if p &lt; 0. Recall 1$(sub A) is the <em>characteristic
function</em> defined by 1$(sub A)(x) = 1 if x &isin; A
and  1$(sub A)(x) = 0 if x &notin; A
</p>
<p>
Define ask(&beta;) = inf$(sub '&beta;(&lambda;) &gt; 0') &lambda;
and bid(&beta;) = sup$(sub '&beta;(&lambda;) &lt; 0') &lambda;
</p>

<h3>Market Orders</h3>
<p>
A <em>market order</em> for an instrument only specifies a quantity.
The customer wishes to immediately obtain the specified quantity of the
instrument. The exchange pairs off the quantity of the market order with
the best quotes for existing limit orders. Between the time the market
order is submitted and time it gets executed, other market orders may
be executed, or limit orders may be cancelled, so there is no guarantee
that the price quoted as the best at the time of submission will be
the same as the price at which the order is executed. This is called
<em>slippage</em>. </p>

<p>
When a market order of quantity q &gt; 0 is executed, the order book
&beta; becomes
<blockquote>
<table cellpadding=\"0\" cellspacing=\"0">
  <tr>
    <td></td>
	<td class="lceil">&nbsp;</td>
    <td>&beta;</td>
	<td>, (&minus;&infin;, ask(&beta;)]</td>
  </tr>
  <tr>
    <td>&beta;' =&nbsp;</td>
	<td class="lbar">&nbsp;</td>
    <td>0</td>
	<td>, (ask(&beta;), &beta;$(sup '&minus;1')(q)]</td>
  </tr>
  <tr>
    <td></td>
	<td class="lfloor">&nbsp;</td>
    <td>&beta; &minus; q</td>
	<td>, (&beta;<sup>&minus;1</sup>(q), &infin;)</td>
  </tr>
</table>
</blockquote>
This defines an operator on order books M<sub>q</sub>(&beta;) =
&beta;' for q &gt; 0. Note M<sub>q</sub>M<sub>q'</sub> = M<sub>q +
q'</sub>. The infinitesimal generator for this semigroup is A(&beta;)
= 1<sub>[ask(&beta;), &infin;)</sub> </p>

<p>
When a market order of quantity q &lt; 0 is executed, the order
book &beta; becomes
<blockquote>
<table cellpadding=\"0\" cellspacing=\"0">
  <tr>
    <td></td>
	<td class="lceil">&nbsp;</td>
    <td>&beta; + q</td>
	<td>, (&minus;&infin;, &beta;<sup>&minus;1</sup>(q)]</td>
  </tr>
  <tr>
    <td>&beta;' =&nbsp;</td>
	<td class="lbar">&nbsp;</td>
    <td>0</td>
	<td>, (&beta;<sup>&minus;1</sup>(q), bid(&beta;)]</td>
  </tr>
  <tr>
    <td></td>
	<td class="lfloor">&nbsp;</td>
    <td>&beta;</td>
	<td>, (bid(&beta;), &infin;)</td>
  </tr>
</table>
</blockquote>
This defines an operator on order books M<sub>q</sub>(&beta;) =
&beta;' for q &lt; 0. Note M<sub>q</sub>M<sub>q'</sub> = M<sub>q +
q'</sub>. The infinitesimal generator for this semigroup is B(&beta;)
= 1<sub>(&minus;&infin;, bid(&beta;)]</sub> </p>

<p>
The price at which a market order will be executed when it arrives
against the book &beta; is &int;$(sub 0)$(sup q) &beta;/q.
</p>
EoT

./foot.cgi
