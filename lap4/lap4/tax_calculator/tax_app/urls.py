urlpatterns = [
    path('', views.default_view, name='default'),
    path('tax/<int:number>', views.calculate_tax_view, name='calculate_tax'),
    path('tax/taxrate', views.tax_rate_view, name='tax_rate'),
]