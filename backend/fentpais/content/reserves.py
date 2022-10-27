from guillotina import app_settings, configure, content
from guillotina.response import HTTPPreconditionFailed
from fentpais.interfaces.reserves import (
    IReservesFolder,
    IReserva
)
from guillotina.interfaces import (
    IObjectAddedEvent,
    IObjectModifiedEvent
)
from guillotina.component import query_utility
from guillotina.interfaces.catalog import ICatalogUtility
from guillotina.utils import get_current_container


# TODO_3
# @configure.contenttype(
#     type_name="ReservesFolder",
#     schema=IReservesFolder,
#     behaviors=[
#         'guillotina.behaviors.dublincore.IDublinCore'
#     ],
#     allowed_types=["Reserva"],
#     globally_addable=False
# )
# class ReservesFolder(content.Folder):
#     async def get_reserves(self):
#         search_instance = query_utility(ICatalogUtility)
#         return search_instance.search({"type_name": "Reserva"})
# END_TODO_3

# TODO_8
# @configure.contenttype(
#     type_name="Reserva",
#     schema=IReserva,
#     behaviors=[
#         'guillotina.behaviors.dublincore.IDublinCore'
#     ],
#     globally_addable=False
# )
# class Reserva(content.Item):
#     async def check_tipus_capsa(self):
#         search_instance = query_utility(ICatalogUtility)
#         container = get_current_container()
#         tipus_capsa_folder = await container.async_get("tipus_capsa")
#         results = await search_instance.unrestrictedSearch(context=tipus_capsa_folder, query={"id": self.tipus_capsa})
#         if results["items_total"] == 0:
#             raise HTTPPreconditionFailed()
# END_TODO_8

# TODO_9
# @configure.subscriber(for_=(IReserva, IObjectAddedEvent))
# @configure.subscriber(for_=(IReserva, IObjectModifiedEvent))
# async def creacio_modificacio_reserva(obj, event):
#     await obj.check_tipus_capsa()
# END_TODO_9
