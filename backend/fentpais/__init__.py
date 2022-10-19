from guillotina import configure


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('fentpais.interfaces')
    configure.scan('fentpais.content')
