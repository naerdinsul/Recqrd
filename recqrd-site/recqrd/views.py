from django.http import HttpResponse

def home( request ):
	return HttpResponse( "Home page" )

def item( request, itemid ):
	return HttpResponse( "<meta name='viewport' content='width=320' />Requested item coded: %s" % itemid.upper() )

#def admin( request ):
#	return HttpResponse( "Admin page" )