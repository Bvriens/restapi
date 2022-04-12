from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api

from database import initialize_db
from resources import initialize_routes
from resources import errors

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'

api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.gn1jf.mongodb.net/Sandbox?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.run()

# test