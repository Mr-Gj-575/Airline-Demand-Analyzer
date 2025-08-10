from flask import Flask
import os

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='../static')
    
    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['API_BASE_URL'] = 'https://api.aviationstack.com/v1'
    
    # Create static folder if it doesn't exist
    static_path = os.path.join(app.root_path, '..', 'static')
    if not os.path.exists(static_path):
        os.makedirs(static_path)
    
    # Register routes
    from .routes import register_routes
    register_routes(app)
    
    return app