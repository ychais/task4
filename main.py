from flask import Flask, render_template, request, redirect
import pymongo
connection = pymongo.MongoClient('localhost', 27017)
database = connection['task4']
collection = database['users']

app = Flask (__name__)
app.secret_key = 'secret key'

#################################
#task3 authentication data
#users={
#    "mr admin": "admin",
#    "ms admin": "admin",
#    "mr user": "user",
#    "ms user": "user"
#}
#################################


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        us = database.users.find_one({"username": username})
        pa = database.users.find_one({"password": password})
        try:
            if password == pa["password"] or username == us["username"]:
                return redirect ('/cabinet')    
        except:
            return render_template('invalid.html')
    else:
        return render_template('login.html')
    return render_template('login.html')

@app.route("/cabinet")
def cabinet():
    return render_template('cabinet.html')




if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

connection.close()