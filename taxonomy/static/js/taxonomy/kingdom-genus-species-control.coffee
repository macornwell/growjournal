root = exports ? this
root.grow_journal = root.grow_journal ? {}


class KingdomGenusSpeciesControl

  constructor: (@dataLayer)->
    @kingdomList = ko.observableArray(@dataLayer.getKingdomList())
    @selectedKingdom = ko.observable()

    @genusList = ko.observableArray()
    @selectedGenus = ko.observable()

    @speciesList = ko.observableArray()
    @selectedSpecies = ko.observable()

    @selectedKingdom.subscribe((kingdomID)=>
      @genusList.removeAll()
      @speciesList.removeAll()
      for entry in @dataLayer.getGenusList(kingdomID)
        @genusList.push(entry)
    )

    @selectedGenus.subscribe((genusID)=>
      @speciesList.removeAll()
      for entry in @dataLayer.getSpeciesList(genusID)
        @speciesList.push(entry)
    )



root.grow_journal.KingdomGenusSpeciesControl = KingdomGenusSpeciesControl