from django.contrib import admin
from .models import *
from guardian.admin import GuardedModelAdmin
from reversion.admin import VersionAdmin


# With object permissions support
class SkosLabelAdmin(GuardedModelAdmin, VersionAdmin):
    pass


class SkosConceptAdmin(GuardedModelAdmin, VersionAdmin):
    pass


class SkosCollectionAdmin(GuardedModelAdmin, VersionAdmin):
    pass


class SkosConceptSchemeAdmin(GuardedModelAdmin, VersionAdmin):
    pass


admin.site.register(SkosLabel, SkosLabelAdmin)
admin.site.register(SkosConcept, SkosConceptAdmin)
admin.site.register(SkosCollection, SkosCollectionAdmin)
admin.site.register(SkosConceptScheme, SkosConceptSchemeAdmin)


# @admin.register(SkosConceptScheme)
# class SkosConceptSchemeAdmin(admin.ModelAdmin):

# 	def save_model(self, request, obj, form, change):
# 		obj.created_by = request.user
# 		super().save_model(request, obj, form, change)