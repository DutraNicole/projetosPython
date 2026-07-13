import random
import string

def Gerador_senha_aleatoria(length = 12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = " ".join(random.choice(caracteres) for _ in range(length))
    return senha
    
senha = Gerador_senha_aleatoria()
print("Senha aleatória: ", senha)