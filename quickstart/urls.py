"""altchain_pool_api URL Configuration

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

from django.urls import path
from quickstart import views

urlpatterns = [
    path('api/email/sendEmailCodeGt/', views.email_code_gen),
    path('api/user/addressBook/batchModifyWithdrawPercent/', views.modify_withdraw_percent),
    path('api/user/register/', views.user_register),
    path('api/user/modifyPwdByEmail/', views.user_register),
    path('api/user/addressBook/getAddressBookListWithWithdrawPercent/', views.get_address_book_list),
    path('api/v1/pool/stats/', views.get_pool_status),
    path('api/v1/accountMining/checkExist/', views.subuser_exist),
    path('api/v1/accountMining/checkPermissions/', views.check_permission),
    path('api/v1/config/getConfigs/', views.get_all_config),
    path('api/v1/accountMining/list/', views.get_mining_account),
    path('api/v1/observer/list/', views.get_observer_account)
]
