
<!-- Para gerar o requirements.txt -->
<!-- pip freeze > requirements.txt -->

<!-- Credenciais /admin -->
<!-- admin -> admin2024 -->

# Chat Zé

Este projeto realiza tarefas de sumarização, tradução e produção de código de acordo com as intruções/entradas do usuário. Ao compila-lo gera um site com rotas:

  - /
  - /resumo
  - /traducao
  - /gerar_codigo
  
reponsáveis cada uma por uma função, respectivamente exibir menu, resumir texto, traduzir texto e gerar código requisitado.

## Instalar todas dependências
Com [python](https://www.python.org/downloads/) instalado execute:

```
pip install -r requirements.txt
```

## Inicializar projeto
Entre na pasta do projeto 'chat_ze' e execute o 'runserver'.
```
cd Code/chat_ze
py manage.py runserver [[IP]:[PORT]]
```

Exemplo:
```
  py manage.py runserver 8080
```
```
  py manage.py runserver localhost
```
```
  py manage.py runserver localhost:8080
```



