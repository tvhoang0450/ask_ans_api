from rest_framework import serializers
from .models import Category, Question, Answer


class AskSerializers(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('author',)


class AnswerSerializers(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='users.username')
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('author',)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        read_only_fields = ('slug',)


# class UpVoteDownVoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UpVoteDownVote
#         fields = ('vote', 'Question')
#
#     # def get_fields(self):
#     #     fields = super(UpVoteDownVoteSerializer, self).get_fields()
#     #     fields['Question'].queryset = Question.objects.filter(approved_comment=True)
#     #     return fields
#
#     def create(self, validated_data):
#         votedata, created = UpVoteDownVote.objects.update_or_create(
#             user=validated_data.get('user', None),
#             Question=validated_data.get('Question', None),
#             defaults={'vote': validated_data.get('vote', None),
#                       })
#         return votedata
