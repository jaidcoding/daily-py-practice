"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

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
