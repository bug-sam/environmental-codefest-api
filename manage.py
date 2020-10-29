import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db


app = create_app(os.getenv("ENV", "dev"))

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()