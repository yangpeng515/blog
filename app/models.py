__author__ = 'ivany'

from datetime import datetime
from app import db
from flask.ext.login import UserMixin

class User:
    id = 0
    name = ''
    emai = ''

class Member(UserMixin, db.Model):
    __tablename__ = 'tb_member'
    tm_id = db.Column(db.BigInteger, primary_key=True)
    tm_name = db.Column(db.String(50), unique=True)
    tm_nickname = db.Column(db.String(50), unique=True)
    tm_sex = db.Column(db.Integer, default=0)
    tm_account = db.Column(db.String(50), unique=True)
    tm_password = db.Column(db.String(100))
    tm_email = db.Column(db.String(50), unique=True)
    tm_phone = db.Column(db.String(20), unique=True)
    tm_addtime = db.Column(db.DateTime, default=datetime.utcnow)
    tm_status = db.Column(db.Integer)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_tm_id(self):
        try:
            return self.tm_id  # python 2
        except NameError:
            return str(self.id)  # python 3

class Article(db.Model):
    __tablename__ = 'tb_article'
    ta_id = db.Column(db.BigInteger, primary_key=True)
    ta_member_id = db.Column(db.BigInteger)
    ta_title = db.Column(db.String(225))
    ta_content = db.Column(db.Text)
    ta_link = db.Column(db.String(225))
    ta_picurl = db.Column(db.String(225))
    ta_category = db.Column(db.Integer, default=0)
    ta_type = db.Column(db.Integer)
    ta_addtime = db.Column(db.DateTime, default=datetime.now())
    ta_update_time = db.Column(db.DateTime, default=datetime.now())
    ta_status = db.Column(db.Integer)

    def tojson(self):
        return {
            'title': self.ta_title,
            'link': self.ta_link,
            'type': self.ta_type,
            'addtime': self.ta_addtime,
            'pic': self.ta_picurl
        }

    @staticmethod
    def add(article):
        db.session.add(article)
        db.session.commit()

    @staticmethod
    def list(page, size):
        result = Article.query.filter_by(ta_status=1).paginate(page, size, False)
        articles = result.items
        list = []
        if articles and len(articles) > 0:
            list = [item.tojson() for item in articles]
            # for item in articles:
            #     if item.ta_type == 2:
            #         print('d ')
            #     item = item.tojson()
            #     list.append(item)
        return list

class File(db.Model):
    __tablename = 'tb_file'
    tf_id = db.Column(db.BigInteger, primary_key=True)
    tf_name = db.Column(db.String(225))
    tf_path = db.Column(db.String(225))
    tf_link = db.Column(db.String(225))
    tf_desp = db.Column(db.String(1024))
    tf_member_id = db.Column(db.BigInteger)
    tf_type = db.Column(db.Integer)
    tf_article_id = db.Column(db.BigInteger)
    tf_addtime = db.Column(db.DateTime, default=datetime.utcnow())
    tf_status = db.Column(db.Integer)

class Comment(db.Model):
    __tablename = 'tb_comment'
    tc_id = db.Column(db.BigInteger, primary_key=True)
    tc_article_id = db.Column(db.BigInteger)
    tc_member_id = db.Column(db.BigInteger)
    tc_name = db.Column(db.String(50))
    tc_parent_id = db.Column(db.BigInteger)
    tc_content = db.Column(db.Text)
    tc_addtime = db.Column(db.DateTime, default=datetime.utcnow())
    tc_status = db.Column(db.Integer)
