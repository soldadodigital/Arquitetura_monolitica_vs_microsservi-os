# Serviço responsável por validar o usuário
class UserService:
    def validate_user(self, user_id):
        # Retorna True se o user_id não for None (simulação simples de validação)
        return user_id is not None  


# Serviço responsável por gerenciar pedidos
class OrderService:
    def __init__(self, user_service):
        # Recebe uma instância de UserService (injeção de dependência)
        self.user_service = user_service

    def confirm_order(self, user_id, product_id):
        # Valida o usuário antes de confirmar o pedido
        if not self.user_service.validate_user(user_id):
            return "Usuário inválido!"

        # Se válido, confirma o pedido
        print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado.")
        return "Pedido confirmado com sucesso!"


# Instanciando o serviço de usuário
user_service = UserService()

# Instanciando o serviço de pedido, passando o user_service como dependência
order_service = OrderService(user_service)

# Executando um exemplo de confirmação de pedido
resultado = order_service.confirm_order(1, 101)

# Exibindo o resultado
print(resultado)


# Função simples para processar pedido (sem usar classes)
def process_order(user_id, product_id, payment_info):
    # Verifica se todos os dados foram fornecidos
    if not (user_id and product_id and payment_info):
        return "Dados inválidos!"

    # Confirma o pedido diretamente
    print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado.")
    return "Pedido confirmado com sucesso!"


# Executando exemplo da função simples
resultado = process_order(1, 101, "cartao_credito")

# Exibindo o resultado
print(resultado)
