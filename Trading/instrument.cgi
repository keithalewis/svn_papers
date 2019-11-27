#!/bin/sh

source ./functions.sh
./head.cgi

cat <<EoT
<h1>$(up Instrument)</h1>
<p>
Instruments are the things that are exchanged. In particular, currency
is an instrument on equal footing with stocks, bonds, options and the
rest of the laundry list. Simple as that.  </p>

<p>
The buyer specifies the <em>base</em> quantity and instrument they
wish to acquire from the seller in exchance for another instrument.
The seller specifies the <em>counter</em>, or <em>quote</em>, quantity
required of the buyer in order for the exchange to occur. </p>

<p>
An <em>amount</em> is a quantity and an instrument. A <em>cash flow</em>
is a date and an amount.  A derivative security is an instrument that is
a contract specifing future cash flows between two counterparties.  </p>

<!-- commodities? -->

EoT

./foot.cgi
