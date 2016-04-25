

class SpeciesOrCultivarMixin:
    """
    A mixin that allows easy seemless access for a class that may or may not
    have a cultivar or a species. The intent is to better blend the two.
    """

    def get_plant(self):
        if self.cultivar:
            return self.cultivar
        if self.species:
            return self.species
        raise ValueError('No name can be found.')

    def get_name(self):
        return self.get_plant().name

