from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView

from .models import Blog, Category
# from tags.models import Tag

"""
Due to time contraints,
Category based view is disabled,
will finish it once I will get time...
"""
class BlogArchiveIndexView(ArchiveIndexView):
    model = Blog
    queryset = Blog.objects.published()
    date_field = 'timestamp'
    template_name = 'blogs/archives_list.html'

"""
Limited Time means limited work
and limited functionality
removing support for Yearly/Monthly Archive Views...
"""
# class BlogYearArchiveView(YearArchiveView):
#     queryset = Blog.objects.published()
#     date_field = "timestamp"
#     make_object_list = True
#     allow_future = False
#     template_name = 'blogs/archives_list.html'

# class BlogMonthArchiveView(MonthArchiveView):
#     queryset = Blog.objects.all()
#     date_field = "timestamp"
#     allow_future = True

# class CategoryListView(ListView):
#     template_name = "blog/category_list.html"

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return Category.objects.all()

# class CategoryDetailView(DetailView):
#     cat_obj = Category.objects.all()
#     template_name = "blog/category_detail.html"

#     def get_object(self, *args, **kwargs):
#         request = self.request
#         slug = self.kwargs.get('slug')
#         try:
#             instance = Category.objects.get(slug=slug, active=True)
#         except Category.DoesNotExist:
#             raise Http404("Not Found")
#         except Category.MultipleObjectsReturned:
#             qs = Category.objects.filter(slug=slug, active=True)
#             instance = qs.first()
#         except:
#             raise Http404("Not Found")
#         return instance


class BlogFeaturedListView(ListView):
    template_name = "blogs/posts_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Blog.objects.all().featured()

class BlogFeaturedDetailView(DetailView):
    queryset = Blog.objects.all().featured()
    template_name = "blogs/single_post.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Blog.objects.all().featured()

class BlogListView(ListView):
    template_name = 'blogs/posts_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context['title'] = "Rejuva Aesthetica | Blogs"
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Blog.objects.published()

class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'blogs/single_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = "Rejuva Aesthetica | " + self.object.title
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # tags = self.args.get('tags')
        try:
            instance = Blog.objects.get(slug=slug, active=True)
            # tags_obj = Tag.objects.get(slug=tags, active=True)
        except Blog.DoesNotExist:
            raise Http404("Not Found")
        except Blog.MultipleObjectsReturned:
            qs = Blog.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Not Found")
        return instance
