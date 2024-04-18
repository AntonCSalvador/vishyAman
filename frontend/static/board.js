let position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
updateBoard();

function updatePosition() {
  position = document.getElementById("positionInput").value;
  document.getElementById("positionInput").value = "";
  updateBoard();
}

function updateBoard() {
  let c = document.getElementById("board");
  let ctx = c.getContext("2d");

  let currentPositionText = document.getElementById("currentPositionText");
  currentPositionText.innerHTML = position;

  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      ctx.fillStyle = (i + j) % 2 == 0 ? "#FFFFFF" : "#888888";
      ctx.fillRect(i * 60, j * 60, 60, 60);
    }
  }

  let currPiece = 0;
  let currSquare = 0;
  while (position[currPiece] && position[currPiece] != " ") {  
    let piece = position[currPiece];
    if (!isNaN(piece)) {
      currSquare += parseInt(piece);
      currPiece++;
      continue;
    }

    if (piece == "/") {
      currPiece++;
      continue;
    }

    let x = currSquare % 8;
    let y = Math.floor(currSquare / 8);

    let img = new Image();
    img.addEventListener("load", function() {
      ctx.drawImage(img, x * 60, y * 60);
    });
    img.src = `static/pieces/${piece}.png`;
    console.log(img.src, x, y);

    currSquare++;
    currPiece++;
  }
}
