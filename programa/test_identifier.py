import pytest
from identifier import Identifier

@pytest.fixture
def identifier():
    return Identifier()

def test_controle(identifier):
    assert identifier.validate_identifier("s12345") is True

def test_inicio_numerico(identifier):
    assert identifier.validate_identifier("1w2345") is False

def test_inicio_vazio(identifier):
    assert identifier.validate_identifier(" w2345") is False

def test_inicio_especial(identifier):
    assert identifier.validate_identifier("_w2345") is False

def test_inicio_estrangeiro(identifier):
    assert identifier.validate_identifier("жw2345") is False

def test_string_vazia(identifier):
    assert identifier.validate_identifier(" ") is False

def test_muito_longo(identifier):
    assert identifier.validate_identifier("w1w23451") is False

def test_caractere_estrangeiro(identifier):
    assert identifier.validate_identifier("wб4ж4") is False

def test_caractere_especial(identifier):
    assert identifier.validate_identifier("wA_b+B") is False