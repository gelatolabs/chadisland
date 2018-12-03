label triviaWrong:
    $ strikecount = strikecount - 1
    show strikes
    "Wrong!"
    if strikecount == 0:
        "Get lost, Chadlet!"
        call screen map
    return

label start:
    python:
        pname = renpy.input("What's your name, bro?", "Anonymous Coward").strip()
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
    mc "If ya know what I mean..."
    show stacy annoyed at right
    stacy "Uh, thanks, but no. I've already got my eyes on Vlad. He's way more Chad than you'll ever be. BYE!"
    show stacy at chide
    hide stacy
    mc "Aw man, that is totally brogus. Even when I'm the Chieftain she still turns me down."
    hide mc

    scene bg chiefHut with fade
    show mc normal
    mc "I can't believe Stacy would choose Vlad over me!"
    mc "Man, if only Vlad wasn't around. Then Stacy would see that I'm clearly the biggest Chad on this island."
    mc "Wait a second... That's it! I'll use my new powers as Chieftain and sacrifice him to the volcano. Then Stacy will have to date me!"
    mc "But first I've gotta find some dirt on him..."
    $ victim = "vlad"
    $ strikecount = 3
    call screen map

label beachHut:
    scene bg beach
    show mc normal at left
    show rad normal at right
    if victim == "vlad":
        show brad normal at center

        if strikecount == 0:
            rad "Get outta here, ya Chadlet!"
            call screen map

        rad "What is up, Chief, my dude? Come to catch some sick waves?"
        mc "Thanks for the offer Rad, but I've got work to do. Can you tell me anything about Vlad?"
        rad "Sure Chief, but you're gonna have to answer some skill testing questions! This is some valuable intel we're talking about here. For true Chad eyes only."
        mc "I'll have you know I graduated top of my class in trivia school! Try me!"
        rad "That's the spirit.!"
        jump surfTriviaA

    elif victim == "plaid":
        show brad normal at center
        mc "How're the waves today?"
        rad "I've been grinding a couple sick ones this morning."
        brad "I dunno the water was a litle chilly, I felt like a brosicle out there."

    elif victim == "brad":
        mc "Hey where's brad at?"
        rad "I dunno, but my surfboard is also missing."
        mc "Alrighty, I'll go investigate."
        rad "Radical, thanks Chief."

#    elif victim == "stacy":
#        if radConvinced:
#            # ...
#            call screen map
#        elif !radConvinced:
#            # ...
#            call screen map
#        else:
#            menu:
                

label surfTriviaA:
    show strikes
    rad "What is it called when you surf with your right foot forward?"
    menu:
        "Mickey":
            call triviaWrong
            jump surfTriviaA
        "Donald":
             call triviaWrong
             jump surfTriviaA
        "Goofy":
            rad "Right on, dude! OK, one more question."
            jump surfTriviaB
        "Sora":
            call triviaWrong
            jump surfTriviaA

label surfTriviaB:
    rad "Who was the first person to surf Severn Bore in England?"
    menu:
        "Kelly Slater":
            call triviaWrong
            jump surfTriviaB
        "Jack Churchill":
            jump surfTriviaWin
        "Winston Churchill":
            call triviaWrong
            jump surfTriviaB
        "Lilo Pelekai":
            call triviaWrong
            jump surfTriviaB

label surfTriviaWin:
    rad "Alright dude, you know your stuff! Here's the intel."
    rad "We keep inviting Vlad to the beach but he bails every time!"
    brad "Super uncool, broseph!"
    rad "He never goes outside! It's like he's afraid of the sun!"
    brad "Laaame!"
    rad "Well, hope it helps. Surf's up, dude!"
    brad "See ya later Broba Fett."
    call screen map

label stacyHut:
    scene bg stacyHut
    show mc normal at left
    show stacy normal at center
    if victim == "vlad":
        show vlad normal at right
        stacy "Uh, hey [pname]. Don't you have an island to run? Vlad was just showing me his cape collection. It's on point."
    elif victim == "plaid":
        show plaid normal at right
        stacy "Uh, hey [pname]. Don't you have an island to run? Plaid was just showing me his lumber collection. He's got some real hard wood."
    elif victim == "brad":
        show brad normal at right
        stacy "Uh, hey [pname]. Don't you have an island to run? Brad was just showing me how to make the most brodacious doobies."
    elif victim == "stacy":
        show thad normal at right
        stacy "Uh, hey [pname]. Don't you have an island to run? Thad was just showing me how to properly make a toga."
    mc "Ugh fine, I'll leave you guys be."
    call screen map

