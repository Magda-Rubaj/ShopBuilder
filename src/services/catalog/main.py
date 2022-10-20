from flask import Flask
from infrastructure.mappers import begin_mapping
from config.container import Container
from api.routes import product_blueprint, category_blueprint
from api import routes


app = Flask(__name__)
container = Container()
app.container = container
app.register_blueprint(product_blueprint)
app.register_blueprint(category_blueprint)

begin_mapping()