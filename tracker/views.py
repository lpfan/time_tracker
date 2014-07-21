import os

from flask.views import MethodView
from flask import (
    render_template,
    send_from_directory,
    redirect
)
from flask.ext.login import login_required
from flask.ext.login import logout_user

from tracker import login_manager
from tracker import app
from tracker import db
from models import User


class IndexView(MethodView):

    def get(self):
        return render_template('index.html')


class AboutPage(MethodView):
    @login_required
    def get(self):
        return render_template('about.html')


class RegisterView(MethodView):

    def get(self):
        return render_template('index.html')


class TemplatePartialView(MethodView):

    def get(self, filename):
        return render_template('partials/%s' % filename)


class UserDashboarfView(MethodView):

    @login_required
    def get(self):
        return render_template('user_dashboard.html')

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


@login_manager.token_loader
def load_token(token_val):
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    #token_val = request.headers.get(app.config['AUTH_HEADER_NAME'])
    token = token_val.replace('Basic ', '', 1)
    return User.verify_auth_token(token)


@app.route("/logout/")
def logout():
    """
    Web Page to Logout User, then Redirect them to Index Page.
    """
    logout_user()
    return redirect("/")
