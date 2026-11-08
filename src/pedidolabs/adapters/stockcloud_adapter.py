"""
Adaptador para integrar la API de StockCloud sin modificarla ni acoplar el núcleo.
"""
from pedidolabs.stockcloud_api import StockCloudAPI


class PuertoInventario:
    """Puerto de salida abstracto para el manejo de inventario."""

    def verificar_y_reservar(self, sku: str, unidades: int) -> bool:
        raise NotImplementedError


class StockCloudAdapter(PuertoInventario):
    """Adaptador concreto para la API externa StockCloud."""

    def __init__(self, api_externa: StockCloudAPI):
        self._api = api_externa

    def verificar_y_reservar(self, sku: str, unidades: int) -> bool:
        stock_disponible = self._api.query_stock(sku)
        if stock_disponible >= unidades:
            respuesta = self._api.reserve_units(sku, unidades)
            return respuesta.get("status") == "SUCCESS"
        return False