label chiefHut:
    scene bg chiefHut
    show mc normal at center
    "Home sweet home, probably a good place to save the game in case I get thrown into a volcano later."
    call screen map

label plaidHut:
    scene bg plaidHut
    show mc normal at left
    if victim == "vlad":
        show plaid normal at right
        "You find Plaid chopping some wood."
        plaid "Well, well, well. If it isn't [pname]. What can I do fer ya, eh?"
        mc "Seen Vlad around recently?"
        plaid "Nah, he doesn't seem to like it around here, eh. Says there's too many sharp pointy sticks for his liking, eh."
        plaid "Don't know what that's aboot."
        mc "Strange. Oh well, catch you later."
    elif victim == "plaid":
        "Plaid must be out, let's come back later."
    else:
        "Smells like roasted Canadian in here."
    call screen map

label shamanHut:
    scene bg shamanHut
    show shaman normal at right
    show mc normal at left
    shaman "Fuck off I'm playing Minesweeper."
    call screen map

label communism:
    scene bg communism
    show mc normal at left
    show chadski normal at right
    if victim == "brad":
        mc "Have you ever seen Brad around here?"
        chadski "Da, a couple years ago he was over here all the time."
        mc "hmm, interesting. Doing what I wonder?"
        chadski "I can tell you if you can answer my questions."
        mc "I'll have you know I graduated top of my class in trivia school! Try me!"
        jump communismTriviaA
    else:
        chadski "Comrade! Fighting the good fight?"
        mc "You know it!"
        mc "You watched any good TV recently?"
        chadski "Nyet, in Soviet Chad Island you don't watch TV, TV watches you."
        mc "..."
        call screen map

label communismTriviaA:
    show strikes
    chadski "What is the best type of government?"
    menu:
        "Monarchy":
            call triviaWrong
            jump communismTriviaA
        "Republic":
             call triviaWrong
             jump communismTriviaA
        "Communism":
            chadski "Da, comrade! OK, one more question."
            jump communismTriviaB
        "Democracy":
            call triviaWrong
            jump communismTriviaA

label communismTriviaB:
    chadski "Who is the best ruler to walk this earth?"
    menu:
        "President Trump":
            call triviaWrong
            jump communismTriviaB
        "Putin":
            jump communismTriviaWin
        "Queen Elizabeth":
            call triviaWrong
            jump communismTriviaB
        "Pope Francis":
            call triviaWrong
            jump surfTriviaB

label communismTriviaWin:
    chadski "Alright comrade, you know your stuff!."
    chadski "Brad was exiled from the communist islands, because of a string of armed robberies he commited."
    chadski "Go get that сука!"
    call screen map

label bar:
    scene bg bar
    show mc normal at left
    show gad normal at right
    show sad normal at center
    if victim == "vlad":
        gad "Hey, it's [pname]! Here's to your newfound Chiefliness. Cheers!"
        sad "Cheers."
        mc "Thanks bros! Say, you wouldn't have happened to hear anything truly heinous about Vlad?"
        gad "As a matter of fact, that pale cutie refuses to eat my garlic bread! He acts like it's going to kill him!"
        sad "Truly heinous..."
        mc "Indeed, your garlic bread is unrivaled in tastiness. What a brogus bro Vlad is."
        gad "Well aren't you just a darling. Here, have a plate on the house."
        mc "Hell yeah, you rock Ga(y)d!" 
        "A mountain of garlic bread is placed before you. You spend the next 30 minutes devouring every last piece."
        gad "See you around.!"
    elif victim == "plaid":
        mc "What's this I've heard about a maple syrup contest coming up?"
        gad "We host one here a the bar every year. Plaid always wins."
        gad "After the contest his throat is so lubricated with syrup that the breakfast sausages just slide right down."
        mc "Interesting, very interesting. Thanks for the tips guys, enjoy drinking your lives away."
        gad "Will do sweet cheeks~"
        sad "I'm so sad Alexa play Despacito."
    call screen map

