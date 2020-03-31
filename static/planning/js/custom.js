function notif_active(switchelement){
	document.getElementById('information_content').style.display = 'block';
	document.getElementById('kt_todo_content').style.display = 'none';
	document.getElementById('kt_todo_content2').style.display = 'none';
	if (switchelement.className != 'kt-widget__item kt-widget__item--active'){
		document.getElementById("info_personnel").className = 'kt-widget__item kt-widget__item';
		document.getElementById("notif_personnel").className = 'kt-widget__item kt-widget__item';
		switchelement.className += "--active";
	}
}

function todolist_active(switchelement){
	document.getElementById('kt_todo_content').style.display = 'block';
	document.getElementById('information_content').style.display = 'none';
	document.getElementById('kt_todo_content2').style.display = 'none';
	if (switchelement.className != 'kt-widget__item kt-widget__item--active'){
		document.getElementById("info_personnel").className = 'kt-widget__item kt-widget__item';
		document.getElementById("todolist_personnel").className = 'kt-widget__item kt-widget__item';
		switchelement.className += "--active";
	}
}

function info_active(switchelement){
	document.getElementById('kt_todo_content').style.display = 'none';
	document.getElementById('information_content').style.display = 'none';
	document.getElementById('kt_todo_content2').style.display = 'block';
	if (switchelement.className != 'kt-widget__item kt-widget__item--active'){
		document.getElementById("notif_personnel").className = 'kt-widget__item kt-widget__item';
		document.getElementById("todolist_personnel").className = 'kt-widget__item kt-widget__item';
		switchelement.className += "--active";
	}
}

function display_filter(){
	if (document.getElementById('more_filter').style.display == 'none'){
		console.log("lol");
		document.getElementById('more_filter').style.display = 'block';
	}else if (document.getElementById('more_filter').style.display == 'block'){
		console.log("lol");
		document.getElementById('more_filter').style.display = 'none';
	}
}

function display_facultatif(switchelement, var_box){
	if (document.getElementById('box_' + var_box).style.backgroundColor != "#a6a6a6"){
		document.getElementById('box_' + var_box).style.backgroundColor = "#a6a6a6" ;
		document.getElementById('text_box_' + var_box).style.color = "#ffffff" ;
		switchelement.style.display = "none";
		document.getElementById("facultatif_box_" + var_box).style.display = "block";
	}
}

function display_pdf(element_name){
	if (document.getElementById('no_element').style.display != 'none'){
		document.getElementById('no_element').style.display = 'none';
		document.getElementById('pdf_' + element_name).style.display = 'block';
	}else{ 
		var inputs = document.getElementsByTagName("iframe");
		for (x = 0 ; x < inputs.length ; x++){
			if (inputs[x].style.display == 'block'){
				inputs[x].style.display = 'none';
			}else if (inputs[x].getAttribute("id") == 'pdf_' + element_name){
				inputs[x].style.display = 'block';
			}
			
		}
	}
}