from guillotina import configure
from guillotina.content import Container, create_content_in_container
from guillotina.interfaces import (
    IContainer,
    IObjectAddedEvent,
    IRolePermissionManager
)
from guillotina.event import notify
from guillotina.events import ObjectAddedEvent

@configure.contenttype(
    type_name="Container",
    schema=IContainer,
    behaviors=[
        'guillotina.behaviors.dublincore.IDublinCore'
    ],
    allowed_types=["ReservesFolder", "TipusCapsaFolder"]
)
class Container(Container):
    pass


@configure.subscriber(for_=(IContainer, IObjectAddedEvent))
async def creacio_container(obj, event):
    manage_roles_instance = IRolePermissionManager(obj)
    manage_roles_instance.grant_permission_to_role_no_inherit("guillotina.AccessContent", "guillotina.Member")
    manage_roles_instance.grant_permission_to_role("guillotina.AccessContent", "guillotina.Editor")
    manage_roles_instance.grant_permission_to_role("guillotina.ViewContent", "guillotina.Editor")
    reserves_folder = await create_content_in_container(
        parent=obj,
        type_="ReservesFolder",
        check_security=False,
        id_="reserves",
        title="Reserves' folder"
    )
    await notify(ObjectAddedEvent(reserves_folder, reserves_folder, reserves_folder.id))
    manage_roles_instance = IRolePermissionManager(reserves_folder)
    manage_roles_instance.grant_permission_to_role_no_inherit("guillotina.AccessContent", "guillotina.Member")

    tipus_capsa_folder = await create_content_in_container(
        parent=obj,
        type_="TipusCapsaFolder",
        check_security=False,
        id_="tipus_capsa",
        title="Tipus capses' folder"
    )
    await notify(ObjectAddedEvent(tipus_capsa_folder, tipus_capsa_folder, tipus_capsa_folder.id))
