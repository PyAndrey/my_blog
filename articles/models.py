from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Тема, которую изучает пользователь."""
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

# class Entry(models.Model):
#     """Информация изученная пользователем по теме."""
#     topic = models.ForeignKey('Topic', null=True, on_delete=models.PROTECT)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'entries'

#     def __str__(self):
#         """Возвращает строковое представление модели."""
#         if len(self.text) > 50:
#             return self.text[:50] + "..."
#         else:
#             return self.text
