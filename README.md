# Flight-Simulator

**still a work in progress!**

The idea behind this code is to provide a simple environment to refine the fine motor controls needed when flying an airplane.
This is not really a simulator, but is purely intended to work on the eye-hand/foot coordination needed when flying.
The code has been developed around my set-up which you can see below, it should be possible to modify to work on anything you may have with minimal effort.
This code is still a work in progress, I am just now getting the controller inputs to register correctly. 
The first thing I will work on will be to get the rudder pedals fully working, then the joystick and throttle.
I will get the axes working, before possibly moving into using button to control certain functionalit.
The input responses will be based on mathematical models of simplified aircraft dynamics (eventually). 

## rudder:
![anim3](https://user-images.githubusercontent.com/79390007/127248163-2e6c6465-1a48-49fc-bc0e-64fc1c10ed1d.gif)


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
