from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from controller.firebase_controller import photo_controller_bp
def create_app(config_name):
    app = Flask(__name__)
    CORS(app=app, origins='*', methods=['GET',
     'POST', 'PUT', 'DELETE'], allow_headers=['Content-Type','Authorization'])

    # config firebase
    ruta_credenciales = './serviceAccountKey.json'
    cred = credentials.Certificate(ruta_credenciales)
    firebase_admin.initialize_app(cred, {
    'storageBucket': 'test-python-fb6c2.appspot.com'  # Reemplaza con tu URL de Storage
    })


    app.register_blueprint(photo_controller_bp)

    @app.route("/")
    def initial_controller():
        return {
        "message": "Wellcome to my API of project firebase"
        }
    return app;