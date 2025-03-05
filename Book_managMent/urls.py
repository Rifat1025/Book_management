
from django.contrib import admin
from django.urls import path
from Book_managMent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.book,name="book"),
    path('register/',views.register,name="register"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update_data")
]
