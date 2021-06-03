import numpy as np
import utils
from planner import Planner
from controller import DualityController


def generate_planner():
    globalpath = np.array([[0.0, 0.2], [0.5, 0.2], [0.5, 0.8], [1.0, 0.8]])
    reference_speed = 0.4
    num_horizon = 4
    localpath_timestep = 0.1
    return Planner(globalpath, reference_speed, num_horizon, localpath_timestep)


def generate_controller():
    sys_timestep = 0.05
    sim_timestep = 0.01
    ctrl_timestep = 0.1
    vehicle_length, vehicle_width = 0.06, 0.04
    num_horizon_opt, num_horizon_cbf = 4, 4
    gamma = 0.5
    dist_margin = 0.005
    return DualityController(
        sys_timestep,
        sim_timestep,
        ctrl_timestep,
        vehicle_length,
        vehicle_width,
        num_horizon_opt,
        num_horizon_cbf,
        gamma,
        dist_margin,
    )


def generate_obstacles():
    obstacles = []
    obstacles.append(utils.RectangleRegion(0.0, 1.0, 0.85, 1.0))
    obstacles.append(utils.RectangleRegion(0.0, 0.45, 0.25, 1.0))
    obstacles.append(utils.RectangleRegion(0.55, 1.0, 0.0, 0.75))
    return obstacles


def main():
    # Planner
    planner = generate_planner()
    # Controller
    controller = generate_controller()
    controller.set_state(np.array([0.0, 0.2, 0.0, 0.0]))
    controller.set_planner(planner)
    # Add obstacles
    obstacles = generate_obstacles()
    controller.set_obstacles(obstacles)
    # Choose obstacle avoidance policy
    # controller.set_obstacle_avoidance_policy("point2region")
    controller.set_obstacle_avoidance_policy("region2region")
    # Setup simulation
    simulation_time = 5.0
    controller.sim(simulation_time)
    controller.plot_world()
    controller.plot_states()
    controller.animate_world()


if __name__ == "__main__":
    main()
