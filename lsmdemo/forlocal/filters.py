
import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *

class PhoneFilter(django_filters.FilterSet):
	brand = CharFilter(field_name = "brand", lookup_expr = 'icontains')
	model = CharFilter(field_name = "model", lookup_expr = 'icontains')
	# ram = CharFilter(field_name = "ram", lookup_expr = 'icontains')
	# rom = CharFilter(field_name = "rom", lookup_expr = 'icontains')
	# color = CharFilter(field_name = "color", lookup_expr = 'icontains')
	status = CharFilter(field_name = "status", lookup_expr = 'icontains')
	# price_start = NumberFilter(field_name = "price", lookup_expr = 'gte')
	# price_stop = NumberFilter(field_name = "price", lookup_expr = 'lte')

	class Meta:
		model = Smartphone
		fields = '__all__'
		exclude = ['owner', 'offer', 'ram', 'rom', 'color']


class HomePhoneFilter(django_filters.FilterSet):
	# brand = CharFilter(field_name = "brand", lookup_expr = 'icontains')
	model = CharFilter(field_name = "model", lookup_expr = 'icontains')
	# ram = CharFilter(field_name = "ram", lookup_expr = 'icontains')
	# rom = CharFilter(field_name = "rom", lookup_expr = 'icontains')
	# color = CharFilter(field_name = "color", lookup_expr = 'icontains')
	# status = CharFilter(field_name = "status", lookup_expr = 'icontains')
	# price_start = NumberFilter(field_name = "price", lookup_expr = 'gte')
	# price_stop = NumberFilter(field_name = "price", lookup_expr = 'lte')

	class Meta:
		model = Smartphone
		fields = '__all__'
		exclude = ['owner', 'offer', 'ram', 'rom', 'color', 'brand', 'status', 'price']