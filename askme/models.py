from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models import Count

class ProfileManager(models.Manager):
    def get_hot_users(self):
        return self.annotate(q_count=Count('questions')).order_by('-q_count')[:10]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True,
                               null=True,
                               upload_to='uploads',
                               default='static/img/1.jpg')

    objects = models.Manager()
    manager = ProfileManager()

    class Meta:
        managed = True
        db_table = 'profile'

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created, **kwargs):
    if created:
        return Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class TagManager(models.Manager):
    def get_hot_tags(self):
        return self.annotate(q_count=Count('questions')).order_by('-q_count')[:10]


class Tag(models.Model):
    text = models.CharField(max_length=40, default="")

    objects = models.Manager()
    manager = TagManager()

    class Meta:
        managed = True
        db_table = 'tag'

    def __str__(self) -> str:
        return self.text


class QuestionManager(models.Manager):
    def get_hot_questions(self):
        return self.order_by('-rating')[:40]

    def get_some_questions(self, count=40):
        return self.order_by('-date')[:count]


class Question(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(max_length=4000, default="")
    author = models.ForeignKey(Profile, models.CASCADE, related_name='questions')
    date = models.DateField(default=timezone.now)
    rating = models.IntegerField(blank=True, null=True, default=0)
    tags = models.ManyToManyField(Tag,
                                  verbose_name=("list of tags"),
                                  related_name='questions')
    likes = models.ManyToManyField('Like')

    objects = models.Manager()
    manager = QuestionManager()

    class Meta:
        managed = True
        db_table = 'question'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(Profile, models.CASCADE)
    date = models.DateField(blank=True, default=timezone.now)
    correct = models.BooleanField(blank=True, default=False)
    rating = models.IntegerField(blank=True, null=True, default=0)
    text = models.TextField(max_length=4000, default="")
    likes = models.ManyToManyField('Like')
    related_question = models.ForeignKey(Question,
                                         on_delete=models.CASCADE,
                                         related_name="answers")

    class Meta:
        managed = True
        db_table = 'answer'

    def __str__(self) -> str:
        return self.text


class Like(models.Model):
    user = models.ForeignKey(Profile, models.CASCADE, )
    like = models.BooleanField(blank=True, default=False)

    class Meta:
        managed = True
        db_table = 'like'

    def __str__(self) -> str:
        return f'{self.user}, {self.like}'
