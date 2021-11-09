from django.views.generic import TemplateView

from .models import Project


class ResumeView(TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # random project in screen
        context['projects'] = Project.objects.all().order_by('?').all()
        return context
