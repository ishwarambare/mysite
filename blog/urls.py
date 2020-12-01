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
    path('form/', views.postform, name='form'),

    ##################### API ########################

    path('post-api/', api_views.PostView.as_view(), ),
    path('comment-api/', api_views.CommentView.as_view(), ),
    path('post-detail-api/', api_views.PostDetialView.as_view(), ),
    path('add-comment-api/', api_views.AddComment.as_view(), ),
    # path('mail-api/', api_views.MailApiView.as_view({'POST': 'mail_send'}), ),


    path('uplode-post-api/', api_views.UplodeImage.as_view(), ),


]
