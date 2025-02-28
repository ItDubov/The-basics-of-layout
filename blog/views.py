from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BlogPost

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        blog_post = super().get_object(queryset)
        blog_post.views_count += 1
        blog_post.save()
        return blog_post


# Список всех записей
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


# Создание новой записи
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    # Перенаправление после создания
    success_url = reverse_lazy('blog:post_list')

# Обновление записи
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'blog_post'

