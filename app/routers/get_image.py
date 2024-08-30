# from flask import Blueprint, send_file, abort
# from io import BytesIO
# from app.models import get_db, User

# image_bp = Blueprint('image', __name__)

# @image_bp.route('/image/<string:profile_id>', methods=['GET'])
# def get_image(profile_id):
#     db = get_db()
#     user_model = User(db)
#     print('profile_id:', profile_id)
    
#     # データベースから画像データを取得
#     profile = user_model.get_user_by_name(profile_id)
#     if not profile:
#         print('profile not found')
#         abort(404)
    
#     image_data = profile.get('profile')
#     if not image_data:
#         print('image not found')
#         abort(404)
    
#     # BytesIOを使用して画像データを返す
#     buffer = BytesIO(image_data)
#     return send_file(buffer, mimetype='image/png', as_attachment=False, download_name='profile.png')
