from django.shortcuts import render_to_response , RequestContext

def my_view(request):
    return render_to_response('demo.html', locals(), context_instance = RequestContext(request))

