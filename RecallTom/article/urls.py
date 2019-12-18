from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'article'


urlpatterns = [
    # 安全删除
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name = 'article_safe_delete'
    ),
    path(
        'article_update/<int:id>/',
        views.article_update,
        name='article_update'
    ),

    path('article-list/', views.article_list, name='article_list'),


    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>',views.article_delete , name='article_delete')
]