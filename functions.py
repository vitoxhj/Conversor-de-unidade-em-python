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
    print('7-Exit')
    print(line)
    while True:
        try:
            a = int(input('->'))
        except ValueError:
            print(line)
            print('Type only numbers!')
            print(line)
            continue
        if a < 1 or a > 7:
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

def temperature():
    mode = 'Temperature'
    unit = {
        'c': 1,
        'f': -17.22,
        'k': -272.15,
        'r': -272.594,
        'Re': 1.25
    }
    calcule(unit,mode)

def distance():
    mode = 'Distance'
    unit = {
        'km': 1000,
        'm': 1,
        'dm': 0.1,
        'cm': 0.01,
        'mm': 0.001,
        'um': 0.000001,
        'nm': 0.000000001,
        'pm': 1e-12,
        'nmi': 1852,
        'mi': 1609.344,
        'fur': 201.168,
        'ftm': 1.8288,
        'yd': 0.9144,
        'ft': 0.3048,
        'pol': 0.0254,
        'li': 500,
        'zhang': 3.333,
        'chi': 0.333,
        'cun': 0.033,
        'fen': 0.003,
        'lii': 0.0003,
        'hao': 0.00003,
        'pc': 30856775814913672.79,
        'ld': 384401000,
        '.': 149597870700,
        'ly': 9460730472580800
    }
    calcule(unit,mode)

def weight():
 
 mode = 'Weight'
 unit = {
     't': 1000000,
     'kn': 101971.6,
     'kg': 1000,
     'hg': 100,
     'dag': 10,
     'g': 1,
     'quilate': 0.2,
     'centigrama': 0.01,
     'mg': 1e-3,
     'ug': 1e-6,
     'ng': 1e-9,
     'u': 1.66e-24,
     'tl': 1016046.91,
     'tc': 907184.74,
     'quintl': 50802.35,
     'quintc': 45359.24,
     'stone': 6350.29,
     'lb': 453.59,
     'onça': 28.35,
     'dr': 1.77,
     'gr': 0.06,
     'pennyweight': 1.56,
     'mite': 3.24e-3,
     'doite': 1.34e-4,
     'koku': 180407.95,
     'kann': 3750.37,
     'kinn': 600.06,
     'monnme': 3.75,
     'tael': 37.79,
     'ku ping': 37.32,
     'lispund': 8502.84,
     'mark': 212.52,
     'onu': 27.9,
     'lod': 13.3
 }
 calcule(unit,mode)

def speed():
    mode = 'Speed'
    unit = {
        'km/s': 1000,
        'm/s': 1,
        'km/h': 0.28,
        'mm/s': 1e-3,
        'um/s': 1e-6,
        'mile per second': 1609.34,
        'mph': 0.45,
        'ft/s': 0.3,
        'knot': 0.51,
        'light': 299792458,
        'sound': 343,
        'walk': 1.7,
        'snail': 1e-3

    }
    calcule(unit,mode)

def time():
    mode = 'Time'
    unit = {
        'years': 525960,
        'months': 43830,
        'weeks': 10080,
        'days': 1440,
        'hours': 60,
        'minutes': 1,
        'seconds': 0.02,
        'ms': 1.67e-5,
        'us': 1.67e-8,
        'ns': 1.67e-11
    }
    calcule(unit,mode)