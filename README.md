# Yeast Calculator
A simple cell count calculator. Able to calculate starting concentration, final concentration, duration of growth, doubling time and dilutions.

## Requirements:
Python, tkinter, math

## Using the Calculator
Running the program will cause a tkinter window to appear. The drop down menu provides the options for types of calculations: including starting concentration, final concentration, duration of growth, doubling time and dilution. 

The calculation of interest can be selected and the inputs can be entered according to the descriptions and units provided. The calculation will be performed and the result displayed after the 'OK' button is clicked.

For the starting concentration calculation after clicking the 'OK' button, a dilution calculator will appear. If the current concentration of the culture is higher than that of the desired starting concentration, the current culture's concentration and the desired final volume can be entered to calculate the dilution to the calculated starting concentration.

## Calculations

Calculations for starting concentration, final concentration, duration and doubling time are derived from the equation:
final_concentration = starting_concentration * 2 ^(duration / doubling_time)

Calculations for dilutions were derived using the equation:
C1 * v1 = C2 * v2


## Author
**Sophie Campione**
