import world
import api.captcha.captcha_phone
from api.token.jwt_token import JWTToken

"""
Django 的 shortcuts.py
"""
world_instance = world.World.instance()
redis_server = world_instance.redis
captcha_manager = api.captcha.captcha_phone.CaptchaPhone(redis_server)
jwt_cli = JWTToken()
import django.db