from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from .routes.auth import auth
from .routes.prompt import prompt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    jwt = JWTManager(app)
    
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(prompt, url_prefix='/api')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)