# Classe mãe
class Animal:
    def falar(self):
        return "O animal faz um som"


class Cachorro(Animal):
    def falar(self):
        return "O cachorro late"


class Gato(Animal):
    def falar(self):
        return "O gato mia"


cachorro = Cachorro()
gato = Gato()

print(cachorro.falar())
print(gato.falar())
