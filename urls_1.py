from django.contrib import admin
from django.urls import include, path # includeをimport

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')), # includeでurl設定を追加
    path('account/', include('allauth.urls')),
]

