from .firestation import draw_firestation
from .hospital import draw_hospital
from .policestation import draw_policestation

def draw_safety():
    draw_firestation()
    draw_hospital(13)
    draw_policestation()
    return
