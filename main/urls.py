from django.urls import path
from .views import show_main, show_json, show_xml, show_json_by_id, show_xml_by_id

urlpatterns = [
    path('', show_main, name='show_main'),
    path('json/', show_json, name="show_json"),
    path('xml/', show_xml, name="show_xml"),
    path('json/<uuid:id>', show_json_by_id, name="show_json"),
    path('xml/<uuid:id>', show_xml_by_id, name="show_xml_by_id")
]