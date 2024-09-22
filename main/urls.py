from .views import ListAPIProducts,ListAPICats,ListAPINews
from django.urls import path

urlpatterns = [
    path('api/v1/<int:pk>/', ListAPIProducts.as_view()),
    path('api/v2/<int:pk>/', ListAPICats.as_view()),
    path('api/v3/<int:pk>/',ListAPINews.as_view())
]