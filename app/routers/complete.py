from flask import Blueprint, render_template, request, url_for
from app.models import get_db, User

complete_bp = Blueprint('complete', __name__)

@complete_bp.route('/complete', methods=['GET'])
def complete():
    group_name = request.args.get('group_name')

    if not group_name:
        return "Group name is not found", 400
    
    db = get_db()
    user_model = User(db)
    profiles = user_model.get_user_by_group_name(group_name)

    # プロフィールをユーザー名でグループ化
    grouped_profiles = {}
    for profile in profiles:
        name = profile['name']
        if name not in grouped_profiles:
            grouped_profiles[name] = []
        grouped_profiles[name].append({
            'profile_image_url': url_for('image.get_image', profile_id=name),  # name を profile_id として渡す
            'name': profile['name']
        })

    return render_template('complete.html', profiles=grouped_profiles, group_name=group_name)
