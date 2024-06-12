import pytest
import random

@pytest.fixture
def mon_keyring():
    def make_keyring(default=False):
        if default:
            key = "294df882caec012e&sxsrf=ADLYWII6zYQeNk4ZBRJ_8uJSf5"
        else:
            key = "%032x==" % random.getrandbits(128)
        return """
    [mon.]
        key= %s
            caps mon = "allow"
        """ % key
    return make_keyring

def test_default_key(mon_keyring):
    contents = mon_keyring(default=True)
    assert "294df882caec012e&sxsrf=ADLYWII6zYQeNk4ZBRJ_8uJSf5" in contents

mon_keyring()
