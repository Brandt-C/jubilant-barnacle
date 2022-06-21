from app import app
from app.models import db, User, Pokemon

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Pokemon': Pokemon}