from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

# ここに他のルートを追加できます
# 例: /api/v1/ など

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
