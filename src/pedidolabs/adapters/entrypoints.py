"""
Adaptadores de entrada para PedidoLab.
Permiten recibir pedidos mediante una API REST (simulada) y procesos batch.
"""

class RestPedidoAdapter:
    """Adaptador para simular una entrada REST."""

    def __init__(self, servicio_pedidos):
        self._servicio_pedidos = servicio_pedidos

    def recibir_pedido(self, data_json_simulado: dict):
        """Traduce la entrada externa y la envía al servicio de aplicación."""
        return self._servicio_pedidos.procesar(data_json_simulado)


class BatchPedidoAdapter:
    """Adaptador para procesar lotes de pedidos nocturnos."""

    def __init__(self, servicio_pedidos):
        self._servicio_pedidos = servicio_pedidos

    def procesar_lote(self, lista_pedidos: list[dict]):
        """Procesa una lista de pedidos reutilizando el servicio de aplicación."""
        resultados = []
        for data_pedido in lista_pedidos:
            resultado = self._servicio_pedidos.procesar(data_pedido)
            resultados.append(resultado)
        return resultados