label gym:
    scene bg gym
    show mc normal at left
    show dad normal at center
    show shad normal at right
    shad "Chief! Got time for some weights?"
    if victim == "vlad":
        mc "No time today boys, got bigger fish to fry."
        mc "Say, heard anything strange about Vlad?"
        shad "Nah bro, don't really see him much. He tends to work out at night."
        dad "I hear it gives you better gains, might try it sometime."
        mc "Oh well, stay swole bros."
        call screen map
    elif victim == "plaid":
        if strikecount == 0:
            dad "Get outta here, ya Chadlet!"
            call screen map

        shad "What is up, Chief, my dude? Come to get swole?"
        mc "Thanks for the offer Shad, but I've got work to do. Can you tell me anything about Plaid?"
        shad "Sure Chief, but you're gonna have to answer some of Dad's skill testing questions! This is some valuable intel we're talking about here. For true Chad eyes only."
        mc "I'll have you know I graduated top of my class in trivia school! Try me!"
        shad "That's the spirit, my guy! Dad get over here and let's see if this Chadlet is worthy."
        jump pokemonTriviaA

label pokemonTriviaA:
    show strikes
    dad "Which Pokemon do I resemble most?"
    menu:
        "Gengar":
            call triviaWrong
            jump pokemonTriviaA
        "Snorlax":
            call triviaWrong
            jump pokemonTriviaA
        "Machamp":
            dad "Way to make it through this set! Just one more, push through the pain!"
            jump pokemonTriviaB
        "Beedrill":
            call triviaWrong
            jump pokemonTriviaA

label pokemonTriviaB:
    dad "Which Pokemon can learn the move strength?"
    menu:
        "Ditto":
            call triviaWrong
            jump pokemonTriviaB
        "Munchlax":
            jump pokemonTriviaWin
        "Kabuto":
            call triviaWrong
            jump pokemonTriviaB
        "Staraptor":
            call triviaWrong
            jump pokemonTriviaB

label pokemonTriviaWin:
    dad "Alright dude, you know your stuff! Here's the intel."
    dad "How does a penguin build its house?"
    mc "How is that intel?"
    dad "Igloos it together."
    shad "*laughs hysterically*"
    mc "*blank stare*"
    call screen map

label aaa:
    scene bg aaa
    show mc normal at left
    show thad normal at center
    show glad normal at right
    if victim == "vlad":
        glad "Oh wow, the Chieftain! Boy am I glad to see you!"
        thad "Hey, man! Welcome to the Alpha Alpha Alpha Fraternity! Enjoying the toga party?"
        mc "You know it! This place is rockin' as always!"
    elif victim == "plaid":
        glad "Oh wow, the Chieftain! Boy am I glad to see you!"
        thad "Hey, man! Welcome to the Alpha Alpha Alpha Fraternity! Enjoying the toga party?"
        mc "You know it! This place is rockin' as always!"
    elif victim == "brad":
        glad "Woah, last night was a blast!"
        mc "Aw man, What'd i miss?"
        thad "Only the most awesome toga party of all time! Just look at my stairs, they're absolutely shredded."
        glad "Yeah! It was so rowdy, someone smashed into the fine china and broke it all."
        mc "Wicked cool. Was Brad at the party last night?"
        thad "Now that you mention it, I saw him with a surfboard for some reason."
    else:
        glad "I'm rennovating the frat to turn it in to a giant bouncy castle!"
    call screen map

