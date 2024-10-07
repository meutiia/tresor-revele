from django.forms import ModelForm
from main.models import GoodsEntry
from django.utils.html import strip_tags

class GoodsEntryForm(ModelForm):
    class Meta:
        model = GoodsEntry
        fields = ["name", "price", "description", "category", "condition"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)
    
    def clean_condition(self):
        condition = self.cleaned_data["condition"]
        return strip_tags(condition)