from django.urls import path
from . import views


urlpatterns = [
    path(
        'city/',
        views.get_post_citys,
        name='get_post_citys'
    ),
    path(
        'city/<str:city_type>',
        views.get_post_citys,
        name='get_post_cityss'
    ),
    path(
        'city/street/',
        views.get_post_street,
        name='get_post_street'
    ),
    path(
        'shop/',
        views.get_post_shop,
        name='get_post_shop'
    ),
   ]

'''urlpatterns = [
    path(
        'city/',
        views.get_post_citys,
        name='get_post_citys'
    ),
    path(
        'shop/',
        views.get_post_shop,
        name='get_post_shop'
    ),
    path(
        'shop/<int:pk>',
        views.get_post_shop,
        name='get_post_shop'
    ),
    path(
        'city/street/',
        views.get_post_street,
        name='get_post_street'
    ),
    path(
        #'city/(?P<pk>[0-9]+)',
        'city/<int:pk>',
        views.get_delete_update_city,
        name='get_delete_update_city'
    ),
]'''