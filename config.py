import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "accounting_craft.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-WTF를 위한 환경변수
SECRET_KEY = 'dev'

