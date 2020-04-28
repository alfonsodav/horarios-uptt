function Horario(dia, hora, codigo){
	this.dia= dia;
	this.hora= hora;
	this.codigo= codigo;
}
let objetivo = null;
let nombre = "vacio";
let registro = null;
let myjson = null;
$(document).ready(function() {

    $('.objetivo').click(function (event) {
        if (objetivo == null) {
            alert("primero debes seleccionar una materia")
        } else {
            let div = $(this);
            let dia = div.attr("id");
            let hora = div.attr("name");
            div.text(nombre);
            if (registro != null) {
                registro = new Horario(dia, hora, nombre);
                myjson = myjson + "," + JSON.stringify(registro);
                console.log(registro);
                $('#id_posicion').text("[" + myjson + "]");
            } else {
                registro = new Horario(dia, hora, nombre);
                myjson = JSON.stringify(registro);
                console.log(myjson);
            }
        }
    });


    $('.horas').click(function (event) {
        objetivo = $(this).attr("id");
        nombre = document.getElementById(objetivo).textContent;
    });
});
