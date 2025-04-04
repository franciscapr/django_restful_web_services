"""Limite de paginaciòn"""

from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    # Set the maximum limit value to 8
    max_limit = 8