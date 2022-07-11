from rest_framework.pagination import PageNumberPagination


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 10


class TodoPageNumberPagination(PageNumberPagination):
    page_size = 20
