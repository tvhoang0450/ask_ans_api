from django.views.generic import RedirectView
from rest_framework import permissions, generics
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, get_object_or_404, )
from rest_framework.permissions import IsAuthenticated

from .serializers import AskSerializers, AnswerSerializers, CategorySerializers
from .permissions import IsOwnerOrReadOnly
from .models import Category, Question, Answer


# Create your views here.
class AskListCreateAPIView(viewsets.GenericViewSet,
                           ListCreateAPIView, ):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AskSerializers
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AskUpdateDeleteAPIView(viewsets.GenericViewSet,
                             RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = AskSerializers
    lookup_field = 'id'


# Answer
class AnswerListCreateAPIView(viewsets.GenericViewSet,
                              ListCreateAPIView, ):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnswerSerializers
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerUpdateDeleteAPIView(viewsets.GenericViewSet,
                                RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    lookup_field = 'id'


# Category
class CategoryListCreateAPIView(viewsets.GenericViewSet,
                                ListCreateAPIView, ):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()



class CategoryUpdateDeleteAPIView(viewsets.GenericViewSet,
                                  RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'id'


class QuestionLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        qn_id = self.kwargs.get('qn_id')
        print(qn_id)
        qn = get_object_or_404(Question, id=qn_id)
        url_ = qn.get_url()
        user = self.request.user

        if user.is_authenticated:
            if user in qn.likes.all():
                qn.likes.remove(user)
                qn.rating -= 1
            else:
                qn.likes.add(user)
                qn.rating += 1
            qn.save()
        return url_


class AnswerLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        a_id = self.kwargs.get('a_id')
        print(a_id)
        ans = get_object_or_404(Answer, id=a_id)
        url_ = ans.get_url()
        user = self.request.user

        if user.is_authenticated:
            if user in ans.likes.all():
                ans.likes.remove(user)
                ans.rating -= 1
            else:
                ans.likes.add(user)
                ans.rating += 1
            ans.save()
        return url_


def get_redirect_url():
    return 1
