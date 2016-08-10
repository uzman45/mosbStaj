from django.conf.urls import include, url
from django.contrib import admin
from  yonetim.views import hello,users
urlpatterns = [
    # Examples:
    url(r'^$', hello),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/',users),
]
