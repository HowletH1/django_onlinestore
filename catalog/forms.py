from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name_product', 'image', 'description', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name_product(self):

        cleaned_data = self.cleaned_data['name_product']

        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Используются запрещенные слова')

        return cleaned_data

    def clean_description(self):

        cleaned_data = self.cleaned_data['description']

        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Используются запрещенные слова')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
