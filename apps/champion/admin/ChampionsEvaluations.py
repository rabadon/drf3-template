from django.contrib import admin

from champion.models.ChampionsEvaluations import ChampionsEvaluations

class ChampionsEvaluationsAdmin(admin.ModelAdmin):
    # 一覧表示したときの表示する項目
    list_display = (
        'id',
        'created_at',
        'updated_at',
    )

    # 登録フォームの項目設定
    fields = ()
    exclude = ()

admin.site.register(ChampionsEvaluations,ChampionsEvaluationsAdmin)
