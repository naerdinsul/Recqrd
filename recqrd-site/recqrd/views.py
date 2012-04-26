from django.http import HttpResponse

def item( request, itemid ):
	return HttpResponse( "Requested item coded: %s" % itemid.upper() )
