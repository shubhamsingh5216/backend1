from django.urls import path
from .views import DesignerListCreateView

urlpatterns = [
   path('services/', DesignerListCreateView.as_view()),
]
