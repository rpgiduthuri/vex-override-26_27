def proportional_control(target, current, kP):
    error = target - current
    output = error * kP
    return output