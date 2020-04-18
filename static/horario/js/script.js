function popUp(URL) {
    window.open(URL, 'profesor', 'toolbar=0,location=0,statusbar=0,menubar=0,resizable=1,width=500,height=350,left = 390,top = 50');

}
function Horario(dia, hora, codigo){
	this.dia= dia;
	this.hora= hora;
	this.codigo= codigo;
}
let objetivo = null;
let nombre = "vacio";
let registro = null;
let myjson = null
	$(document).ready(function(){

	$('.objetivo').click(function(event) {
		if (objetivo == null){
			alert("primero debes seleccionar una materia")
		}else {
		let div = $(this);
		let dia = div.attr("id");
		let hora = div.attr("name");
		div.text(nombre);
		if (registro!=null){
			myjson = myjson + ","+ JSON.stringify( registro);
			console.log(myjson);
		}else {
			registro = new Horario(dia, hora, objetivo);
			myjson = JSON.stringify(registro);
			console.log(myjson);
		}
	}
	});

	$('.horas').click(function(event) {
		objetivo = $(this).attr("id");
		nombre = document.getElementById(objetivo).textContent;
	})
});
