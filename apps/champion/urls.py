from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter

from champion.views import ChampionsViewSet
from champion.views import ChampionsEvaluationsViewSet

router = SimpleRouter()

router.register(r'champions_evaluations', ChampionsEvaluationsViewSet , base_name='champions_evaluations')
router.register(r'champions', ChampionsViewSet , base_name='champions')

urlpatterns = router.urls
