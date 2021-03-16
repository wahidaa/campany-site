from functools import wraps
from flask import request, _request_ctx_stack, abort,session,flash,render_template,g,url_for,redirect
#authentification
def required_manager(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if 'user' in  session:
            if g.current_user[1] !='administrator':
                flash('you are not authorized !')  
                return redirect(url_for('user.signup_logins'))
        return f(*args,**kwargs)
    return wrapper 



def required_login(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if 'user' not in  session:
            flash('please login')
            return redirect(url_for('user.signup_logins'))
        return f(*args,**kwargs)
    return wrapper
