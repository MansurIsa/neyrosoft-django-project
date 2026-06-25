from modeltranslation.translator import register, TranslationOptions
from .models import (
    SiteSettings,
    Banner,
    Service,
    Project,
    CustomerReview,
    Blog,
    SocialMedia
)


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = (
        'last_news_description',
        'location',
        'about_small_title',
        'about_big_title',
        'about_description',
        'about_count_first_title',
        'about_count_second_title',
        'about_count_third_title',
        'about_count_fourth_title',
        'our_mission_title',
        'our_mission_description',
        'our_view_title',
        'our_view_description',
        'our_values_title',
        'our_values_description',
        'contact_description',
    )


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CustomerReview)
class CustomerReviewTranslationOptions(TranslationOptions):
    fields = ('title', 'review')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'blog_type')


@register(SocialMedia)
class SocialMediaTranslationOptions(TranslationOptions):
    fields = ('title',)