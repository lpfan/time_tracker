import views

from tracker import app
from shared_lib.tools import register_routes


routes = (
    ('/', views.IndexView, 'index_view'),
    ('/about', views.AboutPage, 'about_page'),
    ('/register', views.RegisterView, 'register'),
    ('/templates/partials/<string:filename>', views.TemplatePartialView, 'partial'),
)

register_routes(routes, app)
