from flask import Blueprint, render_template, redirect, url_for

# 블루프린터 클래스로 라우터 함수 관리
bp = Blueprint("main", __name__, url_prefix = '/')

# Homepage view
@bp.route("/")
def home():
    return render_template("index.html")