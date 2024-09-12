from django.forms import ModelForm
from main.models import GoodsEntry

class GoodsEntryForm(ModelForm):
    class Meta:
        model = GoodsEntry
        fields = ["name", "price", "description", "category", "condition"]