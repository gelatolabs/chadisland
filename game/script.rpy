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

screen map:
    imagemap:
        ground "map.png"
        hover "map-hover.png"
        
        hotspot (1266, 526, 300, 455) clicked Jump("volcano")

label start:

    python:
        pname = renpy.input("What is your name, bro?", "Anonymous Coward ").strip()

    scene bg intro with fade 
    show mc normal at center with dissolve
    mc "Yo whaddup, it's ya boi [pname]! Just finished my Chad training and ready to slay some serious puss!"
    mc "Hey Stacy, wuss poppin' b?"
    show mc normal at left with dissolve
    show stacy annoyed at right with dissolve
    stacy "Oh... hi there [pname]."
    stacy "I was actually just on my way to see the Chieftain, sooo bye."
    show stacy at chide
    hide stacy
    mc "God dang Chieftain, always cockblocking me!" 
    mc "Now that I'm a full-fledged Chad it's time I show him who the real Chad is!"
    show mc at chide
    hide mc
    
    scene bg mountainHut with fade
    show stacy normal at left with dissolve
    show oc normal at right with dissolve
    stacy "K bye Chief, see you after morning pilates."
    oc "Later Babe."
    show stacy at chide
    hide stacy
    mc "Yo Chieftain! Where you at!?!"
    show mc normal at left
    oc "Ah, [pname]. How is my favourite Chadlet? Still can't get any girls?"
    mc "Joke's on you, Chieftain, I'm officially a Chad now!"
    oc "I guess the Shaman is just letting anyone Chad up now, huh."
    mc "That's it! I'm done being the joke of the island! I challenge you to a Chad-off!"
    show oc laugh at breathing
    oc "A Chad-off??? You're challenging {b}ME{/b} to be Chieftain? Bwahahahahaha! This is too rich!" 
    oc "You actually think you, some brand new baby-Chad, has a chance of beating me? Hahahaha!"
    mc "I will defeat you Chieftain, for you see, whilst you were out partying and drinking, {i}I{/i} was studying {b}The Blade{/b}!"
    oc "Oh Sun God, I can't breathe! This is too funny! Bwahahaha! Agh, my chest! I can't stop laughing! Hahahaha! *cough* Ha... Ha... *cough* Ha...  *cough*"
    show oc normal at right
    "The Chieftain falls over clutching his chest and lays still."
    show oc at chide
    show oc dead at center with dissolve
    mc "Holy crap! I killed the Chieftain! I won!"
    show brad normal at right with dissolve
    brad "Hey Chief, Rad and I were going to go shred some waves if you wanted to... Oh my Sun God! [pname], you killed the Chieftain!"
    mc "That's right, Brad. Look at me, I am the Chieftain now!"
    brad "Oh man, well, I guess we'll have to hold the coronation ceremony. I'll go get the Shaman, bro."
    show brad at chide
    hide brad
    mc "This is the greatest day of my life!"
    show mc at chide
    show oc at chide
    hide mc
    hide oc

    scene bg ceremony with fade
    show oc dead at left
    show mc normal at center
    show shaman normal at right
    shaman "By the power vested in me by His Holy Chadness, Chad the Sun God, I bestow upon you the title of Master Chad, and pronounce you the new Chieftain of Chad Island!"
    mc "Hell yeah, I'm gonna make this island great again!"
    shaman "Your new duties as Chieftain are as follows:" 
    shaman "1. Protect the island from any bogus bros or babes."
    shaman "2. Pray to His Holy Chadness, Chad the Sun God." 
    shaman "And 3. Do whatever it takes to keep His Holy Chadness happy, even if it means sacrificing somebody into the volcano." 
    shaman "Good luck new Chieftain, may your rein be long and hard."
    show shaman at chide
    hide shaman
    mc "Alright! And as my first act as a chieftain, I summon the bodacious babe, Stacy."
    show stacy normal at right with dissolve
    stacy "Uh, hi [pname]. Congrats, I guess..."
    mc "So, Stacy, now that I'm Chieftain, how about you and I get to know each other a little better."
    mc "If you know what I'm saying ;)"
    show stacy annoyed at right
    stacy "Uh, thanks, but no. I've already got my eyes on another hunk, and he's way more Chad than you'll ever be. BYE!"
    show stacy at chide
    hide stacy
    mc "Aw man, that is totally bogus. Even when I'm Chieftain Stacy still turns me down."

label map:
    call screen map

label volcano:
    scene bg volcano
    "volcano"
    jump map
