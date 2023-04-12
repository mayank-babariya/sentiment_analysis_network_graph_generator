from flask import render_template, redirect, request, url_for, make_response, session, flash, jsonify
from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO
from base.com.dao.user_dao import UserDAO
from base.com.vo.user_vo import UserVO
from base.com.vo.analysis_vo import AnalysisVO
from base.com.dao.analysis_dao import AnalysisDAO
from base.com.controller.login_controller import global_login_secretkey_set
from base.com.controller.tweets_collector import start_collector
from tensorflow.keras.models import load_model
from base.com.controller.sentiment_analyzer import start_sentiment

@app.route('/analyze_on_tags', methods=['GET'])
def analyze_on_tags():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    return render_template('analyze_on_tags.html')

@app.route('/start_analyze', methods=['GET','POST'])
def start_analyze():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    data = request.get_json()
    df = start_collector(data['has_tag'],request.cookies.get('login_secretkey'))
    login_vo = LoginVO()
    login_vo.login_secretkey = request.cookies.get('login_secretkey')
    login_dao = LoginDAO()
    user = [i.as_dict() for i in login_dao.find_user_secretkey(login_vo)]
    analysis_vo = AnalysisVO()
    analysis_vo.has_tags = data['has_tag']
    analysis_vo.user_login_id = user[0].get('login_id')
    result = start_sentiment(df)
    print(len(df))
    positive = int()
    negative = int()
    for i in result:
        if i.get('result') and i.get('result')>50:
            positive += 1
        elif i.get('result') and i.get('result') < 50:
            negative += 1
    analysis_vo.result = (positive/len(df))*100
    analysis_dao = AnalysisDAO()
    analysis_dao.insert_analysis(analysis_vo)
    return jsonify({'result': result})