from django import forms

from affiliation.models import Produit, User, Blog


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'nom_d_utilisateur', 'nom_du_parent', 'nom', 'prenom', 'pays_de_residence', 'telephone',
            'groupe', 'avatar', 'sexe',
        )
        widgets = {
            'nom_du_parent': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
            'pays_de_residence': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}),
            'groupe': forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'})
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserCreationAdminForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'nom_d_utilisateur', 'nom', 'prenom',
        )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'nom_d_utilisateur', 'nom_du_parent', 'nom', 'prenom', 'pays_de_residence', 'telephone',
            'groupe', 'avatar', 'sexe',
        )


class UserUpdateForm(forms.ModelForm):
    annee_de_naissance = forms.DateTimeField(widget=DateInput)
    nom_d_utilisateur = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = (
            'nom_d_utilisateur', 'nom', 'prenom', 'pays_de_residence', 'telephone',
            'avatar', 'annee_de_naissance', 'sexe',
        )


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['categorie', 'image1', 'image2', 'image3', 'image4', 'image5', 'designation', 'mini_description',
                  'description', 'prix', 'ancien_prix', 'quantite']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'titre', 'description', 'publie',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10})
        }
