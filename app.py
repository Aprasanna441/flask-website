from flask import Flask,render_template,request


app=Flask(__name__)

registrant_name={}

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
     registrant_name[name]=sport
     
     return render_template("success.html",context=context)
 

@app.route('/registrants')
def registrants():
   return render_template("registrants.html",registrants=registrant_name)