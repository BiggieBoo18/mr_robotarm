from gym.envs.registration import register

register(
    id='mr_robotarm_env-v0',
    entry_point='mr_robotarm_envs.env_v0:MrRobotarmEnv'
)
