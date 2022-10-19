from guillotina import app_settings, configure, content
from fentpais.interfaces.tipus_capsa import ITipusCapsaFolder, ITipusCapsa
from guillotina.component import query_utility
from guillotina.interfaces.catalog import ICatalogUtility


@configure.contenttype(
    type_name="TipusCapsaFolder",
    schema=ITipusCapsaFolder,
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    allowed_types=["TipusCapsa"],
    globally_addable=False
)
class TipusCapsaFolder(content.Folder):
    async def get_experiencies(self):
        search_instance = query_utility(ICatalogUtility)
        return search_instance.search({"type_name": "Experiencia"})


@configure.contenttype(
    type_name="TipusCapsa",
    schema=ITipusCapsa,
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    globally_addable=False
)
class TipusCapsa(content.Item):
    pass
