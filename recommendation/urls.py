from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^recommendations_page/$', views.recommendations_page, name='recommendations_page'),
    url(r'^recommendations_page/$', views.recommendations_page, name='recommendations_page'),
    url(r'^recommendations_page/followers_list/$', views.list_followers, name='list_followers'),
    url(r'^recommendations_page/following_list/$', views.list_following, name='list_following'),
    url(r'^add_recommendation/$', views.add_recommendation, name='add_recommendation'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<recommendation_id>[0-9]+)$', views.recommendation, name='recommendation'),

]