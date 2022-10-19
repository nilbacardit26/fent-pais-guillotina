import pytest


pytestmark = pytest.mark.asyncio


async def test_container(fentpais):
    resp, status = await fentpais('GET', '/db/container/reserves')
    assert status == 200

    resp, status = await fentpais('GET', '/db/container/tipus_capsa')
    assert status == 200
