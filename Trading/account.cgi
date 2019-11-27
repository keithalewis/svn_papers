#!/bin/sh

source ./functions.sh
./head.cgi

cat <<EoT
<h1>$(up Account)</h1>
<p>
An <em>account</em> is a collection of transaction.  Account entries have
the form a = (t, q, i, c,  q', i', c') where t is the time the transaction
occurs, q is the quantity in instrument i that participant c exchanges
for q' in instrument i' with participant c'.  </p>


EoT

./foot.cgi
