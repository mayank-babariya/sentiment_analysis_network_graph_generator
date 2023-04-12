from base import db
from base.com.vo.login_vo import LoginVO

class LoginDAO:
    def insert_login(self, login_vo):
        db.session.add(login_vo)
        db.session.commit()

    def view_login(self):
        login_vo_list = LoginVO.query.all()
        return login_vo_list

    def validate_login(self, login_vo):
        login_vo_list = LoginVO.query.filter_by(login_username=login_vo.login_username,
                                                login_password=login_vo.login_password)
        return login_vo_list

    def update_password(self, login_vo):
        db.session.merge(login_vo)
        db.session.commit()

    def find_user_secretkey(self, login_vo):
        return LoginVO.query.filter_by(login_secretkey=login_vo.login_secretkey)




