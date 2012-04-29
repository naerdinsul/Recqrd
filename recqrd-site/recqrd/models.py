from django.db import models

class User( models.Model ):
	login_name = models.CharField( max_length = 200 )
	first_name = models.CharField( max_length = 200 )
	last_name  = models.CharField( max_length = 200 )
	password   = models.CharField( max_length = 20 )
	
	def __unicode__( self ):
		return u'%s %s' % (self.first_name, self.last_name)

class Building( models.Model ):
	description = models.CharField( max_length = 200 )
	
	def __unicode__( self ):
		return u'%s' % self.description
		
class Type( models.Model ):
	description = models.CharField( max_length = 200 )
	
	def __unicode__( self ):
		return u'%s' % self.description

class Item( models.Model ):
	qrcode      = models.CharField( max_length = 5 )
	description = models.CharField( max_length = 200 )
	building    = models.ForeignKey( Building )
	room        = models.CharField( max_length = 200 )
	type        = models.ForeignKey( Type )

	def __unicode__( self ):
		return u'%s' % self.description
		
class Comment( models.Model ):
	item    = models.ForeignKey( Item )
	user    = models.ForeignKey( User )
	date    = models.DateField()
	comment = models.CharField( max_length = 500 )

class Attachment( models.Model ):
	item = models.ForeignKey( Item )
	description = models.CharField( max_length = 200 )
	filehash = models.CharField( max_length = 200 )

# Modified Pre-order Traversal Tree
# to store what information should
# be displayed for what types
class DescNode( models.Model ):
	description = models.CharField( max_length = 200 )
	fieldtype = models.CharField( max_length = 200 )
	parent = models.ForeignKey( 'self', blank = True, null = True )
	lftidx = models.IntegerField()
	rgtidx = models.IntegerField()
	
	def __unicode__( self ):
		return u'%s' % self.description