#
# vamos receber dois dados diferentes do usuario e concatenar em uma unica string
# Gemini indicou usando .join e pra versao 3.6 usar f-string
# 
"""
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = " ".join([nome, sobrenome])

print("Nome completo:", nome_completo)

"""
# -----------------------------------------------

nome = input("Digite seu nome: ").title() # usado para colocar inicial maiuscula
sobrenome = input("Digite seu sobrenome: ").upper() # usado para colocar tudo maiuscula 

nome_completo = f"{nome} {sobrenome}"

print("Nome completo:", nome_completo)
