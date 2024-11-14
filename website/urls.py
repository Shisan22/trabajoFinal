from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("client/<int:pk>", views.client_details, name="client"),
    path("client/create", views.create_client, name="create_client"),
    path("client/<int:pk>/update", views.update_client, name="update_client"),
    path("client/<int:pk>/delete", views.delete_client, name="delete_client"),
    path("carta/", views.carta, name="carta"),
    path("ubicaciones/", views.ubicaciones, name="ubicaciones"),
    path('recipes/', views.recipe_list, name='recipe_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
