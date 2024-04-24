from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dima_shop1.db'
db = SQLAlchemy(app)


class Things(db.Model):
    __tablename__ = 'things'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    product_information = db.Column(db.Text(300), nullable=False)
    cost = db.Column(db.Float)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=True)


class Cart(db.Model):
    __tablename__ = 'cort'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    thing_id = db.Column(db.Integer, db.ForeignKey("things.id"))
    quantity = db.Column(db.String)


class SiteInfo(db.Model):
    __tablename__ = 'site_inf'
    id = db.Column(db.Integer, primary_key=True)
    website_info = db.Column(db.Text(300), nullable=False)


@app.route("/")
def index():
    with open("design.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors")
def i1():
    with open("add_to_kors.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/add_cors2")
def i4():
    with open("add_to_kors2.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors3")
def i5():
    with open("add_to_kors3.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors4")
def i6():
    with open("add_to_kors4.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors5")
def i7():
    with open("add_to_kors5.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors6")
def i8():
    with open("add_to_kors6.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors7")
def i9():
    with open("add_to_kors7.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors8")
def i10():
    with open("add_to_kors8.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/add_cors9")
def i11():
    with open("add_to_kors9.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/info")
def i12():
    with open("info.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/regist", methods=('POST', 'GET'))
def i2():
    if request.method == 'POST':

        try:
            hash = generate_password_hash(request.form['password'])
            u = User(email=request.form['email'], password=hash)
            db.session.add(u)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print('ошибка добавления')

    with open("regist.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


@app.route("/reg_done")
def i3():
    with open("regist_done.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()

@app.route("/workers")
def i13():
    with open("workers.html", 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1', debug=True)