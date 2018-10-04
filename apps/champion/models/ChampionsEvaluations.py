from django.db import models

# バリデーション
from django.core.validators import validate_image_file_extension

class ChampionsEvaluations(models.Model):

    ### 内容
    content = models.CharField(verbose_name='内容', max_length=2048, default=0)

    ### 日時情報
    created_at = models.DateTimeField(verbose_name='作成日時',null=True, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',null=True)

    class Meta:
        db_table = 't_champions_evaluations'
        verbose_name_plural = 'チャンピオン評価トラン'
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.id)
