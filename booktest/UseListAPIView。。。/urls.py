from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

urlpatterns = [
    # url(r'^books/$',views.BookListAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$',views.BookDetailAPIView.as_view()),
    url(r'^generic_books/$', views.BookListGenericAPIView.as_view()),
    url(r'^generic_books/(?P<id>\d+)/$', views.BookDetailGenericAPIView.as_view()),
    url(r'^mixin_generic_books/$', views.BookListMiXinGenericAPIView.as_view()),
    url(r'^mixin_generic_books/(?P<pk>\d+)/$', views.BookDetailMixinGenericAPIView.as_view()),

    url(r'^three_books/$', views.BookListThreeView.as_view()),
    url(r'^three_books/(?P<pk>\d+)/$', views.BookDetailThreeView.as_view()),

    url(r'^viewset_books/$', views.BookViewSet.as_view({"get": "list"})),
    url(r'^viewset_books/(?P<pk>\d+)/$', views.BookViewSet.as_view({"get": "retrieve"})),

    url(r'^readonly_books/$', views.BookReadOnlyViewSet.as_view({"get": "list"})),
    url(r'^readonly_books/(?P<pk>\d+)/$', views.BookReadOnlyViewSet.as_view({"get": "retrieve"})),

    url(r'^modelviewset_books/$', views.BookListDetailModelViewSet.as_view({"get": "list", "post": "create"})),
    url(r'^modelviewset_books/(?P<pk>\d+)/$',
        views.BookListDetailModelViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    url(r'^max_read_books/$', views.BookListDetailModelViewSet.as_view({"get": "haha"})),
    url(r'^update_read_books/(?P<pk>\d+)/$', views.BookListDetailModelViewSet.as_view({"put": "update_book"})),
]

# 1,创建路由对象
# router = DefaultRouter()
router = SimpleRouter()

# 2,注册视图集
router.register(r'books', views.BookListDetailModelViewSet, base_name="xixi")

# 3,添加视图集路由到urlpatterns中
urlpatterns += router.urls

print(router.urls)
