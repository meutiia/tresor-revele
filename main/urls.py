from django.urls import path
from main.views import show_main, create_goods_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_goods
from main.views import delete_goods
from main.views import add_goods_entry_ajax
from main.views import create_goods_flutter
from main.views import get_user_goods_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-goods-entry', create_goods_entry, name='create_goods_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-goods/<uuid:id>', edit_goods, name='edit_goods'),
    path('delete/<uuid:id>', delete_goods, name='delete_goods'),
    path('create-goods-entry-ajax', add_goods_entry_ajax, name='add_goods_entry_ajax'),
    path('create-flutter/', create_goods_flutter, name='create_goods_flutter'),
    path('json-by-user/', get_user_goods_json, name='get_user_goods_json'),
]