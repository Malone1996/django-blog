from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
#我们首先从 django.conf.urls 导入了 url 函数，又从当前目录下导入了 views 模块。
#然后我们把网址和处理函数的关系写在了 urlpatterns 列表里。