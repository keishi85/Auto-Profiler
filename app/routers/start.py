from flask import Blueprint, render_template, request

"""
     スタート画面
     グループ名の入力
"""

group_bp = Blueprint('start', __name__)

@group_bp.route('/start', methods=['GET', 'POST'])
def group():
    if request.method == 'POST':
        group_name = request.form["group_name"]
        return render_template('input_text.html', group_name=group_name)
    return render_template('start.html')