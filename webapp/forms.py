from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField, TextAreaField, DateField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForms

class CreateAccountForm(FlaskForm):
    account_code = IntegerField("계정코드", validators=[DataRequired()])
    account_name = StringField("계정과목명", validators=[DataRequired()])
    account_type = SelectField("계정유형", choices = [('A', '자산'), ('L', '부채'), ('E', '자본'), ('I', '수익'), ('C', '비용')], validators=[DataRequired()])
    is_sum_account = RadioField("합계계정 여부", choices = [("sum", "합계계정"), ("posting", "기표계정")], validators=[DataRequired()])
    account_group = SelectField("계정그룹", choices = [])
    account_description = TextAreaField("계정설명")
    submit = SubmitField("저장")


class CreateTransactionForm(FlaskForm):

    date = DateField("전표일자", validators = [DataRequired()])
    type = RadioField("전표유형", choices = [("S", "매출전표"), ("P", "매입전표"), ("D", "입금전표"), ("W", "출금전표"), ("A", "대체전표")], validators = [DataRequired()])
    account = SelectField("계정과목", choices = [], validators = [DataRequired()])
    amount = IntegerField("거래금액", validators = [DataRequired()])
    partner = SelectField("거래처", choices = [])
    project = SelectField("프로젝트", choices = [])
    description = TextAreaField("적요")
    submit = SubmitField("저장")






class RegisterForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    name = StringField("Name", validators = [DataRequired()])
    submit = SubmitField("SIGN ME UP!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("LET ME IN!")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators = [DataRequired()])
    submit = SubmitField("Submit Comment")