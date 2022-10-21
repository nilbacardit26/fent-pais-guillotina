from guillotina import configure, content
from fentpais.interfaces.experiencia import IExperiencia


@configure.contenttype(
    type_name="Experiencia",
    schema=IExperiencia,
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    globally_addable=False
)
class Experiencia(content.Item):
    pass
