from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/printing')
def printing():
    return render_template('printing.html')  

@views.route('/pricing') 
def pricing():
    return render_template('pricing.html')     