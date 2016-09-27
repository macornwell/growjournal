from django_wizard_form.form_controls import SimpleSelectionControl, WizardControl
from core.models import Project

class ProjectSelectionControl(SimpleSelectionControl):

    def fill_projects(self, site):
        projects = Project.objects.get_projects_for_site(site)
        list = [(-1, '---')]
        for p in projects:
            list.append((p.project_id, p.name))
        list = sorted(list, key=lambda x: x[1])
        self.selections = tuple(list)


class HiddenSiteControl(WizardControl):
    template_path = 'core/wizard/hidden-site.html'
