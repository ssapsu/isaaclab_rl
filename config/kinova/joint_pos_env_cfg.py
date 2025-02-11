from isaaclab.assets import RigidObjectCfg
from isaaclab.sensors import FrameTransformerCfg
from isaaclab.sensors.frame_transformer.frame_transformer_cfg import OffsetCfg
from isaaclab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg
from isaaclab.sim.spawners.from_files.from_files_cfg import UsdFileCfg
from isaaclab.utils import configclass
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

from isaaclab_tasks.manager_based.classic.isaaclab_rl import mdp
from isaaclab_tasks.manager_based.classic.isaaclab_rl.lift_env_cfg import LiftEnvCfg

from isaaclab.markers.config import FRAME_MARKER_CFG  # isort: skip
from isaaclab_assets.robots.kinova import KINOVA_GEN3_CFG # isort: skip

@configclass
class KinovaCubeLiftEnvCfg(LiftEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # Set Kinova as robot
        self.scene.robot = KINOVA_GEN3_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        # Set actions for the specific robot type (kinova)
        self.actions.arm_action = mdp.JointPositionActionCfg(
            asset_name="robot",
            joint_names=["joint_.*"],
            scale=0.5,
            use_default_offset=True,
        )
        self.actions.gripper_actions = mdp.BinaryJointPositionActionCfg(
            asset_name="robot",
            joint_names=[
                "robotiq_85_right_knuckle_joint",
                # "robotiq_85_right_inner_knuckle_joint",
                "robotiq_85_left_knuckle_joint",
                # "robotiq_85_left_inner_knuckle_joint",
            ],
            open_command_expr={
                "robotiq_85_right_knuckle_joint": 0.0,
                # "robotiq_85_right_inner_knuckle_joint": 0.0,
                "robotiq_85_left_knuckle_joint": 0.0,
                # "robotiq_85_left_inner_knuckle_joint": 0.0,
            },
            close_command_expr={
                "robotiq_85_right_knuckle_joint": 0.85,
                # "robotiq_85_right_inner_knuckle_joint": 0.85,
                "robotiq_85_left_knuckle_joint": 0.85,
                # "robotiq_85_left_inner_knuckle_joint": 0.85,
            },
        )
        # Set the body name for the end effector
        self.commands.object_pose.body_name = "robotiq_arg2f_base_link"

        # Set Cube as object
        self.scene.object = RigidObjectCfg(
            prim_path="{ENV_REGEX_NS}/Object",
            init_state=RigidObjectCfg.InitialStateCfg(pos=[0.5, 0, 0.055], rot=[1, 0, 0, 0]),
            spawn=UsdFileCfg(
                usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Blocks/DexCube/dex_cube_instanceable.usd",
                scale=(0.8, 0.8, 0.8),
                rigid_props=RigidBodyPropertiesCfg(
                    solver_position_iteration_count=16,
                    solver_velocity_iteration_count=1,
                    max_angular_velocity=1000.0,
                    max_linear_velocity=1000.0,
                    max_depenetration_velocity=5.0,
                    disable_gravity=False,
                ),
            ),
        )

        # Listens to the required transforms
        marker_cfg = FRAME_MARKER_CFG.copy()
        marker_cfg.markers["frame"].scale = (0.1, 0.1, 0.1)
        marker_cfg.prim_path = "/Visuals/FrameTransformer"
        self.scene.ee_frame = FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Robot/base_link",
            debug_vis=False,
            visualizer_cfg=marker_cfg,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/_f85/robotiq_arg2f_base_link",
                    name="end_effector",
                    offset=OffsetCfg(
                        pos=[0.0, 0.0, 0.1034],
                    ),
                ),
            ],
        )

@configclass
class KinovaCubeLiftEnvCfg_PLAY(KinovaCubeLiftEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # disable randomization for play
        self.observations.policy.enable_corruption = False
