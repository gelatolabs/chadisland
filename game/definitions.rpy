define mc = Character("[pname]", color="#F6A6FF")
define oc = Character("Chieftain", color="#D5AAFF")
define shaman = Character("Shaman", color="#ECD4FF")
define stacy = Character("Stacy", color="#DCD3FF")
define sg = Character("Chad the Sun God, His Holy Chadness", color="#B5B9FF")
define brad = Character("Brad", color="#97A2FF")
define thad = Character("Thad", color="#AFCBFF")
define glad = Character("Glad", color="#85E3FF")
define dad = Character("Dad", color="#ACE7FF")
define vlad = Character("Vlad", color="#6EB5FF")
define chadski = Character("Comrade Chadski", color="#BFFCC6")
define plaid = Character("Plaid", color="#DBFFD6")
define rad = Character("Rad", color="#E7FFAC")
define shad = Character("Shad", color="#FFBEBC")
define sad = Character("Sad", color="#FFCBC1")
define gad = Character("Ga(y)d(e)", color="#FFFFD1")

image mc normal = "/images/mc/normal.png"
image mc katana = "/images/mc/katana.png"
image brad normal = "/images/brad/normal.png"
image oc normal = "/images/chieftain/normal.png"
image oc laugh = "/images/chieftain/laughing.png"
image oc dead = "/images/chieftain/dead.png"
image stacy normal = "/images/stacy/normal.png"
image stacy annoyed = "/images/stacy/normal.png" # replace me
image sungod normal = "/images/sungod/normal.png"
image rad normal = "/images/rad/normal.png"
image vlad normal = "/images/vlad/normal.png"
image dad normal = "/images/dad/normal.png"
image gad normal = "/images/gad/normal.png"
image plaid normal = "/images/plaid/normal.png"
image shaman normal = "/images/shaman/normal.png"
image chadski normal = "/images/chadski/normal.png"

image gelato = "images/gelato.png"

image LDtext:
    Text("Made for Ludum Dare 43 \n{i}Sacrifices Must Be Made")

image strikes:
    Text("Strikes Remaining: \n {b}[strikecount]{/b}", style="strike_style")
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0

style strike_style:
    xpos 0.1
    ypos 0.9
    size 45
    outlines [ (2, "#fff", 0, 0)]

define audio.main = "sound/main.mp3"
define config.main_menu_music = "sound/main.mp3"

transform menu_bg_move:
    subpixel True
    topleft
    ypos -500
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset 300 yoffset 600
        repeat 5

image menu_bg:
    topleft
    alpha 0.5
    choice:
     "images/menu_tile.png"
    choice:
     "images/menu_tile2.png"
    choice:
     "images/menu_tile3.png"
    subpixel True
    topleft
    ypos -500
    parallel:
        xoffset 0 yoffset 0
        choice:
           linear 3.0 xoffset 300 yoffset 600
        choice:
           linear 3.0 xoffset -300 yoffset 600
    repeat

transform chide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.90 alpha 0.00 yoffset -30

transform breathing(x=640, z=0.80):
    easein .2 yoffset -10
    easeout .2 yoffset 0
    repeat
