from isaaclab.controllers.differential_ik_cfg import DifferentialIKControllerCfg
from isaaclab.envs.mdp.actions.actions_cfg import DifferentialInverseKinematicsActionCfg
from isaaclab.utils import configclass

from . import joint_pos_env_cfg

##
# Pre-defined configs
##
from isaaclab_assets.robots.dobot import DOBOT_CR5_HIGH_PD_CFG  # isort: skip

##
# Rigid object lift environment.
##

@configclass
class DobotCubeLiftEnvCfg(joint_pos_env_cfg:DobotCubeLiftEnvCfg):
    def __post_init__(self):
        super().__post_init__()

        self.scene.robot = DOBOT_CR5_HIGH_PD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")


        # Set actions for the specific robot type (kinova)
        self.actions.arm_action = DifferentialInverseKinematicsActionCfg(
            asset_name="robot",
            joint_names=["joint.*"],
            body_name="robotiq_arg2f_base_link",
            controller=DifferentialIKControllerCfg(command_type="pose", use_relative_mode=True, ik_method="dls"),
            scale=0.5,
            body_offset=DifferentialInverseKinematicsActionCfg.OffsetCfg(pos=[0.0, 0.0, 0.107]),
        )

@configclass
class DobotCubeLiftEnvCfg_PLAY(DobotCubeLiftEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        self.observations.policy.enable_corruption = False
