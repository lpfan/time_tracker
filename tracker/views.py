from flask.views import MethodView
from flask import render_template


class IndexView(MethodView):

    def get(self):
        return render_template('index.html')


class AboutPage(MethodView):
    def get(self):
        return "Hard Code"
