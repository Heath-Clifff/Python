from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:TUy)j&,q!n6!V8M!@localhost/height_collector'
db = SQLAlchemy(app)
class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        send_email(email, height)
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height)
            db.session.commit()
            send_email(email, height)
            return render_template('success.html')
    return render_template('index.html', text = "Seems like")
if __name__ == '__main__':
    app.run(debug = True)
