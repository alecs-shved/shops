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
        'shop/',
        views.get_post_shop,
        name='get_post_shop'
    ),
    path(
        'shved/',
        views.get_post_shved,
        name='get_post_shved'
    ),
   ]