from Rocket import env ,Pioneer5K,kilakila,fin,rail_buttons,main,drogue,test


from rocketpy.stochastic import (
    StochasticEnvironment,
    StochasticSolidMotor,
    StochasticRocket,
    StochasticFlight,
)


stochastic_motor = StochasticSolidMotor(
    solid_motor=Pioneer5K,
    burn_start_time=(0, 0.1, "binomial"),
    grains_center_of_mass_position=0.295,
    grain_density=1608,
    grain_initial_height=164 / 1000,
    grain_initial_inner_radius=45 / 1000,
    grain_outer_radius=45 / 1000,
    total_impulse=(4833, 100),
    throat_radius=9 / 1000,
    nozzle_radius=18 / 1000,
    nozzle_position=0,
)
#stochastic_motor.visualize_attributes()
sampled_motor = stochastic_motor.create_object()
print(sampled_motor)
print("Deterministic Motor with nominal values:\n")
Pioneer5K.prints.all()
print("\n\nSampled Motor considering uncertainties:\n")
sampled_motor.prints.all()