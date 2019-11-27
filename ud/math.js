function math() {
	alert("math called");
	document.getElementsByName("math").forEach(function(e) {
		e.innerText = "it";
	});
}
