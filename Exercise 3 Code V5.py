# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:38:35 2018

@author: angus
"""

############################################################################### 


import matplotlib.pyplot as plt
import numpy as np


############################################################################### 


def valueCheckPosFloat(value):                                                  # This function checks that the user has input a positive float when they're meant to.
    
    while value.isalpha() or float(value) <= 0:
        
        print("You require a positive float!")
        value = input("Please enter a positive float: ")
    
    value = float(value)
    
    return value


############################################################################### 


g = 9.81                                                                        # Initialising the values that reamin constant throughout the program.
velocity0 = 0
time0 = 0
MyInput = "0"


############################################################################### 


while MyInput != "q":                                                           # Menu system for ease of use.
    
    print("-" * 60)
    print("\n")
    print("Option a models the falling of a 100kg sphere through air of")       # Explanations of each option.
    print("constant density and air resistance from 1km, with a time step of")
    print("0.01s. The ratio k / m for this option is 5.64e-3, where")
    print("k is the product of the drag coefficient, the air density,")
    print("and the cross-sectional area, all divided by 2.")
    print("\n")
    print("Option b allows the user to choose their own values for the mass,")
    print("the cross-sectional area, the drag coefficient, the air density,")
    print("and the starting height of the object. It then plots height and")
    print("velocity-time graphs using the values obtained from the")
    print("analytical prediction, and calculates the difference between these")
    print("heights and the Euler Method heights. It then plots a graph")
    print("showing this difference against time.")
    print("\n")
    print("Option c is essentially the same as option b, but c implements the")
    print("modified Euler method, that is, using the derivative at the")
    print("mid-point between time steps.")
    print("\n")
    print("Option d, instead of using a constant value for the air density,")
    print("considers air density a function of height, and by consequence k")
    print("also.")
    print("\n")
    print("-" * 60)
    print()
    
    MyInput = input("Enter a choice, 'a', 'b', 'c', 'd', or 'q' to quit: ")     # The user can choose which section they would like to see.
    print("\n")
    print("You entered the choice: " + MyInput)
    print("\n")
    print("-" * 60)
    
    
###############################################################################     
    
    
    if MyInput == "a":
        
        Cd = 0.47
        m = 100
        A = 1
        rho0 = 1.2
        k = (Cd * rho0 * A) / 2
        height0 = 1000
        deltat = 0.01
        
        
        height = [height0]                                                      # Lists for the height, velocity, and time.
        velocity = [velocity0]
        time = [time0]

        n = 0
        
        
        while height[-1] > 0:                                                   # Check that the end of the list is positive (for when the object reaches the ground).                            
                                                                                # The n + 1th value is appended to each list during each loop.
            velocity.append(velocity[n] - deltat * (g + k / m * 
                            abs(velocity[n]) * velocity[n]))
            
            height.append(height[n] + (deltat * velocity[n]))
            
            time.append(time[n] + deltat)
            
            n += 1
    
    
        for i in range(len(velocity)):                                          # Making the negative velocity positive.
            
            velocity[i] = abs(velocity[i])
    
    
        height.pop(0)                                                           # Popping values from the beginning and end of the lists so they're all the same length.
        velocity.pop()
        velocity.pop()
        height.pop()
        time.pop()
        time.pop()
    
    
        print()
        plt.plot(time, height)
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.show()
        plt.plot(time, velocity)
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.show()
        print("\n")
        
        
        print("\n")      
        print()
        print("The duration of the freefall was " + str(round(time[-1], 1)))    # Displaying information about the fall.
        print("seconds, or " + str(int(time[-1] / 60)) + " minutes,")
        print(str(round((time[-1] % 60), 1)) + " seconds.")
        print()
        
        print("The maximum velocity reached using the")
        print("Euler method was " + str(round(max(velocity), 1)) + "m/s,")
        print("or Mach " + str(round(max(velocity) / 343, 3)) + ".")
        print()
        print("\n")


############################################################################### 


    elif MyInput == "b":
            
        deltat = input("Enter a value for the timestep (~0.01s): ")             # The user enters their own values for this section.
        deltat = valueCheckPosFloat(deltat)
            
        print()
        print("-" * 60)
            
        m = input("Enter a value for the mass: ")
        m = valueCheckPosFloat(m)
            
        print()
        print("-" * 60)
            
        A = input("Enter a value for the cross-sectional area: ")
        A = valueCheckPosFloat(A)
            
        print()
        print("-" * 60)
        print()
            
        print("Enter a value for the drag coefficient (~0.47 for a sphere; ")
        Cd = input("~1.0 − 1.3 for a sky diver or ski jumper): ")
        Cd = valueCheckPosFloat(Cd)
            
        print()
        print("-" * 60)
        print()
            
        print("Enter a value for the air density (~1.2kg/m^3 at ambient ")
        rho0 = input("air pressure and temperature): ")
        rho0 = valueCheckPosFloat(rho0)
            
        print()
        print("-" * 60)
            
        height0 = input("Enter a value for the maximum height: ")
        height0 = valueCheckPosFloat(height0)
            
        print()
        print("-" * 60)
        print("\n")
        
        
        k = (Cd * rho0 * A) / 2
        
        height = [height0]
        velocity = [velocity0]
        time = [deltat]

        n = 0
        
        
        while height[-1] > 0:                                                   # Equations for the analytical values of the height and velocity.
            
            velocity.append(-np.sqrt((m * g) / k) * 
                            np.tanh(np.sqrt((k * g) / m) * time[n]))
            
            height.append(height0 - m / (2 * k) * np.log((np.cosh(np.sqrt((k * 
                          g) / m) * time[n])) ** 2))
            
            time.append(time[n] + deltat)
            
            n += 1
    
    
        for i in range(len(velocity)):
            
            velocity[i] = abs(velocity[i])
    
    
        velocity.pop()
        height.pop()
        time.pop()
        
        
        print()
        print("The value for the ratio k / m is " + str(k / m) + ".")
        print("\n")


        plt.plot(time, height)                                                  # Height and velocity-time graphs for the analytical values.
        plt.xlabel("Time (s)")
        plt.ylabel("Analytical height (m)")
        plt.show()
        plt.plot(time, velocity)
        plt.xlabel("Time (s)")
        plt.ylabel("Analytical velocity (m/s)")
        plt.show()
        print("\n")
        
        
        heightEuler = [height0]
        velocityEuler = [velocity0]
        timeEuler = [deltat]
        difference = []

        n = 0
        
        
        while heightEuler[-1] > 0:
            
            velocityEuler.append(velocityEuler[n] - deltat * (g + k / m *       # Calculating the Euler method values.
                            abs(velocityEuler[n]) * velocityEuler[n]))
            
            heightEuler.append(heightEuler[n] + (deltat * velocityEuler[n]))
            
            timeEuler.append(timeEuler[n] + deltat)
            
            n += 1
    
    
        for i in range(len(velocityEuler)):
            
            velocityEuler[i] = abs(velocityEuler[i])
    
    
        heightEuler.pop(0)
        heightEuler.pop()
        velocityEuler.pop()
        timeEuler.pop()
        time.pop()
        
        
        print()     
        print("| Euler Method Height (m)  | Analytical Height (m)    | Difference (m)           |")
        print("|--------------------------|--------------------------|--------------------------|")
        
        
        for i in range(len(height) - 1):                                        # Table displaying the Euler method heights, the analytical heights, and the difference between them.
            
            print("| " + str(heightEuler[i]) + " " * int(25 - 
                  len(str(heightEuler[i]))) + "| " + str(height[i]) + " " * 
                int(25 - len(str(height[i]))) + "| " + str(abs(heightEuler[i] 
                - height[i])) + " " * int(25 - len(str(abs(heightEuler[i] - 
                        height[i])))) + "|")
            
            difference.append(abs(heightEuler[i] - height[i]))
            
        
        print("\n")
        plt.plot(time, difference)                                              # Graph of difference versus time.
        plt.xlabel("Time (s)")
        plt.ylabel("Difference (m)")
        plt.show()

        
        print("\n")      
        print()
        print("The duration of the freefall was " + str(round(time[-1], 1)))   
        print("seconds, or " + str(int(time[-1] / 60)) + " minutes,")
        print(str(round((time[-1] % 60), 1)) + " seconds.")
        print()
        
        print("The maximum velocity reached using the")
        print("Euler method was " + str(round(max(velocityEuler), 1)) + "m/s,")
        print("or Mach " + str(round(max(velocityEuler) / 343, 3)) + ".")
        print()
        
        print("The maximum velocity reached using the")
        print("analytical method was " + str(round(max(velocity), 1)) + "m/s,")
        print("or Mach " + str(round(max(velocity) / 343, 3)) + ".")
        print("\n")  
        print()
       
        
###############################################################################         
        
        
    elif MyInput == 'c':                   
        
        deltat = input("Enter a value for the timestep (~0.01s): ")
        deltat = valueCheckPosFloat(deltat)
            
        print()
        print("-" * 60)
            
        m = input("Enter a value for the mass: ")
        m = valueCheckPosFloat(m)
            
        print()
        print("-" * 60)
            
        A = input("Enter a value for the cross-sectional area: ")
        A = valueCheckPosFloat(A)
            
        print()
        print("-" * 60)
        print()
            
        print("Enter a value for the drag coefficient (~0.47 for a sphere; ")
        Cd = input("~1.0 − 1.3 for a sky diver or ski jumper): ")
        Cd = valueCheckPosFloat(Cd)
            
        print()
        print("-" * 60)
        print()
            
        print("Enter a value for the air density (~1.2kg/m^3 at ambient ")
        rho0 = input("air pressure and temperature): ")
        rho0 = valueCheckPosFloat(rho0)
            
        print()
        print("-" * 60)
            
        height0 = input("Enter a value for the maximum height: ")
        height0 = valueCheckPosFloat(height0)
            
        print()
        print("-" * 60)
        print("\n")


        k = (Cd * rho0 * A) / 2
        
        height = [height0]                                                      # More lists in section c to accommodate for the heights and velocities in the middle of the timestep.
        heightmid = [height0]
        heightAnalytical = [height0]
        velocity = [velocity0]
        velocitymid = [velocity0]
        velocityAnalytical = [velocity0]
        timemid = [time0 + deltat / 2]
        difference = []
        
        n = 0
        
        
        while heightmid[-1] > 0:                                                # Adjusted algorithm for appending on values as per the modified Euler method.
            
            velocity.append(velocity[n] - deltat * (g + k / m * 
                            abs(velocity[n]) * velocity[n]))
            
            heightmid.append(height[n] + (deltat / 2) * velocity[n])
            
            velocitymid.append(velocity[n] - (deltat / 2) * (g + k / m * 
                            abs(velocity[n]) * velocity[n]))
            
            height.append(height[n] + (deltat * velocitymid[n]))
            
            timemid.append(timemid[n] + deltat)
            
            n += 1
    
    
        for i in range(len(velocitymid)):
            
            velocitymid[i] = abs(velocitymid[i])
    
    
        height.pop(0)
        heightmid.pop(0)
        heightmid.pop()
        velocity.pop()
        velocity.pop()
        velocitymid.pop()
        velocitymid.pop()
        height.pop()
        timemid.pop()
        timemid.pop()
        
        print()
        print("The value for the ratio k / m is " + str(k / m) + ".")
        print("\n")        
        
        plt.plot(timemid, heightmid)                                            # Height and velocity-time graphs for the values generated using the modified Euler method.
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.show()
        plt.plot(timemid, velocitymid)
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.show()
        print("\n")
        
        
        n = 0       
        timemid = [time0 + deltat / 2]
        
        
        while heightAnalytical[-1] > 0:
            
            velocityAnalytical.append(-np.sqrt((m * g) / k) * 
                            np.tanh(np.sqrt((k * g) / m) * timemid[n]))
            
            heightAnalytical.append(height0 - m / (2 * k) * 
                                    np.log((np.cosh(np.sqrt((k * g) / m) 
                                    * timemid[n])) ** 2))
            
            timemid.append(timemid[n] + deltat)
            
            n += 1
    
        
        for i in range(len(velocityAnalytical)):
            
            velocityAnalytical[i] = abs(velocityAnalytical[i])
           
            
        velocityAnalytical.pop()
        heightAnalytical.pop()
        heightAnalytical.pop()
        timemid.pop()
        timemid.pop()
        timemid.pop()
        
        
        print()       
        print("| Modified Euler Method Height (m)  | Analytical Height (m)    | Difference (m)           |")
        print("|-----------------------------------|--------------------------|--------------------------|")
        
        
        for i in range(len(heightAnalytical) - 1):                              # Again comparing the modified Euler method with the analytic.
                        
            print("| " + str(heightmid[i]) + " " * int(34 - 
                  len(str(heightmid[i]))) + "| " + str(heightAnalytical[i]) 
                + " " * int(25 - len(str(heightAnalytical[i]))) + "| " + 
                str(abs(heightmid[i] - heightAnalytical[i])) + " " * 
                int(25 - len(str(abs(heightmid[i] - 
                        heightAnalytical[i])))) + "|")
            
            difference.append(abs(heightmid[i] - heightAnalytical[i]))
        
        
        print("\n")
        plt.plot(timemid, difference)
        plt.xlabel("Time (s)")
        plt.ylabel("Difference (m)")
        plt.show()
        
        
        print("\n")      
        print()
        print("The duration of the freefall was " + str(round(timemid[-1], 1)))
        print("seconds, or " + str(int(timemid[-1] / 60)) + " minutes,")
        print(str(round((timemid[-1] % 60), 1)) + " seconds.")
        print()
        
        print("The maximum velocity reached was " + str(round(max(velocitymid), 1)) + "m/s,")
        print("or Mach " + str(round(max(velocitymid) / 343, 3)) + ".")
        print("\n")
        print()

        
###############################################################################         
        
        
    elif MyInput == 'd':           
        
        deltat = input("Enter a value for the timestep (~0.01s): ")
        deltat = valueCheckPosFloat(deltat)
            
        print()
        print("-" * 60)
            
        m = input("Enter a value for the mass: ")
        m = valueCheckPosFloat(m)
            
        print()
        print("-" * 60)
            
        A = input("Enter a value for the cross-sectional area: ")
        A = valueCheckPosFloat(A)
            
        print()
        print("-" * 60)
        print()
            
        print("Enter a value for the drag coefficient (~0.47 for a sphere; ")
        Cd = input("~1.0 − 1.3 for a sky diver or ski jumper): ")
        Cd = valueCheckPosFloat(Cd)
            
        print()
        print("-" * 60)
            
        rho0 = input("Enter the sea-level air density (~1.2kg/m^3): ")
        rho0 = valueCheckPosFloat(rho0)
            
        print()
        print("-" * 60)
            
        height0 = input("Enter a value for the maximum height: ")
        height0 = valueCheckPosFloat(height0)
            
        print()
        print("-" * 60)
        print("\n")
        
        
        height = [height0]
        heightmid = [height0]
        heightAnalytical = [height0]
        velocity = [velocity0]
        velocitymid = [velocity0]
        velocityAnalytical = [velocity0]
        k = [(Cd * A * rho0 * np.exp(- height0 / 7640)) / 2]                    # k is now a function of height, as such, it needs its own list.
        timemid = [time0 + deltat / 2]
                
        n = 0
        
        
        while heightmid[-1] > 0:           
            
            velocity.append(velocity[n] - deltat * (g + k[n] / m * 
                            abs(velocity[n]) * velocity[n]))
            
            heightmid.append(height[n] + (deltat / 2) * velocity[n])
            
            velocitymid.append(velocity[n] - (deltat / 2) * (g + k[n] / m * 
                            abs(velocity[n]) * velocity[n]))
            
            height.append(height[n] + (deltat * velocitymid[n]))
            
            k.append((Cd * A * rho0 * np.exp(- heightmid[n] / 7640)) / 2)
            
            timemid.append(timemid[n] + deltat)
            
            n += 1
    
        
        for i in range(len(velocitymid)):            
            
            velocitymid[i] = abs(velocitymid[i])
    
        
        height.pop(0)
        heightmid.pop(0)
        heightmid.pop()
        velocity.pop()
        velocity.pop()
        velocitymid.pop()
        velocitymid.pop()
        height.pop()
        k.pop()
        k.pop()
        timemid.pop()
        timemid.pop()
        
        
        plt.plot(timemid, heightmid)
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.show()
        plt.plot(timemid, velocitymid)
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.show()
        
        
        print("\n")      
        print()
        print("The duration of the freefall was " + str(round(timemid[-1], 1)))
        print("seconds, or " + str(int(timemid[-1] / 60)) + " minutes,")
        print(str(round((timemid[-1] % 60), 1)) + " seconds.")
        print()
        
        print("The maximum velocity reached was " + str(round(max(velocitymid), 1)) + "m/s,")
        print("or Mach " + str(round(max(velocitymid) / 343, 3)) + ".")
        print("\n")
        print()
                
        
###############################################################################         
        
        
    elif MyInput != 'q':        
        
        print("\n")
        print("Please enter a valid input!")
        print("\n")
        
        
###############################################################################     
        
        
print("\n")
print("later tater :)")
print("\n")
print("-" * 60)
        
        
###############################################################################         
        
        
  
    
    
    
    
    
    
    
    
    
    
    