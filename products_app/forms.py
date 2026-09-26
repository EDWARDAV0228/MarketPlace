from django import forms
from products_app.models import Products


class ProductForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Выберите категорию"
        self.fields["brand"].empty_label = "Выберите бренд"
        self.fields["condition"].empty_label = "Выберите состояния"

    class Meta:
        model = Products
        fields = (
            "name",
            "brand",
            "image",
            "model",
            "price",
            "author",
            
            "category",
            "condition",
            "description",
            "full_description",
        )

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "id": "name",
                    "autocomplete": "off",
                    "placeholder": "Введите название товара",
                }
            ),
            "brand": forms.Select(
                attrs={
                    "id": "brand",
                }
            ),
            "image": forms.FileInput(attrs={"id": "image_inp", "accept": "images/*"}),
            "description": forms.Textarea(
                attrs={
                    "id": "description",
                    "placeholder": "Введите короткое описание товара (максимум 120 символов)",
                }
            ),
            "full_description": forms.Textarea(
                attrs={
                    "id": "full_description",
                    "placeholder": "Введите подробное описание товара...",
                }
            ),
            "category": forms.Select(
                attrs={
                    "id": "category",
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "id": "author",
                    "placeholder": "Введите имя автора",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "id": "price",
                    "placeholder": "Введите цену товара",
                }
            ),
            "condition": forms.Select(
                attrs={
                    "id": "condition",
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "id": "model",
                    "placeholder": "Введите модель товара",
                }
            ),
        }
