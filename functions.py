import json
import os
import datetime

def create_json(variavel,dados):
    if not os.path.exists(variavel):
        with open(variavel, 'w', encoding='utf-8') as f:
            json.dump(dados, f , indent=4, ensure_ascii=False)
    else:
        return

def open_json():
    with open('history_conversor.json', 'r', encoding='utf-8') as arquive:
	    return json.load(arquive)
    
def open_measurement():
    with open('measurement.json', 'r', encoding='utf-8') as arquive:
	    return json.load(arquive)

def save_json(variavel):
    with open('history_conversor.json', 'w', encoding='utf-8') as f:
        json.dump(variavel, f, indent=4, ensure_ascii=False)

line = '-' * 50
def interface():
    print(line)
    print('Conversor'.center(50))
    print(line)
    print('Choose a measurement')
    print()
    print('1-Temperature')
    print('2-Distance')
    print('3-Weight')
    print('4-Time')
    print('5-Speed')
    print('6-History')
    print('7-View units')
    print('8-Exit')
    print(line)
    while True:
        try:
            a = int(input('->'))
        except ValueError:
            print(line)
            print('Type only numbers!')
            print(line)
            continue
        if a < 1 or a > 8:
            print('Option unavailable!')
            print(line)
            continue 
        return a

def calcule(unit,mode):
    while True:
        source = input(f'{mode} source:').lower()
        print(line)
        if not source in unit:
            print('Option unabailable!')
            print(line)
            continue
        target = input(f'{mode} target:').lower()
        print(line)
        if not target in unit:
            print('Option unabailable!')
            print(line)
            continue
        try:
            value = float(input(f'{mode} value:'))
            print(line)
        except ValueError:
            print('Type only numbers!')
            print(line)
            continue

        global_value = value * unit[source]
        result = global_value / unit[target]
        print(f"{value} {source} = {result:.2f} {target}")
        date = datetime.datetime.now()
        date_formatad = f'{date.strftime('%d/%m/%Y %H:%M:%S')}'
        history = open_json()
        info = {
            'mode': mode,
            'source': source,
            'target': target,
            'value': value,
            'result': result,
            'date': date_formatad
        }
        history.append(info)
        save_json(history)
        return

def get_measurement(mode):
    measurements = open_measurement()

    for measurement in measurements:
        if mode in measurement:
            return measurement[mode]

    return None    
    
def temperature():
    mode = 'Temperature'
    units = get_measurement(mode)

    while True:
        source = input(f'{mode} source: ').lower().strip()
        print(line)

        if source not in units:
            print('Option unavailable!')
            print(line)
            continue

        target = input(f'{mode} target: ').lower().strip()
        print(line)

        if target not in units:
            print('Option unavailable!')
            print(line)
            continue

        try:
            value = float(input(f'{mode} value: '))
            print(line)

        except ValueError:
            print('Type only numbers!')
            print(line)
            continue

        # =========================
        # SOURCE -> CELSIUS
        # =========================

        if source == 'celsius':
            celsius = value

        elif source == 'fahrenheit':
            celsius = (value - 32) * 5 / 9

        elif source == 'kelvin':
            celsius = value - 273.15

        elif source == 'rankine':
            celsius = (value - 491.67) * 5 / 9

        elif source == 'reaumur':
            celsius = value * 5 / 4

        # =========================
        # CELSIUS -> TARGET
        # =========================

        if target == 'celsius':
            result = celsius

        elif target == 'fahrenheit':
            result = (celsius * 9 / 5) + 32

        elif target == 'kelvin':
            result = celsius + 273.15

        elif target == 'rankine':
            result = (celsius + 273.15) * 9 / 5

        elif target == 'reaumur':
            result = celsius * 4 / 5

        print(f'{value} {source} = {result:.2f} {target}')

        # =========================
        # SAVE HISTORY
        # =========================

        date = datetime.datetime.now()
        date_formatted = date.strftime('%d/%m/%Y %H:%M:%S')

        history = open_json()

        info = {
            'mode': mode,
            'source': source,
            'target': target,
            'value': value,
            'result': result,
            'date': date_formatted
        }

        history.append(info)
        save_json(history)

        return


def distance():
    mode = 'Distance'
    unit = get_measurement(mode)
    calcule(unit,mode)

def weight():
 
 mode = 'Weight'
 unit = get_measurement(mode)
 calcule(unit,mode)

def speed():
    mode = 'Speed'
    unit = get_measurement(mode)
    calcule(unit,mode)

def time():
    mode = 'Time'
    unit = get_measurement(mode)
    calcule(unit,mode)

def history():
    history = open_json()
    for info in history:
        print(f'Mode: {info['mode']}')
        print(f'Source: {info['source']}')
        print(f'Target: {info['target']}')
        print(f'Value: {info['value']}')
        print(f'Result: {info['result']}')
        print(f'Date: {info['date']}')
        print(line)
        print()

def view_units():

    print(line)
    print('View units of measurement'.center(50))
    print(line)

    print()
    print('1-Temperature')
    print('2-Distance')
    print('3-Weight')
    print('4-Time')
    print('5-Speed')
    print(line)

    while True:

        try:
            a = int(input('-> '))

        except ValueError:
            print(line)
            print('Type only numbers!')
            print(line)
            continue

        if a < 1 or a > 5:
            print('Option unavailable!')
            print(line)
            continue

        mode = a - 1

        history = open_measurement()

        # Get category
        category = history[mode]

        # Get category name
        name = list(category.keys())[0]

        # Get units
        units = category[name]

        print(line)
        print(name.center(50))
        print(line)

        if isinstance(units, list):

            # Temperature
            for unit in units:
                print(f'- {unit}')

        elif isinstance(units, dict):

            # Distance, Weight, Time, Speed...
            for unit, value in units.items():
                print(f'- {unit:<20} {value}')

        print(line)

        return