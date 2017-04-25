function drag() {
	mantis = document.getElementById("mantisShrimp");
	leftbox = document.getElementById("leftBox");
	
	mantis.addEventListener("dragstart", startDrag, false);
	mantis.addEventListener("dragend", endDrag, false);
	
	leftbox.addEventListener("dragenter", dragEnter, false);
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) 
{
	var pic = '<img id = "mantisShrimp" src = "http://www.slate.com/content/dam/slate/articles/video/video/2015/09/mantis_shrimp_fights_are_long_brutal_but_not_fatal_video/tnc150925_shrimpfight_1280.jpg.CROP.promo-xlarge2.jpg">';
	e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) 
{
	e.preventDefault();
	leftbox.style.background = "purple";
	leftbox.style.border = "3px solid green";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "white";
	leftbox.style.border = "3px solid purple";
} 

function endDrag(e) {
	pic = e.target;
	pic.style.visibility = "hidden";
}

function drop(e) 
{
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

window.addEventListener("load", drag, false);

