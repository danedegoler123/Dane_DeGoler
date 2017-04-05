function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	var g = canvas.createLinearGradient(10, 10, 350, 450);
	g.addColorStop(0, "purple");
	g.addColorStop(.5, "white");
	g.addColorStop(1, "yellow");
	canvas.fillStyle = g
	canvas.beginPath();
	canvas.moveTo(50, 50);
	canvas.lineTo(100, 150);
	canvas.lineTo(10, 200);
	canvas.lineTo(100, 250);
	canvas.lineTo(50, 360);
	canvas.lineTo(150, 300);
	canvas.lineTo(200, 400);
	canvas.lineTo(250, 300);
	canvas.lineTo(350, 360);
	canvas.lineTo(300, 250);
	canvas.lineTo(400, 200);
	canvas.lineTo(300, 150);
	canvas.lineTo(350, 50);
	canvas.lineTo(250, 150);
	canvas.lineTo(200, 50);
	canvas.lineTo(150, 150);
	canvas.closePath();
	canvas.stroke();
	canvas.fill();

}

window.addEventListener("load", shapes, false);