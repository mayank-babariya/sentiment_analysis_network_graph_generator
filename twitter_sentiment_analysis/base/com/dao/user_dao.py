from base import db
from base.com.vo.user_vo import UserVO


class UserDAO():
    def insert_user(self, user_vo):
        db.session.add(user_vo)
        db.session.commit()

    def search_user(self, user_vo):
        user_vo_list = UserVO.query.filter_by(user_login_id=user_vo.user_login_id).all()
        return user_vo_list


