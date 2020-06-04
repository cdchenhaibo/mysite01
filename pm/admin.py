from django.contrib import admin
from .models import PMProjects
from .models import PMYears
from .models import PMAreas
from .models import PMCountys
from .models import PMPrjPreFeasibility
from .models import PMPrjFeasibility
from .models import PMPrjPreFirstFounded
from .models import PMPrjFirstFounded
# Register your models here.


class PMYearsAdmin(admin.ModelAdmin):
    list_display = ("year",)


class PMAreasAdmin(admin.ModelAdmin):
    list_display = ("prj_area",)


class PMCountysAdmin(admin.ModelAdmin):
    list_display = ("county_name",)


class PMProjectsAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "supply_area", "dev_attr", "county", "capacity_size", "line_len", "cable_len",
                    "total_investment", "is_country_grid", "info")


class PMPrjPreFeasibilityAdmin(admin.ModelAdmin):
    list_display = ("prj", "capacity_size", "line_len", "cable_len", "total_investment","file_info")


class PMPrjFeasibilityAdmin(admin.ModelAdmin):
    list_display = ("prj", "info")


class PMPrjPreFirstFoundedAdmin(admin.ModelAdmin):
    list_display = ("prj", "info")


class PMPrjFirstFoundedAdmin(admin.ModelAdmin):
    list_display = ("prj", "info")


# admin.site.register(PMYears, PMYearsAdmin)
# admin.site.register(PMAreas, PMAreasAdmin)
# admin.site.register(PMCountys, PMCountysAdmin)
admin.site.register(PMProjects, PMProjectsAdmin)
admin.site.register(PMPrjPreFeasibility, PMPrjPreFeasibilityAdmin)
admin.site.register(PMPrjFeasibility, PMPrjFeasibilityAdmin)
admin.site.register(PMPrjPreFirstFounded, PMPrjPreFirstFoundedAdmin)
admin.site.register(PMPrjFirstFounded, PMPrjFirstFoundedAdmin)