"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = temperature_c * (9/5) + 32
    return temperature_f


def convert_c_to_k(temperature_c):
    """Convert Celsius to Kelvin."""
    temperature_k = temperature_c + 273.15
    return temperature_k


def convert_k_to_c(temperature_k):
    """Convert Kelvin to Celsius."""
    temperature_c = temperature_k - 273.15
    return temperature_c


def convert_f_to_k(temperature_f):
    """Convert Fahrenheit to Kelvin."""
    temperature_k = convert_c_to_k(convert_f_to_c(temperature_f))
    return temperature_k
    

def convert_k_to_f(temperature_k):
    """Convert Kelvin to Fahrenheit"""
    temperature_f = convert_c_to_f(convert_k_to_c(temperature_k))
    return temperature_f

                                   
def convert_to_all(temperature_f):
    print("The temperature", temperature_f, "F is:")
    c = convert_f_to_c(temperature_f)
    k = convert_f_to_k(temperature_f)
    print("\t ", round(c,2), "degrees C")
    print("\t ", round(k,2), "degrees K")
                   
