from flask import Flask, jsonify, request
from firebase import firebase
import os
from flask_cors import CORS

app = Flask(__name__)
fb = firebase.FirebaseApplication(
    'https://semantics2-97dc6.firebaseio.com/', None)

#cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/add-user', methods=['POST'])
def add_user():
    user_data = request.get_json(force=True)
    response = fb.post('/users', user_data)
    return jsonify(response)


@app.route("/get-users")
def get_users():
    response = fb.get('/users', None)
    return jsonify(**response)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))  # production IP
