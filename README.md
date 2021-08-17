# Flight-Simulator

**still a work in progress!**

The idea behind this code is to provide a simple environment to refine the fine motor controls needed when flying an airplane.
This is not really a simulator, but is purely intended to work on the eye-hand/foot coordination needed when flying.
The code has been developed around my set-up which you can see below, it should be possible to modify to work on anything you may have with minimal effort.
This code is still a work in progress, I am just now getting the controller inputs to register correctly. 
The first thing I will work on will be to get the rudder pedals fully working, then the joystick and throttle.
I will get the axes working, before possibly moving into using button to control certain functionalit.
The input responses will be based on mathematical models of simplified aircraft dynamics (eventually). 

please note that the color of the animations if off due to the software encoding I used to generate the gif, if you run the code the target will remain visible throughout
## rudder:
![anim5](https://user-images.githubusercontent.com/79390007/129777967-38238cc0-d2dc-486b-ba6f-25fff751ab15.gif)

## stick:
![anim6](https://user-images.githubusercontent.com/79390007/129778003-1d5a94b2-56a1-4486-95be-4828a97fad35.gif)



## My Controller Set-up
CH Pro Pedals (joystick id = 0)
- axis 2 -> rudder (-1 = yaw left, 1 = yaw right)

Saitek X-56 Throttle (joystick id = 1)
- axis 0 -> roll (-1 = throttle max, 1 = throttle back)

Saitek X-56 Stick (joystick id = 2)
- axis 0 -> roll (-1 = roll left, 1 = roll right)
- axis 1 -> pitch (1 = pitch back, -1 = pitch forward)

## Disclaimer
This code has been independently developed and not verified, it is for educational purposes only. 
