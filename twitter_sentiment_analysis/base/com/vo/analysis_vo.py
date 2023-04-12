from base import db
from base.com.vo.login_vo import LoginVO

class AnalysisVO(db.Model):
    __tablename__ = 'analysis_table'
    analysis_id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    has_tags = db.Column('has_tags', db.String(100), nullable=False)
    result = db.Column('result', db.String(100), nullable=False)
    user_login_id = db.Column('user_login_id', db.Integer, db.ForeignKey(LoginVO.login_id))

    def as_dict(self):
        return {
            'analysis_id': self.analysis_id,
            'has_tags' : self.has_tags,
            'result' : self.result,
            'result' : self.result,
            'user_login_id': self.user_login_id,
        }
db.create_all()
