import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import init_app

env = os.environ.get("FLASK_ENV") or "default"

app = init_app(env)
manage = Manager(app)
manage.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manage.run()
