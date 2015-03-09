import os
from flask import Flask
from simple_page import simple_page

def create_app():
    app = Flask(__name__)
    app.register_blueprint(simple_page, url_prefix=os.environ.get('URL_PREFIX',''))
    app.config.update(dict(DEBUG=True))
    return app

app = create_app()

if __name__ == '__main__':
  app.run()
