from tracker import tt_api
from views import RegisterView


tt_api.add_resource(RegisterView, '/api/register')
