from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in self.forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Название не должно содержать запрещенные слова: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in self.forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать запрещенные слова: {word}")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной!")
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
