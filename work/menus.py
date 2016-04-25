from farm_log.menus import MenuItem, AddModelMenuItem, main_menu
from work.views import add_work_completed


_CHILD_MENU_ITEMS = (
    ('work', 'work', 'Work Completed', add_work_completed),
)

@main_menu.register
class WorkMenu(MenuItem):

    def __init__(self):
        MenuItem.__init__(self, 'work', 'Work', AddModelMenuItem.generate_add_model_menu_items(_CHILD_MENU_ITEMS))

