from django.contrib import admin
from . import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','slug','status']
    search_fields =('title','body',)
    list_filter=('title','body',)
    fieldsets = [('Description', {'fields': ['title','slug','body','thumb','status']}), ]
    actions=['make_approved',]


    def make_approved(self, request, queryset):
        rows_updated = queryset.update(status='a')
        if rows_updated == 1:
             message_bit = "1 story was"
        else:
             message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    make_approved.short_description='Approve'


class TrainerAdmin(admin.ModelAdmin):
    list_display=['title','name','article']
    search_fields =('title','name','article')
    list_filter=('title','bio',)
    fieldsets = [('Description', {'fields': ['title','name','article','bio','twitter','instagram','facebook']}), ]

class SponsorshipAdmin(admin.ModelAdmin):
    list_display =['first_name','last_name','company_name','type','email']
    search_fields =('first_name','last_name','type','company_name')
    list_filter= ['first_name','last_name','type','company_name']
    fieldsets = [('Description', {'fields': ['first_name','last_name','type','company_name','twitter','instagram','facebook','email']}), ]

class TrainingAdmin(admin.ModelAdmin):
    list_display=['name','thumb','trainer','training_type']
    search_fields =('name','trainer','training_type')
    list_filter=('name','trainer','training_type')


class ActivityAdmin(admin.ModelAdmin):
    list_display=['name','slug','description','date_happen']
    search_fields =('name','slug','description','date_happen')
    list_filter=('name','slug','description','date_happen')
admin.site.register(models.Sponsorship,SponsorshipAdmin)
admin.site.register(models.Trainer,TrainerAdmin)
admin.site.register(models.Activity,ActivityAdmin)
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Training,TrainingAdmin)
