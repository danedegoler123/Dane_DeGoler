function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");

	window.addEventListener("mousemove", icon, false);
	
}
	


function icon(e) {
	canvas.clearRect(0, 0, 600, 600);
	var xPos = e.clientX;
	var yPos = e.clientY;
	var pic = new Image();
	pic.src = "https://lh3.googleusercontent.com/JQEkafjTG0MhpXUZ-d0YIduMv1cIS33yg0AHnKRF9V8sGEHlsgffGOBG01wD59pefkk=w300";
	canvas.drawImage(pic, xPos-100, yPos-100, 200, 200);

}

window.addEventListener("load", mouse, false)
