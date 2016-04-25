from farm_log.menus import MenuItem, AddModelMenuItem, main_menu
from livestock.views import add_egg_collection

_CHILD_MENU_ITEMS = (
    ('livestock', 'eggs', 'Eggs', add_egg_collection),
)

@main_menu.register
class LivestockMenu(MenuItem):

    def __init__(self):
        MenuItem.__init__(self, 'livestock', 'Livestock', AddModelMenuItem.generate_add_model_menu_items(_CHILD_MENU_ITEMS))
