from django.shortcuts import render
from .services import gemini_impl as gnai
from markdown_it import MarkdownIt

# Converte a estrutura de .md para .html
md = MarkdownIt('commonmark', {'breaks':True, 'html':True}).enable('table')

def home(request):
   return render(request, 'home.html')

def resumo(request):
   texto = request.POST.get("inputChat")

   if(texto != None):
      response = {
         'resumo': md.render(gnai.resumir(texto))
      }
   else:
      response = {}

   return render(request, 'resumo.html', response)

def traducao(request):
   texto = request.POST.get("inputChat")

   if(texto != None):
      response = {
         'traducao': md.render(gnai.traduzir(texto))
      }
   else:
      response = {}

   return render(request, 'traducao.html', response)

def gerar_codigo(request):
   texto = request.POST.get("inputChat")

   if(texto != None):
      response = {
         'codigo': md.render(gnai.gerar_codigo(texto))
      }
   else:
      response = {}

   return render(request, 'gerar_codigo.html', response)
