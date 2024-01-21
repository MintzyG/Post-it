from flask import Flask
import os

app = Flask(__name__)

def create_app():
    @app.route('/')
    def Hello():
        return 'Hello, World!'
   
    return app

create_app()
app.run()
