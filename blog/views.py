from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BlogPost

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'
    context_object_name = 'blog_post'


# Список всех записей
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_post_list.html'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


# Создание новой записи
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    # Перенаправление после создания
    success_url = reverse_lazy('blog:post_list')


# Обновление записи
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    success_url = reverse_lazy('blog:post_list')  # Перенаправление на список после успешного редактирования


# Удаление записи
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
