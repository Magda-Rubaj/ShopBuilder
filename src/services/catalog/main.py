from flask import Flask
from infrastructure.mappers import begin_mapping
from api.routes import product_blueprint


app = Flask(__name__)
app.register_blueprint(product_blueprint)

begin_mapping()