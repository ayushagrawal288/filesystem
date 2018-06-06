from django.urls import path
from core.views import upload_file, list_files, get_file, delete_file, rename_file


urlpatterns = [
    path("", list_files, name='list'),
    path('get/', get_file, name='get'),
    path('rename/', rename_file, name='rename'),
    path("upload/", upload_file, name='upload'),
    path("delete/", delete_file, name='delete'),
]
