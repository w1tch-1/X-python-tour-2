from flask import Flask

__all__ = ('app')
app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
