from flask import Flask, render_template, url_for, redirect
from flask import request, session 
from flask import flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "ahmad123" 
app.permanent_session_lifetime = timedelta(days=5) 


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("home.html")





@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        user_name = request.form['nm']
        password = request.form['ps']
        confirm_password = request.form['confirm_ps']
        
        if password == confirm_password:
            
            return f"Username is {user_name}, Password is {password}"
        else:
            return f"confirm password and password doesnt match"
    else: 
        
        return render_template("users/signup.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET": 
        if 'username' in session.keys():
            flash("Already Logined", "info")
            return redirect(url_for('user.profile'))
        else:
            flash("Please Type username and password", "info")
            return render_template("login.html", images=['images_3.png', 'images_4.png'])
    else: 
        user_name = request.form['nm']
        password = request.form['ps']
        
        session['username'] = user_name
        session['password'] = password
        session.permanent = True 
        flash("Successfully login", "info")
        return redirect(url_for('user.profile'))
    
@app.route("/profile", endpoint='user.profile')
def show_profile():
    if 'username' in session.keys():
        name = session['username']
        password = session['password']
        return render_template("profile.html", name=name, password=password)
    else: 
        flash("Sessions ends, please rewrite username and password", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if 'username' in session.keys():
        session.pop('username')
        session.pop('password')
    return redirect(url_for("home_page"))
        

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=5000)