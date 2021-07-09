from django.conf import settings

from rest_framework import viewsets

from comparer.models import *
from comparer.serializers import InstitutionListSerializer, InstitutionDetailSerializer, PolicyCategorySerializer


__all__ = ('PolicyCategoryViewSet', 'InstitutionViewSet')


class PolicyCategoryViewSet(viewsets.ModelViewSet):
    queryset = PolicyCategory.objects.active()
    serializer_class = PolicyCategorySerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    queryset = Institution.objects.active().with_scores()
    search_fields = ['name', 'region', 'country']
    ordering_fields = ['name', 'country', 'score_total'] + [f'score_{s}' for s in settings.POLICY_CATEGORY_SLUGS]

    def get_serializer_class(self):
        if self.action == 'list':
            return InstitutionListSerializer
        if self.action == 'retrieve':
            return InstitutionDetailSerializer
        return InstitutionListSerializer
