from quart import Quart
from .config import Config
from .db import init_db
from .auth import auth_bp
from .products import products_bp
from quart_schema import QuartSchema




def create_app() -> Quart:
app = Quart(__name__)
app.config.from_object(Config)


# Schema / validation
QuartSchema(app)


# DB init
init_db(app)


# Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(products_bp, url_prefix='/products')


# Middleware, error handlers, CORS, headers can be added here


return app