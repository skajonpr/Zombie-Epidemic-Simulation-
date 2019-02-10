# Zombie-Epidemic-Simulation

This is a program simulating the rise in zombie population in the zombie epidemic event.
The objective of this study is to help authorities inform the mitigation strategie to guard against a zombie epidemic.

We assumed state variables to be susceptible, actively-infected zombie, and removed.

The model of decrease in human population is the contact rate (Beta)(contacts per day) times the product of humans H and 
zombies Z divided by the population N.

The model of increase in zombies is the contact rate times the product of humans H and zombies Z divided by 
the population N and decreases by the removal rate(zombies per day) times the number of zombies Z.

The model of increase in removed population is the removal rate(Alpha) times the number of zombies Z.

Note: This model is just to show how the simulation could help inform the strategies to solve problems. All models are assumed based on our estimation.
