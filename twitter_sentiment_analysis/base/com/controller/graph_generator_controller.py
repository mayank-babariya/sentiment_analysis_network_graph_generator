from flask import render_template, redirect, request, url_for, make_response, session, flash, jsonify
from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO
from base.com.dao.user_dao import UserDAO
from base.com.vo.user_vo import UserVO
from base.com.controller.login_controller import global_login_secretkey_set
from base.com.controller.tweets_collector import start_collector
from base.com.controller.generate_graph_nkx import main_start_generate_graph
import os
import time

@app.route('/graph_generator', methods=['GET'])
def graph_generator():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    return render_template('graph.html')

@app.route('/start_generate_graph', methods=['GET','POST'])
def start_generate_graph():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    data = request.form.get('has_tag')
    df = start_collector(data,request.cookies.get('login_secretkey'))
    if main_start_generate_graph(df,data,request.cookies.get('login_secretkey')):
        time.sleep(5)
        return render_template('graph.html',result_img = '../../static/user/'+request.cookies.get('login_secretkey')+'.png')
    else:
        return render_template('graph.html')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response