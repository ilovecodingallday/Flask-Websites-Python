from flask import Flask

app = Flask(__name__)
from my_site import routes

