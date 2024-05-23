from flask import Blueprint
from Http.controllers import loginController

app = Blueprint('routes',__name__)



app.add_url_rule('/register', 'register', loginController.register, methods=['POST'])
app.add_url_rule('/login', 'login', loginController.login, methods=['POST'])

