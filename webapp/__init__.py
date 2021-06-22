from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from flask_bootstrap import Bootstrap

import config


# 개발환경변수 설정(.env)
load_dotenv()

# 데이터베이스 객체 생성
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata = MetaData(naming_convention=naming_convention))
migrate = Migrate()

# 플라스크 애플리케이션 팩토리 사용
def create_app():
    app = Flask(__name__)

    # config.py 파일항목을 환경변수로 호출
    app.config.from_object(config)

    Bootstrap(app)

    # ORM
    db.init_app(app)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    # 블루프린트
    from .views import main_views, master_views, transaction_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(master_views.bp)
    app.register_blueprint(transaction_views.bp)

    return app

