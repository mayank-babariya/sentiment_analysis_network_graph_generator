from base import db
from base.com.vo.analysis_vo import AnalysisVO

class AnalysisDAO:
    def insert_analysis(self, analysis_vo):
        db.session.add(analysis_vo)
        db.session.commit()