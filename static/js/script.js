var canvas = document.getElementById('drawingCanvas');
var context = canvas.getContext('2d');

var radius = 14;
var start = 0;
var end = Math.PI * 2;
var clicking = false;

context.lineWidth = radius * 2;

var drawPoint = function(e){
	if(clicking){
		context.lineTo(e.offsetX, e.offsetY);
		context.stroke();
		context.beginPath();
		context.arc(e.offsetX, e.offsetY, radius, start, end);
		context.fill(); 
		context.beginPath();
		context.moveTo(e.offsetX, e.offsetY);
	}
}

var mouseclick = function(e){
	clicking = true;
	drawPoint(e);
}

var mouserelease = function(){
	clicking = false;
	context.beginPath();
}

canvas.addEventListener('mousedown', mouseclick);
canvas.addEventListener('mousemove', drawPoint);
canvas.addEventListener('mouseup', mouserelease);