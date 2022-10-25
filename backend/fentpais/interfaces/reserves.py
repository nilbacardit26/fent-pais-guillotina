from guillotina import interfaces, schema


class IReservesFolder(interfaces.IFolder):
    pass


class IReserva(interfaces.IItem):
    tipus_capsa = schema.TextLine()
