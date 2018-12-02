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

image gelato = "images/gelato.png"

image LDtext:
    Text("Made for Ludum Dare 43 \n{i}Sacrifices Must Be Made")

define audio.main = "sound/main.mp3"
define config.main_menu_music = "sound/main.mp3"

transform menu_bg_move:
    subpixel True
    topleft
    ypos -500
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset 194 yoffset 485
        repeat

image menu_bg:
    topleft
    alpha 0.5
    "images/menu_tile.png"
    menu_bg_move