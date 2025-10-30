from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("assignments/", include("apps.assignments.urls")),
    path("api/answers/", include("apps.common.urls")),
]