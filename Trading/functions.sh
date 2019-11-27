function mi { echo "<i class=\"mi\">$@</i>"; }
function sub { echo "<sub>$@</sub>"; }
function sup { echo "<sup>$@</sup>"; }
function smath { echo "<span class=\"math\">$@</span>"; }
function dmath { echo "</p><div class=\"math\">$@</div><p>"; }
function up { echo "<a href=\"${SCRIPT_URI%/*}\">$@</a>&uarr;"; }

#export SCRIPT_URI
