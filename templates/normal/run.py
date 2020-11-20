import cadCAD
import pandas

from model import configs

def run():
    exec_mode = cadCAD.engine.ExecutionMode()
    ctx = cadCAD.engine.ExecutionContext(context=exec_mode.local_mode)
    simulation = cadCAD.engine.Executor(exec_context=ctx, configs=configs)
    system_events, tensor_field, sessions = simulation.execute()

    # Post-processing
    df = pandas.DataFrame(system_events)
    df = df[df["substep"] == df.substep.max()]

    return df