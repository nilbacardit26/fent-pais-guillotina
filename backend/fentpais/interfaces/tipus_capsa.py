from guillotina import interfaces, schema


class ITipusCapsaFolder(interfaces.IFolder):
    async def get_experiencies():
        """
        Get all experiences
        """


class ITipusCapsa(interfaces.IFolder):
    async def get_experiencies():
        """
        Get experiences of the capsa
        """

    nom = schema.Text(required=True)

    descripcio = schema.TextLine(required=True)
