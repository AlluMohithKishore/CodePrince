from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

def credentials():
    return {"email": f"test-{uuid4().hex}@example.com", "password": "supersecret"}

def test_auth_and_private_tests():
    with TestClient(app) as c:
        assert c.post('/api/auth/register', json=credentials()).status_code == 201
        q = c.get('/api/questions').json()['items'][0]
        detail = c.get('/api/questions/' + q['slug']).json()
        assert len(detail['tests']) == 1

def test_custom_question_and_progress():
    with TestClient(app) as c:
        assert c.post('/api/auth/register', json=credentials()).status_code == 201
        r = c.post('/api/questions', json={
            'title': 'My original problem', 'statement': 'Print hello',
            'tests': [{'input': '', 'expected_output': 'hello', 'is_hidden': True}],
        })
        assert r.status_code == 201
        assert c.get('/api/questions/' + r.json()['slug']).json()['tests'] == []
