"""kiddies_kingdom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from kiddies_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.login),
    path('login1/',views.login1),
    path('adminhead/',views.adminhead),
    path('customerhead/',views.customerhead),
    path('uploadproduct/',views.uploadproduct),
    path('uploadproduct1/',views.uploadproduct1),
    path('changeprice/',views.changeprice),
    path('changeprice1/<int:id>',views.changeprice1),
    path('changeprice2/<int:id>',views.changeprice2),
    path('removeproduct/',views.removeproduct),
    path('removeproduct1/<int:id>',views.removeproduct1),
    path('customerregistration/',views.regcustomer),
    path('customerregistration1/',views.regcustomer1),
    path('category/',views.category),
    path('viewproduct/',views.viewproduct),
    path('home/',views.home),
    path('viewproduct1/',views.givereview),
    path('givereview/<int:id>',views.givereview1),
    path('givereview1/',views.givereview2),
    path('viewproduct2/',views.viewproduct1),
    path('givecomplaint/<int:id>',views.givecomplaint),
    path('givecomplaint1/',views.givecomplaint1),
    path('addtocart/',views.categorycart),
    path('addtocart1/',views.viewprdctcart),
    path('order/<int:id>',views.order),
    path('order1/',views.order1),
    path('finishorder/',views.finishorder),
    path('finishorder1/',views.finishorder1),
    path('viewreview/',views.reviewcategory),
    path('viewreview1/',views.viewprdctreview),
    path('viewreview2/<str:id>',views.viewreview),
    path('viewreview-public/',views.reviewcategory_public),
    path('viewreview-pbc1/',views.viewprdctreview_public),
    path('viewreview-pbc2/<str:id>',views.viewreview_public),
    path('viewreview-admin/',views.reviewcategory_admin),
    path('viewreview-admin1/',views.viewprdctreview_admin),
    path('viewreview-admin2/<str:id>',views.viewreview_admin),
    path('viewcomplaint/',views.complaint_category),
    path('viewcomplaint1/',views.viewprdct_complaint),
    path('viewcomplaint2/<str:id>',views.viewcomplaint),
    path('vieworder/',views.vieworder),
    path('placeorder/',views.placeorder),
    path('orderaccept/<int:id>',views.orderaccept),
    path('orderdetails/<int:id>',views.orderdetails),
    path('orderreject/<int:id>',views.orderreject),
    path('vieworderdetails/<str:id>',views.vieworderdetails),
    path('accept1/<int:id>',views.detailaccept),
    path('reject1/<int:id>',views.detailreject),
    path('paymentdetails/<str:id>',views.viewpaymentdetails),
    path('orderstatus/',views.orderstatus),
    path('vieworderdetails1/',views.vieworderdetails1),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
