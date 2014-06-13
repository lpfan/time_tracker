import views

from tracker import app
from shared_lib.tools import register_routes


routes = (
    ('/', views.IndexView, 'index_view'),
    ('/about', views.AboutPage, 'about_page')
)

register_routes(routes, app)
