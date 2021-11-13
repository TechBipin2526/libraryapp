from django.conf.urls.static import static
from django.urls import path
from . import views
from library_app.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload, name="upload"),
    path('update/<int:book_id>', views.update_book, name="update_book"),
    path('delete/<int:book_id>', views.delete_book, name="delete_book")
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)