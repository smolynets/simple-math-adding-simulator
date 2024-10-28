import random

from counting.models import SiteConfiguration


def get_max_number():
    site_configuration = SiteConfiguration.get_solo()
    return site_configuration.max_number
