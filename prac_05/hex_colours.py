HEX_COLOUR_TO_CODE = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "black": "#000000", "blue1": "#0000ff", "blueviolet": "#8a2be2", "brown": "#a52a2a", "cyan1": "#00ffff", "darkgoldenrod": "#b8860b"}

print(HEX_COLOUR_TO_CODE)

hex_colour = input("Hex Colour: ").lower()
while hex_colour != "":
    if hex_colour in HEX_COLOUR_TO_CODE:
        print(f"{hex_colour} in hex code is {HEX_COLOUR_TO_CODE[hex_colour]}")
    else:
        print("Invalid Hex Colour")
    hex_colour = input("Hex Colour: ").lower()
