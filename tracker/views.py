import os

from flask.views import MethodView
from flask import render_template, send_from_directory
from flask.ext.login import login_required

from tracker import login_manager
from tracker import app
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


@login_manager.user_loader
def load_user(id):
    return User.objects.get(int(id))
