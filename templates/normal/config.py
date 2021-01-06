from cadCAD import configuration

from .psub import psubs
from .state import genesis_state

simulation_config = configuration.utils.config_sim({
    "T": range(10),
    "N": 1
})

exp = configuration.Experiment()

exp.append_configs(sim_configs=simulation_config, initial_state=genesis_state, partial_state_update_blocks=psubs)