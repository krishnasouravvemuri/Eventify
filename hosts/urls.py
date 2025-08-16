from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('hosts_home/', login_required(views.hosts_home, login_url='login_user'), name='hosts_home'),
    path('host_event/', login_required(views.host_event, login_url='login_user'), name='host_event'),
    path('edit_event/<int:event_id>/', login_required(views.edit_event, login_url='login_user'), name='edit_event'),
    path('delete_event/<int:event_id>/', login_required(views.delete_event, login_url='login_user'), name='delete_event'),
    path('view_event', login_required(views.view_event, login_url='login_user'), name='view_event'),
]
