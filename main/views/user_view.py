from flask import Blueprint,g,session
from main.services.user_service import *
from decorator import required_login
from utilities import *

user=Blueprint('user',__name__)



@user.before_request
def current_user_():
  if 'user' in session:
    id=session['user']
    g.current_user=current_user(id)
  else:
    g.current_user=None



@user.route('/home',methods=['POST','GET'])
def signup_logins():
    return signup_login()

@user.route('/about',methods=['POST','GET'])
def abouts():
    return about()

@user.route('/logout',methods=['POST','GET'])
@required_login
def logouts():
    return logout()


@user.errorhandler(422)
def unprocessable(error):
    return error_422(error)

@user.errorhandler(400)
def bad_request(error):
    return error_400(error)
      
@user.errorhandler(404)
def not_found(error):
    return error_404(error)
