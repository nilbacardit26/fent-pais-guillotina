import pytest
import json


pytestmark = pytest.mark.asyncio


async def test_creacio_capsa(fentpais):
    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_tipus_capsa",
            "@type": "TipusCapsa"
        })
    )
    assert status == 201


async def test_creacio_experiencia(fentpais):
    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_tipus_capsa",
            "@type": "TipusCapsa"
        })
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa/foo_tipus_capsa',
        data=json.dumps({
            "id": "experiencia1",
            "@type": "Experiencia"
        })
    )
    assert status == 201


async def test_tipus_capsa_get_experiencies_endpoint(fentpais):
    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_tipus_capsa",
            "@type": "TipusCapsa"
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa',
        data=json.dumps({
            "id": "foo_tipus_capsa_2",
            "@type": "TipusCapsa"
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa/foo_tipus_capsa',
        data=json.dumps({
            "id": "experiencia1",
            "@type": "Experiencia"
        }),
        headers={"X-Wait": "10"}
    )
    assert status == 201

    resp, status = await fentpais(
        'POST',
        '/db/container/tipus_capsa/foo_tipus_capsa_2',
        data=json.dumps({
            "id": "experiencia",
            "@type": "Experiencia"
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
