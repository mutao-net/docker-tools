from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import app


class User(app.db.Model):

    __tablename__ = 'users'

    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(255), nullable=False)
    register_date = app.db.Column(app.db.DateTime, nullable=False, default=datetime.now)
    update_time = app.db.Column(app.db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)