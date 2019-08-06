from django.urls import path
from bookinfo import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('search/find/', views.book_search),
    path('search/find/create', views.add_book),
    path('list/', views.book_list),
]