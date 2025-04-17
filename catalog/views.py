from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from users.forms import  RegisterForm
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product, Category
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden

# Перенаправление на регистрацию для неавторизованных пользователей
@login_required
def home_redirect(request):
    return render(request, 'catalog/home.html')

# Главная страница (доступ только для авторизованных пользователей)
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/home.html'

# Страница контактов
class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'

# Детальная страница продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = ProductForm()
        return context

# Создание продукта (только авторизованные пользователи)
@method_decorator(login_required, name='dispatch')
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

@login_required
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if not request.user.has_perm('catalog.can_unpublish_product'):
        return HttpResponseForbidden("У вас нет прав на снятие с публикации.")

    product.is_published = False
    product.save()
    return redirect('products:product_list')

# Редактирование продукта
@method_decorator(login_required, name='dispatch')
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'category']
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('products:product_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

# Удаление продукта
@method_decorator(login_required, name='dispatch')
class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')
    permission_required = 'catalog.delete_product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('catalog.delete_product')

# Список продуктов
@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

# Форма регистрации
class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Автовход после регистрации
        return redirect(self.get_success_url())


def product_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'catalog/product_list.html', {'products': products, 'categories': categories})