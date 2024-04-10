# python projects use packages to organize code into multiple modules so that they can be imported as needed
# project directory normally has
    # `flaskr/` python package containing app code and files
    # `tests/` directory with test modules
    # `.venv/` the python virtual environment
    # `readme.md` file that has instructions to install and run flask
    # version control config like `git`
    # other project files too that get added as time passes

import os

from flask import Flask

# flask application is an instance of the `Flask` class
# instead of creating the Flask instance globally, create it inside a function called as the application factory
# the `__init__.py` file inside the `flaskr` directory acts as the application factory 
# it also tells python that the `flaskr` directory should be treated as a package

def create(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'vy',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    if (test_config is None):
        # load the instance config when not testing from the file (if it exists)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if it is passed
        app.config.from_mapping(test_config)
        
    # ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except (OSError):
        pass
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return ("Hello World!")
    
    return app  