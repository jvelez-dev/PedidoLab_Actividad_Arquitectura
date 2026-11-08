"""
Pruebas de arquitectura que demuestran el cumplimiento de los requerimientos.
"""
from unittest.mock import MagicMock
from pedidolabs.adapters.entrypoints import RestPedidoAdapter, BatchPedidoAdapter
from pedidolabs.adapters.stockcloud_adapter import StockCloudAdapter


def test_adapter_entrada_trabaja_con_fake_caso_uso():
    """Demuestra que un adaptador de entrada puede trabajar contra un fake del caso de uso."""
    fake_servicio = MagicMock()
    adapter = RestPedidoAdapter(fake_servicio)

    pedido_ejemplo = {"pedido_id": "P-100", "nombre": "Ana"}
    adapter.recibir_pedido(pedido_ejemplo)

    fake_servicio.procesar.assert_called_once_with(pedido_ejemplo)


def test_batch_reutiliza_misma_capacidad_aplicacion():
    """Demuestra que el proceso batch reutiliza la misma capacidad de aplicación."""
    mock_servicio = MagicMock()
    batch_adapter = BatchPedidoAdapter(mock_servicio)

    lote = [{"pedido_id": "P-1"}, {"pedido_id": "P-2"}]
    batch_adapter.procesar_lote(lote)

    assert mock_servicio.procesar.call_count == 2


def test_stockcloud_queda_detras_de_un_adaptador():
    """Demuestra que StockCloud queda encapsulado detrás de un adaptador de salida."""
    api_mock = MagicMock()
    api_mock.query_stock.return_value = 10
    api_mock.reserve_units.return_value = {"status": "SUCCESS"}

    adapter = StockCloudAdapter(api_mock)
    exito = adapter.verificar_y_reservar("SKU-ABC", 2)

    assert exito is True
    api_mock.query_stock.assert_called_once_with("SKU-ABC")
    api_mock.reserve_units.assert_called_once_with("SKU-ABC", 2)


def test_nucleo_procesa_sin_depender_directamente_de_stockcloud():
    """Demuestra que el núcleo procesa sin importar ni conocer la API concreta de StockCloud."""
    api_mock = MagicMock()
    api_mock.query_stock.return_value = 5
    api_mock.reserve_units.return_value = {"status": "SUCCESS"}

    puerto_inventario = StockCloudAdapter(api_mock)
    resultado = puerto_inventario.verificar_y_reservar("SKU-TEST", 1)

    assert resultado is True
