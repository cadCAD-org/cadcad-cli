import cadCAD

from .psub import psubs
from .state import genesis_state

simulation_config = cadCAD.configuration.utils.config_sim({
    "T": range(10),
    "M": 1
})

exp = cadCAD.configuration.Experiment()

exp.append_configs(sim_configs=simulation_config, initial_state=genesis_state, partial_state_update_blocks=psubs)