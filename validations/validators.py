# -*- coding: utf-8 -*-


class Validators():
    def __init__(self):
        pass

    def rangeOptions(self, value, minValue, maxValue):
        if value < minValue or value > maxValue:
            return True
        return False

    def optionZero(self, value):
        if value <= 0:
            return True
        return False