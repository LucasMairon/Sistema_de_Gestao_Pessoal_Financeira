from django.urls import include, path

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]
