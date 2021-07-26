//Wie alt bin ich in Jahre nicht genau

var Geburtsjahr = prompt("Wie ist Ihr Geburtsjahr?");
var Aktuellesdatum = new Date();
var Aktuellesjahr = Aktuellesdatum.getFullYear();
var Alter = Aktuellesjahr - Geburtsjahr;


alert("Du bist aktuell " + Alter + " Jahre alt!");
