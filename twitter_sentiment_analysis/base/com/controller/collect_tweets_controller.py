from flask import render_template,send_from_directory, redirect, request, url_for, make_response, session, flash, jsonify
from base import app
from base.com.controller.login_controller import global_login_secretkey_set
from base.com.controller.tweets_collector import start_collector
import os

@app.route('/collect_tweets', methods=['GET'])
def collect_tweets():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    return render_template('collect_tweets.html')

@app.route('/start_collect', methods=['GET','POST'])
def start_collect():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    data = request.get_json()
    df = start_collector(data['has_tag'],request.cookies.get('login_secretkey'))
    return jsonify({'result':df})

@app.route('/download_file', methods=['GET'])
def download_file():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    return send_from_directory(directory=os.getcwd()+'/base/static/user/',filename=request.cookies.get('login_secretkey')+'.csv',as_attachment=True)
