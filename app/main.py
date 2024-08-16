from flask import Flask, jsonify
from app.models import init_app


app = Flask(__name__)

# MongoDBの初期化
app.config['MONGO_URI'] = 'mongodb://mongo:27017/web_app_db'
init_app(app)


@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
