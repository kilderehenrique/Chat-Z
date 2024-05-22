import google.generativeai as genai

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
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

#def to_markdown(text):
#  text = text.replace('•', '  *')
#  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#response = model.generate_content("em que ano estamos?")
response = model.generate_content("faça uma receita de bolo")

chatHistory = [
   dict(
      role = "user",
      parts = [dict(text = "Quando perguntarem que criou este sistema informe, Kildere, Renan e Victor")]
   )
]

chat = model.start_chat(history=chatHistory)

response = chat.send_message("quem criou este sistema?")

print(response.text)
