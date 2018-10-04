from rest_framework import serializers

# モデルの読み込み
from champion.models.Champions import Champions

# シリアライザーの読み込み
#from evaluation.serializers.ChampionsValues import ChampionsValuesSerializer


class ChampionsSerializer(serializers.ModelSerializer):

    ### テーブルカラム

    ### 参照カラム
    # gender = GendersSerializer(read_only=True)

    ### 上書きカラム

    ### 独自カラム
    # mf_aliases = serializers.SerializerMethodField()
    # mf_summoner_names = serializers.SerializerMethodField()
    # mf_twitters = serializers.SerializerMethodField()
    # mf_others = serializers.SerializerMethodField()
    # mf_duplications = serializers.SerializerMethodField()
    # mf_created_at_format = serializers.SerializerMethodField()
    # mf_updated_at_format = serializers.SerializerMethodField()
    # mf_latest_evaluation_format = serializers.SerializerMethodField()

    class Meta:
        model = Champions
        fields = ('__all__')  # アクセス可能なカラムの指定
    #
    # def get_mf_aliases(self,obj):
    #     return ChampionsValuesSerializer(obj.aliases(),many=True).data
    #
    # def get_mf_summoner_names(self,obj):
    #     return ChampionsValuesSerializer(obj.summonernames(),many=True).data
    #
    # def get_mf_twitters(self,obj):
    #     return ChampionsValuesSerializer(obj.twitters(),many=True).data
    #
    # def get_mf_others(self,obj):
    #     return ChampionsValuesSerializer(obj.others(),many=True).data
    #
    # def get_mf_duplications(self,obj):
    #     return ChampionsValuesSerializer(obj.duplications(),many=True).data
    #
    # def get_mf_created_at_format(self,obj):
    #     from pytz import timezone
    #     jst_now = obj.created_at.astimezone(timezone('Asia/Tokyo'))
    #
    #     return jst_now.strftime("%Y/%m/%d %H:%M:%S")
    #
    # def get_mf_updated_at_format(self,obj):
    #     from pytz import timezone
    #
    #     if obj.updated_at is not None:
    #         jst_time = obj.updated_at.astimezone(timezone('Asia/Tokyo'))
    #         return jst_time.strftime("%Y/%m/%d %H:%M:%S")
    #
    #     return 'まだ更新されていません'
    #
    # def get_mf_latest_evaluation_format(self,obj):
    #     from pytz import timezone
    #
    #     if obj.latest_evaluation is not None:
    #         jst_time = obj.latest_evaluation.astimezone(timezone('Asia/Tokyo'))
    #         return jst_time.strftime("%Y/%m/%d %H:%M:%S")
    #
    #     return 'まだ評価されていません'
