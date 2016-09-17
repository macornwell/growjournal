from grow_journal.menus import MenuItem, AddModelMenuItem, main_menu
from observations.views import add_observation, add_temperature_reading, add_weather_reading

_CHILD_MENU_ITEMS = (
    ('observations', 'observation', 'Observation', add_observation),
    ('observations', 'temperature', 'Temperature', add_temperature_reading),
    ('observations', 'weather', 'Weather', add_weather_reading),
)

@main_menu.register
class ObservationsMenu(MenuItem):

    def __init__(self):
        MenuItem.__init__(self, 'observations', 'Observations', AddModelMenuItem.generate_add_model_menu_items(_CHILD_MENU_ITEMS))