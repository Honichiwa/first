
print("")
print("DC Watts-Amps-Watts calculator")
print("")
electrical_m = input(
    "Type in conversion type: \n \n A - Watts to Amps \n W - Amps to Watts \n \n A/W? : ")

if electrical_m == "A" or electrical_m == "a" \
        or electrical_m == "W" or electrical_m == "w":
    voltage = input("\n Type in systems voltage: ")
    if int(voltage) > 0:
        if electrical_m == "A" or electrical_m == "a":
            watt = input("\n Type in Watts: ")
            amp = float(watt) / float(voltage)
            print("")
            print(f"{watt} W is equal to {amp:.02f} A.")
        elif electrical_m == "W" or electrical_m == "w":
            amp = input("\n Type in Amps: ")
            watt = float(amp) * float(voltage)
            print("")
            print(f"{amp} A is equal to {watt:.02f} W.")
    else:
        print("Incorrect voltage: restart program")

else:
    print("Incorrect selection: restart program")
