from flask import Blueprint, render_template, request


questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        answers = request.form.tp_dict()

        # 回答の処理
        return 