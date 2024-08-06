class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Plano Inválido!')   
    

    
cliente = Cliente('Frederico de La Fuente', 'fredlafuente@gmail.com', 'basic')
print(cliente.nome)