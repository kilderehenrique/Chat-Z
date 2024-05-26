from django.shortcuts import render
from .services import gemini_impl as gnai

def home(request):
   return render(request, 'home.html')

def resumo(request):
   texto = request.POST.get("inputChat")

   if(texto != None):
      response = {
         #'resumo': textToHTML(gnai.resumir(texto))
         'resumo': gnai.resumir(texto)
      }
   else:
      response = {}

   return render(request, 'resumo.html', response)

def traducao(request):
   texto = request.POST.get("inputChat")

   if(texto != None):
      response = {
         #'traducao': textToHTML(gnai.traduzir(texto))
         'traducao': gnai.traduzir(texto)
      }
   else:
      response = {}

   return render(request, 'traducao.html', response)

def gerar_codigo(request):
   texto = request.POST.get("inputChat")

   if(texto != None):
      response = {
         #'codigo': textToHTML(gnai.gerar_codigo(texto))
         #'codigo': f"<code>{gnai.gerar_codigo(texto)}</code>"
         'codigo': gnai.gerar_codigo(texto)
      }
   else:
      response = {}

   return render(request, 'gerar_codigo.html', response)

"""
def textToHTML(texto):
   texto = f"<p>{texto}"
   texto = texto.replace(".", ".</p><p>")
   texto = f"{texto}</p>"

   return texto
"""