###
A wizard like menu flipping that occurs on mobile devices for building objects.
Dependencies:
Knockout
Knockout.validation
 ###
root = exports ? this
root.grow_journal = root.grow_journal ? {}

class WizardPane

  constructor: (name, @type, isRequired)->
    @value = ko.observable()
    @name = ko.observable(name)
    console.log('wizardpane constructor')
    console.log(@name())
    console.log(@)

    @value.subscribe((newValue)=>
      console.log('NewValue: ' + newValue)
    )



class AddWizard

  constructor: (@objectName)->
    @panes = ko.observableArray()
    @name = ko.observable()

  addPane: (name, type, isRequired) =>
    @panes.push(new WizardPane(name, type, isRequired))
    @panes()[0].value('new')
    console.log(@panes().length)

  selectPaneTemplate: (pane)=>
    console.log(pane.type)
    return pane.type



root.grow_journal.AddWizard = AddWizard
