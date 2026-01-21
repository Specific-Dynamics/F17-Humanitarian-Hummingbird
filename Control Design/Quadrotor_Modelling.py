import math

##########################################################################################################

# Planning and Reference

##########################################################################################################

# Equations and method from Advances in Unmanned Aerial Vehicles: State of the Art and the Road to Autonomy (2007), Chapter 6
# Other modeling: 
#   https://www.researchgate.net/publication/343309950_Modeling_Control_and_Simulation_of_Quadrotor_UAV
#   https://www.sciencedirect.com/science/article/pii/S1367578823000640
#   https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=885341

# IMU Datasheet: https://invensense.tdk.com/wp-content/uploads/2022/07/DS-000330-ICM-40609-D-v1.2.pdf
# ARHS: https://files.microstrain.com/product_datasheets/3DM-GX3-25_datasheet_version_1.07a.pdf

# Might want to use an ARHS instead of an IMU for less processing. Madgwick is for working with raw
# IMU data to find heading and attitude.

# We should consider using library implementations of code for getting the Euler angles from
# the IMU data. We could also consider learning the quaternion based implementation to avoid
# some of the errors with the explosion of the trig. functions, also the computational overhead
# is supposedly lower with quaternions beacuse we avoid needing to call trig. functions.

# Madgwick Filter: https://x-io.co.uk/downloads/madgwick_internal_report.pdf
# C Madgwick Implementation to steal: https://github.com/mongoose-os-libs/imu/blob/master/src/madgwick.c
# Supposed Madgwick filter implementation would return attiude as a quaternion which could be converted
# into Euler angles for use in the model developed in the textbook paper. Also returns angular acceleration 
# data and directional acceleration which we should be able to integrate to get relative velocity and relative 
# position.

##########################################################################################################

# Control Variables

##########################################################################################################

# Motivation: Feedback will control the RPM on each of the rotors

# The original paper recommends integral-backstepping
# With integral-backstepping, the Lyapunov function is used to maintain stability
# We also want the integral and derivative values of pretty much every error 

# Each of the derivative values essentially implements a PID

# Attitude Control
#   Setpoints:
#       Attitude (3-axis)
#       Angular velocity (3-axis) 

# Altitude Control
#   Setpoints:
#       Altitude (1-axis)
#       Climb (1-axis)

# Position Control
#   Setpoints:
#       Position (2-axis)
#       Speed (2-axis)

##########################################################################################################

# Pseudocode

##########################################################################################################

# Attitude Control
roll_tracking_error = roll_tracking_error
pitch_tracking_error = pitch_tracking_error
yaw_tracking_error = yaw_tracking_error

##########################################################################################################

# Model Parameters

##########################################################################################################

MAX_MASS: float = 100 # g
MAX_SPAN: float # mm
TARGET_THRUST_TO_WEIGHT: float

AIR_DENSITY: float = 1.225 # kg/m^3
SOLIDITY_RATIO: float
LIFT_SLOPE: float
ROTOR_ADVANCE_RATIO: float
INFLOW_RATIO: float
INDUCED_VELOCITY: float 
ROTOR_RADIUS: float
ROTOR_SPEED: float = 3e4 # RPM (Approximate)
ROTOR_AREA: float
PITCH_OF_INCIDENCE: float
TWIST_PITCH: float
AVERAGE_DRAG_COEFFICIENT: float

##########################################################################################################

# Equations for Modelling a Quadrotor

##########################################################################################################

# Solidity ratio is the ratio of area of the blades to the total area of the roto
def solidity_ratio(rotor_radius: float, avg_chord: float, num_blades: int) -> float:
    return num_blades * avg_chord  / (math.pi * rotor_radius)

def pitch_to_twist(pitch: float, rotor_radius: float) -> float:
    circumference = 2 * rotor_radius * math.pi
    twist_angle = math.atan(pitch / circumference)
    return twist_angle

# For simplification, thrust coefficient is set at 0.1
def thrust_force(
        thrust_coefficient: float,
        air_density: float,
        rotor_area: float,
        rotor_speed: float,
        rotor_radius: float,
            ) -> float:
    thrust = thrust_coefficient * air_density * rotor_area * (rotor_speed * rotor_radius) ** 2
    return thrust

##########################################################################################################

# Propeller Class

##########################################################################################################

class Propeller():
    def __init__(self, diameter: float):
        self.radius = diameter / 2 # mm

##########################################################################################################

# Main

##########################################################################################################


def main() -> None:
    # 2512 Hurricane PC 3 Blade 
    Hurricane = Propeller(diameter=63.5e-3)
    # GEMFAN D51
    D51 = Propeller(diameter=50.3e-3)
    # GEMFAN 2512
    GEMFAN2512 = Propeller(diameter=63.76e-3)

    propellers = [Hurricane, D51, GEMFAN2512]

    for propeller in propellers:
        rotor_area = math.pi * (propeller.radius) ** 2
        thrust = thrust_force(
            thrust_coefficient=0.1,
            air_density=AIR_DENSITY,
            rotor_area=rotor_area,
            rotor_speed=ROTOR_SPEED,
            rotor_radius=propeller.radius
            )
        total_thrust = thrust * 4
        print(total_thrust)


if __name__ == "__main__":
    main()