from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.utils.text import slugify

from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.slug

    def get_url(self):
        return f"/category/{self.id}"

    def get_number(self):
        # this method returns a number of related questions
        c = Category.objects.annotate(num_questions=models.Count('question')).filter(id=self.id)
        return c[0].num_questions

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) + str(self.id)
        super(Category, self).save(*args, **kwargs)


class Question(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(value='Deleted'))
    rating = models.IntegerField(default=0, blank=True)
    likes = models.ManyToManyField('auth.User', related_name='get_likes', blank=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('qa:Asks-list')

    def get_like_toggle(self):
        return reverse('qa', kwargs={'qn_id': self.id})

    def has_answer(self):
        res = len(self.answer_set.filter(best_answer=True))
        return True if res > 0 else False


class Answer(models.Model):
    added_at = models.DateField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(value='Deleted'))
    text = models.TextField(null=True)
    rating = models.IntegerField(default=0, blank=True)
    likes = models.ManyToManyField('auth.User', related_name='get_likes1', blank=True)
    active = models.BooleanField(default=True)  # added in case i'll need to deactivate some answers fsr
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies',
                               on_delete=models.CASCADE)  # deals with comments on answers

    best_answer = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.text

    def get_url(self):
        return reverse('qa:Answers-list')


# class UpVoteDownVote(models.Model):
#     UPVOTE = 1
#     NEUTRALVOTE = 0
#     DOWNVOTE = -1
#
#     VOTES = (
#         (UPVOTE, 'Upvote'),
#         (NEUTRALVOTE, 'Neutralvote'),
#         (DOWNVOTE, 'Downvote')
#     )
#
#     vote = models.SmallIntegerField(choices=VOTES)
#     user = models.ForeignKey('auth.User', related_name='upvotedownvotes', on_delete=models.CASCADE)
#     Question = models.ForeignKey(Question, related_name='upvotedownvotes', on_delete=models.CASCADE)
