"""
Definition of urls for RESTful_tagsManager.
"""

from datetime import datetime
from django.urls import path,re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from Music.views import tag_list,tag_detail
from Music.views import add_queryTrackTag,add_queryAlbumTag,add_queryArtistTag
from Music.views import export


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
    ##TAG
    #path(r'^tags/$', tag_list),
    path('tags/<int:pk>/', tag_detail),
    #path(r'^tags/(?P<pk>[0-9]+)$', tag_detail),
    path('tags/', tag_list),
    re_path(r'^tags/$', tag_list),
    re_path(r'^tags/(?P<pk>[0-9]+)$', tag_detail),
    
    #The URLs corresponding to specify a particular view
    re_path(r'^tracks/$', add_queryTrackTag),
    re_path(r'^albums/$', add_queryAlbumTag),
    re_path(r'^artist/$', add_queryArtistTag),

    ##EXPORT ALL
    re_path(r'^export/$',export)
   
]
