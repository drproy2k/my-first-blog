"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),      # ^ 로 시작해서 $ 로 끝나는지 조사. 즉 아마것도 없는 경우에 해당. http://127.0.0.1:8000/ 으로 접속해 오는 경우를 의미
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),     # 브라우저에 http://127.0.0.1:8000/post/5/라고 입력하면, 장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달
]

