# RestFramework
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

# モデルとシリアライザーの読み込み
from champion.models.ChampionsEvaluations import ChampionsEvaluations
from champion.serializers.ChampionsEvaluations import ChampionsEvaluationsSerializer

# ページネーション
from rabadon.drf.pagination import MDPagination,LGPagination

# 認証
from rest_framework.permissions import AllowAny,IsAuthenticated

class ChampionsEvaluationsViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = ChampionsEvaluationsSerializer
    pagination_class = LGPagination

    # 認証情報の設定
    def get_permissions(self):

        permission_classes = [AllowAny]

        #if self.action in ['create','update','partial_update','destroy'] :
        #    permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    # クエリセットの設定
    def get_queryset(self):

        ### データの取得
        queryset = ChampionsEvaluations.objects.all()

        return queryset
