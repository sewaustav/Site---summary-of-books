from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all, name = 'all_stories'),
    path('test/', test, name = 'test'),
    path('story/<int:pk>', ContentView.as_view(), name = 'id_story'),
    path('create/', create_post, name = 'create'),
    path('create/ok/', ok, name = 'ok'),
    path('signup/', signup, name = 'signup'),
    # path('login/', user_login, name = 'login'),
    path('search/', post_search, name='post_search'),
]