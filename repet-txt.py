
# vamos digitar uma string e um nuero inteiro como entrada, 
# depois retornar a string repetida o numero de vezes informado
#

def repetir_com_for(texto, vezes):
  """
  Repete a string 'texto' 'vezes' vezes usando um laço for.

  Argumentos:
    texto: A string a ser repetida.
    vezes: O número de vezes que a string deve ser repetida.

  Retorno:
    A string repetida 'vezes' vezes.
  """
  string_repetida = ""
  for i in range(vezes):
    string_repetida += texto
  return string_repetida

# Exemplo de uso
texto = input("Digite a string: ")
vezes = int(input("Digite o número de repetições: "))

string_final = repetir_com_for(texto, vezes)
print(f"String repetida: {string_final}")
