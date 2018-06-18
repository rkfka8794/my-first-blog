from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^login/$', auth_views.login,  {'template_name':'memo_app/login.html'}),
    url(r'^accounts/signup$', views.UserView.as_view(), name = 'signup'),
    url(r'^accounts/login/done$', views.RegisteredView.as_view(), name = 'create_user_done'),
    url(r'^ex_info/$', views.ex_info, name ='ex_info'),
    url(r'^painting/$', views.painting, name ='painting'),
    url(r'^crafts/$', views.crafts, name ='crafts'),
    url(r'^design/$', views.design, name='design'),
    url(r'^art_piece/$', views.art_piece, name='art_piece'),
    url(r'^picture/$', views.picture, name='picture'),
    url(r'^engraving/$', views.engraving, name='engraving'),
    url(r'^etc/$', views.etc, name='etc'),
    url(r'^mypage/$', views.mypage, name='mypage'),
]