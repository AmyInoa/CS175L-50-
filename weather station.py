#Weather Station V1
#Amy Inoa
#CS-175

#Asked for the user inputs
name = input("weather Station Name: ")
temp_F = float(input("what is the current temperature (fahrenheit)?: "))
wind_speed = int(input("what is the wind speed?: "))
wind_dir = input("what is the wind direction?: ")
temp_C = (temp_F-32)*(5/9)

#Make strings that can be formatted
STR_NAME = name + " Weather Station"
STR_FAHRENHEIT = "temperature(fahrenehit)"
STR_CELSIUS = "temperature(Celsius)"
STR_SPEED = "Wind speed(mph)"
STR_DIR = "wind direction"

#Print out the formatted weather report
print(f"\n\t{STR_NAME}\n")
print(f"{STR_FAHRENHEIT+':':>24}",f"{temp_F:<.1f}")
print(f"{STR_CELSIUS+':':>24}",f"{temp_C:<.1f}")
print(f"{STR_SPEED+':':>24}",f"{wind_speed:<}")
print(f"{STR_DIR+':':>24}",f"{wind_dir:<}")



    
