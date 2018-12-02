﻿define mc = Character("[pname]", color="#F6A6FF")
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

screen map:
    imagemap:
        ground "map.png"
        hover "map-hover.png"
        
        hotspot (1266, 526, 300, 455) clicked Jump("volcano")

label start:
    play music "sound/main.mp3"

    python:
        pname = renpy.input("Who are you?", "Anonymous Coward").strip()

    scene bg intro with dissolve
    show mc katana at center
    mc "Yo whaddup it's ya boi [pname]! Just finished my Chad training and ready to slay some serious puss!"
    mc "Hey Stacy, how's it hanging gurl?"
    show mc katana at left
    show stacy annoyed at right
    stacy "Oh... hi there [pname]. I was actually just on my way to see the Chieftain, sooo bye."
    hide stacy
    mc "God dang Chieftain, always cock blocking me! Now that I'm a full-fledged Chad it's time I show him who the real Chad is!"
    hide mc
    
    scene bg mountainHut with fade
    show stacy normal at left
    show oc normal at right
    stacy "K bye Chief."
    oc "Bye Stacy."
    hide stacy
    show mc katana at left
    mc "Yo Chieftain! Where you at!?!"
    oc "Ah, [pname]. How is my favourite non-Chad? Still can't get any girls?"
    mc "Joke's on you, Chieftain, I'm officially a Chad now!"
    oc "I guess the Shaman is just letting anyone become a Chad now, huh."
    mc "That's it! I'm done being the joke of this island! I challenge you to a Chad-Off!"
    oc "A Chad-Off??? You're challenging me to be Chieftain? Bwahahahahaha! This is too rich! You actually think you, some brand new baby-Chad, has a chance of beating me? Hahahaha!"
    mc "I will defeat you Chieftain, for you see, whilst you were out partying and drinking, {i}I{/i} was studying {b}The Blade{/b}!"
    oc "Oh Sun God, I can't breathe! This is too funny! Bwahahaha! Agh, my chest! I can't stop laughing! Hahahaha! *cough* Ha... Ha... *cough* Ha...  *cough*"
    "The Chieftain falls over clutching his chest and lays still."
    show oc dead at center
    mc "Holy crap! I killed the Chieftain! I won!"
    show brad normal at right
    brad "Hey Chief, Rad and I were going to go shred some waves if you wanted to... Oh my Sun God! [pname], you killed the Chieftain!"
    mc "That's right, Brad. Look at me, I am the Chieftain now!"
    brad "Oh man, well, I guess we'll have to hold the coronation ceremony. I'll go get the Shaman."
    hide brad
    mc "This is the greatest day of my life!"

    scene bg ceremony with fade
    show oc dead left
    show mc center normal
    show shaman normal right
    shaman "By the power vested in me by His Holy Chadness, Chad the Sun God, I bestow upon you the title of Master Chad, and pronounce you the new Chieftain of Chad Island!"
    
    

label map:
    call screen map

label volcano:
    scene bg volcano
    "volcano"
    jump map
