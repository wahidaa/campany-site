import os
from flask import session
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main import create_app
from main.views.user_view import user 
app = create_app(os.getenv('SERVICE_ENV') or 'dev')
app.register_blueprint(user)
app.app_context().push()
manager = Manager(app)
#migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)
#db.create_all()
@manager.command
def run(): 
    app.run()
   

if __name__ == "__main__":
    manager.run()
   
