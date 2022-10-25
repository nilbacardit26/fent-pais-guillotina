from guillotina import interfaces, schema, directives
from guillotina.directives import index_field


class IExperiencia(interfaces.IItem):
    index_field("nom", type="text")
    nom = schema.TextLine(required=True)

    index_field("description", type="text")
    descripcio = schema.TextLine(required=True)

    categories = schema.List(
        title="Categories",
        description="Categories de la experiència",
        value_type=schema.TextLine(),
        required=False
    )


@directives.index_field.with_accessor(
    IExperiencia,
    "categories",
    type="text",
    field="categories",
    store=True
)
async def index_tests_respondre(obj):
    results = ""
    for category in obj.categories:
        results = results + category
    if results != "":
        return results
