from django.db import models

# バリデーション
# from django.core.validators import validate_image_file_extension

class Champions(models.Model):

    ### ユニーク
    # unique_field = models.CharField(verbose_name='ユニークフィールド', max_length=20)

    ### 内容
    name = models.CharField(verbose_name='チャンピオン名', max_length=20)

    ### 日時情報
    created_at = models.DateTimeField(verbose_name='作成日時',null=True, auto_now_add=True )
    updated_at = models.DateTimeField(verbose_name='更新日時',null=True, auto_now=True )

    ### リレーション
    # relation_field = models.ForeignKey('common.HogeMaster',on_delete=models.PROTECT,default=1)

    class Meta:
        ### 実テーブル名
        db_table = 'm_champions'

        ### 管理サイトで使用する名称
        verbose_name_plural = 'チャンピオンマスター'

        ### インデックス
        #indexes = [
        #    models.Index(fields=['index_field']),
        #]

        ### デフォルトの並び順
        ordering = ['id']

    # 管理サイトで扱われる名称
    def __str__(self):
        return str(self.id) +': '+str(self.name)

    # def save(self, *args, **kwargs):
    #     # 新規か更新の判断
    #     status = 'create' if self.pk == None else 'update'
    #
    #     if status == 'update':
    #         PlayersBefore = Players.objects.filter(pk=self.pk).first()
    #         # アバターを変更？
    #         if(PlayersBefore.avator_file != self.avator_file):
    #             print('アバターを変更しようとしています。')
    #             # 拡張子の取得
    #             import os.path
    #             name,ext = os.path.splitext(str(self.avator_file))
    #
    #             print(ext)
    #             self.avator_file = 'avator_file/' + str(PlayersBefore.id) + ext
    #
    #     super().save(*args, **kwargs)  # Call the "real" save() method.


    def avatar_file_name(self):
        return str(self.avatar_file)

    # 別名
    def aliases(self):
        from evaluation.models.PlayersValues import PlayersValues
        return PlayersValues.objects.filter(group = 'AL')\
                                    .filter(player = self.id)
    # サモナー名
    def summonernames(self):
        from evaluation.models.PlayersValues import PlayersValues
        return PlayersValues.objects.filter(group = 'SN')\
                                    .filter(player = self.id)
    # ツイッター
    def twitters(self):
        from evaluation.models.PlayersValues import PlayersValues
        return PlayersValues.objects.filter(group = 'TW')\
                                    .filter(player = self.id)
    # その他タグ
    def others(self):
        from evaluation.models.PlayersValues import PlayersValues
        return PlayersValues.objects.filter(group = 'OT')\
                                    .filter(player = self.id)
    # 重複先ID
    def duplications(self):
        from evaluation.models.PlayersValues import PlayersValues

        return PlayersValues.objects.filter(group = 'DU')\
                                      .filter(player = self.id)
