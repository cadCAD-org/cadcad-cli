import pandas
from cadCAD import configs, engine

from model import config

def run():
    exec_mode = engine.ExecutionMode()
    ctx = engine.ExecutionContext(context=exec_mode.local_mode)
    simulation = engine.Executor(exec_context=ctx, configs=configs)
    system_events, tensor_field, sessions = simulation.execute()

    # Post-processing
    df = pandas.DataFrame(system_events)
    df = df[df["substep"] == df.substep.max()]

    return df