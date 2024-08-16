from flask import Blueprint, request, jsonify   
from models import get_db, User


questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions', methods=['POST'])
def questions():
    # JSON形式で送られてきたデータ（質問項目とその回答）
    data = request.json

    group_name = data['group_name']
    name = data['name']
    age = data['age']
    country = data['country']
    favorite_things = data['favorite_things']
    mbti = data['mbti']
    image_binary = data['image_binary']

    # 上記のデータ以外は質問とその回答
    questions_and_answers = {key: value for key, value in data.items() if key not in ['group_name', 'name', 'age', 'country', 'favorite_things', 'mbti', 'image_binary']}

    # MongoDBに接続し，Userクラスのインスタンスを作成
    db = get_db()
    user_model = User(db)

    # MongoDBにデータを格納
    result = user_model.create_user(
        group_name=group_name,
        name=name,
        age=age,
        country=country,
        favorite_things=favorite_things,
        mbti=mbti,
        image_data=image_binary,
        questions_and_answers=questions_and_answers
    )

    # 保存結果を返す(ドキュメントのID)
    return jsonify({"message": "Data saved successfully", "user_id": str(result.inserted_id)}), 201
