import views

from tracker import api
 

api.add_resource(views.IndexView, '/home')
