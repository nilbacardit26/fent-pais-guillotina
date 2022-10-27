import json
import pytest

pytestmark = pytest.mark.asyncio


async def test_permisos_GET(fentpais):
    fentpais, token = fentpais
    resp, status = await fentpais(
        'GET',
        '/db/container/reserves',
        authenticated=False,
        headers={"AUTHORIZATION": f"Bearer {token}"}
    )
    assert status == 401

    resp, status = await fentpais(
        'GET',
        '/db/container/tipus_capsa',
        authenticated=False,
        headers={"AUTHORIZATION": f"Bearer {token}"}
    )
    assert status == 200

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "@type": "TipusCapsa",
            "preu": 10,
            "id": "foo_capsa",
            "nom": "Foo Capsa",
            "descripcio": "Foo descripcio"
        })
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa/foo_capsa',
        data=json.dumps({
            "@type": "Experiencia",
            "id": "foo_experiencia",
            "nom": "Foo Capsa",
            "descripcio": "Foo descripcio"
        })
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/reserves',
        authenticated=False,
        data=json.dumps({
            "@type": "Reserva",
            "id": "foo_reserva",
            "preu": 10,
            "tipus_capsa": "foo_capsa"
        }),
        headers={"AUTHORIZATION": f"Bearer {token}"}
    )
    assert status == 201

    resp, status = await fentpais(
        'GET',
        '/db/container/reserves/foo_reserva',
        authenticated=False,
        headers={"AUTHORIZATION": f"Bearer {token}"}
    )
    assert status == 200

    resp, status = await fentpais(
        'GET',
        '/db/container/tipus_capsa/foo_capsa/foo_experiencia',
        authenticated=False,
        headers={"AUTHORIZATION": f"Bearer {token}"}
    )
    assert status == 200
