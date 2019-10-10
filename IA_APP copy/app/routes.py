import os
from app import app

from datetime import datetime
from flask import render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm, PostForm
#url_for is a function that will find the location for routes
#this protects from cookies, foregery, etc with random secret key
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


# #OOP
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True) #unique id for user
#     username = db.Column(db.String(15), unique=True, nullable=False) #15 is the max character # specified earlier
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     #this says that the post attribute has a relationship to post model, backref allows us to get user who created post, lazy just defines so alchemy loads the data as necessary in one go
#     posts = db.relationship('Post', backref='author', lazy=True)
#
#
#     def __repr__(self): #this is how our object is printed
#         return User('{self.username}', '{self.email}', '{self.image_file}')"
#
# class Post(db.Model): #this inherits from db.Model
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #id of user who authored post
#
#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"



#from flask_pymongo import PyMongo

#list of dictionaries (to check)
posts = [
{
'author': 'Carlota Bustos',
'title': 'Announcement #1',
'content': 'This is the content',
'date': 'May, 24, 2019'
},
{
'author': 'Jacobo Bustos',
'title': 'Anoucement #2',
'content': 'This is the content',
'date': 'May, 29, 2019'
},

]

@app.route("/")
@app.route('/home')
def home():
    #post is a variable we have access in this template and it is = to posts data
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    msg=Message('Hey there', recipients=['2020cbustos@dwight.edu'])
    mail.send(msg)
    #renders to static HTML file
    return render_template("about.html", title = 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #tells you if form validated
    if form.validate_on_submit():
    #flash mtessage
        flash('Account created for {form.username.data}!', 'success')
        #redirect to hoe (name of function)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #fake data to simulate log-in
        if form.username.data == '2020cbustos' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Check username and failure', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    return render_template('create_post.html', title='New Post', form=form)
