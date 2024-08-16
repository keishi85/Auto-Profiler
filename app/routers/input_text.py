from flask import Blueprint, render_template, request


"""
    プロフィール作成のための入力画面
    
"""


input_text = Blueprint('input_text', __name__)

@input_text.route('/input-text', methods=['GET', 'POST'])
def input_text():
    if request.method == 'POST':
        name = request.form['name']
        group = request.form['group']
        mbti = request.form['mbti']
        image = request.files['image']

        # 画像データをバイナリ形式に変換
        image_data = image.read()

        return render_template('questions.html', name=name, group=group, mbti=mbti, image_data=image_data)
    return render_template('input_text.html')