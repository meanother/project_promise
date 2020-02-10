from django.conf.urls import url
from .views import PromiseCreateView, PromiseDetailView, PromiseListView, UserDetail, UserList
from django.conf.urls import include



urlpatterns = [
    url(r'^prom/new/$', PromiseCreateView.as_view()),
    url(r'^prom/$', PromiseListView.as_view()),
    url(r'^prom/(?P<pk>[0-9]+)/$', PromiseDetailView.as_view()),

    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]