from flask import Blueprint, render_template, request, make_response, redirect
from commom.mysql import Mysql

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    print(2)
    return render_template('admin.html')