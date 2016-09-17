// Generated by CoffeeScript 1.10.0
(function() {
  var Genus, Kingdom, LifeForm, LifeFormSelector, Species, ref, root,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  root = typeof exports !== "undefined" && exports !== null ? exports : this;

  root.grow_journal = (ref = root.grow_journal) != null ? ref : {};

  Kingdom = (function() {
    function Kingdom(id1, name1) {
      this.id = id1;
      this.name = name1;
    }

    return Kingdom;

  })();

  Genus = (function() {
    function Genus(id1, kingdom, name1) {
      this.id = id1;
      this.kingdom = kingdom;
      this.name = name1;
    }

    return Genus;

  })();

  Species = (function() {
    function Species(id1, kingdom, genus1, name1) {
      this.id = id1;
      this.kingdom = kingdom;
      this.genus = genus1;
      this.name = name1;
    }

    return Species;

  })();

  LifeForm = (function() {
    function LifeForm(id1, kingdom, genus1, name1) {
      this.id = id1;
      this.kingdom = kingdom;
      this.genus = genus1;
      this.name = name1;
    }

    return LifeForm;

  })();

  LifeFormSelector = (function() {
    function LifeFormSelector(__easyData) {
      this.__easyData = __easyData;
      this._onSelectedKingdom = bind(this._onSelectedKingdom, this);
      this._resetData = bind(this._resetData, this);
      this.addKingdom = bind(this.addKingdom, this);
      this.kingdoms = ko.observableArray();
      this.selectedKingdom = ko.observable();
      this.availableGenus = ko.observableArray();
      this.selectedGenus = ko.observable();
      this.availableSpecies = ko.observableArray();
      this.selectedSpecies = ko.observable();
      this.availableVarieties = ko.observableArray();
      this.selectedVariety = ko.observable();
      this.selectedKingdom.subscribe(_onSelectedKingdom);
    }

    LifeFormSelector.prototype.addKingdom = function(id, name) {
      return this.kingdomChoices.push(new Kingdom(id, name));
    };

    LifeFormSelector.prototype._resetData = function(genus, species, variety) {
      if (genus) {
        this.availableGenus = ko.observableArray();
        this.selectedGenus = ko.observable();
      }
      if (species) {
        this.availableSpecies = ko.observableArray();
        this.selectedSpecies = ko.observable();
      }
      if (variety) {
        this.availableVarieties = ko.observableArray();
        return this.selectedVariety = ko.observable();
      }
    };

    LifeFormSelector.prototype._onSelectedKingdom = function(kingdomSelected) {
      var id, name;
      id = kingdomSelected.id;
      name = kingdomSelected.name;
      this._resetData(true, true, true);
      if (id) {
        return "";
      }
    };

    return LifeFormSelector;

  })();

  root.grow_journal.LifeFormSelector = LifeFormSelector;

}).call(this);

//# sourceMappingURL=LifeFormSelector.js.map