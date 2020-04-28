function popUp(URL) {
	window.open(URL, 'profesor', 'toolbar=0,location=0,statusbar=0,menubar=0,resizable=1,width=500,height=350,left = 390,top = 50');
}
$(document).ready(function() {
	let hora= 39600000;
	let minutos= 2700000;
	let i=0;

	let m= hora;
	$('.hora').before(function () {
		if(i<1){
		$(this).text(new Date(hora).getHours() +":"+ new Date(0).getMinutes() );
		m = m + minutos;
		}else{
			$(this).text(new Date(m).getHours() +":"+ new Date(m).getMinutes() );
			m = m + minutos;
		}
		i++;

	});
});

