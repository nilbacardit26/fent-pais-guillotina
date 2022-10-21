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
