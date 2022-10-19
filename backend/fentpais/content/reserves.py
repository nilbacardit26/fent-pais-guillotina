from guillotina import app_settings, configure, content
from fentpais.interfaces.reserves import IReservesFolder, IReserva
from guillotina.component import query_utility
from guillotina.interfaces.catalog import ICatalogUtility


@configure.contenttype(
    type_name="ReservesFolder",
    schema=IReservesFolder,
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    allowed_types=["Reserva"],
    globally_addable=False
)
class ReservesFolder(content.Folder):
    async def get_reserves(self):
        search_instance = query_utility(ICatalogUtility)
        return search_instance.search({"type_name": "Reserva"})


@configure.contenttype(
    type_name="Reserva",
    schema=IReserva,
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    globally_addable=False
)
class Reserva(content.Item):
    pass
