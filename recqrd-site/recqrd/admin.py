from django.contrib import admin
from recqrd.models import User
from recqrd.models import Building
from recqrd.models import Type
from recqrd.models import Item
from recqrd.models import Comment
from recqrd.models import Attachment
from recqrd.models import DescNode

admin.site.register( User )
admin.site.register( Building )
admin.site.register( Type )
admin.site.register( Item )
admin.site.register( Comment )
admin.site.register( Attachment )
admin.site.register( DescNode )