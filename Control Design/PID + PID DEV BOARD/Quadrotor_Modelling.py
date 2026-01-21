
# Equations and method from Advances in Unmanned Aerial Vehicles: State of the Art and the Road to Autonomy (2007), Chapter 6
# Other modeling: 
#   https://www.researchgate.net/publication/343309950_Modeling_Control_and_Simulation_of_Quadrotor_UAV
#   https://www.sciencedirect.com/science/article/pii/S1367578823000640

# Equations for Modelling a Quadrotor

# How much do we care about

# Section 6.4.1 details 3 important design contstraints:
#   1. Maximum Mass
#   2. Maximum Span
#   3. Target Thrust-to-Weight Ratio

# Model Parameters

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
ROTOR_SPEED: float
ROTOR_AREA: float
PITCH_OF_INCIDENCE: float
TWIST_PITCH: float
AVERAGE_DRAG_COEFFICIENT: float

# Equations

def thrust_force(
        thrust_coefficient: float,
        air_density: float,
        rotor_area: float,
        rotor_speed: float,
        rotor_radius: float,
            ) -> float:
    thrust = thrust_coefficient * air_density * rotor_area * (rotor_speed * rotor_radius) ** 2
    return thrust

def thrust_coefficient(
        solidity_ratio: float,
        lift_slope: float,
        rotor_advance_ratio: float,
        pitch_of_incidence: float,
        twist_pitch: float,
        inflow_ratio: float,
            ) -> float:
    thrust_coefficient = solidity_ratio * lift_slope * ()

def main() -> None:
    pass

if __name__ == "__main__":
    main()