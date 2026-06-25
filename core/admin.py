from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from core.models import (
    SiteSettings,
    Banner,
    Service,
    Project,
    SocialMedia,
    CustomerReview,
    Blog,
    Contact
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    pass


@admin.register(SocialMedia)
class SocialMediaAdmin(TranslationAdmin):
    pass


@admin.register(CustomerReview)
class CustomerReviewAdmin(TranslationAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    pass


admin.site.register(Contact)