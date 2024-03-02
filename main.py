from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'your_username', 'your_password', and 'your_dbname' with your MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_username:your_password@localhost/your_dbname'

db = SQLAlchemy(app)

class AgentName(db.Model):
    __tablename__ = 'agentname'
    name_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), default=None)
    phone = db.Column(db.String(13), nullable=False)
    pollingunit_uniqueid = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    agent_names = AgentName.query.all()
    return render_template('index.html', agent_names=agent_names)

if __name__ == '__main__':
    app.run(debug=True)
