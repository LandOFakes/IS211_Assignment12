from flask import Flask, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) 

from app import routes
