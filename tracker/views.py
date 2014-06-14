from flask.views import MethodView
from flask import render_template
from flask.ext.login import login_required

from tracker import login_manager
from models import User


class IndexView(MethodView):

    def get(self):
        return render_template('index.html')


class AboutPage(MethodView):
    @login_required
    def get(self):
        return render_template('about.html')


@login_manager.user_loader
def load_user(id):
    return User.objects.get(int(id))
