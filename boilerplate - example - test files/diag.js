//#region Set up

var rows = 10;
var columns = 10;

// max window width and height
var height = document.documentElement.clientHeight;
var width = document.documentElement.clientWidth;

var ctx = document.querySelector("canvas").getContext("2d");

ctx.canvas.height = height;
ctx.canvas.width = width;

// Procedurally creates all the nested div's
for (let y = 0; y < rows; y++) {
  for (let x = 0; x < columns; x++) {
    var tile = document.createElement("div");
    document.getElementById("button_container").appendChild(tile);
  }
}

//#endregion Set up

//#region Procedural

ctx.canvas.addEventListener("mousemove", (event) => {
  mousex = event.x;
  mousey = event.y;
});

//#endregion Procedural
