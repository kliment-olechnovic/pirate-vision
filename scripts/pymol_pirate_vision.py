from pymol import cmd, util

def pirate(speed=90):
    speed = float(speed)

    if speed == 0:
        cmd.mstop()
        return

    fps = cmd.get_setting_float('movie_fps') or 30
    frames = max(2, round(360 * fps / abs(speed)))

    cmd.mstop()
    cmd.mset(f"1 x{frames}")
    util.mroll(1, frames, 1, '-y' if speed > 0 else 'y')
    cmd.set('movie_loop', 1)
    cmd.mplay()

cmd.extend('pirate', pirate)
