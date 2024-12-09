import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_sanitized_input(client):
    response = client.post('/v1/sanitized/input/', json={"payload": "safe input"})
    assert response.status_code == 200
    assert response.json == {"result": "sanitized"}

def test_unsanitized_input(client):
    response = client.post('/v1/sanitized/input/', json={"payload": "select * from table--"})
    assert response.status_code == 200
    assert response.json == {"result": "unsanitized"}
