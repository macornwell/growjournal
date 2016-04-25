###
A wizard like menu flipping that occurs on mobile devices for building objects.
Dependencies:
Knockout
Knockout.validation
 ###
root = exports ? this
root.farm_log = root.farm_log ? {}

_easyData = new farm_log_data.EasyRestData()


class AddWizard

  constructor: (@objectName)->

