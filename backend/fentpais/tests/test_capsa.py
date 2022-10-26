import pytest
import json


pytestmark = pytest.mark.asyncio


async def test_creacio_capsa(fentpais):
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


async def test_creacio_experiencia(fentpais):
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
        '/db/container/tipus_capsa/foo_tipus_capsa',
        data=json.dumps({
            "id": "experiencia1",
            "@type": "Experiencia",
            "nom": "tipus a",
            "descripcio": "Aquesta capsa conté experiencies",
            "categories": ["categoria1", "categoria2"]
        })
    )
    assert status == 201


async def test_tipus_capsa_get_experiencies_endpoint(fentpais):
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
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_capsa_tipus2",
            "@type": "TipusCapsa",
            "nom": "tipus a",
            "descripcio": "Aquesta capsa conté experiencies",
            "preu": 10.0
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa/foo_tipus_capsa',
        data=json.dumps({
            "id": "experiencia1",
            "@type": "Experiencia",
            "nom": "tipus a",
            "descripcio": "Aquesta capsa conté experiencies",
            "categories": ["categoria1", "categoria2"]
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa/foo_capsa_tipus2',
        data=json.dumps({
            "id": "experiencia",
            "@type": "Experiencia",
            "nom": "tipus a",
            "descripcio": "Aquesta capsa conté experiencies",
            "categories": ["categoria1", "categoria2"]
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'GET',
        '/db/container/tipus_capsa/foo_tipus_capsa/@getExperiences',
        headers={"X-Wait": "10"}
    )
    assert status == 200
    assert resp["items_total"] == 1

    resp, status = await fentpais(
        'GET',
        '/db/container/tipus_capsa/@getExperiences',
        headers={"X-Wait": "10"}
    )
    assert status == 200
    assert resp["items_total"] == 2
