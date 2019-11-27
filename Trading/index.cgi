#!/bin/sh
# Creates html output.

source ./functions.sh
./head.cgi

cat <<EoT
<span class="blurb">
<em>Toward a Transformative Hermeneutics of Technical Analysis...</em>
</span>
<h1>Introduction</h1>
<p>
I used to think technical analysis was a bunch of phony baloney until I
worked at Morgan Stanley in the late 90's. They paid a bunch of people
to divine the best execution of trades by looking at head-and-shoulders
patterns or other "tea leaves" in the market. I knew then that there
had to be something to it. Morgan Stanley has a lot of bright people
and they don't pay for things that don't work. I just didn't know what
there was to it.  </p>

<p>
Technical analysis resembles stamp collecting. There does not seem
to be any theory behind it, just descriptions of how some people
claim to trade. These notes are my attempt to deconstruct technical
analysis. Don't ask why, but my current subway reading is Derrida. I
used to think he was full of baloney too, but not anymore. There is a
reason so many people still read him. The blurb at the top is a play
on <a href="http://www.physics.nyu.edu/faculty/sokal/">Alan Sokal</a>'s
article that parodied postmodernists. As a mathematician, I have a lot
of respect for Derrida's attempts to get to the bottom line.
 </p>

<h2><a href="participant.cgi">Participant</a></h2>
<p>
Adam Smith noted man's "propensity to truck, barter, and exchange one
thing for another." </p>

<h2><a href="price.cgi">Price</a></h2>
<p>
Price determines the quantity the seller exchanges with the buyer.  </p>

<h2><a href="instrument.cgi">Instrument</a></h2>
<p>
This section describes the raw material of technical analysis. The
things that are exchanged.
</p>

<h2><a href="market.cgi">Market</a></h2>
<p>
Markets exist for participants to exchange instruments.
</p>

<h2><a href="account.cgi">Account</a></h2>
<p>
Accounts keep track of exchanges participants make.
</p>

<h2><a href="trading.cgi">Trading</a></h2>
<p>
The heart of the matter.
</p>

<h2><a href="model.cgi">Model</a></h2>
<p>
Models allow one to mathematically reason about the future.
</p>

EoT

./foot.cgi