label chopper:
    scene bg chopper
    if victim == "vlad":
        "You call Vlad to the top of the volcano to be accused."
        show shaman normal at left
        show rad normal at kindaLeft
        show mc normal at center
        show gad normal at kindaRight
        show vlad normal at right
        vlad "Yo, Chiefvtain, vhy have I been summvoned here?"
        menu:
            "Accuse Vlad of being way too pale":
                jump vladAccusePale
            "Accuse Vlad of being a ghost":
                jump vladAccuseGhost
            "Accuse Vlad of being a literal vampire":
                jump vladAccuseVamp
    elif victim == "plaid":
        "You call Plaid to the top of the volcano to be accused."
        show shaman normal at left
        show dad normal at kindaLeft
        show mc normal at center
        show gad normal at kindaRight
        show plaid normal at right
        plaid "How ya doin' [pname], lovely day for a helicopter ride, eh?"
        plaid "Why'd ya call me up here anyway, eh?"
        menu:
            "Accuse Plaid of being American":
                jump accuseplaidAmerican
            "Accuse Plaid of being Japanese":
                jump accuseplaidJapanese
            "Accuse Plaid of being Canadian":
                jump accuseplaidCanadian
            "Accuse Plaid of being Russian":
                jump accuseplaidRussian
    elif victim == "brad":
        "You call Brad to the top of the volcano to be accused."
        show shaman normal at left
        show rad normal at kindaLeft
        show mc normal at center
        show chadski normal at kindaRight
        show brad normal at right
        brad "How ya doin' [pname], lovely day for a helicopter ride, eh?"
        brad "Why'd ya call me up here anyway, eh?"
        menu:
            "Accuse Brad of being too high.":
                jump accuseBradWeed
            "Accuse Brad of not being bro.":
                jump accuseBradBro
            "Accuse Brad of stealing Rad's surf board and riding it down the stairs at the frat.":
                jump accuseBradSteal

label vladAccusePale:
    shaman "Seriously? You want to kill him because he's pale? That's pretty racist bro, and I will not stand for that in this day and age."
    "The shaman wacks you with his staff, sending you flying out of the helicopter."
    jump death

label vladAccuseGhost:
    vlad "Vhat? Vho you callving a ghvost, bvro?"
    "Vlad shoves you with his giant arms, sending you flying out of the helicopter."
    jump death

label vladAccuseVamp:
    shaman "Holy crap, you're totally right [pname]. This guy is totally a vampire. Let's murk this foo!"
    vlad "Vhat? That's crazy! Vhy vould you think I am a vampire?"
    rad "Well first off, you never come to the beach to hang. Seems reall suspect, bro."
    vlad "I'm not a vampire, I just have a bvad skin condition!"
    gad "Prove it then, eat this garlic bread!"
    "With that, Ga(y)d whips whole platter of garlic bread out of nowhere."
    vlad "AAAH! No! I'm allergic to garlic!"
    "Vlad backs away from Ga(y)d, falling out of the helicopter"
    hide vlad
    vlad "AAAAAAAAAAAAAAAAHHH"
    "You hear a splash as Vlad hits the lava, then no more."
    mc "Alright! Now, to business. Shaman, summon Stacy to my hut!"
    shaman "Yes, Chieftain, as you wish."
    hide shaman
    hide gad
    hide rad
    hide mc
    scene bg chiefHut with fade
    show mc normal at left
    show shaman normal at right
    shaman "The brodacious babe Stacy is here to see you as requested, Chieftain."
    mc "Excellent, send her in."
    hide shaman
    show stacy annoyed at right with dissolve
    stacy "Ugh, what do you want now [pname]?"
    mc "So, Stacy, now that Vlad is gone how about you and I pick up where we left off?"
    stacy "Yeah, no thanks. I've already got my eyes on a new hunk, Plaid. The way he swings his axe is just so..."
    stacy "Anyway, yeah, you'll never be half the Chad he is. Bye."
    show stacy at chide
    hide stacy
    mc "Aw man, not again! This is totally brogus! Guess I'll just have to kill Plaid too."
    mc "Time to go find more dirt."
    hide mc
    $ victim = "plaid"
    $ strikecount = 3
    call screen map

label plaidaccuseAmerican:
    shaman "Dude, American? Look at his BMI."
    "The shaman whacks you with his staff, sending you flying out of the helicopter."
    jump death

label accuseplaidJapanese:
    shaman "What? Being Japanese isn't a reason to kill somebody, you baka gaijin! I have the power of the Sun God and anime on my side!"
    shaman "Omae wa mou shindeiru!"
    "The shaman teleports behind you and pushes you out of the helicopter."
    jump death

label accuseplaidRussian:
    plaid "Who do you think I am, eh? Comrade Chadski?"
    "Plaid pushes you out of the helicopter"
    jump death

