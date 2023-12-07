from django.shortcuts import render, redirect, get_object_or_404

from affiliation.forms import ProduitForm, UserCreationForm, UserCreationAdminForm, BlogForm
from affiliation.models import Produit, CategorieProduit, User, Groupe, Blog


def accueil(request):
    return render(request, 'base.html', locals())


def apropos(request):
    return render(request, 'apropos/apropos.html', locals())


def produit(request):
    all_product = Produit.objects.filter(archive=False)
    all_categorie = CategorieProduit.objects.filter(archive=False)
    vedettes = Produit.nouveau_produit()
    return render(request, 'produit/produit.html', locals())


def detailproduit(request, id):
    # get_product = get_object_or_404(Produit, id=id)
    get_product = Produit.objects.get(id=id)
    all_categorie = CategorieProduit.objects.filter(archive=False)
    vedettes = Produit.nouveau_produit()
    return render(request, 'produit/detailproduit.html', locals())


def blog(request):
    return render(request, 'blog/blog.html', locals())


def contact(request):
    return render(request, 'contact/contact.html', locals())


def compte(request):
    return render(request, 'compte/compte.html', locals())


def compteadmin(request):
    utilisateurs = User.objects.filter(is_admin=False)
    all_product = Produit.objects.filter(archive=False)
    all_categorie = CategorieProduit.objects.filter(archive=False)

    if request.method == 'POST':
        p_form = ProduitForm(request.POST, request.FILES)
        if p_form.is_valid():
            p_form.save()
            return redirect('compteadmin')
    else:
        p_form = ProduitForm()

    # FOR ADMIN USER CREATION
    a_groupe = get_object_or_404(Groupe, nom_du_groupe="Administration")
    admins = User.objects.filter(is_admin=True)

    if request.method == 'POST':
        a_form = UserCreationAdminForm(request.POST, request.FILES)
        if a_form.is_valid():
            final = a_form.save(commit=False)
            final.is_admin = True
            final.groupe = a_groupe
            final.save()
            return redirect('compteadmin')
    else:
        a_form = UserCreationAdminForm()

    # FOR BLOG CREATION
    blogs = Blog.objects.filter(archive=False)

    if request.method == 'POST':
        b_form = BlogForm(request.POST, request.FILES)
        if b_form.is_valid():
            b_form.save()
            return redirect('compteadmin')
    else:
        b_form = BlogForm()

    return render(request, 'compteadmin/compteadmin.html', locals())
