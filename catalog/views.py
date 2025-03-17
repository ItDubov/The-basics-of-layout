from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from .models import Product
from users.forms import  RegisterForm
from catalog.forms import ProductForm

# Перенаправление на регистрацию для неавторизованных пользователей
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('products:product_list')  # Перенаправление на главную страницу после входа
    return redirect('users:register')

# Главная страница (доступ только для авторизованных пользователей)
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

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
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('products:product_list')

# Редактирование продукта
@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'category']
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('products:product_detail', kwargs={'pk': self.object.pk})

# Удаление продукта
@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')

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
