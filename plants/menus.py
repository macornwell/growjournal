from farm_log.menus import MenuItem, AddModelMenuItem, main_menu
from plants.views import add_harvest, add_watering, add_productivity, add_bloom

_CHILD_MENU_ITEMS = (
    ('plants', 'harvest', 'Harvest', add_harvest),
    ('plants', 'watering', 'Watering', add_watering),
    ('plants', 'plant-productivity', 'Productivity', add_productivity),
    ('plants', 'bloom', 'Bloom', add_bloom)
)

class PlantsMenu(MenuItem):

    def __init__(self):
        MenuItem.__init__(self, 'plants', 'Plants', AddModelMenuItem.generate_add_model_menu_items(_CHILD_MENU_ITEMS))
