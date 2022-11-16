from django.core.management.base import BaseCommand, CommandError
from askme.models import *
import datetime
from random import randint
from PIL import Image
import logging
from django.utils import timezone


class Command(BaseCommand):
    help = 'Fills database'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        try:
            ratio = options['ratio']
        except Exception:
            raise CommandError('Error')

        # теги

        # try:
        #     [Tag(text=f'tag №{i}').save() for i in range(1, ratio+1)]
        # except Exception:
        #     raise CommandError(Exception)
        # self.stdout.write(self.style.SUCCESS(
        #     'Successfully filled tags in database'))

        # профили

        # try:
        #     users = []
        #     for i in range(1, ratio*10 + 1):
        #         user = User(username=f'user {i}',
        #                     first_name=f'name {i}',
        #                     last_name=f'last name {i}',
        #                     email=f'email {i}',
        #                     password=f'password {i}')
        #         user.save()
        # except Exception as e:
        #     logging.exception(e)
        #     print('profiles failed')
        #     raise CommandError(Exception)
        # self.stdout.write(self.style.SUCCESS(
        #     'Successfully filled users in database'))

        # лайки

        # try:
        #     [
        #         Like(
        #             like=bool(randint(0, 1)),
        #             user=Profile.objects.get(pk=randint(1, ratio*10))
        #         ).save() for i in range(1, ratio*200+1)]

        # except Exception:
        #     print('likes failed')
        #     raise CommandError(Exception)
        # self.stdout.write(self.style.SUCCESS(
        #     'Successfully filled likes in database'))

        # вопросы

        # left = 1
        # right = 0
        # try:
        #
        #     for i in range(1, ratio*10 + 1):

        #         tags = [Tag.objects.get(pk=randint(1, ratio))
        #                 for i in range(randint(1, 5))]

        #         right += randint(1, 10)
        #         likes = [Like.objects.get(pk=i)
        #                  for i in range(left, right)]
        #         left = right

        #         question = Question(
        #             author=Profile.objects.get(pk=randint(1, ratio*10)),
        #             title=f'title {i}',
        #             text=f'text {i}',
        #         )

        #         rating = 0
        #         for like in likes:
        #             rating += like.like

        #         question.save()
        #         question.tags.set(tags)
        #         question.likes.set(likes)
        #         question.rating = rating
        #         question.save()

        # except Exception:
        #     print('questions failed')
        #     raise CommandError(Exception)
        # self.stdout.write(self.style.SUCCESS(
        #     'Successfully filled questions in database'))

        # ответы

        try:
            for i in range(105_523, 1_000_000 + 1):

                likes = [Like(like=bool(randint(0, 1)),
                              user=Profile.objects.get(pk=randint(1, ratio*10))
                              ) for i in range(randint(0,10))]
                rating = 0
                for like in likes:
                    like.save()
                    rating += like.like

                answer = Answer(
                    author=Profile.objects.get(pk=randint(1, ratio * 10)),
                    correct=i % 2,
                    text=f'text {i}',
                    related_question=Question.objects.get(
                        pk=randint(1, ratio*10)),
                    rating=rating
                )
                answer.save()
                answer.likes.set(likes)
                answer.save()

        except Exception:
            print('answers failed')
            self.stdout.write(self.style.ERROR(str(Exception)))
            raise CommandError(Exception)
        self.stdout.write(self.style.SUCCESS(
            'Successfully filled answers in database'))
