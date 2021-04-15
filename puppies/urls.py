from django.urls import path
from . import views

urlpatterns = [
    path(
        'city/',
        views.get_post_citys,
        name='get_post_citys'
    ),
    path(
        'city/street/',
        views.get_post_street,
        name='get_post_street'
    ),
    path(
        'city/(?<pk>[0-9]+)',
        #'api/v1/puppies/(?P<pk>[0-9]+)',
        views.get_delete_update_city,
        name='get_delete_update_city'
    ),
]