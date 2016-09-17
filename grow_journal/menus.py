from django.core.urlresolvers import reverse

class MainMenu:

    def __init__(self):
        self._items = []

    def register(self, menu_item_class):
        self._items.append(menu_item_class())

    def iterate_menu_items(self):
        return (i for i in self._items)






class MenuItem:

    def __init__(self, app, name, friendlyName, childrenItems, url_prefix=None, view=None):
        self.__urlPrefix = url_prefix
        self.__app = app
        self.__name = name
        self.__view = view
        self.__friendlyName = friendlyName
        self.__childrenItems = childrenItems


    def get_url_name(self):
        if self.__urlPrefix:
            return '{0}_{1}'.format(self.__urlPrefix, self.__name)
        return None

    def get_url(self):
        return reverse(self.get_url_name())
        """
        prefix = self.__urlPrefix or ''
        if prefix:
            prefix += '/'
        return '^{0}{0}/{1}'.format(prefix, self.__app, self.__name)
        """


    def get_name(self):
        """
        A name for using programatically. This must be unique
        :return:
        """
        return self.__name


    def get_friendly_name(self):
        """
        The name that the user will see on the main Menu
        :return:
        """
        return self.__friendlyName

    def get_children_menu_items(self):
        """
        Gets the children menu items that fall under this menu. (Of type MenuItem)
        :return:
        """
        return self.__childrenItems


class AddModelMenuItem(MenuItem):

    def __init__(self, app, name, friendlyName, view):
        MenuItem.__init__(app, name, friendlyName, [], 'add', view=view)

    @staticmethod
    def generate_add_model_menu_items(iterable):
        for i in iterable:
            yield AddModelMenuItem(i[0], i[1], i[2], i[3])

"""
The actual main menu global instance.
"""
main_menu = MainMenu()
