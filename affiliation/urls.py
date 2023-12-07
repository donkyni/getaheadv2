from affiliation import views
from django.urls import re_path as url, path

urlpatterns = [
    url(r'^apropos$', views.apropos, name="apropos"),
    url(r'^produit$', views.produit, name="produit"),
    url(r'^(?P<id>\d+)/detailproduit$', views.detailproduit, name="detailproduit"),
    # path("detailproduit/<int:id>", views.detailproduit, name="detailproduit"),
    url(r'^blog$', views.blog, name="blog"),
    url(r'^contact$', views.contact, name="contact"),
    url(r'^compte$', views.compte, name="compte"),
    url(r'^compteadmin$', views.compteadmin, name="compteadmin"),
]
