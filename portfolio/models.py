from django.db import models

# Model Category
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Model Project
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('mobile', 'Mobile'),
        ('nouveau', 'Nouveau'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
     
# Model Contact
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom

# Model Competence
class Competence(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nom

# Model Experience
class Experience(models.Model):
    titre = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    description = models.TextField()
    lien_entreprise = models.URLField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.entreprise

# Model Education
class Education(models.Model):
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    description = models.TextField()
    lien_etablissement = models.URLField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.diplome

# Model Client
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

# Model Service
class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom

# Model Langue
class Langue(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.nom

    
