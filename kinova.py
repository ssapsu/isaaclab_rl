import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

KINOVA_GEN3_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/mnt/storage/assets/robot/assembled_robots/kinova_robot.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "joint_1": 3.14,
            "joint_2": -0.785,
            "joint_3": 1.57,
            "joint_4": 0.0,
            "joint_5": 0.785,
            "joint_6": 1.57,
            "robotiq_85_right_knuckle_joint": 0.0,
            # "robotiq_85_right_inner_knuckle_joint": 0.0,
            # "robotiq_85_left_inner_knuckle_joint": 0.0,
            "robotiq_85_left_knuckle_joint": 0.0,
        },
    ),
    actuators={
        "gen3_shoulder": ImplicitActuatorCfg(
            joint_names_expr=["joint_[1-3]"],
            effort_limit=87.0,
            velocity_limit=2.175,
            stiffness=80.0,
            damping=4.0,
        ),
        "gen3_forearm": ImplicitActuatorCfg(
            joint_names_expr=["joint_[4-6]"],
            effort_limit=12.0,
            velocity_limit=2.61,
            stiffness=80.0,
            damping=4.0,
        ),
        "gen3_hand": ImplicitActuatorCfg(
            joint_names_expr=[
                "robotiq_85_right_knuckle_joint",
                # "robotiq_85_right_inner_knuckle_joint",
                # "robotiq_85_left_inner_knuckle_joint",
                "robotiq_85_left_knuckle_joint"],
            effort_limit=200.0,
            velocity_limit=0.2,
            stiffness=2e3,
            damping=1e2,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)

KINOVA_GEN3_HIGH_PD_CFG = KINOVA_GEN3_CFG.copy()
KINOVA_GEN3_HIGH_PD_CFG.spawn.rigid_props.disable_gravity = True
KINOVA_GEN3_HIGH_PD_CFG.actuators["gen3_shoulder"].stiffness = 400.0
KINOVA_GEN3_HIGH_PD_CFG.actuators["gen3_shoulder"].damping = 80.0
KINOVA_GEN3_HIGH_PD_CFG.actuators["gen3_forearm"].stiffness = 400.0
KINOVA_GEN3_HIGH_PD_CFG.actuators["gen3_forearm"].damping = 80.0
