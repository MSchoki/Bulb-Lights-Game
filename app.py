from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bulbdb'
db = SQLAlchemy(app)

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    highscore = db.Column(db.Integer)

db.create_all()


@app.route('/players/create', methods=['POST'])
def create_player():
    player = request.form.get('playerName')
    formHighscore = request.form.get('highscore')
    higherScores = Score.query.filter(Score.highscore > formHighscore).count()
    if higherScores < 10:
        score = Score(name=player, highscore=formHighscore)
        db.session.add(score)
        db.session.commit()
    return redirect(url_for('scores'))


@app.route('/scores')
def scores():
    return render_template('scores.html',
                           data=Score.query.order_by
                           (db.desc('highscore')).limit(10).all()
                           )

@app.route('/')
def index():
    return render_template('index.html')

