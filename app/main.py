from flask import Flask, render_template
from app.models import init_app

from app.routers.start import start_bp
from app.routers.questions import questions_bp


app = Flask(__name__)

# MongoDBの初期化
app.config['MONGO_URI'] = 'mongodb://mongo:27017/web_app_db'
init_app(app)

# ルーティングの登録
app.register_blueprint(start_bp)
app.register_blueprint(questions_bp)


@app.route('/')
def index():
    return render_template('start.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
