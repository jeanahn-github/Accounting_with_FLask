from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from ..forms import CreateTransactionForm
from ..models import ChartOfAccount, Transaction, Partner, Project

from webapp import db

import random

# 블루프린터 클래스로 라우터 함수 관리
bp = Blueprint("transaction", __name__, url_prefix = '/')

# 전표데이터 조회/입력/수정
@bp.route("/transaction/create", methods = ["GET", "POST"])
def create_transaction():

    available_account = ChartOfAccount.query.filter(ChartOfAccount.is_sum_account == "posting")
    available_sales_partner = Partner.query.filter(Partner.partner_type == "S")
    available_purchase_partner = Partner.query.filter(Partner.partner_type == "P")
    available_project = Project.query.all()

    account_list = [(account.account_code, account.account_name) for account in available_account]
    sales_partner_list = [(partner.partner_code, partner.partner_name) for partner in available_sales_partner]
    purchase_partner_list = [(partner.partner_code, partner.partner_name) for partner in available_purchase_partner]
    project_list = [(project.project_code, project.project_name) for project in available_project]

    form = CreateTransactionForm()

    form.account.choices = account_list

    if form.type == "S":
        form.partner.choices = sales_partner_list
    elif form.type == "P":
        form.partner.choices = purchase_partner_list
    else:
        form.partner.choices = sales_partner_list + purchase_partner_list

    form.project.choices = project_list

    if form.validate_on_submit():
        # 전표번호 자동생성
        doc_num = form.type.data + form.date.data + random.randint(1, 100)

        new_transaction = Transaction(
            document_number = doc_num,
            document_date = form.date.data,
            document_type = form.type.data,
            account_code = form.account.data,
            transaction_amount = form.amount.data,
            partner_code = form.partner.data,
            project_code = form.project.data,
            transaction_description = form.description.data,
            user_id = current_user.user_id,

        )
        db.session.add(new_transaction)
        db.session.commit()
        return redirect(url_for("main.home"))

    return render_template("transaction/transaction_create.html", form = form)
