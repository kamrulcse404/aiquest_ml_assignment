temperature = float(input('Enter temperature: '))
scale = input('Enter temperature scale c/f: ')

scale = scale.lower()


def temperature_converter(temperature, scale):

    def fahrenheit(temperature):
        return (temperature * 9/5) + 32
    
    def celsius(temperature):
        return (temperature - 32) * 5/9
    
    if scale == 'c':
        return fahrenheit(temperature)
    if scale == 'f':
        return celsius(temperature)

res = temperature_converter(temperature, scale)

if scale == 'c':
    print(f"temperature {temperature} covert to fahrenheit = {res}")
else:
    print(f"temperature {temperature} covert to celsius = {res}")