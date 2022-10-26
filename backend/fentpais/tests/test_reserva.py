import json
import pytest

pytestmark = pytest.mark.asyncio


async def test_creacio_experiencia_correcte(fentpais):
    fentpais, token = fentpais
    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_tipus_capsa",
            "@type": "TipusCapsa",
            "nom": "tipus a",
            "descripcio": "Aquesta capsa conté experiencies",
            "preu": 10.0
        })
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/reserves',
        data=json.dumps({
            "id": "foo_reserva",
            "@type": "Reserva",
            "tipus_capsa": "foo_tipus_capsa",
        })
    )
    assert status == 201


async def test_creacio_experiencia_412(fentpais):
    fentpais, token = fentpais
    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_tipus_capsa",
            "@type": "TipusCapsa",
            "nom": "tipus a",
            "descripcio": "Aquesta capsa conté experiencies",
            "preu": 10.0
        })
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/reserves',
        data=json.dumps({
            "id": "foo_reserva",
            "@type": "Reserva",
            "tipus_capsa": "foo_wrong_tipus_capsa",
            "preu": 10.0
        })
    )
    assert status == 412
