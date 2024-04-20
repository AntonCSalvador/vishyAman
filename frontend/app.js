function sendFen() {
    const fen = document.getElementById('positionInput').value;
    fetch('http://localhost:5000/process_fen', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ fen: fen })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Display the returned data in the HTML
        document.getElementById('currentPositionText').innerText = data.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

