define d = Character("[pname]")

screen map:
    imagemap:
        ground "map.png"
        hover "map-hover.png"
        
        hotspot (1266, 526, 300, 455) clicked Jump("volcano")

label start:
    python:
        pname = renpy.input("Who are you?", "Anonymous Coward").strip()

    scene bg fight
    show sad angry at left
    show opponent angry at right
    d "sup"
    jump map

label map:
    call screen map

label volcano:
    scene bg volcano
    "volcano"
    jump map
