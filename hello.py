#!usr/bin/env python3
"""Hello world Multi Línguas.

Este programa mostra uma saudação diferente dependendo do idioma configurado na variável de ambiente LANG.

Como usar:

1. Configure a variável LANG:
   -No PwoerShell (windows): $Env:LANG="pt_Br"
   -No Git Bash/Linux: export LANG=pt_Br

2. Execute com: python hello.py
"""

__version__ = "0.01"
__author__ = "Kelcily Lessa"
__license__ = "Unlicense"

import os

# Pegando a linguaguem do sistema
current_languagem = os.getenv("LANG", "en_Us")[:5]

# Mensagem padrão
msg= "Hello World!"

# Mudando a mensagem com base no idioma
if current_languagem == "pt_BR":
   msg = "Olá, Mundo!"
elif current_languagem == "it_IT":
  msg = "Ciao, Mondo!"
elif current_languagem == "fr_FR":
  msg= "Bonjour,Monde!"

# Mostrando no terminal
print (msg)