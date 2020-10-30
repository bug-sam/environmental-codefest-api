import os

from flask_script import Manager

from api import create_app


app = create_app(os.getenv("ENV", "dev"))

manager = Manager(app)

@manager.command
def initialize_database():
    from api.models.issue import Issue
    db.create_all()

@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()