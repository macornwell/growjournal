from django.core.urlresolvers import reverse
from django.shortcuts import render

WIZARD_FORM_TEMPLATE = 'wizard/wizard-form.html'


class ListEntry:
    edit_url = None
    model = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class CRUDView:
    model_type = None
    form_type = None
    singular = None
    plural = None
    list_model_template_path = None
    list_template_path = None

    def get_back_list_url(self):
        return None

    def get_id(self, model):
        raise NotImplemented('get_id')

    def get_model(self, modelID):
        raise NotImplemented('get_model')

    def post(self, request, model=None):
        raise NotImplemented('post')

    def get_edit_url(self):
        return 'edit_{0}'.format(self.singular.lower()).replace(' ', '_')

    def get_list_url(self):
        return self.plural.lower().replace(' ', '_')

    def get_add_url(self):
        return 'add_{0}'.format(self.singular.lower()).replace(' ', '_')

    def create_form(self, request):
        return self.form_type()

    def get_list_of_models(self, request):
        return self.model_type.objects.all()

    def list(self, request):
        entries = []
        for model in self.get_list_of_models(request):
            entries.append(ListEntry(model=model, edit_url=reverse(self.get_edit_url(), kwargs={'modelID': self.get_id(model)})))
        backUrl = self.get_back_list_url()
        if not backUrl:
            backUrl = reverse('home')
        return self.list_model_view(request, self.plural, reverse(self.get_add_url()), self.singular, self.plural, entries, backButtonUrl=backUrl)

    def list_model_view(self, request, title, addUrl, singularName, pluralName, listEntries, backButtonUrl=None):
        data = {
        'title': title,
        'add_url': addUrl,
        'singular_name': singularName,
        'plural_name': pluralName,
        'list_entries': listEntries,
        'model_template_path': self.list_model_template_path,
        'back_button_url': self._get_back_url(backButtonUrl),
        }
        if not self.list_template_path:
            return render(request, 'wizard_crud/model-list.html', data)
        else:
            return render(request, self.list_template_path, data)

    def add(self, request):
        data = {}
        if request.POST:
            return self.post(request)
        form = self.create_form(request)
        data['form'] = form
        return render(request, WIZARD_FORM_TEMPLATE, data)

    def edit(self, request, modelID):
        data = {}
        model = self.get_model(modelID)
        if request.POST:
            if 'delete-button' in request.POST:
                return self.delete(request, model)
            return self.post(request, model)
        form = self.create_form(request)
        form.apply_instance(model)
        data['form'] = form
        data['is_editing_model'] = True
        return render(request, WIZARD_FORM_TEMPLATE, data)

    def delete(self, request, model):
        model.delete()
        return self.list(request)

    def _get_back_url(self, url):
        return "window.location.href = '{0}'".format(url)
