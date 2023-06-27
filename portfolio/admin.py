from django.contrib import admin
from .models import Project, Contact, Competence, Experience, Education, Client, Service, Langue, Categorie

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'categorie', 'date_creation')
    
class EducationAdmin(admin.ModelAdmin):
    list_display = ('diplome', 'etablissement')
    
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'entreprise')
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Competence)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Service)
admin.site.register(Langue)
admin.site.register(Contact)
admin.site.register(Categorie)
