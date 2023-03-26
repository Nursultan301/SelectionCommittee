from django.urls import path
from .organization import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('entrant/', views.EntrantViewSet.as_view({'get': 'list'})),
    path('entrant/<int:pk>/', views.EntrantViewSet.as_view({'get': 'retrieve'}))
])
