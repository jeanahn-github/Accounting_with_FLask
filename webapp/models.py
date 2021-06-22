from webapp import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    role = db.Column(db.String(100), nullable=True)


class ChartOfAccount(db.Model):

    __tablename__ = "chart_of_account"

    account_code = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(1), nullable=False)
    is_sum_account = db.Column(db.String(10), nullable=False)
    account_group = db.Column(db.String(50), nullable=True)
    account_name = db.Column(db.String(100), unique=True, nullable=False)
    account_description = db.Column(db.Text, nullable=True)


class Transaction(db.Model):

    __tablename__ = "transaction"

    document_number = db.Column(db.String(20), primary_key = True)
    document_date = db.Column(db.String(10), nullable=False)
    document_type = db.Column(db.String(1), nullable=False)
    account_code = db.Column(db.Integer, db.ForeignKey('chart_of_account.account_code'), nullable=False)
    account = db.relationship('ChartOfAccount', backref = db.backref('transaction_set'))
    transaction_amount = db.Column(db.Integer, nullable=False)
    partner_code = db.Column(db.Integer, db.ForeignKey('partner.id'), nullable=False)
    partner = db.relationship('Partner', backref=db.backref('transaction_set'))
    project_code = db.Column(db.Integer, db.ForeignKey('project.id'), nullable = False)
    project = db.relationship('Project', backref = db.backref('transaction_set'))
    transaction_description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('transaction_set'))


class Partner(db.Model):

    __tablename__ = "partner"

    id = db.Column(db.Integer, primary_key=True)
    partner_name = db.Column(db.String(100), nullable=False)
    partner_type = db.Column(db.String(1), nullable=False)
    partner_description = db.Column(db.Text, nullable = True)


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable = False)
    project_description = db.Column(db.Text, nullable = True)


