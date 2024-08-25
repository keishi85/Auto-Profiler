from flask import Blueprint, render_template, request

"""
    終了画面への遷移
"""

complete_bp = Blueprint('complete', __name__)

@complete_bp.route('/complete', methods=['GET', 'POST'])
def complete():
    return render_template('complete.html')