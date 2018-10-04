from rest_framework import serializers

# モデルの読み込み
from champion.models.ChampionsEvaluations import ChampionsEvaluations

class ChampionsEvaluationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChampionsEvaluations
        fields = ('__all__')
