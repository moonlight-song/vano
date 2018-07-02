from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register ('humen', views.HumanView)

urlpatterns = [
    path ('', views.index, name='index'),
    path ('news/', views.displayNewsList),
    path ('news/<slug:articleUrl>/', views.displayFullArticle),
    path ('humen/', include (router.urls)),
    path ('books/<int:book_id>', views.Books.as_view())
]