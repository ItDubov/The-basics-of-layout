from django.views.generic import ListView, TemplateView, DetailView
from .models import Product
from blog.models import BlogPost

class HomePageView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'  # Имя контекста, которое будет использоваться в шаблоне

class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'

    def get_object(self, queryset=None):
        blog_post = super().get_object(queryset)
        blog_post.views_count += 1
        blog_post.save()
        return blog_post