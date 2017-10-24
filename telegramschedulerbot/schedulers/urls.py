from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.SchedulerListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~create/$',
        view=views.SchedulerCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~redirect/$',
        view=views.SchedulerRedirectView.as_view(),
        name='redirect'
    ),    
    url(
        regex=r'^(?P<pk>\d+)/~update/$',
        view=views.SchedulerUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~delete/$',
        view=views.SchedulerDeleteView.as_view(),
        name='delete'
    ),            
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.SchedulerDetailView.as_view(),
        name='detail'
    ),        
]
