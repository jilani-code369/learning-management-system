from rest_framework.pagination import PageNumberPagination


#Pagination to return 10 data:
class PaginationOf10(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 
    
 
#Pagination to return 20 data:   
class PaginationOf20(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
#Pagination to return 30 data:
class PaginationOf30(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100
    
