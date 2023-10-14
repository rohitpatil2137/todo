from django.urls import path

from todos.views import IndexView, app_view, delete, update, add

app_name = 'todos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('app/', app_view, name='app'),
    path('<int:todo_id>/delete', delete, name='delete'),
    path('<int:todo_id>/update', update, name='update'),
    path('add/', add, name='add'),
]
