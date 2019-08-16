from django.urls import path
from . import views


urlpatterns = [
    path('', views.page, name="page"),
    path('<int:page_id>/<slug:page_title>', views.page, name="page"),

]
