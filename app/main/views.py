# -*- coding: utf-8 -*-
__author__ = 'ivany'
from flask import render_template, redirect, url_for, g, request, session, current_app, jsonify
from flask.ext.login import current_user, logout_user, login_required, login_user
from . import main
from app import login_manager
from ..models import Article, Comment, Member
from ..utils import md5
from datetime import datetime
from config import config

@main.before_request
def before_request():
    g.member = current_user

@login_manager.user_loader
def user_loader(tm_id):
    return Member.query.get(tm_id)

@main.route("/")
def index():



    return render_template("index.html")

@main.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("signin.html")
    account = request.form['account']
    password = request.form['password']
    if account == '' or password == '':
        return render_template("signin.html")

    member = Member.query.filter_by(tm_account=account).first()

    if member is not None and member.tm_password == md5(password):
        login_user(member)
        g.member = member
        session['tm_id'] = member.tm_id
        return redirect(url_for("main.index"))
    return render_template("signin.html")

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route("/add", methods=['GET','POST'])
@login_required
def add():
    method = request.method
    if method == 'GET':
        return render_template("add.html")
    else:
        try:
            article = Article()
            title = request.form['title']
            content = request.form['editer-markdown-doc']
            html = request.form['editer-html-code']
            type = request.form['ta_type']
            article.ta_title = title
            if title == '' or content == '':
                return render_template("add.html", data={'title': title, 'content': content})
            if type == '':
                type = 0

            article.ta_title = title
            article.ta_addtime = datetime.now()
            article.ta_update_time = datetime.now()
            article.ta_category = 0
            article.ta_type = type
            article.ta_status = 1
            article.ta_member_id = session['tm_id']
            article.ta_content = content

            loginUser = g.member
            htmlContent = render_template("post.html",type=type, title=title, html=html, datetime=article.ta_addtime.strftime('%Y-%m-%d %H:%M:%S'), user=loginUser.tm_nickname)
            fileName = md5(str(session['tm_id'])+"-"+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+".html"
            filePath = current_app.config['BASE_FILEPATH'] + fileName
            with open(filePath, 'w') as f:
                f.write(htmlContent.encode('utf-8'))
            # website = config['production'].WEBSITE
            article.ta_link = current_app.config['WEBSITE'] + "/article/"+fileName
            Article.add(article)
        except Exception, e:
            print Exception, ":", e
        return redirect(url_for('main.index'))

@main.route("/add_photo")
@login_required
def add_photo():
    method = request.method
    if method == 'GET':
        render_template("add_photo.html")
    else:
        render_template("index.html")
    return render_template("add_photo.html")

@main.route("/add_link")
@login_required
def add_link():
    method = request.method
    if method == 'GET':
        render_template("add_link.html")
    else:
        render_template("index.html")
    return render_template("add_link.html")

@main.route("/article/<id>")
def article(id):
    # article = Article.query.get(id)
    return render_template('7b44f657abe74c3d8426dd7bee8c3f10.html')

@main.route("/post")
def post_list():

    page = request.args.get('page')
    size = request.args.get('size')

    if page is None:
        page = 1

    if size is None:
        size = 20

    list = Article.list(int(page), int(size))

    return jsonify({'list': list, page: page, size: len(list)})

