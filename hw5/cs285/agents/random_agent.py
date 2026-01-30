from typing import Tuple
import numpy as np


class RandomAgent:
    def __init__(self, observation_shape: Tuple[int, ...], num_actions: int):
        super().__init__()
        self.num_actions = num_actions

    def get_action(self, *args, **kwargs):
        # TODO(student): Return a random action
        obs = args[0]
        batch_size = 1
        if len(obs.shape) > 1:
            batch_size = obs.shape[0]
        actions = np.random.randint(0, self.num_actions, batch_size)
        return actions
    
    def update(self, *args, **kwargs):
        # Update is a no-op for the random agent
        return {}
