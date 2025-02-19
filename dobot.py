import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

DOBOT_CR5_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/mnt/storage/assets/robot/assembled_robots/dobot_assembly.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "joint1": 0,
            "joint2": 0,
            "joint3": 0,
            "joint4": 0.0,
            "joint5": 0,
            "joint6": 0,
            "robotiq_85_right_knuckle_joint": 0.0,
            # "robotiq_85_right_inner_knuckle_joint": 0.0,
            # "robotiq_85_left_inner_knuckle_joint": 0.0,
            "robotiq_85_left_knuckle_joint": 0.0,
        },
    ),
    actuators={
        "cr5_shoulder": ImplicitActuatorCfg(
            joint_names_expr=["joint[1-3]"],
            effort_limit=87.0,
            velocity_limit=2.175,
            stiffness=80.0,
            damping=4.0,
        ),
        "cr5_forearm": ImplicitActuatorCfg(
            joint_names_expr=["joint[4-6]"],
            effort_limit=12.0,
            velocity_limit=2.61,
            stiffness=80.0,
            damping=4.0,
        ),
        "cr5_hand": ImplicitActuatorCfg(
            joint_names_expr=[
                "robotiq_85_right_knuckle_joint",
                # "robotiq_85_right_inner_knuckle_joint",
                # "robotiq_85_left_inner_knuckle_joint",
                "robotiq_85_left_knuckle_joint",
            ],
            effort_limit=200.0,
            velocity_limit=0.2,
            stiffness=2e3,
            damping=1e2,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)

DOBOT_CR5_HIGH_PD_CFG = DOBOT_CR5_CFG.copy()
DOBOT_CR5_HIGH_PD_CFG.spawn.rigid_props.disable_gravity = True
DOBOT_CR5_HIGH_PD_CFG.actuators["cr5_shoulder"].stiffness = 400.0
DOBOT_CR5_HIGH_PD_CFG.actuators["cr5_shoulder"].damping = 80.0
DOBOT_CR5_HIGH_PD_CFG.actuators["cr5_forearm"].stiffness = 400.0
DOBOT_CR5_HIGH_PD_CFG.actuators["cr5_forearm"].damping = 80.0
