from django.urls import path
from . import views

urlpatterns = [
    path(
        'api/v1/puppies/(?P<pk>[0-9]+)',
        views.get_delete_update_city,
        name='get_delete_update_city'
    ),
    path(
        'api/v1/puppies/',
        views.get_post_citys,
        name='get_post_city'
    )
]