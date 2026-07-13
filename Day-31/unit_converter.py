"""
Unit Converter
"""

import sys

# ---------- Conversion Functions ----------

def convert_length():
    units = ["km", "m", "cm", "miles", "feet", "inches"]
    # conversions stored in meters
    to_meter = {"km": 1000, "m": 1, "cm": 0.01, "miles": 1609.34, "feet": 0.3048, "inches": 0.0254}

    print("\n  Units:", ", ".join(units))
    from_unit = input("  From unit: ").strip().lower()
    to_unit   = input("  To unit  : ").strip().lower()

    if from_unit not in to_meter or to_unit not in to_meter:
        print("\n  Invalid unit entered.\n")
        return

    value = input("  Enter value: ").strip()
    if not value.replace(".", "", 1).isdigit():
        print("\n  Enter a valid number.\n")
        return

    value = float(value)
    result = value * to_meter[from_unit] / to_meter[to_unit]
    print(f"\n  {value} {from_unit} = {result:.4f} {to_unit}\n")

def convert_weight():
    units = ["kg", "g", "lb", "ounces"]
    to_gram = {"kg": 1000, "g": 1, "lb": 453.592, "ounces": 28.3495}

    print("\n  Units:", ", ".join(units))
    from_unit = input("  From unit: ").strip().lower()
    to_unit   = input("  To unit  : ").strip().lower()

    if from_unit not in to_gram or to_unit not in to_gram:
        print("\n  Invalid unit entered.\n")
        return

    value = input("  Enter value: ").strip()
    if not value.replace(".", "", 1).isdigit():
        print("\n  Enter a valid number.\n")
        return

    value = float(value)
    result = value * to_gram[from_unit] / to_gram[to_unit]
    print(f"\n  {value} {from_unit} = {result:.4f} {to_unit}\n")

def convert_temperature():
    print("\n  Units: celsius, fahrenheit, kelvin")
    from_unit = input("  From unit: ").strip().lower()
    to_unit   = input("  To unit  : ").strip().lower()
    valid = ["celsius", "fahrenheit", "kelvin"]

    if from_unit not in valid or to_unit not in valid:
        print("\n  Invalid unit entered.\n")
        return

    value = input("  Enter value: ").strip()
    try:
        value = float(value)
    except ValueError:
        print("\n  Enter a valid number.\n")
        return

    # convert to celsius
    if from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        celsius = value

    # convert celsius to target
    if to_unit == "fahrenheit":
        result = (celsius * 9 / 5) + 32
    elif to_unit == "kelvin":
        result = celsius + 273.15
    else:
        result = celsius

    print(f"\n  {value} {from_unit} = {result:.4f} {to_unit}\n")

# ---------- Main ----------

def main():
    print("=" * 35)
    print("        Unit Converter")
    print("=" * 35)
    print()
    while True:
        print("[1] Length  [2] Weight  [3] Temperature  [4] Exit")
        choice = input("\nChoice: ").strip()
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("\nGoodbye.")
            sys.exit(0)
        else:
            print("\n  Enter 1 to 4.\n")

if __name__ == "__main__":
    main()
