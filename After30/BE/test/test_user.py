"""Sample test for IMFast"""
import pytest
from httpx import AsyncClient
from loguru import logger
from time import time, localtime, gmtime


class random_dumy_data:
    tm = localtime(gmtime(time()))
    phone = f"010-{str(tm.tm_day)}{str(tm.tm_hour)
                                   }-{str(tm.tm_min)}{str(tm.tm_sec)}"
    email = f"user{str(tm.tm_hour)}{str(tm.tm_min)}{
        str(tm.tm_sec)}@example.com"

# TODO: test시 테스트 db 사용하도록하고 테스트마다 초기화


@pytest.mark.anyio
async def test_sign_up(client: AsyncClient):
    """Test sign up"""
    dumy_data = random_dumy_data()
    response = await client.post("/api/v1/users", json={
        "email": dumy_data.email,
        "password": "password",
        "name": "홍길동",
        "sex": "M",
        "birth": "1990-01-01",
        "address": "서울시 강남구",
        "phone": dumy_data.phone
    })
    assert response.status_code == 201
    assert response.json()['result'] == {
        "email": "user@example.com"
    }


@pytest.mark.anyio
async def test_sign_up_email_duplicated_user(client: AsyncClient):
    """Test duplicated user"""
    dumy_data = random_dumy_data()
    response = await client.post("/api/v1/users", json={
        "email": "user@example.com",
        "password": "password",
        "name": "홍길동",
        "sex": "M",
        "birth": "1990-01-01",
        "address": "서울시 강남구",
        "phone": dumy_data.phone
    })
    assert response.status_code == 400
    assert response.json() == {
        "msg": "already_exists_user"
    }


@pytest.mark.anyio
async def test_sign_up_phone_duplicated_user(client: AsyncClient):
    """Test duplicated user"""
    dumy_data = random_dumy_data()
    response = await client.post("/api/v1/users", json={
        "email": dumy_data.email,
        "password": "password",
        "name": "홍길동",
        "sex": "M",
        "birth": "1990-01-01",
        "address": "서울시 강남구",
        "phone": "010-1234-5678"
    })
    assert response.status_code == 400
    assert response.json() == {
        "msg": "already_exists_user"
    }


@pytest.mark.anyio
async def test_sign_up_password_hash(client: AsyncClient):
    # TODO : get 기능 개발 후 sign_up 후 get으로 유저 가져와서 password가 hash되어 있는지 확인
    pass
