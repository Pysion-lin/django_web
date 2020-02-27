from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    #1,默认每页大小
    page_size = 1

    #2,每页指定的大小
    page_size_query_param = 'pagesize'

    #3,限制每页的最大数量
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('pages', self.page.paginator.num_pages),
            ('page', self.page.number),
            ('lists', data)
        ]))
