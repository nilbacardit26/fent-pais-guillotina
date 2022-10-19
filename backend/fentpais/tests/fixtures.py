import json
import pytest

from guillotina import testing

def base_settings_configurator(settings):
    settings['applications'].append('fentpais')
    settings['applications'].append('guillotina.contrib.redis')
    settings['applications'].append('guillotina.contrib.dbusers')
    settings["applications"].append("guillotina.contrib.mailer")
    settings["applications"].append("guillotina.contrib.image")
    settings["applications"].append("guillotina.contrib.email_validation")
    settings["applications"].append("guillotina.contrib.catalog.pg")
    settings["applications"].append("guillotina.contrib.templates")
    settings["applications"].append("guillotina.contrib.cache")
    settings["allow_register"] = True
    settings["auth_token_validators"] = [
        "guillotina.auth.validators.SaltedHashPasswordValidator",
        "guillotina.auth.validators.JWTValidator"
    ]
    settings["mailer"] = {
        "utility": "guillotina.contrib.mailer.utility.TestMailerUtility",
        "default_sender": "noreply@iskradevelopment.com"
    }
    settings["auth_extractors"] = [
        "guillotina.auth.extractors.BearerAuthPolicy",
        "guillotina.auth.extractors.BasicAuthPolicy",
        "guillotina.auth.extractors.WSTokenAuthPolicy"
    ]
    settings["load_utilities"] = {
        "catalog": {
            "provides": "guillotina.interfaces.ICatalogUtility",
            "factory": "guillotina.contrib.catalog.pg.utility.PGSearchUtility"
        }
    }
    settings["max_size_allowed"] = 1024 * 1024 * 100


testing.configure_with(base_settings_configurator)

@pytest.fixture(scope="function")
async def fentpais(db, guillotina):
    resp, status = await guillotina(
        'POST', '/db',
        data=json.dumps({
            "@type": "Container",
            "title": "Container",
            "id": "container",
        }))
    assert status == 200
    yield guillotina
