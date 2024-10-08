from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(
                    "Извините, но в названии продукта запрещены недопустимые слова."
                )
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(
                    "Извините, но в описании продукта запрещены недопустимые слова."
                )
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = (
            "is_published",
            "description",
            "category",
        )
