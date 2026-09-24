from cryptography.fernet import Fernet

chave = open("chave.key", "rb").read()            
arquivo = open("arquivo_criptografado.txt", "rb").read()
arquivo = Fernet(chave).decrypt(arquivo)
open("arquivo_restaurado.txt", "mb").write(arquivo)
print("Arquivo Restaurado!")
