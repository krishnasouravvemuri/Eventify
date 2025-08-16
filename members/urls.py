from django.urls import path
from . import views as v

urlpatterns = [
    path('members_home/' , v.members_home , name = "members_home"),
    path('event_register/<int:event_id>/' , v.event_register , name = "event_register"),
    path('show_registrations' , v.show_registrations , name = "show_registrations"),
    path('show_ticket/<str:registration_code>/' , v.show_ticket , name = "show_ticket"),
    path('ticket/<int:ticket_id>/', v.ticket_detail, name='ticket_detail'),
]
