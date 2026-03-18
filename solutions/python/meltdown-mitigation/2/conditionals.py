"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone without using extra variables."""

    if (voltage * current / theoretical_max_power) * 100 >= 80:
        return "green"
    elif (voltage * current / theoretical_max_power) * 100 >= 60:
        return "orange"
    elif (voltage * current / theoretical_max_power) * 100 >= 30:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""

    if (temperature * neutrons_produced_per_second) < threshold * .90:
        return "LOW"
    elif ( temperature * neutrons_produced_per_second) <= threshold * 1.1:
        return "NORMAL"
    else:
        return "DANGER"
