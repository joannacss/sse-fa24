from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment_text = request.args['comment']
    new_comment = Comment(text=comment_text['text'])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment added successfully!"})

if __name__ == "__main__":
    with app.app_context():
    	db.create_all()
    	app.run(debug=True)
