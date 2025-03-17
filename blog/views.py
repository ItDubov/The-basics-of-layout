from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Детальная страница записи
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        blog_post = super().get_object(queryset)
        blog_post.views_count += 1
        blog_post.save()
        return blog_post

# Список всех опубликованных записей
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

# Создание новой записи
@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    success_url = reverse_lazy('blog:post_list')

# Обновление записи
@method_decorator(login_required, name='dispatch')
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})

# Удаление записи
@method_decorator(login_required, name='dispatch')
class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'blog_post'
