from .lake import draw_lake
from .park import draw_park
from .hospital import draw_hospital

def draw_outdoors():
    draw_lake()
    draw_park()
    draw_hospital(13)
    return
