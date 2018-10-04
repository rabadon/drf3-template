# RestFramework
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action

# モデル
from champion.models.Champions import Champions

# シリアライザー
from champion.serializers.Champions import ChampionsSerializer

# ページネーション
from rabadon.drf.pagination import SDPagination, MDPagination

# 認証
from rest_framework.permissions import IsAuthenticated

class ChampionsViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    serializer_class = ChampionsSerializer
    pagination_class = MDPagination # ページングを無効にする場合はコメントアウト

    # 認証情報の設定
    def get_permissions(self):
        # permission_classes = [IsAuthenticated]
        # if self.action in ['list','retrieve'] :
        permission_classes = []

        return [permission() for permission in permission_classes]

    # クエリセットの設定
    def get_queryset(self):

        ### データの取得
        queryset = Champions.objects.all()

        return queryset
    #
    # def list(self,request):
    #
    #     p_tag = request.query_params.get('tag',None)
    #     p_game = request.query_params.get('game',1)
    #
    #     queryset = Players.objects.all()
    #
    #     # デフォルトの設定
    #     if p_tag is not None :
    #         queryset_tags = PlayersValues.objects.values('player_id')\
    #                                              .filter(game=p_game)\
    #                                              .filter(group='OT')\
    #                                              .filter(value=p_tag)
    #         where_ids = []
    #         for row in queryset_tags:
    #             where_ids.append(row['player_id'])
    #
    #         queryset = queryset.filter(id__in=where_ids).order_by('-access_count')
    #
    #     page = self.paginate_queryset(queryset)
    #     serializer = self.get_serializer(page, many=True)
    #
    #     return self.get_paginated_response(serializer.data)
    #
    # # プレイヤーの検索(名前 → ID)
    # @action(methods=['GET'],
    #         detail=False,
    #         url_path='getIdByName/(?P<name>.+?)',
    #         pagination_class=MDPagination)
    # def getId(self, request, name):
    #
    #     queryset = Players.objects.filter(name=name).first()
    #
    #     serializer = PlayersForGetIdSerializer(queryset)
    #     return Response(serializer.data)
    #
    #
    # # プレイヤーの検索
    # @action(methods=['GET'],
    #         url_path='search/(?P<name>.+?)',
    #         detail=False)
    # def search(self, request, name):
    #
    #     # 名前の一致
    #     pv = PlayersValues.objects.filter(value__icontains = name).distinct()[0:20]
    #
    #     # 検索に一致したプレイヤーIDの取得
    #     list_player_id = []
    #     list_search = {}
    #     for row in pv:
    #         search_item = { 'type':row.group ,'value':row.value }
    #         list_search[row.player_id] = search_item
    #         list_player_id.append(row.player_id)
    #
    #     # ------------------------------------------------------------------------------
    #     # ★メインデータ取得
    #     # ------------------------------------------------------------------------------
    #     p = Players.objects.filter(id__in = list_player_id)\
    #                        .order_by('-access_count')
    #
    #     new_p = []
    #     for row in p:
    #         row.search_type_jp = list_search[row.id]['type']
    #         row.search_value = list_search[row.id]['value']
    #         new_p.append(row)
    #
    #     serializer = PlayersForSearchSerializer(new_p, many=True)
    #     return Response(serializer.data)
    #
    # # プレイヤーランキング
    # @action(methods=['GET'],
    #         detail=False,
    #         url_path='ranking/(?P<type>good|bad|popularity|access|hot)',
    #         pagination_class=SDPagination)
    # def ranking(self, request, type):
    #
    #     p_page = int(request.query_params.get('page',1))
    #
    #     queryset = Players.objects.all()
    #
    #     if type == 'good' : queryset = queryset.order_by('-per_evaluation_points','-access_count')
    #     elif type == 'bad' : queryset = queryset.order_by('per_evaluation_points','access_count')
    #     elif type == 'popularity' : queryset = queryset.order_by('-evaluation_count')
    #     elif type == 'access' : queryset = queryset.order_by('-access_count')
    #     elif type == 'hot':
    #         from datetime import date, datetime, timedelta
    #         from evaluation.models.AccessHistoryPlayers import AccessHistoryPlayers
    #
    #         # 3日前からカウント
    #         today = date.today()
    #         since = today - timedelta(3)
    #
    #         from django.db.models import Count
    #         queryset2 = AccessHistoryPlayers.objects.values('player')\
    #                                                 .order_by('-count','player')\
    #                                                 .filter(created_at__gt = since)\
    #                                                 .annotate(count=Count('player'))[0:50]
    #         where_ids = []
    #         count_work = []
    #         for row in queryset2:
    #             count_work.append(row['count'])
    #             where_ids.append(row['player'])
    #
    #         queryset = queryset.filter(id__in=where_ids)
    #
    #     if type == 'hot':
    #
    #         qs_result = [0] * 50
    #         for i,row in enumerate(queryset):
    #             qs_result[where_ids.index(row.id)] = row
    #
    #         page = self.paginate_queryset(qs_result)
    #
    #     else:
    #         page = self.paginate_queryset(queryset)
    #
    #     serializer = PlayersForRankingSerializer(page, many=True)
    #
    #     # ホットカウントの付与
    #     if type == 'hot':
    #         for i,row in enumerate(serializer.data):
    #             serializer.data[i]['hot_count'] = count_work[i+(p_page-1)*12]
    #
    #     return self.get_paginated_response(serializer.data)
    #
    # # プレイヤーの検索
    # @action(methods=['GET'],
    #         url_path='search/(?P<name>.+?)',
    #         detail=False)
    # def search(self, request, name):
    #
    #     # 名前の一致
    #     pv = PlayersValues.objects.filter(value__icontains = name).distinct()[0:20]
    #
    #     # 検索に一致したプレイヤーIDの取得
    #     list_player_id = []
    #     list_search = {}
    #     for row in pv:
    #         search_item = { 'type':row.group ,'value':row.value }
    #         list_search[row.player_id] = search_item
    #         list_player_id.append(row.player_id)
    #
    #     # ------------------------------------------------------------------------------
    #     # ★メインデータ取得
    #     # ------------------------------------------------------------------------------
    #     p = Players.objects.filter(id__in = list_player_id)\
    #                        .order_by('-access_count')
    #
    #     new_p = []
    #     for row in p:
    #         row.search_type_jp = list_search[row.id]['type']
    #         row.search_value = list_search[row.id]['value']
    #         new_p.append(row)
    #
    #     serializer = PlayersForSearchSerializer(new_p, many=True)
    #     return Response(serializer.data)
    #
    # # 画像アップロード
    # @action(methods=['POST'],
    #         detail=False,
    #         url_path='avatar_upload',)
    # def avatar_upload(self, request):
    #
    #     # 容量の判定
    #     filesize_about = (len(request.data['avatar']) * 3) / 4 - request.data['avatar'].count('=', -2)
    #
    #     if filesize_about > 1048576:
    #         return Response(['画像サイズが大きすぎます。1MBを超えていなくても、もう少しだけ小さくして下さい。'], status=400)
    #
    #     # アップロード開始
    #     from evaluation.serializers.PlayersBase64Image import MyImageModelSerializer
    #     data = {
    #         'avatar_file': request.data['avatar']
    #     }
    #     player = Players.objects.filter(id=request.data['id']).first()
    #     serializer = MyImageModelSerializer(player,data=data,partial=True)
    #
    #     if serializer.is_valid():
    #
    #         # 画像操作
    #         import os
    #         from django.conf import settings
    #
    #         file_path = Players.objects.filter(id=request.data['id']).first()
    #         file_path = file_path.avatar_file
    #
    #         #ext = os.path.splitext()[1]
    #         # 現状のファイルを削除
    #         file = os.path.join(settings.MEDIA_ROOT, str(file_path))
    #
    #         if str(file_path) != 'player_avatars/default.png' and os.path.isfile(file):
    #             os.remove(file)
    #
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    #
    # # ピックアッププレイヤー
    # @action(methods=['GET'],
    #         url_path='pickup',
    #         detail=False)
    # def pickup(self, request):
    #     # タグマスタの取得 → ランダムでピックアップタグを選ぶ
    #     from evaluation.models.Tags import Tags
    #     from django.db.models import Q
    #     import random
    #
    #     pickup_tags = Tags.objects.filter(Q(total_count__gte=12) | Q(is_pickup=True))
    #
    #     tag_name = pickup_tags[random.randrange(len(pickup_tags))].name
    #
    #     queryset_tags = PlayersValues.objects.values('player_id')\
    #                                          .filter(game=1)\
    #                                          .filter(group='OT')\
    #                                          .filter(value=tag_name)[0:11]
    #     where_ids = []
    #     for row in queryset_tags:
    #         where_ids.append(row['player_id'])
    #
    #     queryset = Players.objects.filter(id__in=where_ids).order_by('-access_count')
    #
    #     serializer = PlayersForRankingSerializer(queryset, many=True)
    #
    #     result = {}
    #     result['tag_name'] = tag_name
    #     result['data'] = serializer.data
    #
    #     return Response(result)
