from django.contrib import admin
from django.urls import path, include
#from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API proyecto PatitasChile",
        default_version='V1 ',
        description="V1 API proyecto PatitasChile",
        #terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="patitaschile@gmail.com"),
        #license=openapi.License(name="BSD License"),
    ),
    public=True,
    #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('user/', include('users.api.router')),
    path('PetAdopcion/', include('PetAdopcion.api.router')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
