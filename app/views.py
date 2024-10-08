from flask import render_template
from config import app

__all__ = ('index')


@app.route('/')
def index():
    return render_template('index.html')
