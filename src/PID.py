def proportional_control(target, current, kP):
    error = target - current
    output = error * kP
    return output

def angle_error(target, current):
    error = target - current
    while error > 180:
        error -= 360
    while error < -180:
        error += 360
    return error


def proportional_turn(target, current, kP):
    error = angle_error(target, current)
    output = error * kP
    return output
