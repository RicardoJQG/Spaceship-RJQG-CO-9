from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE


class Shield (PowerUp):
    def init__(self):
        super()._init_(SHIELD, SHIELD_TYPE)