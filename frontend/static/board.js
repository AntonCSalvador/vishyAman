let position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
let greed = 0.0
let dfs_position = ""
let bfs_position = ""

updateBoard();

function updatePosition() {
  position = document.getElementById("positionInput").value;
  greed = document.getElementById("greedInput").value;
  document.getElementById("positionInput").value = "";
  document.getElementById("greedInput").value = "";
  sendFen(position, greed);
  updateBoard();
}

function viewDfs() {
  position = dfs_position;
  updateBoard();
}

function viewBfs() {
  position = bfs_position;
  updateBoard();
}

function updateBoard() {
  let c = document.getElementById("board");
  let ctx = c.getContext("2d");

  let currentPositionText = document.getElementById("currentPositionText");
  let currentGreedText = document.getElementById("currentGreedText");
  currentPositionText.innerHTML = position;
  currentGreedText.innerHTML = `greed = ${greed}`

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

    currSquare++;
    currPiece++;
  }
}

function getRandomPosition() {
  fetch("http://127.0.0.1:5000/random_fen", {
    method: "GET",
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    if (data.result.fen) {
      sendFen(data.result.fen, data.result.greed);
    }
    position = data.result.fen;
    greed = data.result.greed;
    updateBoard();
  })
}

function sendFen(fen, greed) {
  fetch('http://127.0.0.1:5000/process_fen', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ fen: fen, greed: greed })
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    // Update the frontend with BFS and DFS results, including execution times
    if (data.result.generate_time_s) {
      document.getElementById('generateTime').textContent = `Time taken to generate graph: ${data.result.generate_time_s} s`
    }
    if (data.result.dfs_best_move) {
      document.getElementById('dfsBestMove').textContent = `DFS Best Move: ${data.result.dfs_best_move} (Time: ${data.result.dfs_time_ms} ms)`;
      document.getElementById('viewDfs').style.display = 'block';
      dfs_position = data.result.dfs_fen;
    } else {
      document.getElementById('dfsBestMove').textContent = `DFS Best Move: No move found`;
    }
    if (data.result.bfs_best_move) {
      document.getElementById('bfsBestMove').textContent = `BFS Best Move: ${data.result.bfs_best_move} (Time: ${data.result.bfs_time_ms} ms)`;
      document.getElementById('viewBfs').style.display = 'block';
      bfs_position = data.result.bfs_fen;
    } else {
      document.getElementById('bfsBestMove').textContent = `BFS Best Move: No move found`;
    }
  })
  .catch((error) => {
    console.error('Error:', error);
    // Handle errors gracefully on the frontend
    document.getElementById('generateTime').textContent = 'Time taken to generate graph: Error fetching data'
    document.getElementById('dfsBestMove').textContent = 'DFS Best Move: Error fetching data';
    document.getElementById('bfsBestMove').textContent = 'BFS Best Move: Error fetching data';
  });
}


