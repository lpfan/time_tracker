from tracker import tt_api
from views.register import RegisterView
from views.signin import SignInView
from views.dashboard import SyncNewTask


tt_api.add_resource(RegisterView, '/api/register')
tt_api.add_resource(SignInView, '/api/signin')
tt_api.add_resource(SyncNewTask, '/api/sync/start_task')
#tt_api.add_resource(DashboardView, '/api/user_dashboard')