label accuseplaidCanadian:
    shaman "Canadian?! But they've been banned from Chad Island ever since the Great Hockey Incident of '06!"
    plaid "Pssshhhh, that's not true."
    dad "I can prove it. I am NOT sorry."
    plaid "NOOOO, It's too much!"
    "Plaid runs and falls out of the helicopter"
    hide plaid
    plaid "AAAAAAAAAAAAAAAAHHH"
    "You hear a splash as Plaid hits the lava, then no more."
    mc "Alright! Now, to business. Shaman, summon Stacy to my hut!"
    shaman "Yes, Chieftain, as you wish."
    hide dad
    hide gad
    hide shaman
    hide mc
    scene bg chiefHut with fade
    show mc normal at left
    show shaman normal at right
    shaman "The brodacious babe Stacy is here to see you as requested, Chieftain."
    mc "Excellent, send her in."
    hide shaman
    show stacy annoyed at right with dissolve
    stacy "Ugh, what do you want now [pname]?"
    mc "So, Stacy, now that Plaid is gone how about you and I pick up where we left off?"
    stacy "Yeah, no thanks. I've already got my eyes on a new hunk, Brad. The way he emmits swagger is just so..."
    stacy "Anyway, yeah, you'll never be half the Chad he is. Bye."
    show stacy at chide
    hide stacy
    mc "Aw man, not again! This is totally brogus! Guess I'll just have to kill Brad too."
    mc "Time to go find more dirt."
    hide mc
    $ victim = "brad"
    $ strikecount = 3
    call screen map

label accuseBradWeed:
    shaman "Are you kidding, Brad makes the best doobies on the island! How's that bad?"
    "The shaman teleports behind you and pushes you out of the helicopter."
    jump death

label accuseBradBro:
    brad "Who do you think I am bro, I'm brozilla"
    "Brad bangs chest likes a true bro and then headbutts you out of the helicopter"
    jump death

label accusepBradSteal:
    shaman "WHAT! A THIEF!"
    brad "No way bro, you can brust me."
    chadski "I can prove it. My soviet spies saw everthing."
    "brad Drops his weed out of the helicopter in surprise"
    brad "NOOOO, My brodacious Doobies"
    "Brad jumps out after his pot"
    hide brad
    brad "AAAAAAAAAAAAAAAAHHH"
    "You hear a splash as Brad hits the lava, then no more."
    mc "Alright! Now, to business. Shaman, summon Stacy to my hut!"
    shaman "Yes, Chieftain, as you wish."
    hide rad
    hide chadski
    hide shaman
    hide mc
    scene bg chiefHut with fade
    show mc normal at left
    show shaman normal at right
    shaman "The brodacious babe Stacy is here to see you as requested, Chieftain."
    mc "Excellent, send her in."
    hide shaman
    show stacy annoyed at right with dissolve
    stacy "Ugh, what do you want now [pname]?"
    mc "So, Stacy, now that Brad is gone how about you and I pick up where we left off?"
    stacy "Yeah, no thanks. I've already got my eyes on a new hunk, Thad. The way he emmits swagger is just so..."
    stacy "Anyway, yeah, you'll never be half the Chad he is. Bye."
    show stacy at chide
    hide stacy
    mc "This is getting ridiculous. If i can't have Stacy, no one can."
    mc "Time to go convince everyone that she's gotta go."
    hide mc
    $ victim = "stacy"
    call screen map

label end:
    scene bg shamanHut
    show shaman normal at right
    shaman "Oh, Great Chad, The Sun God, I ask thee for guidance."
    sg "What is troubling you my loyal disciple?"
    shaman "[pname] is being a total Chadlet and screwing up the balance of the island, what should we do?"
    sg "I dunno, chuck him into the volcano?"
    shaman "Right good call."
    scene bg chopper
    show mc normal at left
    show shaman normal at center
    shaman "Chief [pname]! Your sacrifices have gone too far!"
    shaman "Sun God, I summon thee to smack a bitch!"
    show sg normal at right
    sg "[pname]! Your reign of terror is totally uncool, broseph. See ya!"
    jump death

label death:
    "You fall into the mouth of the volcano, regretting the fact you never lost your virginity."
    "You are dead."
