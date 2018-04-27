# Test IntiveFdv

Test about Rental Bikes in Python 3

## Getting Started

Application to calculate the bicycle rental with different options.
Scroll through the menu by entering the option you require.
For example:
For a rent for hours select 1 then for 1 bicycle enter the value and finally the number of hours, this will reflect the total cost to pay for the rent.
There is also a family payment option that discounts the total price

### Prerequisites

Use a Linux distribution recommended, since the tests were done in this operating system, with Python 3.6 and install the library covegare with the command:

```
pip install coverage
```

### Run App

Run main.py to start the application and navigate through the different options

```
python main.py
```

## Running the tests

Run test_rate.py to apply test

```
python test_rate.py
```

You can also do tests of total coverage of the code, which should be noted, but it shows 100% is because it is not always entered in all conditional

```
coverage run main.py
```

Then execute

```
coverage html
```

This will generate a folder with html files inside the project folder. Inside that folder execute index.html in the browser and the coverage will be shown in detail