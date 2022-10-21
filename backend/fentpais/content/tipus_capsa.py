from guillotina import app_settings, configure, content
from fentpais.interfaces.tipus_capsa import ITipusCapsaFolder, ITipusCapsa
from guillotina.component import query_utility
from guillotina.interfaces.catalog import ICatalogUtility
from guillotina.api.service import Service


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
        return await search_instance.search(
            context=self,
            query={"type_name": "Experiencia"}
        )

@configure.service(context=ITipusCapsa, name="@getExperiences", method="GET", permission="guillotina.ViewContent")
@configure.service(context=ITipusCapsaFolder, name="@getExperiences", method="GET", permission="guillotina.ViewContent")
class GetExperiencesCapsa(Service):
    async def __call__(self):
        return await self.context.get_experiencies()


@configure.contenttype(
    type_name="TipusCapsa",
    schema=ITipusCapsa,
    allowed_types=["Experiencia"],
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    globally_addable=False
)
class TipusCapsa(content.Folder):
    async def get_experiencies(self):
        search_instance = query_utility(ICatalogUtility)
        return await search_instance.search(
            context=self,
            query={"type_name": "Experiencia", "metadata": "*"}
        )
