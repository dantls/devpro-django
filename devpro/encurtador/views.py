from django.http import HttpResponse
from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect
from devpro.encurtador.models import UrlLog

def redirecionar(requisicao, slug):
    #return HttpResponse(f'Olá Django: {slug}')
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origem = requisicao.META.get('TTP_REFERER'),
        user_agent = requisicao.META.get('HTTP_USER_AGENT'),
        host = requisicao.META.get('HTTP_HOST'),
        ip = requisicao.META.get('HTTP_ADDR'),
        url_redirect = url_redirect
    )
    return redirect(url_redirect.destino)

def relatorios(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')
    contexto = {
        'reduce': url_redirect,
        'url_reduzida':url_reduzida
    }
    return render(requisicao, 'encurtador/relatorio.html', contexto)