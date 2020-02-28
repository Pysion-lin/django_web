from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$',views.BookListAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$',views.BookDetailAPIView.as_view()),
]