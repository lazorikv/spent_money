from django.contrib import admin
from django.urls import path
from api.views import ResultsView, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ResultsView.as_view(), name="index"),
    path('post/', index, name="post"),
]
