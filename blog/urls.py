# from django.urls import path
# from . import views

from django.urls import path
from . import views, api_views

app_name = 'blog'

urlpatterns = [
    #################### Blog ########################

    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),


    #################### API ########################

    path('post-api/', api_views.PostView.as_view(), ),
    path('comment-api/', api_views.CommentView.as_view(), ),
    path('post-detail-api/', api_views.PostDetialView.as_view(), ),
]
