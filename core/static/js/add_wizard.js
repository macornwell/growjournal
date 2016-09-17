// Generated by CoffeeScript 1.10.0

/*
A wizard like menu flipping that occurs on mobile devices for building objects.
Dependencies:
Knockout
Knockout.validation
 */

(function() {
  var AddWizard, WizardPane, ref, root,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  root = typeof exports !== "undefined" && exports !== null ? exports : this;

  root.grow_journal = (ref = root.grow_journal) != null ? ref : {};

  WizardPane = (function() {
    function WizardPane(name, type1, isRequired) {
      this.type = type1;
      this.value = ko.observable();
      this.name = ko.observable(name);
      console.log('wizardpane constructor');
      console.log(this.name());
      console.log(this);
      this.value.subscribe((function(_this) {
        return function(newValue) {
          return console.log('NewValue: ' + newValue);
        };
      })(this));
    }

    return WizardPane;

  })();

  AddWizard = (function() {
    function AddWizard(objectName) {
      this.objectName = objectName;
      this.selectPaneTemplate = bind(this.selectPaneTemplate, this);
      this.addPane = bind(this.addPane, this);
      this.panes = ko.observableArray();
      this.name = ko.observable();
    }

    AddWizard.prototype.addPane = function(name, type, isRequired) {
      this.panes.push(new WizardPane(name, type, isRequired));
      this.panes()[0].value('new');
      return console.log(this.panes().length);
    };

    AddWizard.prototype.selectPaneTemplate = function(pane) {
      console.log(pane.type);
      return pane.type;
    };

    return AddWizard;

  })();

  root.grow_journal.AddWizard = AddWizard;

}).call(this);

//# sourceMappingURL=add_wizard.js.map
