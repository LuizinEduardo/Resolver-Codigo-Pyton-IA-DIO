#
# vamos solicitar como entrada dois numeros passados pelo usuario e 
# depois vamos realizar uma operacao simples entre eles que foi passada pelo usuario, 
# que pode ser soma, subtracao, multiplicacao ou divisao
# 

#  1. Pedir os números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# 2. Perguntar a operação
operacao = input("Digite a operação (+, -, *, /): ")

# 3. Calcular o resultado
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = abs(numero1 - numero2)
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida!")
    # Aqui você pode adicionar um tratamento para erros

# 4. Mostrar o resultado
print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")
