# -*- coding: utf-8 -*-
from django.db import models
from django.forms.widgets import TextInput

from phone_application.phone_app.forms import *
from phone_application.phone_app.models import *


	
class MyTypeaheadWidget(TextInput):
    """Wigdet stworzony na potrzebe bootstrap twitter typehead + ladny twitter search"""

    
    def keys_to_string(self,r):
	print "r",r
	l = "["
	for i in xrange(len(r)):
	  #print str(r[i])
	  if i == len(r)-1:	l += u'"%d. %s"'  % (r[i][1], r[i][0])
	  else:			l += u'"%d. %s",' % (r[i][1], r[i][0])
	l += "]"	
	return l
    
    
    def __init__(self, attrs=None):

	keys = self.keys_to_string(list(set([(r.key, r.pk) for r in Product.objects.all()])))

	_attrs = { 'id':"key", 'class':"search-query", 'placeholder':"Search", 'maxlength':"200", 'name':"key", 'type':"text", 'data-provide':'typeahead', 'data-source' : keys, "autocomplete":"off"}

	super(MyTypeaheadWidget, self).__init__(_attrs)

	
