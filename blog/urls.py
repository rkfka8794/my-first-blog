from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^login/$', auth_views.login,  {'template_name':'memo_app/login.html'}),
    url(r'^accounts/signup$', views.UserView.as_view(), name = 'signup'),
    url(r'^accounts/login/done$', views.RegisteredView.as_view(), name = 'create_user_done'),
]