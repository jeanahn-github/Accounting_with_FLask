from flask import Blueprint, render_template, redirect, url_for

from ..forms import CreateAccountForm
from ..models import ChartOfAccount, Partner, Project

from webapp import db

# 블루프린터 클래스로 라우터 함수 관리
bp = Blueprint("master", __name__, url_prefix = '/')

# 마스터데이터 조회/생성/변경

# 계정과목 생성
@bp.route("/coa/create", methods = ["GET", "POST"])
def create_account():
    available_account_group = ChartOfAccount.query.filter(ChartOfAccount.is_sum_account == "sum")
    account_group_list = [(i.account_name, i.account_name) for i in available_account_group]

    form = CreateAccountForm()
    form.account_group.choices = account_group_list

    if form.validate_on_submit():
        new_account = ChartOfAccount(
            account_code = form.account_code.data,
            account_name = form.account_name.data,
            account_type = form.account_type.data,
            is_sum_account = form.is_sum_account.data,
            account_group = form.account_group.data,
            account_description = form.account_description.data
        )
        db.session.add(new_account)
        db.session.commit()
        return redirect(url_for("main.home"))

    return render_template("master/account_master.html", form = form)

# 계정과목 수정
@bp.route("/coa/edit/<int:account_code>", methods = ["GET", "POST"])
def edit_account(account_code):
    account = ChartOfAccount.query.get(account_code)
    edit_form = CreateAccountForm(
        account_code = account.account_code,
        account_name = account.account_name,
        account_type = account.account_type,
        is_sum_account = account.is_sum_account,
        account_group = account.account_group,
        account_description = account.account_description
    )
    if edit_form.validate_on_submit():
        account.account_code = edit_form.account_code.data
        account.account_name = edit_form.account_name.data
        account.account_type = edit_form.account_type.data
        account.is_sum_account = edit_form.is_sum_account.data
        account.account_group = edit_form.account_group.data
        account.account_description = edit_form.account_description.data

        db.session.commit()

        return redirect(url_for("main.home"))

    return render_template("master/account_master.html", form = edit_form, is_edit = True, account = account)




