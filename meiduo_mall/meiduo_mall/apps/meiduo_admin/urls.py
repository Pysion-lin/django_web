from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from meiduo_admin.home import views
from meiduo_admin.user import user_views
from meiduo_admin.good import sku_views,spu_views,spec_views,spec_options_views,sku_images_views
from meiduo_admin.order import order_views
from meiduo_admin.system import permission_views,group_permission_views,admin_permission_views

urlpatterns = [
    #1,home
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$', views.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', views.UserIncrementCountView.as_view()),
    url(r'^statistical/day_active/$', views.UserDayActiveCountView.as_view()),
    url(r'^statistical/day_orders/$', views.UserDayOrderCountView.as_view()),
    url(r'^statistical/month_increment/$', views.UserMonthIncreamentCountView.as_view()),
    url(r'^statistical/goods_day_views/$', views.UserGoodsVisitCountView.as_view()),

    #2,user
    url(r'^users/$',user_views.UserView.as_view()),

    #3,sku
    url(r'^skus/categories/$',sku_views.SKUCategoryView.as_view()),
    url(r'^goods/simple/$',sku_views.SKUGoodSimpleView.as_view()),
    url(r'^goods/(?P<spu_id>\d+)/specs/$',sku_views.SKUGoodsSpecsView.as_view()),

    #4,spu
    url(r'^goods/brands/simple/$',spu_views.SPUBrandSimpleView.as_view()),
    url(r'^goods/channel/categories/$',spu_views.SPUCategoryView.as_view()),
    url(r'^goods/channel/categories/(?P<category_id>\d+)/$',spu_views.SPUCategorySubView.as_view()),
    url(r'^goods/images/$',spu_views.SPUImageUploadView.as_view()),

    #6,/specs/options/
    url(r'^goods/specs/simple/$',spec_options_views.OptionSpecView.as_view()),

    #7,/skus/images/
    url(r'^skus/simple/$',sku_images_views.SKUImageViewSet.as_view({"get":"simple"})),

    #8,orders
    # url(r'^orders/(?P<pk>\w+)/status/$',order_views.OrderViewSet.as_view({"put":"status"}))

    # 9,/permission/perms/
    url(r'^permission/content_types/$',permission_views.PermissionContentTypeView.as_view()),

    #10,/permission/groups/
    url(r'^permission/simple/$',group_permission_views.PermissionSimpleView.as_view()),

    #11,/permission/admins/
    url(r'^permission/groups/simple/$',admin_permission_views.GroupPermissionView.as_view())
]

#11,/permission/admins/
router = DefaultRouter()
router.register(r'permission/admins',admin_permission_views.AdminPermissionViewSet,base_name="admins")
urlpatterns += router.urls


#10,/permission/groups/
router = DefaultRouter()
router.register(r'permission/groups',group_permission_views.GroupPermissionViewSet,base_name="groups")
urlpatterns += router.urls


#9,/permission/perms/
router = DefaultRouter()
router.register(r'permission/perms',permission_views.PermissionViewSet,base_name="permission")
urlpatterns += router.urls

#8,orders
router = DefaultRouter()
router.register(r'orders',order_views.OrderViewSet,base_name="orders")
urlpatterns += router.urls


#7,/skus/images/
router = DefaultRouter()
router.register(r'skus/images',sku_images_views.SKUImageViewSet,base_name="images")
urlpatterns += router.urls

#6,/specs/options/
router = DefaultRouter()
router.register(r'specs/options',spec_options_views.SpecOptionsViewSet,base_name="options")
urlpatterns += router.urls


#5,/goods/specs/
router = DefaultRouter()
router.register(r'goods/specs',spec_views.SpecViewSet,base_name="specs")
urlpatterns += router.urls

#4,spu
router = DefaultRouter()
router.register(r'goods',spu_views.SPUViewSet,base_name="goods")
urlpatterns += router.urls


#3,sku
router = DefaultRouter()
router.register(r'skus',sku_views.SKUViewSet,base_name="skus")
urlpatterns += router.urls
