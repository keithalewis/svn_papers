#!/bin/sh

source ./functions.sh
./head.cgi

cat <<EoT
<h1>$(up Price)</h1>

<p>
Usually price is quoted as the quantity in an implied currency that
can be exchanged for one unit of an instrument. If the buyer wants to
obtain quantity q of instrument i and gives quantity q' of instrument
i' to the seller, the <em>price</em> is p = &minus;q'/q.  When q &gt; 0
the buyer is <em>going long</em> and if q is the minimum quantity that
the seller uses for instrument i, the price is called the <em>ask</em>.
When q &lt; 0 the buyer is <em>going short</em> and if q is the minimum
quantity that the seller uses for instrument i, the price is called
the <em>bid</em>.  </p>

<p>
The terms <em>buy</em> and <em>sell</em> are also used to
indicate long and short, but a buyer selling sounds oxymoronish to me
so I will use the terms long and short.  </p>

<p>
The ask price is also referred to as the offer, although one could
say the seller is offering to purchase at the bid.
The bid is typically less than the ask. This gives another way to
signal who is the buyer and who is the seller in a transaction. When the
bid is greater than the ask the market is said to be <em>crossed</em>
and arbitrage opportunities exist for buyers.  </p>

EoT

./foot.cgi
