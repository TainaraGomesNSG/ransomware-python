from cryptography.fernet import Fernet

nome_arquivo = "arquivo_teste.txt"

chave = Fernet.generate_key( )

with open("chave.key", "wb") as arquivo:
  arquivo.write(chave)

with open (nome_arquivo, "rb") as arquivo:
  texto = arquivo.read( )

fernet = Fernet(chave)
texto_criptografado = 
fernet.encrypt(texto)

with open ("arquivo_criptografado.txt", "wb") as arquivo:
  arquivo.write(texto_criptografado)

print("Arquivo criptografado com sucesso")
