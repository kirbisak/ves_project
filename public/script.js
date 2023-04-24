// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {
	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	// this reprezentuje ten formular, ktory odosielame
	const ves = this.querySelector("textarea").value; // Načítame text z textarea
	const width = document.querySelector("section:nth-child(2)").clientWidth; // Načítame aktuálnu šírku výstupného okna

	const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
	formular.append('ves', ves); // Pridáme tam naše hodnoty
	formular.append('width', width);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob()) // Dostali sme binárne dáta (blob)
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image); // Nastavíme src našeho <img> na načítaný obrázok
		})
}
document.querySelector("form").addEventListener("submit", handleSubmit); // Nastavíme formulár, aby pri submit udalosti spustil našu handleSubmit funkciu

function clearbutton() {
	document.getElementById("text").value='';
	document.getElementById("output").style.visibility='none';
	}

function kirbisak() {
	document.getElementById("text").value="VES v1.8 600 600\nCLEAR #FFFFFF\nFILL_CIRCLE 300 300 200 #3b3f45\nFILL_RECT 50 50 500 250 #FFFFFF\nCIRCLE 300 300 200 2 #2c3036\nFILL_TRIANGLE 400 300 480 300 440 350 #92969c\nFILL_TRIANGLE 350 300 430 300 390 400 #92969c\nFILL_TRIANGLE 300 300 390 300 345 370 #92969c\nFILL_CIRCLE 250 400 50 #FFFFFF\nFILL_CIRCLE 270 370 55 #3b3f45\nFILL_CIRCLE 190 390 5 #9c9c0e\nFILL_CIRCLE 400 400 2 #9c9c0e\nFILL_CIRCLE 370 400 2 #9c9c0e\nFILL_CIRCLE 420 390 2 #9c9c0e\nFILL_CIRCLE 390 410 2 #9c9c0e\nFILL_CIRCLE 300 340 3 #9c9c0e\nFILL_CIRCLE 380 370 2 #9c9c0e\nFILL_CIRCLE 290 480 4 #9c9c0e\nFILL_CIRCLE 340 435 2 #9c9c0e\nFILL_CIRCLE 200 320 2 #9c9c0e\nFILL_CIRCLE 180 340 2 #9c9c0e\nFILL_CIRCLE 150 350 3 #9c9c0e\nFILL_CIRCLE 220 180 10 #000000\nFILL_CIRCLE 210 180 10 #000000\nFILL_CIRCLE 210 188 14 #FFFFFF\nFILL_CIRCLE 220 188 14 #FFFFFF\nFILL_CIRCLE 200 200 10 #000000\nFILL_CIRCLE 190 200 10 #000000\nFILL_CIRCLE 190 208 14 #FFFFFF\nFILL_CIRCLE 200 208 14 #FFFFFF\nFILL_CIRCLE 350 200 50 #92969c\nFILL_RECT 270 295 5 5 #542d03\nFILL_TRIANGLE 265 295 280 295 273 280 #0e9c28\nFILL_TRIANGLE 265 285 280 285 273 265 #0e9c28\nFILL_TRIANGLE 265 275 280 275 273 255 #0e9c28\nFILL_TRIANGLE 265 265 280 265 273 240 #0e9c28\nFILL_TRIANGLE 265 255 280 255 273 225 #0e9c28\nFILL_RECT 220 297 5 3 #542d03\nFILL_TRIANGLE 215 255 230 255 223 230 #0e9c28\nFILL_TRIANGLE 215 235 230 235 223 210 #0e9c28\nFILL_TRIANGLE 215 215 230 215 223 190 #0e9c28\nFILL_TRIANGLE 215 275 230 275 223 250 #0e9c28\nFILL_TRIANGLE 215 295 230 295 223 270 #0e9c28\nFILL_RECT 150 280 20 20 #542d03\nFILL_TRIANGLE 145 280 175 280 160 275 #542d03\nFILL_RECT 180 270 5 30 #542d03\nFILL_TRIANGLE 175 270 190 270 183 255 #0e9c28\nFILL_TRIANGLE 175 260 190 260 183 245 #0e9c28\nFILL_TRIANGLE 175 250 190 250 183 235 #0e9c28\nFILL_TRIANGLE 175 240 190 240 183 225 #0e9c28"
	}

function samv() {
	document.getElementById("text").value="VES v2.1 600 400\nCLEAR #736f6f\nFILL_RECT 250 200 100 100 #e0781d\nFILL_TRIANGLE 250 200 250 299 150 299 #e0781d\nFILL_TRIANGLE 350 200 350 299 450 299 #e0781d\nFILL_TRIANGLE 150 299 180 299 180 269 #000000\nFILL_TRIANGLE 450 299 420 299 420 269 #000000\nFILL_TRIANGLE 350 200 350 150 420 150 #e0781d\nFILL_TRIANGLE 420 150 400 150 420 180 #ffffff\nFILL_RECT 130 150 100 50 #e0781d\nFILL_TRIANGLE 150 200 210 200 180 230 #e0781d\nFILL_CIRCLE 180 230 10 #000000\nFILL_TRIANGLE 130 150 160 150 130 120 #e0781d\nFILL_TRIANGLE 229 150 199 150 229 120 #e0781d\nFILL_TRIANGLE 140 170 160 170 160 190 #000000\nFILL_TRIANGLE 219 170 199 170 199 190 #000000\nFILL_CIRCLE 130 120 5 #ffffff\nFILL_CIRCLE 229 120 5 #ffffff"
}
function zoro() {
	document.getElementById("text").value="VES v1.0 600 400\nCLEAR #666666\nLINE 0 0 0 400 10 #000000\nLINE 0 0 600 0 10 #000000\nLINE 600 0 600 400 10 #000000\nLINE 600 400 0 400 10 #000000\nFILL_RECT 100 200 400 100 #bf1717\nFILL_CIRCLE 200 300 40 #000000\nFILL_CIRCLE 400 300 40 #000000\nFILL_RECT 200 125 175 76 #bf1717\nFILL_TRIANGLE 200 200 200 125 150 200 #bf1717\nFILL_TRIANGLE 375 125 375 200 450 200 #bf1717\nFILL_TRIANGLE 500 250 510 230 510 270 #bf1717\nFILL_RECT 310 130 60 65 #31a1b5\nFILL_TRIANGLE 370 130 370 194 435 195 #31a1b5\nFILL_RECT 205 130 80 65 #31a1b5\nFILL_TRIANGLE 205 130 205 194 165 195 #31a1b5"
}

// dropdown menu
function myFunction() {
		document.getElementById("myDropdown").classList.toggle("show");
	  }
	  
	  window.onclick = function(event) {
		if (!event.target.matches('.dropbtn')) {
		  var dropdowns = document.getElementsByClassName("dropdown-content");
		  var i;
		  for (i = 0; i < dropdowns.length; i++) {
			var openDropdown = dropdowns[i];
			if (openDropdown.classList.contains('show')) {
			  openDropdown.classList.remove('show');
			}
		  }
		}
	  }