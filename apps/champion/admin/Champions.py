from django.contrib import admin

from champion.models.Champions import Champions

class ChampionsAdmin(admin.ModelAdmin):

    # 一覧表示したときの表示する項目
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
    )

    # 登録フォームから除外する項目
    exclude = ()

admin.site.register(Champions,ChampionsAdmin)
