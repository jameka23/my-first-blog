from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # match empty string,
                                                  # so once user comes to site, they will see the post_list
]
