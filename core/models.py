from django.db import models


class SiteSettings(models.Model):
    logo = models.TextField()
    favicon = models.TextField()

    last_news_image = models.ImageField(upload_to="site_settings/")
    last_news_description = models.TextField()

    tel_number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=200)

    about_small_title = models.CharField(max_length=100)
    about_big_title = models.CharField(max_length=100)
    about_description = models.TextField()
    about_image = models.ImageField(upload_to="site_settings/")
    about_count_first = models.IntegerField()
    about_count_second = models.IntegerField()
    about_count_third = models.IntegerField()
    about_count_fourth = models.IntegerField()
    about_count_first_title = models.TextField()
    about_count_second_title = models.TextField()
    about_count_third_title = models.TextField()
    about_count_fourth_title = models.TextField()
    our_mission_title = models.CharField(max_length=100)
    our_mission_description = models.TextField()
    our_view_title = models.CharField(max_length=100)
    our_view_description = models.TextField()
    our_values_title = models.CharField(max_length=100)
    our_values_description = models.TextField()

    contact_description = models.TextField()

    class Meta:
        verbose_name = "Ayar"
        verbose_name_plural = "Ayarlar"
    

    def __str__(self):
        return "Ayarlar"
    
    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError("Only one instance of SiteSettings is allowed.")
        return super().save(*args, **kwargs)


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banners/")
    description = models.TextField()

    def __str__(self):
        return self.title_az or self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerler"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.TextField()

    def __str__(self):
        return self.title_az or self.title
    
    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    link = models.URLField()

    def __str__(self):
        return self.title_az or self.title
    
    class Meta:
        verbose_name = "Layihə"
        verbose_name_plural = "Layihələr"


class CustomerReview(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField()
    image = models.ImageField(upload_to="reviews/")
    star_rating = models.IntegerField()

    def __str__(self):
        return self.title_az or self.title

    class Meta:
        verbose_name = "Müştəri Rəyi"
        verbose_name_plural = "Müştəri Rəyleri"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blogs/")
    blog_type = models.CharField(max_length=100)
    view_count = models.IntegerField()
    blog_date = models.DateField()

    def __str__(self):
        return self.title_az or self.title
    
    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    date=models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Əlaqə"
        verbose_name_plural = "Əlaqələr"

class SocialMedia(models.Model):
    title = models.TextField()
    icon = models.TextField()

    def __str__(self):
        return self.title_az or self.title
    
    class Meta:
        verbose_name = "Sosial Media"
        verbose_name_plural = "Sosial Medialar"
