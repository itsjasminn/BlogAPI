import json

from redis import Redis

from core.config import RedisConfig


class OTPServices:
    def __init__(self):
        self.redis_client = Redis.from_url(RedisConfig.REDIS_URL)

    def _get_otp_phone_key(self, phone_number: str) -> str:
        return f"otp_phone_{phone_number}"

    def _get_otp_email_key(self, email: str) -> str:
        return f"send_otp:{email}"

    def _get_registration_key(self, email: str) -> str:
        return f"registration_key:{email}"

    def set_code_phone(self, phone_number: str, code: str, expire_time: int = 120) -> tuple[bool, int]:
        _key = self._get_otp_phone_key(phone_number)
        _ttl = self.redis_client.ttl(_key)
        if _ttl > 0:
            return False, _ttl

        self.redis_client.set(_key, code, expire_time)
        return True, 0

    def set_code_email(self, email: str, code: str, expire_time: int = 120) -> tuple[bool, int]:
        _key = self._get_otp_email_key(email)
        _ttl = self.redis_client.ttl(_key)
        if _ttl > 0:
            return False, _ttl

        self.redis_client.set(_key, code, expire_time)
        verification_send_email(email, code)
        return True, 0

    def save_user_before_registration(self, email: str, user_data: dict, expire_time: int = 120):
        _key = self._get_registration_key(email)
        _ttl = self.redis_client.ttl(_key)
        if _ttl > 0:
            return False, _ttl
        user_data = json.dumps(user_data)
        self.redis_client.set(_key, user_data, expire_time)
        return True, 0

    def verify_email(self, email: str, code: str) -> tuple[bool, dict]:
        _key = self._get_otp_email_key(email)
        saved_code = self.redis_client.get(_key)

        _key = self._get_registration_key(email)
        user_data = self.redis_client.get(_key)
        user_data = json.loads(user_data)
        return saved_code == code, user_data
