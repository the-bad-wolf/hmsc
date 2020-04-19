from App import app
# from models import User, Post, ROLE_USER, ROLE_ADMIN

@app.route('/index/')
def index():
    return 'hello flask'