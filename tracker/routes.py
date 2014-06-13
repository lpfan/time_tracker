from tracker import app
from shared_lib.tools import register_routes


routes = (
    ('/', views.IndexView, 'index_view'),
)

register_routes(routes, app)
