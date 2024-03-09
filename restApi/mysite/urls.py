from django.contrib import admin
from django.urls import path
from myapp.views import BookList,BookDetail

urlpatterns = [
    path('books',BookList.as_view()),
    path('books/<int:pk>',BookDetail.as_view()),
    path('admin/', admin.site.urls),
]