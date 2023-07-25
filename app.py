from flask import render_template,request,redirect,Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Sports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport=db.Column(db.String(80),nullable=False)
    name=db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return f"<Person {self.name}>"
    
with app.app_context():
    db.create_all()




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=["POST"])
def register():
    name=request.form.get("firstname")
    sport=request.form.get("sport")
    

    context={
    "name":name,
        "sport":sport
    }
    if not sport:
     return render_template("index.html",message="Not a valid ")
    else:
        person=Sports(name=name,sport=sport)
        db.session.add(person)
        db.session.commit()
     
    return render_template("success.html",context=context)
 

@app.route('/registrants')
def registrants():
   persons = Sports.query.all()
   return render_template("registrants.html",registrants=persons)







if __name__ == '__main__':
    app.run(debug=True)