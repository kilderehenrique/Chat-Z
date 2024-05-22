import google.generativeai as genai

# API key garada para uso "Kildere"
GOOGLE_API_KEY = 'AIzaSyAQW-I36q7IC2ZAvTgb6Kfds5v_HZrehuE'

genai.configure(api_key=GOOGLE_API_KEY)

# Listar modelos possiveis
#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

# MODELS
"""
   gemini-1.0-pro
   gemini-1.0-pro-001
   gemini-1.0-pro-latest
   gemini-1.0-pro-vision-latest
   gemini-1.5-flash-latest
   gemini-1.5-pro-latest
   gemini-pro
   gemini-pro-vision
"""

model = genai.GenerativeModel('gemini-1.5-pro-latest')

chatResumir = [
   dict(
      role = "user",
      parts = [dict(text = "Oi, voce poderia me ajudar a resumir um texto?")]
   ),
   dict(
      role = "model",
      parts = [dict(text = "Claro, pode me informar o texto")]
   )
]

chatTraduzir = [
   dict(
      role = "user",
      parts = [dict(text = "Oi, voce poderia me ajudar a traduzir um texto de QUALQUER LINGUA para o PORTUGUÊS DO BRASIL? voce deve me respondesse com um texto corrido e sem explicações")]
   ),
   dict(
      role = "model",
      parts = [dict(text = "Certo, vou responder apenas com um texto corrido e sem explicações.")]
   ),
]

chatGerarCodigo = [
   dict(
      role = "user",
      parts = [dict(text = "Oi, voce poderia gerar um código para mim? gere um texto corrido")]
   ),
   dict(
      role = "model",
      parts = [dict(text = "Claro, gerarei um texto corrido, que tipo de código gostaria que eu gerasse?")]
   )
]

chatInstrucao = [
   dict(
      role = "user",
      parts = [dict(text = "Pode analisar um texto para mim?")]
   ),
   dict(
      role = "model",
      parts = [dict(text = "Claro, posso sim")]
   ),
   dict(
      role = "user",
      parts = [dict(text = "Responda com 'SIM' ou 'NAO'.")]
   ),
   dict(
      role = "model",
      parts = [dict(text = "Ok, responderei apena com 'SIM' ou 'NAO'.")]
   ),
]

AVISOS = {
   'NUMERO_REQUESTS': "Calma ai filhão, nois é pobre! Financia ai que o Chat vira PRO.",
}


def resumir(texto):
   texto = f"Resuma esse texto: '{texto}'"

   chat = model.start_chat(history = chatResumir)

   try:
      response = chat.send_message(texto)
   except:
      return AVISOS["NUMERO_REQUESTS"]

   return response.text

def traduzir(texto):
   texto = f"Traduza esse texto: '{texto}'"

   chat = model.start_chat(history = chatTraduzir)

   try:
      response = chat.send_message(texto)
   except:
      return AVISOS["NUMERO_REQUESTS"]

   return response.text

def gerar_codigo(texto):
   if(isDescricaoCodigo(texto)):
      chat = model.start_chat(history = chatGerarCodigo)

      try:
         response = chat.send_message(texto)
      except:
         return AVISOS["NUMERO_REQUESTS"]

      return response.text
   
   return "Forneça uma descrição do código que deseja gerar por favor!"

def isDescricaoCodigo(texto):
   texto = f"'{texto}'\nEsse texto é uma descrição das funcionalidades de um código ou algoritmo?"
   chat = model.start_chat(history = chatInstrucao)

   try:
      response = chat.send_message(texto)
   except:
      return AVISOS["NUMERO_REQUESTS"]

   return "SIM" in response.text
