import django_filters
from job.models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = Job
        fields = ['state','industry','title','job_type']