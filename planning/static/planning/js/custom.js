function notif_active_admin(){
	document.getElementById('information_content').style.display = 'block';
	document.getElementById('kt_todo_content2').style.display = 'none';
	document.getElementById('kt_todo_content3').style.display = 'none';

	document.getElementById("info_personnel").className = 'kt-widget__item kt-widget__item';
	document.getElementById("notif_personnel").className = 'kt-widget__item kt-widget__item--active';
	document.getElementById('mission').className= 'kt-widget__item kt-widget__item';
}
function info_active_admin(){
	document.getElementById('information_content').style.display = 'none';
	document.getElementById('kt_todo_content2').style.display = 'block';
	document.getElementById('kt_todo_content3').style.display = 'none';
	
	document.getElementById('mission').className= 'kt-widget__item kt-widget__item';
	document.getElementById("info_personnel").className = 'kt-widget__item kt-widget__item--active';
	document.getElementById("notif_personnel").className = 'kt-widget__item kt-widget__item';
}
function mission_active_admin()
{
	document.getElementById('information_content').style.display = 'none';
	document.getElementById('kt_todo_content2').style.display = 'none';
	document.getElementById('kt_todo_content3').style.display = 'block';
	
	document.getElementById('mission').className= 'kt-widget__item kt-widget__item--active';
	document.getElementById("info_personnel").className = 'kt-widget__item kt-widget__item';
	document.getElementById("notif_personnel").className = 'kt-widget__item kt-widget__item';
}

function display_onglet(element)
{
	for(var i = 0; i < document.getElementsByClassName("onglet").length; i++)
	{
		document.getElementsByClassName("onglet")[i].className = "kt-widget__item kt-widget__item onglet";
	}
	for(var i = 0; i < document.getElementsByClassName("onglet_content").length; i++)
	{
		document.getElementsByClassName("onglet_content")[i].style.display = "none";
	}
	document.getElementById(element).className = "kt-widget__item kt-widget__item--active onglet";
	document.getElementById("kt_todo_content_" + element).style.display = "block";
}