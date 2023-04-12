from flask import render_template, redirect, request, url_for, make_response, session, flash
from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO
from base.com.dao.user_dao import UserDAO
from base.com.vo.user_vo import UserVO
import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
email_username = os.environ.get('EMAIL_USER')
email_password = os.environ.get('EMAIL_PASSWORD')

global_login_secretkey_set = {0}

@app.route('/', methods=['GET'])
def login():
    return redirect('/validate_login')

@app.route('/validate_login', methods=['GET','POST'])
def validate_login():
    try:
        if request.method == 'POST':
            login_vo = LoginVO()
            login_dao = LoginDAO()
            login_vo.login_username = request.form.get('loginUsername')
            login_vo.login_password = request.form.get('loginPassword')
            login_vo_list = login_dao.validate_login(login_vo)
            login_list = [i.as_dict() for i in login_vo_list]
            if len(login_list) == 0:
                error_message = 'username or password is incorrect !'
                flash(error_message)
                return redirect('/')
            else:
                user_vo = UserVO()
                user_vo.user_login_id = login_list[0].get('login_id')
                user_dao = UserDAO()
                list_users =user_dao.search_user(user_vo)
                list_users = [i.as_dict() for i in list_users]
                session['first_name'] = list_users[0].get('user_firstname')
                response = make_response(redirect(url_for('load_dashboard')))
                response.set_cookie('login_secretkey', value=login_list[0].get('login_secretkey'))
                global_login_secretkey_set.add(login_list[0].get('login_secretkey'))
                return response
        elif request.method =='GET':
            return render_template('login.html')
    except Exception as ex:
        print("validate_login route exception occured>>>>>>>>>>", ex)

@app.route('/load_dashboard', methods=['GET'])
def load_dashboard():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    return render_template('home.html')

@app.route('/register_user', methods=['GET','POST'])
def register_user():
    try:
        if request.method == 'GET':
            return render_template('signup.html')

        elif request.method == 'POST':
            login_dao = LoginDAO()
            login_vo = LoginVO()
            user_dao = UserDAO()
            user_vo = UserVO()

            login_username = request.form.get("loginUsername")
            user_firstname = request.form.get("userFirstname")
            user_lastname = request.form.get("userLastname")
            user_gender = request.form.get("userGender")
            user_contact = request.form.get("userContact")
            user_address = request.form.get("userAddress")
            user_area_id = request.form.get("userAreaId")
            user_password = request.form.get("loginPassword")

            login_secretkey = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(32))
            login_vo_list = login_dao.view_login()
            if len(login_vo_list) != 0:
                for i in login_vo_list:
                    if i.login_secretkey == login_secretkey:
                        login_secretkey = ''.join(
                            (random.choice(string.ascii_letters + string.digits)) for x in range(32))
                    if i.login_username == login_username:
                        error_message = "The username is already exists !"
                        flash(error_message)
                        return redirect("/")
            login_vo.login_username = login_username
            login_vo.login_password = user_password
            login_vo.login_role = "user"
            login_vo.login_status = "active"
            login_vo.login_secretkey = login_secretkey
            login_dao.insert_login(login_vo)

            user_vo.user_firstname = user_firstname
            user_vo.user_lastname = user_lastname
            user_vo.user_gender = user_gender
            user_vo.user_address = user_address
            user_vo.user_contact = user_contact
            user_vo.user_login_id = login_vo.login_id
            user_vo.user_area_id = user_area_id
            user_dao.insert_user(user_vo)
            return redirect('/')
    except Exception as ex:
        print("in register_user route exception occured>>>>>>>>>>", ex)

@app.route('/home', methods=['GET'])
def home():
    if request.cookies.get('login_secretkey') not in global_login_secretkey_set:
        return redirect('/')
    return render_template('home.html')

@app.route('/logout', methods=['GET'])
def logout():
    login_secretkey = request.cookies.get('login_secretkey')
    response = make_response(redirect('/'))
    response.set_cookie('login_secretkey', "", max_age=0)
    session.clear()
    return response

@app.route('/forget_password', methods=['GET'])
def forget_password():
    return render_template('forget.html')

@app.route('/change_password', methods=['POST'])
def change_password():
    login_vo = LoginVO()
    login_dao = LoginDAO()
    login_vo.login_username = request.form.get('loginUsername')
    login_vo.login_password = request.form.get('loginPassword')
    new_password = request.form.get('NewPassword')
    login_vo_list = login_dao.validate_login(login_vo)
    login_list = [i.as_dict() for i in login_vo_list]
    if login_list:
        login_vo.login_id = login_list[0].get('login_id')
        login_vo.login_secretkey = login_list[0].get('login_secretkey')
        login_vo.login_password = new_password
        login_dao.update_password(login_vo)
        send_mail(login_vo.login_username)
        return redirect(url_for('login'))
    else:
        flash('Username or password is incorrect!')
    return redirect('/forget_password')

def send_mail(username):
    sender = email_username
    password = email_password
    receiver = username
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Confirmation: Your Account Password Has Been Successfully Changed."
    body = "Dear Sir/Ma'am,\nWe are writing to confirm that your account password has been successfully changed.\nIf you did not authorize this change, please contact us immediately, so that we can secure your account.\n\nBest regards,\nSentiment Analyzer and Network graph generator."
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()
