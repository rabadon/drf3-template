"""django_lolune URL Configuration

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
from django.contrib import admin
from django.urls import include,path
# jwt
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    # 管理サイト
    path('admin/', admin.site.urls),
    # API
    path('api/', include('champion.urls')),
    path('api/token/obtain/', obtain_jwt_token),
    path('swagger/', schema_view),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static('media/', document_root=settings.MEDIA_ROOT)
