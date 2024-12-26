from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example whitelist for testing
whitelist = ["B4USdgqb5teCConcGhjA9u9Pi4fzyyLfpoc5jfyyBP",
             "wallet2", 
             "wallet3"]

@app.route("/check_wallet", methods=["POST"])
def check_wallet():
    data = request.json
    wallet_address = data.get("wallet", "").strip()
    if wallet_address in whitelist:
        return jsonify({"status": "success", "message": "You are on the whitelist!"})
    else:
        return jsonify({"status": "error", "message": "You are NOT on the whitelist!"})

if __name__ == "__main__":
    app.run(debug=True)
