

print("\nDC Watts-Amps-Watts converter")

electrical_m = input(
    "\nType in conversion type: \n \nA - Watts to Amps \nW - Amps to Watts \n \nA/W? : ")

if electrical_m.lower() == "a" or electrical_m == "w":
    try:
        voltage = float(input("\nType in systems voltage: "))

    except ValueError:
        print("\nIncorrect voltage: restart program")

    if electrical_m.lower() == "a":
        watt = float(input("\nType in Watts: "))
        amp = float(watt) / float(voltage)
        print(f"\n{watt} W is equal to {amp:.02f} A in {voltage} Voltage DC system.")

    elif electrical_m.lower() == "w":
        amp = float(input("\nType in Amps: "))
        watt = float(amp) * float(voltage)
        print(f"\n{amp} A is equal to {watt:.02f} W in {voltage} Voltage DC system.")

else:
    print("\nIncorrect selection: restart program")
