from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('signup/',views.SignUpAPI.as_view(), name='signup'),
    path('products/search/', views.ProductSearchList.as_view(), name='product-search'),
    path('products/ordering/', views.ProductList.as_view(), name='product-ordering'),
    path('products/pagination/', views.ProductList.as_view(), name='product-pagination'),
    path('products/details/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    # path for ordering by price
    path('products/order_by_price/', views.ProductOrdering.as_view(), name='product-ordering'),
]  

urlpatterns = format_suffix_patterns(urlpatterns)  


#Here provide all urls---->>
#Change pagination-->>>http://127.0.0.1:8000/project/products/ordering/?page_size=10
#search page number--->>http://127.0.0.1:8000/project/products/ordering/?page=2  
#all_sort -->>http://127.0.0.1:8000/project/products/ordering/?ordering=-price&page_size=10&page=1

###Sort By------------------------------------------------------------------------------>>>
#sort base on  price--->>
# http://127.0.0.1:8000/project/products/ordering/?ordering=-price
# http://127.0.0.1:8000/project/products/ordering/?ordering=id
# 

#Order BY ------------------------------------------------------------------------------>>>
#http://127.0.0.1:8000/project/products/ordering/?ordering=-created_at

#http://127.0.0.1:8000/project/products/order_by_price/

#filter----------------------------------------------------------------------------------->>
#base on price--->>price,Max & min
#http://127.0.0.1:8000/project/products/search/?price=64400
#http://127.0.0.1:8000/project/products/search/?max_price=64400
#http://127.0.0.1:8000/project/products/search/?min_price=36000

#base on id---->>>
#http://127.0.0.1:8000/project/products/search/?id=1

#base on name--->>
#http://127.0.0.1:8000/project/products/search/?name=gokul

#base on description--->>
#http://127.0.0.1:8000/project/products/search/?query=mobile
