from tracker import tt_api
from views.register import RegisterView
from views.signin import SignInView


tt_api.add_resource(RegisterView, '/api/register')
tt_api.add_resource(SignInView, '/api/signin')
