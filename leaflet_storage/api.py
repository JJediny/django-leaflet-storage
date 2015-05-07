from django.conf.urls import url
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from guardian.shortcuts import get_objects_for_user
from taggit.models import Tag

from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.utils import trailing_slash

from .models import Map

class GeoJsonResource(ModelResource):
    class Meta:
        queryset = Map.objects.all()
        resource_name = 'geojson'
        allowed_methods = ['get']

