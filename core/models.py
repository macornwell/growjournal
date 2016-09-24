from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from core.managers import SiteManager


def get_objects_with_datetime_property_on_given_date(modelClass, date):
    return modelClass.objects.filter(datetime__year=date.year,
                                     datetime__month=date.month,
                                     datetime__day=date.day)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserActivityModel(BaseModel):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True


class Site(BaseUserActivityModel):
    objects = SiteManager()
    site_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    site_users = models.ManyToManyField(User, related_name='user_group', blank=True)
    is_public_viewable = models.BooleanField(default=True)
    is_public_joinable = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def delete(self, using=None):
        self.deleted = True
        self.save()

    def save(self, *args, **kwargs):
        isNew = False
        if not self.site_id:
            isNew = True
        if isNew:
            sites = Site.objects.filter(user=self.user)
            if len(sites) > 4:
                raise ValueError('Currently only five sites allowed.')
        super(BaseUserActivityModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserCoreSettings(BaseModel):
    user = models.OneToOneField(User)
    active_site = models.ForeignKey(Site, blank=True, null=True)


class BaseUserActivityOnSiteModel(BaseModel):
    user = models.ForeignKey(User)
    site = models.ForeignKey(Site)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.user != self.site.user and self.user not in self.site.site_users:
            raise Exception('User is not related to the site.')
        super(BaseModel, self).save(*args, **kwargs)


class Project(BaseUserActivityOnSiteModel):
    project_id = models.AutoField(primary_key=True)
    date_started = models.DateField(default=timezone.now, blank=True, null=True)
    date_ended = models.DateField(blank=True, null=True)
    is_perpetual = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_public_viewable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class WebsiteFeedback(BaseUserActivityModel):
    website_feedback_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(default=timezone.now)
    closed_date = models.DateTimeField(blank=True, null=True)
    feedback = models.TextField()

    def __str__(self):
        return self.feedback