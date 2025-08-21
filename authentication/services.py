import logging
import re
import secrets

from redis import Redis, ConnectionError

from core.config import RedisConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OTPServices:
    def __init__(self):
        try:
            self.redis_client = Redis.from_url(RedisConfig.REDIS_URL, decode_responses=True)
            self.redis_client.ping()
        except ConnectionError as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error initializing Redis client: {e}")
            raise

    def _get_otp_key(self, email: str) -> str:
        return f"send_otp:{email}"

    def generate_code(self) -> str:
        return str(secrets.randbelow(1000000)).zfill(6)

    def set_code(self, email: str, code: str, expire_time: int = 120) -> tuple[bool, int]:
        if not self._is_valid_email(email):
            logger.error(f"Invalid email format: {email}")
            return False, 0

        try:
            key = self._get_otp_key(email)
            ttl = self.redis_client.ttl(key)
            if ttl > 0:
                return False, ttl
            self.redis_client.set(key, code, ex=expire_time)
            logger.info(f"OTP set for {email}")
            return True, 0
        except Exception as e:
            logger.error(f"Error setting OTP for {email}: {e}")
            return False, 0

    def verify_code(self, email: str, code: str) -> bool:
        if not self._is_valid_email(email):
            logger.error(f"Invalid email format: {email}")
            return False

        try:
            key = self._get_otp_key(email)
            stored_code = self.redis_client.get(key)
            if stored_code and stored_code == code:
                self.redis_client.delete(key)
                logger.info(f"OTP verified successfully for {email}")
                return True
            logger.warning(f"Invalid or expired OTP for {email}")
            return False
        except Exception as e:
            logger.error(f"Error verifying OTP for {email}: {e}")
            return False

    def _is_valid_email(self, email: str) -> bool:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))
