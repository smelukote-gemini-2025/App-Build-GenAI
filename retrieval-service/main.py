import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {"message": "Data from retrieval service"}
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
