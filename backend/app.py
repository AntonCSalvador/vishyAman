from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

@app.route('/process_fen', methods=['POST'])
def process_fen():
    data = request.get_json()  # Get JSON data sent from frontend
    fen = data['fen']  # Extract FEN string from data

    # Process the FEN string
    result = process_fen_string(fen)
    
    return jsonify({'result': result})  # Return result as JSON

def process_fen_string(fen):
    # Replace this placeholder with the actual logic to process the FEN string
    return f"Processed FEN: {fen}"  # Example processing function

if __name__ == '__main__':
    app.run(debug=True)

