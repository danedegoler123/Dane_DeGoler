function validate() {
	var x = document.forms.input.username.value;
	var y = document.forms.input.password.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	
	//we need... username@webaddress.extension
	//if, the following...
		//@ is not in the string
		//@ is in the wrong place
		//there is no .com, .gov or any other extensino
		//final dot is in the wrong place
	if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length) 
		if (y.length < 6)
			alert("We were unable to process your request. Please correct the following errors... You did not provide a valid email adress AND your password does not mee the minimum requirements");

	if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
			alert("We were unable to process your request. Please correct the following errors... You did not provide a valid email adress");

	if(y.length < 6)
		alert("We were unable to process your request. Please correct the following errors... Your password does not meet the minimum requirements");

	else
		alert("Success!")
}

validate()