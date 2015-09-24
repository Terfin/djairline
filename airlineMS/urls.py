from django.conf.urls import patterns, url
from .views import HomeView, PilotAssignmentView, TicketView

urlpatterns = patterns('',

    url(r'^pilots/$', PilotAssignmentView.as_view(), name='pilots'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tickets/$', TicketView.as_view(), name='tickets')

)
