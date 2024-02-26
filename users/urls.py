from django.urls import path, re_path
from .views import (
    AccountProviderAuthView,
    AccountTokenObtainPairView,
    AccountTokenRefreshView,
    AccountTokenVerifyView,
    LogoutView
)

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        AccountProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('jwt/create/', AccountTokenObtainPairView.as_view()),
    path('jwt/refresh/', AccountTokenRefreshView.as_view()),
    path('jwt/verify/', AccountTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
]
