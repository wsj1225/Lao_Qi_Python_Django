from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.

from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})


class blog_title_c(generic.ListView):
    template_name = 'blog/titles.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogArticles.objects.all()


def blog_article(request, blog_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=blog_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article': article, 'pub': pub})


class blog_article_c(generic.DetailView):
    model = BlogArticles
    template_name = 'blog/content.html'
    context_object_name = 'article'


# Webservice test

from spyne import Application, rpc, ServiceBase, Integer, Iterable, Unicode, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
from lxml import etree


class HelloWorldService(ServiceBase):
    @rpc(String, _returns=String,_out_variable_name='output')
    def OperationA(ctx, input):
        try:
            root=etree.fromstring(input)
        except etree.XMLSyntaxError:
            return '<Response><RetInfo><RetCode>-1</RetCode><RetCon>请检查XML格式</RetCon>' \
                   '</RetInfo></Response>'
        else:
            
            "MQ 操作 "


            
            return '<Response><RetInfo><RetCode>0</RetCode><RetCon>成功</RetCon>' \
                   '</RetInfo></Response>'


application = Application([HelloWorldService],
                          tns='http://esb.ewell.cc',
                          name='TestBinding',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )

hello_app = csrf_exempt(DjangoApplication(application))
