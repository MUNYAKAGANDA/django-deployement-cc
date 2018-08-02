from django.urls import path
from . import views

app_name='app'
urlpatterns=[
   path('',views.ArticleViews.as_view(),name='articleview'),
   path('/login',views.login,name='login'),
   path('/register',views.register,name='register'),
   path('article/create',views.AddArticleView.as_view(),name='addarticleview'),
   path('article/detail/<int:pk>',views.ArticleDetailView.as_view(),name='article_detail'),
   path('article/delete/<int:pk>',views.ArticleDeleteView.as_view(),name='article_delete'),

   path('/training',views.TrainingViews.as_view(),name='training'),
   path('training/add',views.AddTrainingView.as_view(),name='add_training'),
   path('training/detail/<int:pk>',views.TrainingDetailView.as_view(),name='training_detail'),
   path('training/delete/<int:pk>',views.TrainingDeleteView.as_view(),name='training_delete'),

   path('',views.TrainingViews.as_view(),name='training'),
   path('activity/detail/<int : pk>',views.TrainingDetailView.as_view(),name='training_detail'),


]
