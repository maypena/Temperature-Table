# May Pena

# This is a basic program that outputs a temperature table. The user inputs an
# initial temperature in Farengheit and how many lines they would like to see.
# Then those temeperatures are converted to Celcius and Kelvin and displayed.


t     = eval( input( "Enter starting temperature in Farengheit: " ) )
lin   = eval( input( "How many lines do you want for the table? " ) )
space = "                "

print()

print( "Fahrenheit        Celsius              Kelvin" )
for temp in range( t, t + lin ):
    c =  ( temp - 32 ) * 5/9
    k =  c + 273.15
    print( temp, space, int(c), space, int( k))
