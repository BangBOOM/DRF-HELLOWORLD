from movie import views
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

app_name='movie'

router=DefaultRouter()
router.register(r'movie',views.MovieViewSet)
router.register(r'login',views.LogInViewSet)
router.register(r'register',views.RegisterViewSet)

urlpatterns=[
    url(r'^api/',include(router.urls)),
]
