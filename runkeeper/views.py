# Create your views here.

from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

import oauth2 as oauth
import time
import urlparse

from local_settings import *

consumer = oauth.Consumer(client_id, client_secret)
client = oauth.Client(consumer)

def index(request):
	t = loader.get_template('index.html')
	c = RequestContext(request, {})
	return HttpResponse(t.render(c))

def authorize(request):
	## Create the client
	consumer = oauth.Consumer(client_id, client_secret)
	client = oauth.Client(consumer)
	
	params = {
		# 'client_id': client_id,
		# 'response_type': 'code',
		# 'redirect_uri': "http://twitter.com/schbank"
	}
	
	## Make a request
	## client_id, response_type & redirect_uri
	resp, content = client.request(
		authorization_url,
		# "GET",
		client_id,
		"code",
		# "http://twitter.com/schbank",
		redirect_uri,
	)
	print resp
	print content
	return HttpResponse(content)
	
	# if resp['status'] != '200':
	# 	raise Exception("Invalid response %s." % resp['status'])

	# request_token = dict(urlparse.parse_qsl(content))
	# print "Request Token:"
	# print request_token
	# print resp
	# 
	# url = "%s?oauth_token=%s" % (authenticate_url,
	#         request.session['request_token']['oauth_token'])
	# 
	# return HttpResponseRedirect(url)
	
	
	
	
	