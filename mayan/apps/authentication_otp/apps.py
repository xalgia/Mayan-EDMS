import logging

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from mayan.apps.common.apps import MayanAppConfig
from mayan.apps.common.menus import menu_secondary, menu_user

from .links import link_otp_detail, link_otp_disable, link_otp_enable

logger = logging.getLogger(name=__name__)


class AuthenticationOTPApp(MayanAppConfig):
    app_namespace = 'authentication_otp'
    app_url = 'authentication_otp'
    has_tests = True
    name = 'mayan.apps.authentication_otp'
    verbose_name = _('Authentication OTP')

    def ready(self):
        super().ready()

        User = get_user_model()

        menu_secondary.bind_links(
            links=(link_otp_disable, link_otp_enable,), sources=(User,)
        )

        menu_user.bind_links(
            links=(
                link_otp_detail,
            )
        )
