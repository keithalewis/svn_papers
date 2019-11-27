#!/bin/sh

source ./functions.sh
./head.cgi

cat <<EoT
<h1>$(up Participant)</h1>
<p>
Every exchange of one thing for another involves two
<em>participants</em>. A participant can be either a
<em>buyer</em> or <em>seller</em>. The buyer is characterized as the
one deciding to initiate the exchange. The seller is characterized
by the passive advertisement of the possibility of exchange to potential
buyers. Or maybe not so passive.
</p>

<h2>Counterparty</h2>
<p>
The legal definition of <em>counterparty</em> is a party to a contract.
The contract specifies the terms and conditions of the exchange between
the buyer and seller. Technically, every participant is a counterparty
but brokers and dealers aren't usually considered couterparties.
</p>

<h2>Broker</h2>
<p>
A <em>broker</em> brings together buyers and sellers, but does not take
a position in the things being exchanged. Typically, a broker has an
agreement with a number of <em>market makers</em> that quote
prices at which they are willing to trade. The broker provides
clients with the best quotes from the market makers plus a spread,
or markup, that they charge to their customers.</p>

<h2>Dealer</h2>
<p>
A <em>dealer</em> is a participant willing to either buy or sell the
things being exchanged and typically keeps an inventory.  The dealer
quotes an ask price at which the dealer will sell and a bid price at
which the dealer will buy. </p>

EoT

./foot.cgi
