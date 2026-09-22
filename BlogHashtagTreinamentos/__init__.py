"""
import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

from sqlalchemy.future import engine

app = Flask(__name__)



app.config['SECRET_KEY'] = '0d979629c3fe2692cc0a11969a070d99'  # Segurança do Formulários

database_url = os.getenv("DATABASE_URL")
print(f"DEBUG - DATABASE_URL lida: {database_url}")  # linha temporária
if database_url:  ## Banco de Dados servidor Railway
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:  ## Banco de Dados Local, para teste
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

from BlogHashtagTreinamentos import models

engine = sqlalchemy.create_engine(['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table ("usuario"):
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Base de Dados Criada")
else:
    print("Base de Dados já Existente")


from BlogHashtagTreinamentos import routes
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '0d979629c3fe2692cc0a11969a070d99'  # Segurança do Formulários

# --- ROTA DE DEBUG TEMPORÁRIA ---
@app.route('/debug-env')
def debug_env():
    output = "<h1>Variáveis de Ambiente</h1><pre>"
    for key, value in sorted(os.environ.items()):
        if "SECRET" not in key.upper():
            output += f"{key} = {value}\n"
    output += "</pre>"
    return output
# --- FIM DA ROTA DE DEBUG ---

database_url = os.getenv("DATABASE_URL")
print(f"DEBUG - DATABASE_URL lida: {database_url}")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:SUA_SENHA_AQUI@postgres.railway.internal:5432/railway"
print("DEBUG - Usando URL hardcoded do Postgres")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from BlogHashtagTreinamentos import routes