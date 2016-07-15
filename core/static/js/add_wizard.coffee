###
A wizard like menu flipping that occurs on mobile devices for building objects.
Dependencies:
Knockout
Knockout.validation
 ###
root = exports ? this
root.farm_log = root.farm_log ? {}

_easyData = new farm_log_data.EasyRestData()

class WizardPane

  constructor: (@name, @type, @isRequired)->
    @value = ko.observable()



class AddWizard

  constructor: (@objectName)->
    @panes = ko.observableArray()

    addPane: (name, type, isRequired) =>
      @panes.push(new WizardPane(name, type, isRequired))

    selectPaneTemplate: (type)=>
      return type



root.farm_log.AddWizard = AddWizard
