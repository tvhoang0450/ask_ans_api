from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import *

app_name = 'qa'

router = routers.DefaultRouter()
router.register(r'asks', views.AskListCreateAPIView, basename="Asks")
router.register(r'asks', views.AskUpdateDeleteAPIView, basename="Asks")
router.register(r'answers', views.AnswerListCreateAPIView, basename="Answers")
router.register(r'answers', views.AnswerUpdateDeleteAPIView, basename="Answers")
router.register(r'categorys', views.CategoryListCreateAPIView, basename="Categorys")
router.register(r'categorys', views.CategoryUpdateDeleteAPIView, basename="Categorys")
urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('question/<int:qn_id>/like/', QuestionLikeRedirect.as_view(), name='like'),
    path('answer/<int:a_id>/like/', AnswerLikeRedirect.as_view(), name='ans_like'),

]
