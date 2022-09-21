from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class SmallNumberNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'sayfa'

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'sayfadaki veri sayısı'

class MyCursorPagination(CursorPagination) :
    ordering = "-number"
    #? reverse order (200,199,198.......) 👆
    page_size = 10

"""
çok büyük verilerde kullanışlı cursor pagination. Bulunduğu noktaya cursor koyuyor ve direk ordan itibaren veri okuyor. Limit&off sette her seferinde en baştan arka planda tarıyor veriyi
"""