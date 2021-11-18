code = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

msgEncrypt = input("Digite a mensagem encripitada separando os numeros com espaço: ").split("")
msgDecrypt = []

for num in msgEncrypt:
  num = int(num)
  msgDecrypt.append(code[num])


print(msgDecrypt)