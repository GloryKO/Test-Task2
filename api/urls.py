from django.urls import path
from . import views
urlpatterns = [
    path('get/', views.get_task_list, name="get"),
    path('create/', views.create_task, name="create"),
    path('update/<int:pk>', views.update_task, name="update"),
    path('delete/<int:pk>', views.delete_task, name="delete"),
    path('details/<int:pk>', views.get_single_task_details, name="details")
]

