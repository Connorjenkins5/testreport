from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bot-status', methods=['POST'])
def bot_status():
    data = request.json  # Get JSON data from the POST request
    status = data.get('status', 'Unknown')
    
    # Here, you can store the status in a database, log it, etc.
    print(f"Received bot status: {status}")
    
    return jsonify({"message": "Status received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
