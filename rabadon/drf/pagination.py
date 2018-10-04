from rest_framework.pagination import PageNumberPagination

XS_PAGE_SIZE = 5
SM_PAGE_SIZE = 8
SD_PAGE_SIZE = 12
MD_PAGE_SIZE = 16
LG_PAGE_SIZE = 24
XL_PAGE_SIZE = 32

class XSPagination(PageNumberPagination):
    page_size = XS_PAGE_SIZE

class SMPagination(PageNumberPagination):
    page_size = SM_PAGE_SIZE

class SDPagination(PageNumberPagination):
    page_size = SD_PAGE_SIZE

class MDPagination(PageNumberPagination):
    page_size = MD_PAGE_SIZE

class LGPagination(PageNumberPagination):
    page_size = LG_PAGE_SIZE

class XLPagination(PageNumberPagination):
    page_size = XL_PAGE_SIZE
