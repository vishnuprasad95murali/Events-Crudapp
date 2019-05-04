import os
from flask import request, render_template, session, url_for, jsonify, redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating server path
project_dir = os.path.dirname(os.path.abspath(__file__))
databasefile = "sqlite:///{}".format(os.path.join(project_dir, "daily_dairy.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databasefile

# Database variable creation
db = SQLAlchemy(app)

class do(db.Model):

    title = db.Column(db.String(80), primary_key = True, unique = True, nullable = False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
        

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.form :
        try:
            to_do = do(title = request.form.get("title"))
            db.session.add(to_do)
            db.session.commit()
        except Exception as e:
            print("Couldn't add the event, Please try again")
            print(e)
    every_line=do.query.all()
    return render_template("home.html", every_line = every_line)


@app.route("/dairy", methods = ["POST"])
def edit():
    if request.form:
        try:
            edit = request.form.get('edit')
            editas = request.form.get('editas')
            update = do.query.filter_by(title= edit).first()
            update.title = editas
            db.session.commit()
        except Exception as e:
            print(" Couldn't Update, please check the entry again")
            print(e)
    return redirect(url_for('home'))



        
if __name__ == "__main__":
    app.run(debug=True)
    

