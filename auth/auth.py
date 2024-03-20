from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_name = "Arslanali", cookie_max_age = 3600)

# так нельзя оставлять. Нужно спрятать этот код в .env и как соединение с базой вытаскивать этот ключ
# A constant secret which is used to encode the token.
SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret = SECRET, lifetime_seconds = 3600)

auth_backend = AuthenticationBackend(
    name = "jwt",
    transport = cookie_transport,
    get_strategy = get_jwt_strategy,
)