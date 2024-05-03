from xhtml2pdf import pisa 
from io import BytesIO # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import RequestContext
from django.conf import settings
import io as StringIO
import cgi
import os




    

def render_to_pdf(template_src, context_dict={}):
   
    template = get_template(template_src)
    html  = template.render(context_dict)
    #result = StringIO.StringIO()
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, link_callback=fetch_resources )
    #pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='apps/pdf')
    return HttpResponse('Gremlins ate your pdf! %s' % cgi.escape(html))


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path

'''

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    now = datetime.now()
    filename = now.strftime('%Y-%m-%d') + '.pdf'
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),result, path=path)

    if not pdf.err:
      response = HttpResponse(result.getvalue(), mimetype='application/pdf')
      response['Content-Disposition'] = 'attachment; filename="'+filename+'"'
      return response
   return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def get_full_path_x(request):
    full_path = ('http', ('', 's')[request.is_secure()], '://',
    request.META['HTTP_HOST'], request.path)
    return ''.join(full_path) 

    html = template.render(context) 
'''