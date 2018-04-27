# -*- coding: utf-8 -*-

import os
import sys
from model.rate import Rate
from validations.validators import Validators
from config import config

rate = Rate()
validators = Validators()

clear = "clear" if sys.platform.startswith("linux") else "cls"
percent = config.percent.split('.')[1]


class Menu():
    def __init__(self):
        self.hour = 'Hour'
        self.day = 'Day'
        self.week = 'Week'
        self.loop()

    def loop(self):
        try:
            print('\nChosse an option of rental\n\n')
            rentOption = int(input(
                '1) Rental by Hour. 5$\n2) Rental by Day. 20$\n' +
                '3) Rental by Week. 60$\n4) Family Rental. ' +
                'From 3 to 5 rentals of any type with ' +
                percent + '% discount of the total pay\n' +
                '5) Exit Program\n'))
            validattionRange = validators.rangeOptions(rentOption, 1, 5)
            if validattionRange:
                input('Invalid option.\n\nPress Enter to back the menu')
            if rentOption == 1:
                quantityBikes = self.quantityBikes()
                quantityCharging = self.quantityCharging(rentOption)
                print(rate.calculateTotalPay(
                    1, quantityBikes, quantityCharging))
                input()
            elif rentOption == 2:
                quantityBikes = self.quantityBikes()
                quantityCharging = self.quantityCharging(rentOption)
                print(rate.calculateTotalPay(
                    2, quantityBikes, quantityCharging))
                input()
            elif rentOption == 3:
                quantityBikes = self.quantityBikes()
                quantityCharging = self.quantityCharging(rentOption)
                print(rate.calculateTotalPay(
                    3, quantityBikes, quantityCharging))
                input()
            elif rentOption == 4:
                rentOptionFamiliar = self.rentOption()
                quantityBikes = self.quantityBikes(True)
                quantityCharging = self.quantityCharging(rentOptionFamiliar)
                print(rate.calculateTotalPay(
                    rentOptionFamiliar, quantityBikes, quantityCharging, True))
                input()
            elif rentOption == 5:
                input('Good bye! Press Enter to exit')
                self.clear()
                exit()
        except ValueError:
            input('You must enter a number.\n\nPress Enter to back the menu')
        except KeyboardInterrupt:
            self.clear()
            exit()
        self.launchLoop()

    def quantityBikes(self, family=False):
        quantityFamily = ''
        if family:
            quantityFamily = '(3-5)'
        quantityBikes = int(input(
            'Enter the quantity of bikes to rent' +
            quantityFamily + ':\n'))
        validationZero = validators.optionZero(quantityBikes)
        if validationZero:
            input('This value is not allowed.\n\nPress Enter to retry')
            self.launchLoop()
        if family and quantityBikes < 3 or family and quantityBikes > 5:
            input('Invalid option.\n\nPress Enter to retry')
            self.launchLoop()
        return quantityBikes

    def quantityCharging(self, rentType):
        rentType = self.rentType(rentType)
        quantityCharging = int(input(
            'Enter the quantity of ' + rentType + ' to charging:\n'))
        validationZero = validators.optionZero(quantityCharging)
        if validationZero:
            input('This value is not allowed.\n\nPress Enter to retry')
            self.launchLoop()
        return quantityCharging

    def rentOption(self):
        rentOption = int(input(
            '1) Rental by Hour. 5$\n2) Rental by Day. 20$\n' +
            '3) Rental by Week. 60$\n'))
        validattionRange = validators.rangeOptions(rentOption, 1, 3)
        if validattionRange:
            input('Invalid option.\n\nPress Enter to retry')
            self.launchLoop()
        return rentOption

    def rentType(self, rentType):
        if rentType == 1:
            textType = self.hour
        elif rentType == 2:
            textType = self.day
        elif rentType == 3:
            textType = self.week
        return textType

    def clear(self):
        os.system(clear)

    def launchLoop(self):
        self.clear()
        self.loop()