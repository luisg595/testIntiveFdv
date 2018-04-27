# -*- coding: utf-8 -*-
from config import config


class Rate():
    def __init__(self):
        pass

    def calculateTotalPay(
            self, optionType, quantityBikes, quantityCharging, family=False):
        quantityType = self.quantityType(optionType)
        totalPay = (quantityCharging * quantityType) * quantityBikes
        if family:
            totalPay = self.percent(totalPay)
        return(
            'Total to pay is ' + str(totalPay) +
            '$\n\nPress Enter to back the menu')

    def quantityType(self, optionType):
        if optionType == 1:
            quantityType = config.rentalHour
        elif optionType == 2:
            quantityType = config.rentalDay
        elif optionType == 3:
            quantityType = config.rentalWeek
        return quantityType

    def percent(self, totalPay):
        percent = totalPay * float(config.percent)
        totalPay = totalPay - percent
        return totalPay
