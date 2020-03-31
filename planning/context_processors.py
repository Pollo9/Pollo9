from planning.models import bdd_messages

def notif_total(request):
	msg = bdd_messages.objects.all()
	notif_total = 0

	if request.user.groups.filter(name__in=['Administrateur']).exists():
		for m in msg:
			if m.user == m.consultant:
				if not m.lu:
					notif_total += 1

	elif request.user.groups.filter(name__in=['Consultant']).exists():
		for m in msg:
			if (m.user != m.consultant and m.consultant == request.user):
				if not m.lu:
					notif_total += 1

	return {"notif_total": notif_total}