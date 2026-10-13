from chimerax.core.commands import CmdDesc, FloatArg, register, run
from chimerax.core.errors import UserError

def pirate(session, speed=90):
    try:
        run(session, "perframe stop")
    except UserError as e:
        if "No per-frame command active" not in str(e):
            raise

    if speed != 0:
        run(session, f'perframe "turn y {speed / 60}"')

register(
    'pirate',
    CmdDesc(
        optional=[('speed', FloatArg)],
        synopsis='Spin the molecule for Pirate Vision'
    ),
    pirate,
    logger=session.logger
)
