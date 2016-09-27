
class WizardForm:
    form_title = None
    model = None
    steps = []

    def apply_instance(self, instance):
        raise NotImplemented()


class WizardStep:
    name = ''
    legend = ''
    form_controls = []
    scripts = []

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)