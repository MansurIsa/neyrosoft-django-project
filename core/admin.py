from django.contrib import admin

from core.models import SiteSettings, Banner, Service, Project, SocialMedia,CustomerReview, Blog, Contact


admin.site.register(SiteSettings)
admin.site.register(Banner)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(SocialMedia)
admin.site.register(CustomerReview)
admin.site.register(Blog)
admin.site.register(Contact)
