import time

_last_alert = {
    "cpu": 0,
    "ram": 0,
}

COOLDOWN = 30  # segundos


def cpu_alert(cpu):
    now = time.time()

    if cpu > 80 and now - _last_alert["cpu"] > COOLDOWN:
        _last_alert["cpu"] = now
        return True

    return False


def ram_alert(ram):
    now = time.time()

    if ram > 80 and now - _last_alert["ram"] > COOLDOWN:
        _last_alert["ram"] = now
        return True

    return False
