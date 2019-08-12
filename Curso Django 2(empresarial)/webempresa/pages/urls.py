from django.urls import path
from . import views


urlpatterns = [
    path('', views.Page, name="page"),
    path('category/<int:page_id>/', views.Page, name="page"),

]
