# SCENE 12: Lindsey phase 2 convo
# Locations: School Hallway, School Janitor Closet
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 5)
# Time: Afternoon

label v15s12:
    if v14s51_take_diary:
        # -MC and Lindsey are walking along the hallway, in the general direction of the janitor's closet-
        scene v15s12_1    # TPP. MC and Lindsey walking down the school hallway.
        with dissolve
        
        pause 0.75

        scene v15s12_2    # FPP. Lindsey, happy, smiling, mouth open. 
        with dissolve 

        li "Oh! *Whispers* I forgot to tell you, I got Chloe's diary open."

        scene v15s12_2a   # FPP. same as v15s12_2, but mouth closed
        with dissolve

        u "*Whispers* Oh shit! You actually got it open?"

        scene v15s12_2b   # FPP. same as v15s12_2, but with Lindsey winking at MC.
        with dissolve

        li "Of course I got it open, haha."

        scene v15s12_2a
        with dissolve

        u "*Chuckles* Nice, Linds. So, what did you find?"

        scene v15s12_1
        with dissolve

        li "Well, it's kind of just filled with a lot of boring everyday thoughts about college and guys."    

        li "Like whether or not she should change her style, her hair color..."

        scene v15s12_2c   # FPP. Same as v15s12_2, but with a mischevious (naughty) smile.
        with dissolve

        li "And then there were a few interesting entries."
        
        if chloegf or chloers: # -if ChloeGF or ChloeRS
            scene v15s12_3    # TPP. MC worried, mouth closed. 
            with dissolve

            u "(*Gulps*)"

        scene v15s12_2d   # FPP. Same as v15s12_2a, but neutral expression mouth closed. 
        with dissolve

        u "Such as...?"

        scene v15s12_2c
        with dissolve

        li "Oh... Just a few small details about her campaign plans!"

        scene v15s12_2f   # FPP. Same as v15s12_2a, but slightly surprised mouth closed.
        with dissolve

        u "What?! She wrote everything in there? That's like a pot of gold, haha."

        scene v15s12_2g   # FPP. Same as v15s12_2f, mouth open.
        with dissolve

        li "Yes! I know, I literally got handed the inside scoop on her next big idea. Unless for some reason she decides not to follow through with this plan."

        scene v15s12_2a
        with dissolve

        u "Well, you're welc-"

        scene v15s12_2
        with dissolve

        li "Thank you. Tremendously."

        scene v15s12_2a
        with dissolve

        u "Yeah, of course. *Chuckles*"

        scene v15s12_2d
        with dissolve

        li "So, believe it or not, she has this master plan to get me absolutely hammered and then somehow get a recording of me saying something shitty about her and the Chicks."

        scene v1v15s12_2e   # FPP. Same as v15s12_2d, but mouth open.
        with dissolve

        u "What the fuck?"

        scene v15s12_2h   # FPP. Same as v15s12_2, but slightly angry mouth open.
        with dissolve

        li "*Scoffs* She's trying to trick me [name], so that she can publicly embarrass me... Can you believe that?"

        if v14_help_chloe and v15s8_chloe_pb_DamageLindseyRep: # -if MC is helping Chloe and chose the Embarrass Lindsey option on Chloe's planning board
            scene v15s12_3
            with dissolve

            u "(Oh, I can believe it... What the fuck was Chloe thinking just writing down the plan?!)"

            scene v15s12_2i   # FPP. Same as v15s12_2h, but mouth closed.
            with dissolve

            u "No... I can't. That's really shitty."

            scene v15s12_2d
            with dissolve

            li "*Sighs* I'm just glad I got this information ahead of time. Who knows what kind of trouble I just avoided."

        elif v14_help_chloe: # -if MC is helping Chloe and did not chose the Embarrass Lindsey option
            scene v15s12_2i
            with dissolve
            
            u "*Sighs* That's so fucked..."

            scene v15s12_2h
            with dissolve

            li "It's completely fucked! And the shadiest way you can play this game."

            scene v15s12_2e
            with dissolve

            li "But now I know to stay away from alcohol and Chloe until the whole thing is over..."

            scene v15s12_4    # TPP. MC neutral expression, mouth closed.
            with dissolve

            u "(Damn, I'm so glad we chose to not do that to her.)"
            
        else: # -if MC is not helping Chloe
            scene v15s12_2i
            with dissolve

            u "That's so fucking shady. *Laughs* Why is she trying to humiliate you?"

            scene v15s12_2h
            with dissolve

            li "Because she knows she can't win without putting a dent in my reputation."

            scene v15s12_2e
            with dissolve

            li "I needed money to win, I can admit that. That's the reason we have her diary in the first place. But Chloe has money, and she has resources..."

            scene v15s12_2d
            with dissolve

            u "She just doesn't have the votes."

            scene v15s12_2
            with dissolve

            li "Exactly. We do."

            # -They are looking very pleased with themselves-
            scene v15s12_5    # TPP. MC and Lindsey walking down the hall, glancing at each other, smiling, mouth closed.
            with dissolve

            pause 0.75

            scene v15s12_2d
            with dissolve

            u "I'm glad that taking her diary was worth it... I felt bad for a second there."

            scene v15s12_2e
            with dissolve

            li "Ha, yeah. I know... Me too."        

        if chloegf: # -if ChloeGF
            scene v15s12_2e
            with dissolve
            
            li "And... There was something else too."

            scene v15s12_2d
            with dissolve

            u "Yeah?"

            scene v15s12_2e
            with dissolve

            li "Yeah, but I'm not sure you want to hear about it since, you know... You and Chloe are together..."
            
            li "It's about her past with Grayson and the big breakup."

            scene v15s12_3
            with dissolve

            u "(*Sighs* Do I want to know?)"       

        # -MC chooses event1 or event2
        # -event1 Tell me
        # -event2 Not interested
        menu:
            "Tell me": # -if Tell me
                $ add_point(KCT.TROUBLEMAKER)# TODO - KCT and character points
                $ chloe.points -= 1  
                
                scene v15s12_2d
                with dissolve
                
                u "It's alright. I mean, thank you, haha... But go ahead. You can tell me."

                scene v15s12_2e
                with dissolve

                li "Haha, okay... I mean it was nothing too specific, I guess."
                
                li "Grayson apparently had major trust issues, and I guess it got to the point where he wouldn't let her go anywhere without telling him exactly where or who she was going with."

                scene v15s12_2d
                with dissolve

                u "Jeez..."

                scene v15s12_2e
                with dissolve

                li "If she was ever seen talking to another guy, he would instantly accuse her of cheating and that would lead to an argument..."

                scene v15s12_2j   # FPP. Same as v15s12_2, but concerned, mouth open.
                with dissolve

                li "After a while, she realized she had to stop dating him if she didn't want to be yelled at and untrusted all day."

                scene v15s12_2k   # FPP. Same as v15s12_2j, but mouth closed.
                with dissolve

                u "*Sighs* That's so toxic."

                scene v15s12_2j
                with dissolve

                li "Yeah, it was a very toxic relationship."

                scene v15s12_2e
                with dissolve

                li "But to be fair, this is only one side of the story. I guess you would have to steal Grayson's diary to get the full picture, haha."

                scene v15s12_2a
                with dissolve

                u "*Laughs* Yeah, I don't think he's the type to keep it under his pillow though..."

                scene v15s12_2
                with dissolve

                li "*Chuckles* What a horrible hiding spot."

                scene v15s12_2d
                with dissolve

                u "Anyway, thanks for telling me."

                scene v15s12_2e
                with dissolve

                li "No problem."

            "Not interested": # -if Not interested
                $ add_point(KCT.BOYFRIEND) # TODO: KCT and character points 
                $ chloe.points += 1
                
                scene v15s12_2e
                with dissolve
                
                u "Eh, to be honest... It's in the past and... it should just be left there, haha."
                
                u "I don't want to know about what problems she had with her ex-boyfriends unless she tells me of course."

                scene v15s12_2d
                with dissolve

                li "Yeah, fair enough, I respect that. That's why I wanted to ask."            

        # -regardless of previous choice, still if ChloeGF
        if chloegf and lindseyrs:  # -if ChloeGF and LindseyRS
            scene v15s12_2j
            with dissolve

            li "So, real quick, just to rip off the band-aid, haha..."

            scene v15s12_3
            with dissolve

            u "(Oh shit.)"

            scene v15s12_2j
            with dissolve

            li "You and Chloe are together, she's told just about everyone. *Chuckles* So, where does that leave us?"

            scene v15s12_2k
            with dissolve

            u "I-"

            scene v15s12_2j
            with dissolve

            li "I don't need details or... commitment. I don't need that, not right now at least."
            
            li "All I need to know is if you're serious about her or not, because if you are, then you and I should just..."
            
            # -MC chooses event1 or event2
            # -event1 It's pretty serious (LindseyRS becomes LindseyFriend)
            # -event2 It's not that serious
            menu:                        
                "It's pretty serious": # -if It's pretty serious (LindseyRS becomes LindseyFriend)
                    $ add_point(KCT.BOYFRINED) # TODO KCT and character points 
                    $ chloe.points += 1
                    $ lindsey.points -= 1

                    scene v15s12_2d
                    with dissolve

                    u "It's pretty serious between us, yeah. Chloe and I get along really well, and-"

                    # -Lindsey disappointed but then hides her pain behind a fake smile-
                    scene v15s12_2l
                    with dissolve

                    li "Great! That's so good. I'm really, really glad... Thanks for telling me."

                    scene v15s12_2m   # FPP. Same as v15s12_2l, but mouth closed. 
                    with dissolve

                    u "Yeah, of course. I'm sorry if-"

                    scene v15s12_2l
                    with dissolve

                    li "No, I mean... You're fine, I guess? I just-"
                    
                    li "Next time you decide to make a girl fall in love with you, take her feelings into consideration first. Yeah?"

                    scene v15s12_2m
                    with dissolve

                    u "Linds..."

                    scene v15s12_2d
                    with dissolve

                    li "Let's move on. We're good. I promise."

                    scene v15s12_4
                    with dissolve

                    u "(Sighs... Well, it needed to happen eventually, I guess.)"                

                "It's not that serious":  # -if It's not that serious
                    $ add_point(KCT.TROUBLEMAKER) # TODO: KCT and Character points
                    $ lindsey.points += 1
                    $ chloe.points -= 1

                    scene v15s12_2d
                    with dissolve

                    u "Lindsey... No."

                    scene v15s12_2e
                    with dissolve

                    li "No?"

                    scene v15s12_2d
                    with dissolve

                    u "It's not that serious between me and Chloe, I mean..."
                    
                    u "It kind of just became official naturally..."

                    scene v15s12_2e
                    with dissolve

                    $ add_point(KCT.TROUBLEMAKER) # -MC needs to be losing Loyal KCT here because he's lying through his teeth :)-
                    
                    li "So... Do you have other people on your mind?"                

                    scene v15s12_2d
                    with dissolve

                    u "Ha, you can say that... At least one."

                    scene v15s12_2
                    with dissolve

                    # -Lindsey very happy-
                    li "Okay. Cool. *Chuckles* Thanks for letting me know."

                    scene v15s12_2a
                    with dissolve

                    u "Haha, yeah. Of course."

        # -Regardless-
            scene v15s12_2
            with dissolve
            
            li "Here we go... After you, sir."

            scene v15s12_2a
            with dissolve

            u "Why thank you, madam..."

    else: 
        # -MC and Lindsey arrive at and enter the janitor's closet, closing the door behind them-
        scene v15s12_6    # TPP. MC walks through the Janitor door closet and Lindsey follows behind him.
        with dissolve

        pause 0.75

        scene v15s12_7    # TPP. Lindsey closes the door behind her.
        with dissolve

        pause 0.75

        # -Lindsey points at the planning board-
        scene v15s12_8    # FPP. Lindsey smiling, mouth open, pointing at the planning board.
        with dissolve

        li "So, here's what I'm thinking... Basically, our focus this time is to gain more allies. Allies that we can trust to support us now, during the election, and also in the future, when I'm president of the Chicks."

        scene v15s12_8b   # FPP. Same as v15s12_8a, but mouth closed.
        with dissolve

        u "Haha, damn straight!"

        scene v15s12_8a   # FPP. Same as v15s12_8, but not pointing at the board, smiling mouth open.
        with dissolve

        li "So basically, it's just who you think should come, and what the best way to gain their support would be."

        scene v15s12_8b
        with dissolve

        u "They're both fine ideas, I think we can go with the club, or a game night regardless, and still end up having a good time... But I think that's our best option."

        # -The planning board pops up and MC makes his choices from what's presented-

        #### Planning Board work goes here 
        python:
            v15_lindsey_board.add_approach("gameNight",
                "Game Night",
                opinion="\"Hosting a game night would be the perfect excuse to get a few of Chloe's allies alone. We'll get booze, snacks, and make sure they have a fun night while also making it known that I'm so much better than Chloe\"")

            v15_lindsey_board.add_approach("vipNight",
                "VIP Night",
                opinion="\"There's a few people on Chloe's side that I think I could sway... Their opinion of me isn't horrible, they just seem to perfer her... If we give them a spectacular night out, there's absolutely no way they'll be  able to choose her over me.\"")

            v15s12_lindsey_pb_fakeId = v15_lindsey_board.add_task("gameNight",
                "Buy booze with fake ID",
                opinion="\"Since neither of us are of the legal drinking age, we're gonna need a fake ID if we want booze. A friend of mine makes them, so I'll take care of that.\"",
                people=[mc, lindsey],
                cost=100)

            v15_lindsey_board.add_subtask("gameNight",
                "Who's Most Likely...",
                opinion="\"\"Who's Most Likely To\" is always a fun game to play with a group of people. We'll laugh, learn, a bit about each other and maybe some secrets will come out as well.\"")

            v15s12_lindsey_pb_wouldYouRather = v15_lindsey_board.add_subtask("gameNight",
                "Would You Rather",
                opinion="\"\"Would you rather\" is the easiest game to play when you want to get the conversation rolling. Hopefully we get a few laughs and maybe some secrets out of them as well.\"")

            v15_lindsey_board.add_task("gameNight",
                "Host the game night",
                opinion="\"Once we got the games and (hopefully) the booze, all that's left is to make sure everyone has a good time and leaves wanting to vote for me.\"",
                people=[mc, lindsey, autumn, aubrey])

            v15_lindsey_board.add_task("vipNight",
                "Book a limousine & private club",
                "\"It takes a pretty big chunk out of my campaign fund, but this limo rental and VIP room at the nearest nightclub are going to blow our friends out of the fucking waters. I can't wait to spoil them all night.\"",
                cost=800)

            v15_s12_lindsey_pb_inviteSebastian = v15_lindsey_board.add_subtask("vipNight",
                "Invite Aubrey, Autumn, and Sebastian",
                opinion="\"Aubrey and Autumn are for sure going to come, I want some time with them away from Chloe. The third person I want to invite is Sebastian. We're pretty close, but in the end he has to vote the way the Wolves do. If we can convince him to support me, and ask others to; Seb being on my side would mean more support from the Wolves.\"",
                people=[aubrey, autumn, sebastian])

            v15_lindsey_board.add_subtask("vipNight",
                "Invite Aubrey, Autumn, and Grayson",
                opinion="\"Aubrey and Autumn are for sure going to come, I want some time with them away from Chloe. The last person I'm thinking about inviting is Grayson. He already has this burning hatred for Chloe, mixed with a little bit of horniness but stil... I think he's closer to boarding the Lindsey train than we think, and Grayson being on my side would mean support from the Apes.\"",
                people=[aubrey, autumn, grayson])

            v15_lindsey_board.add_task("vipNight",
                "Host exclusive VIP Night",
                opinion="\"Finally, a night to remember! Our main focus during the night out is the three people we want to impress. Keeping them satisfied and entertained all night is the only goal besides having a damn good time.\"",
                people=[mc, lindsey, aubrey, autumn]) # Can't add Sebastian or Grayson here because we're loading the menu before the player can select. 

        call screen planning_board(v15_lindsey_board)

        if v15_lindsey_board.approach is not None:
            $ v15s12_lindsey_pb_gameNight = v15_lindsey_board.approach.id == "gameNight"

        if v15_lindsey_board.selected_task is not None:
            $ v15s12_lindsey_pb_fakeId = v15_lindsey_board.selected_task  == v15s12_lindsey_pb_fakeId
            $ v15s12_lindsey_pb_wouldYouRather = v15_lindsey_board.selected_task == v15s12_lindsey_pb_wouldYouRather
            $ v15_s12_lindsey_pb_inviteSebastian = v15_lindsey_board.selected_task == v15_s12_lindsey_pb_inviteSebastian

        # End planning board (screen disappears)

        if v15s12_lindsey_pb_gameNight: # -if chose Game night
            scene v15s12_8b
            with dissolve
            
            u "A small group with snacks, drinks, and intimate surroundings. You can really focus on each person and convince them why they should support you."

            scene v15s12_8a
            with dissolve

            li "Yes! It should be a fun night too, but most importantly, no interruptions."

            scene v15s12_8b
            with dissolve

            u "Haha, of course it'll be fun. We must enjoy ourselves at the end of the day, you know."

            scene v15s12_8a
            with dissolve

            li "*Laughs* Exactly."

        else: # -if chose Host an exclusive VIP night
            scene v15s12_8a
            with dissolve
            
            u "It might be more money that we're taking from the budget, but there's no chance they'll vote for Chloe after you roll up in a limo to take them out for the night."

            scene v15s12_8b
            with dissolve

            li "Haha, that's so true. It's going to be epic!"        

        # -Regardless-
        scene v15s12_8a
        with dissolve

        li "I can't wait. I'm so excited for this one."

        scene v15s12_8b
        with dissolve

        u "Me too, I'll be waiting for your call to start the next phase. *Laughs*"

        scene v15s12_8a
        with dissolve

        li "Hehe, thank you!"        

        if lindseyrs: # -if LindseyRS
            # -Lindsey gives MC a passionate kiss-           
            scene v15s12_9    # FPP. Lindsey passionately kisses MC.
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 0.75        

            scene v15s12_9a   # FPP. Lindsy happy, smiling, mouth closed looking at MC.  
            with dissolve

            u "Mmm, coffee again this morning?"

            scene v15s12_8a
            with dissolve

            li "Haha, I've been a busy girl! I have to stay awake somehow."

            scene v15s12_8b
            with dissolve

            u "Hey, I'm not complaining..."

    # -Regardless-
    scene v15s12_8b
    with dissolve

    u "I'll see you in a bit."

    # -MC leaves the janitor's closet, leaving Lindsey watching him go with a smile-
    scene v15s12_10   # TPP. MC exiting through the Janitor door, smiling, mouth closed, with Lindsey looking at her planning board behind him.
    with dissolve

    pause 0.75

    # -Now MC is walking along the hallway-
    scene v15s12_11   # TPP. MC walking down the school hallways, smiling, mouth closed.
    with dissolve

    pause 0.75

    # -MC's phone vibrates-
    scene v15s12_12   # TPP. MC in the hallway looking down at his phone in his hand.
    with dissolve

    $ riley.newMessage("Hey! I'm assuming you'll be at Lauren's birthday party later?")
    $ riley.addReply("Yeah, I'll be there.")
    $ riley.newMessage("Cool. FYI, the stores are running low on costumes, you need to hurry up and buy one! Lol")
    $ riley.addReply("Ah, shit... You're right.")
    $ riley.newMessage("Of course I am ;)")
    $ riley.addReply("I'd be lost without you")
    $ riley.newMessage("Oh trust me, I know... hehe. See you soon!")
    $ riley.addReply("Thanks red!")
    $ riley.newMessage("Haha, welcome nerd!")

label v15s12_PhoneContinue:
    if riley.messenger.replies:
        play sound "sounds/vibrate.mp3"
        call screen phone
    if riley.messenger.replies:
        u "(I should reply to Riley.)"
        jump v15s12_PhoneContinue

    # -MC exits his texts, puts his phone away, continues walking-
    scene v15s12_13   # TPP. MC puts his phone in his pocket.
    with dissolve

    u "(I'm a man on a mission. Find Lauren a gift and find a costume. Easy.)"
    
    if msrosers and v15s5_mc_angry_with_rose: # -if RoseRs and MC acted angry in v15.5
        # -Transition to Scene 14-
        jump v15s14

    else: # -Otherwise-
        # -Transition to Scene 17-
        jump v15s17