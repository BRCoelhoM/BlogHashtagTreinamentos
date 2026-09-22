from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)



app.config['SECRET_KEY'] = '0d979629c3fe2692cc0a11969a070d99' #Segurança do Formulários
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mssql+pyodbc://sa:123456@localhost/api"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&TrustServerCertificate=yes"
)

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from BlogHashtagTreinamentos import routes