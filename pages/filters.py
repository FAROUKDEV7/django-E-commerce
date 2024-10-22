import django_filters
from .models import Product




class ProductFilter(django_filters.FilterSet):
    PRDname = django_filters.CharFilter(lookup_expr='icontains')
    PRDprice = django_filters.CharFilter(lookup_expr='icontains')
    PRDdiscountprice = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['PRDname','PRDcategory','PRDprice','PRDdiscountprice']
        