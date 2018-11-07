from django.urls import path, include

from .views import BlogDetailView, BlogListView, BlogFeaturedListView, BlogFeaturedDetailView, BlogArchiveIndexView


app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<slug>/', BlogDetailView.as_view(), name='detail'),
    path('featured/all/', BlogFeaturedListView.as_view(), name='featured_list'),
    path('featured/<slug>/', BlogFeaturedDetailView.as_view(), name='featured_detail'),
    path('archive/all', BlogArchiveIndexView.as_view(), name='archive'),
]