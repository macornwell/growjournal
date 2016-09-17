root = exports ? this
root.grow_journal = root.grow_journal ? {}



class ObservationType
  constructor: (@id, @name, @kingdom)->


class AddObservation
  constructor: ()->
    @lifeFormSelector = new LifeFormSelector()
    @kingdomChoices = ko.observableArray()
    @selectedKingdom = ko.observable()

  add_kingdom: (id, name)=>
    @kingdomChoices.push(new Kingdom(id, name))





root.grow_journal.AddObservation = AddObservation