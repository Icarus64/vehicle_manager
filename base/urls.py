from django.urls import path
from .views import VehicleList, VehicleDetail, VehicleUpdate, VehicleDelete, VehicleCreate, VehicleLogin, RegisterPage, NoPermissionView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', VehicleLogin.as_view(), name = 'login'), 
    path('logout/', LogoutView.as_view(next_page = "login"), name = "logout"),
    path('register/', RegisterPage.as_view(), name = 'register'),

    path('forbidden/', NoPermissionView.as_view(), name = 'forbidden'),

    path("vehicle-list", VehicleList.as_view(), name="vehicle_list"),
    path("vehicle/<int:pk>", VehicleDetail.as_view(), name="vehicle"),
    path('vehicles/create/', VehicleCreate.as_view(), name='vehicle-create'),
    path("vehicles/<int:pk>/update/", VehicleUpdate.as_view(), name="vehicle-update"),
    path("vehicles/<int:pk>/delete/", VehicleDelete.as_view(), name="vehicle-delete"),
]
