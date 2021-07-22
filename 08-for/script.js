var myArray = [500,500,500,500,500];

var erg = 0;

for (var i = 0; i < myArray.length; i++) {
	erg = myArray[i] + erg;
}

alert("Das Ergebnis ist: " + erg)
