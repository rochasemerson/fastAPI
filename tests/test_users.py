from fastapi import status
from app import schemas
import pytest
from jose import jwt
from app.config import settings

def test_create_user(client):
    res = client.post("/users/", json={
    "email": "emerson@gmail.com",
    "password": "pasword123"})

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "emerson@gmail.com"
    assert res.status_code == status.HTTP_201_CREATED

def test_login_user(client, test_user):
    res = client.post("/login", data={
    "username": test_user['email'],
    "password": test_user['password']})

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.acess_token, settings.secret_key, 
        algorithms=[settings.algorithm])

    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == status.HTTP_200_OK

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('emerson@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('emerson@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("login", data={"username": email,
        "password": password})
    
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'