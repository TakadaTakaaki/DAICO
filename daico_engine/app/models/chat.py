from django.db import models
from django.utils import timezone

class Chat(models.Model):
    class Meta:
        db_table = 'chat'
    # kind = {
    #     ("A","ご注文について"),
    #     ("B","会員情報について"),
    #     ("C","ご利用方法について"),
    #     ("D","その他"),
    # }
    EXAMPLE_FOO = ((1, 'ご注文について'), (2, '会員情報について'), (3, 'ご利用方法について'), (4, '掲載資料請求について'), (5, 'その他'))
    # kinds = models.CharField(
    #     max_length=1,
    #     choices=kind,
    #     default='C'
    # )
    foo = models.IntegerField(choices=EXAMPLE_FOO)
    name = models.CharField(
        max_length=10,
    )
    date = models.DateTimeField(default=timezone.now)
    # email = models.EmailField(
    #     max_length=128,
    #     unique=True
    # )
    message = models.TextField(
        max_length=300,
        null=False
    )
    # phone = models.TextField(
    #     max_length=12,
    #     null=False
    # )


    def __str__(self):
        return self.name