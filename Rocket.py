from rocketpy import Environment, SolidMotor, Rocket, Flight, NoseCone
import numpy as np
import datetime
import random
from random import sample

env = Environment(latitude=22.17475, longitude=120.89275, elevation=2)
env.set_date((2025,4,25,6))
env.set_atmospheric_model(type="Forecast", file="GFS")
"""
env = Environment(latitude=22.17475, longitude=120.89275, elevation=2)
env.set_atmospheric_model(
    type="custom_atmosphere",
    pressure=None,
    temperature=300,
    wind_u=[
        (0,0), # 5 m/s at 0 m
        (1000,0) # 10 m/s at 1000 m
    ],
    wind_v=[
        (0,0), # 5 m/s at 0 m
        (1000,0)# 10 m/s at 1000 m

    ],
)
"""
#env.plots.atmospheric_model()


Pioneer5K = SolidMotor(
    thrust_source = r"./thrustcurve.eng",
    dry_mass=9,
    dry_inertia=(0.34, 0.340, 0.02),
    nozzle_radius=18 / 1000,
    grain_number=3,
    grain_density=1608,
    grain_outer_radius= 45 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height= 164 / 1000,
    grain_separation=0,
    grains_center_of_mass_position=0.295,
    center_of_dry_mass_position=0.281798,
    nozzle_position=0,
    burn_time=6,
    throat_radius=9 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber")



kilakila = Rocket(
    radius = 165/2000,
    mass = 14.89,
    inertia=(6.321, 6.321, 0.034),
    power_off_drag="./powerOffDragCurve.csv",
    power_on_drag="./powerOnDragCurve.csv",
    center_of_mass_without_motor = 1.06,
    coordinate_system_orientation = "nose_to_tail"
)


kilakila.add_motor(Pioneer5K , position = 2.60)


kilakila.add_nose(
    length=0.66,
    kind = "ogive",
    position = 0
)

fin = kilakila.add_trapezoidal_fins(
    n = 4,
    root_chord=0.3,
    tip_chord=0.1,
    span = 0.165,
    position = 2.3

)



rail_buttons = kilakila.set_rail_buttons(
    upper_button_position = 1,
    lower_button_position = 2,
    angular_position = 45 
)

main = kilakila.add_parachute(
    name="Main",
    cd_s=5.19,
    trigger=700,
    sampling_rate=200,
    lag=2,
    noise=(0, 8.3, 0.5),
)
drogue = kilakila.add_parachute(
    name="drogue",
    cd_s=0.154,
    trigger="apogee",  # ejection at apogee
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)
test = Flight(
    rocket = kilakila, environment=env, rail_length=4, inclination=86, heading=90
)

test.export_kml(
    file_name="trajectory.kml",
    extrude=True,
    altitude_mode="relative_to_ground",
)

env.info()
#kilakila.draw()
Pioneer5K.info()

test.prints.initial_conditions()
test.prints.launch_rail_conditions()
test.prints.out_of_rail_conditions()
test.prints.burn_out_conditions()
test.prints.apogee_conditions()
test.prints.events_registered()
test.prints.impact_conditions()
test.prints.maximum_values()
test.plots.trajectory_3d()
test.speed.plot(0,test.max_time)
#test.plots.angular_kinematics_data()
#test.plots.stability_and_control_data()
#test.plots.linear_kinematics_data()
#test.plots.flight_path_angle_data()


