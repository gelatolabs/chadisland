screen map:
    imagemap:
        ground "map.jpg"
        hover "map-hover.jpg"
        
        hotspot (341, 60, 75, 75) clicked Jump("beachHut")
        hotspot (1030, 148, 75, 75) clicked Jump("stacyHut")
        hotspot (1135, 327, 75, 75) clicked Jump("chiefHut")
        hotspot (1250, 664, 75, 75) clicked Jump("plaidHut")
        hotspot (1395, 714, 75, 75) clicked Jump("shamanHut")
        hotspot (558, 42, 83, 82) clicked Jump("communism")
        hotspot (610, 227, 104, 122) clicked Jump("bar")
        hotspot (1035, 451, 141, 147) clicked Jump("gym")
        hotspot (1394, 478, 108, 95) clicked Jump("aaa")
        hotspot (1260, 122, 263, 179) clicked Jump("chopper")

label start:
    python:
        pname = renpy.input("What is your name, bro?", "Anonymous Coward").strip()

    scene bg chiefHutOutside with fade 
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
    
    scene bg chiefHut with fade
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
    oc "You actually think you, some brand new baby-Chad, have a chance of beating me? Hahahaha! Do you even lift, bruh?"
    mc "I will defeat you Chieftain, for you see, whilst you were out partying and drinking, {i}I{/i} was studying {b}The Blade{/b}!"
    oc "Oh Sun God, I can't breathe! This is too funny! Bwahahaha! Agh, my chest! I can't stop laughing! Hahahaha! *cough* Ha... Ha... *cough* Ha...  *cough*"
    show oc normal at right
    "The Chieftain falls over clutching his chest and lays still."
    show oc at chide
    show oc dead at center with dissolve
    mc "Holy crap! I killed the Chieftain! I won!"
    show brad normal at right with dissolve
    brad "Hey Chief, Rad and I were going to go shred some waves if you wanted to... Oh my Sun God! [pname], you killed the Chieftain, bro!"
    mc "That's right, Brad. Look at me, I'm the Chieftain now!"
    brad "Oh man, well, I guess we'll have to hold the coronation ceremony. I'll go get the Shaman, broski."
    show brad at chide
    hide brad
    mc "This is the greatest day of my life!"
    show mc at chide
    show oc at chide
    hide mc
    hide oc

    scene bg beach with fade
    show oc dead at left
    show mc normal at center
    show shaman normal at right
    shaman "By the power vested in me by His Holy Chadness, Chad the Sun God, I bestow upon you the title of Master Chad, and pronounce you the new Chieftain of Chad Island!"
    shaman "Your new duties as Chieftain are as follows:" 
    shaman "1. Protect the island from any bogus bros or babes."
    shaman "2. Pray to His Holy Chadness, Chad the Sun God." 
    shaman "And 3. Do whatever it takes to keep His Holy Chadness happy, even if it means sacrificing somebody into the volcano." 
    shaman "Good luck new Chieftain, may your reign be long and hard."
    show shaman at chide
    hide shaman
    mc "Alright! And as my first act as a chieftain, I summon the brodacious babe, Stacy."
    show stacy normal at right with dissolve
    stacy "Uh, hi [pname]. Congrats, I guess..."
    mc "So, Stacy, now that I'm Chieftain, how about you and I get to know each other a little better."
    mc "If you know what I'm saying ;)"
    show stacy annoyed at right
    stacy "Uh, thanks, but no. I've already got my eyes on Vlad. He's way more Chad than you'll ever be. BYE!"
    show stacy at chide
    hide stacy
    mc "Aw man, that is totally brogus. Even when I'm Chieftain she still turns me down."
    hide mc
    
    scene bg chiefHut with fade
    show mc normal
    mc "I can't believe Stacy would choose Vlad over me!"
    mc "Man, if only Vlad wasn't around. Then Stacy would see that I'm clearly the biggest Chad on this island."
    mc "Wait a second... That's it! I'll use my new powers as Chieftain and sacrifice him to the volcano. Then Stacy will have to date me!"
    mc "But first I've gotta find some dirt on him..."
    call screen map

label beachHut:
    scene bg beach
    "beach"
    call screen map

label stacyHut:
    scene bg stacyHut
    "stacy's hut"
    call screen map

label chiefHut:
    scene bg chiefHut
    "chief's hut"
    call screen map

label plaidHut:
    scene bg plaidHut
    "plaid's hut"
    call screen map

label shamanHut:
    scene bg shamanHut
    "shaman's hut"
    call screen map

label communism:
    scene bg communism
    "communism"
    call screen map

label bar:
    scene bg bar
    "bar"
    call screen map

label gym:
    scene bg gym
    "gym"
    call screen map

label aaa:
    scene bg aaa
    "alpha alpha alpha frat"
    call screen map

label chopper:
    scene bg chopper
    "chopper"
    call screen map
