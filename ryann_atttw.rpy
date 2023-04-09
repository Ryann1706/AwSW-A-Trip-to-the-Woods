
label ryann_atttw_start:

show eckannaendingseenimgd with dissolveslow
$ renpy.pause (2.5)
hide eckannaendingseenimgd with dissolveslow

label ryann_atttw_mca_start:
    
$ renpy.pause (4.0)
m "At some point in time, after ending [[D] of Not-So-Tragic Hero…"
$ renpy.pause (4.0)
play music "mx/serene.ogg" fadein 3.0
play sound "fx/steps/rough_gravel.wav"
$ renpy.pause (4.0)
scene ryann_wilderness
show anna normal
with dissolveslow
stop sound fadeout 2.0

$ renpy.pause (1.5)
c "You know, I’m still finding it hard to believe you actually agreed to do this."
c "Given how seriously you take your work, I didn’t expect you to just take a whole week off."
An face "Well, what did you expect? You’re the one who’s been constantly pestering me about having a proper work-life balance and finally burning through all those vacation days I have saved up."
An smirk "Plus, you getting to spend some time in the wilderness might actually help toughen you up."
c "Hey! I’m not that weak."
An normal "Says the one who brought a tent because their soft, sensitive skin can’t handle the ground."
c "I don’t know why you’re complaining, since you’re not the one carrying it. Plus, you’ll be using it too, unless you’re planning to sleep on the ground by yourself instead."
An smirk "Fine. You win this time."
show anna normal with dissolve

$ renpy.pause (0.5)
c "By the way, you still haven’t told me where we’re going."
An "It’s a spot I found last time I went out like this. It’s quiet and free of predators, if that’s what you’re scared of."
c "And how long will it take to get there?"
An face "You sure do love asking questions, don’t you?"
An normal "You’ll know when we get there."
$ renpy.pause (1.5)

menu:
    "[[Be mature.]":
        $ renpy.pause (0.5)
        jump ryann_atttw_arrive

    "Are we there yet?":
        $ ryann_atttw_annoy_anna += 1
        c "Hey, Anna, are we there yet?"
        An face "Yes, actually. In the past 5 seconds of walking, we {i}did{/i} get there."
        show anna normal with dissolve
        jump ryann_atttw_are_we_there_yet

label ryann_atttw_are_we_there_yet:

menu:
    "[[Stop.]":
        $ renpy.pause (1.5)
        jump ryann_atttw_arrive

    "Are we there yet?":
        c "Are we there yet?"

        if ryann_atttw_annoy_anna == 1:
            An sad "Oh."
            An face "Don’t you {i}dare{/i} start this."

        if ryann_atttw_annoy_anna == 2:
            An disgust "Grow up, [player_name]."

        if ryann_atttw_annoy_anna == 3:
            An face "…"

        if ryann_atttw_annoy_anna == 4:
            An rage "[player_name], I will turn around and leave you out here."
            c "Alright, alright. I get it."
            An disgust "You better."
            m "In fear of my own safety, I decided now was a good point to stop."
            jump ryann_atttw_arrive

$ ryann_atttw_annoy_anna += 1
jump ryann_atttw_are_we_there_yet

label ryann_atttw_arrive:

scene black with dissolve
$ renpy.pause (0.5)
scene ryann_forest2_evening with dissolve
$ renpy.pause (1.5)
show anna normal with easeinright
$ renpy.pause (1.0)
if ryann_atttw_annoy_anna >= 4:
    An face "We’re finally here. Are you happy now, [player_name]?"
    show anna normal with dissolve
else:
    An "Alright. We’re here. "

c "So, what do we do now?"
An "You can set up that tent you were so desperate to bring, and I’ll get some firewood."
c "Firewood? What, can you not make fire by yourself anymore?"
An face "I can obviously still make fire. I just don’t want to be relighting it every 15 minutes."
An normal "Do you think you can handle setting up the tent by yourself, or do you want to wait for me to help you?"
c "Yes, I can handle setting up a tent by myself."
c "I know I’m not a master outdoorsman, but I’m not that incompetent."
An "Well, I guess we’ll see."
$ renpy.pause (0.5)
show anna normal flip with dissolve
$ renpy.pause (0.2)
hide anna with easeoutright
$ renpy.pause (0.5)

m "I found a relatively clear spot to pitch up the tent and started to unpack it."
m "It was actually surprisingly easy to set up, which I put up to my extra dexterity."
m "From what I could find while shopping for camping gear, dragons didn’t have sleeping bags, so the blankets and pillows I brought would have to do instead."
m "After it was all done, Anna still hadn’t returned, so I started to work on a simple fire pit."
m "After a bit of searching, I found some rocks and eventually lugged some of the more manageable ones back to our campsite."
$ renpy.pause (1.0)
show anna normal with easeinright
$ renpy.pause (0.5)
An smirk "Looks like someone’s been busy."
c "See? I know what I’m doing."
An normal "Don’t start getting cocky already. We still have the rest of the week out here."
$ renpy.pause (1.5)
show anna at Position(xpos=0.3) with ease
$ renpy.pause (0.2)
m "Anna then walked over to the fire pit and made the beginnings of a campfire."
$ renpy.pause (1.5)
An "Stand back."
show anna at Position(xpos=0.5) with ease
m "She proceeded to take a few steps back too and light the fire the same way she had before."
play sound "fx/firex.ogg"
$ renpy.pause (1.5)
An smirk "Ta-da."
c "Wow. I totally haven’t seen that trick before."
An face "Oh, haha, smartass."
stop sound fadeout 6.0
c "You’re one to talk."
show anna normal with dissolve

$ renpy.pause (1.5)
play sound "fx/undress.ogg"
m "Anna then took off her own bag and tossed it over to me."
An "Check the front pocket."
play sound "fx/searchpav.ogg"
$ renpy.pause (1.5)
stop sound
c "Crackers?"
An "And?"
play sound "fx/searchpav.ogg"
$ renpy.pause (1.5)
stop sound
c "Oh, smores."
An smirk "Yes, [player_name]. Smores. Well done."
c "Alright, now we’re even."
An "But there’s something else too."
show anna normal with dissolve
m "Anna opened a different compartment of her bag, then pulled out two metal cups, a recycled bottle full of milk, and some hot chocolate mix."
c "Has that milk been in your bag the whole time? Is it even still fresh?"
An "I bought it yesterday, and it’s been in the fridge since this morning, so it’s fresh enough."
An face "We’re going to be heating it anyway, so why does it matter if it’s warm now?"
show anna normal with dissolve
c "I guess it doesn’t."
m "Grabbing some small twigs from the firewood Anna brought over, I skewered some marshmallows and started roasting them, while Anna filled the two cups with milk and put them close to the fire."
An "I didn’t bring much with me the last time I went out like this, but these are some of the things I wished I did."
c "You haven’t really told me much about you going out into the woods like this, other than your vacation where you just went in a random direction for a week."
An "Well, is there anything specific you want to know?"

label ryann_atttw_campfire_questions_start:

if ryann_atttw_campfire_questions == 1:
    $ renpy.pause (0.5)
    m "By now, the marshmallows we’d been roasting were a beautiful golden brown, and the milk was sufficiently heated up."
    m "I got two of the marshmallow and put them on some graham crackers and chocolate, while Anna mixed the chocolate powder into the milk."
    m "After I finished the smores, instead of handing me a hot chocolate, Anna had taken the other marshmallows I’d roasted and added them in, and put the cups back near the fire."
    An smirk "Be patient. It’ll be worth it."
    show anna normal with dissolve
    m "In the meantime, the two of us tried the smores."
    $ renpy.pause (0.5)
    play sound "fx/pizzabite.ogg" # Pizza and smores are close enough
    $ renpy.pause (1.0)
    An smirk "You know, these aren’t too bad."
    c "Yeah. They’re pretty good."
    m "We set another pair of marshmallows to start toasting."
    show anna normal with dissolve
    $ renpy.pause (0.5)

if ryann_atttw_campfire_questions == 2:
    m "Our second set of marshmallows were also now perfectly toasted, and the ones in the hot chocolate were melted as well."
    m "I made our second set of smores while Anna retrieved our drinks from the fire."
    $ renpy.pause (0.5)
    play sound "fx/pizzabite.ogg"
    $ renpy.pause (1.0)
    c "These are really satisfying after walking all day."
    An "Not as much as the first ones, but sure."
    $ renpy.pause  (1.0)
    play sound "fx/slurp.ogg"
    $ renpy.pause (3.0)
    c "This is probably the best hot chocolate I’ve ever had."
    An smirk "I’d have to agree with you there."
    An normal "It’s been far too long since I’ve had this. I didn’t expect it to feel so nostalgic."
    $ renpy.pause (2.5)
    m "Just after finishing our drinks, I suddenly felt something touch my face. A raindrop. I looked up, and some heavier rain clouds were only a few minutes from hitting us."
    An "I guess we should go in the tent before you and your clothes get soaked."
    $ renpy.pause (0.5)
    menu:
        "Yeah.":
            c "Yeah, we probably should."
            jump ryann_atttw_tent

        "Actually, in a minute.":
            c "Actually, can we wait for a minute?"
            An "Alright. If you want to get drenched, it’s your choice."
            $ renpy.pause (0.5)

if ryann_atttw_campfire_questions == 3:
    $ ryann_atttw_annoy_anna += 1
    m "The few light raindrops from earlier were now turning into a much heavier shower."
    An face "Okay, we’re going in the tent now. I’m not letting you get sick because you want to sit out in the rain."
    $ renpy.pause (0.5)
    jump ryann_atttw_tent

$ ryann_atttw_campfire_questions += 1
menu: 
    "Would you stay out in the wild forever given the chance?" if not ryann_atttw_campfire_questions_stay_in_wild:
        $ ryann_atttw_campfire_questions_stay_in_wild = True
        c "Would you stay out in the wild forever like this given the chance?"
        An sad "Forever, huh?"
        $ renpy.pause (2.0)
        An normal "I wouldn’t. The work I do for our society is far too important to just stay out here like a wild animal."
        c "I guess your whole “enjoying different experiences” mentality must have dried up."
        An face "[player_name], while I can appreciate spending some time isolated in the woods, I still do take pride in my work, and I also do enjoy some of the modern comforts of society."
        An smirk "Though, I have to admit, being out here again is a lot more appealing than I remember."
        c "Maybe it’s because you actually have some company this time?"
        An normal "Maybe."

    "How did you find this spot?" if not ryann_atttw_campfire_questions_find_spot:
        $ ryann_atttw_campfire_questions_find_spot = True
        c "How did you find this spot?"
        An "I already told you, I found it the last time I was out here."
        An "It’s safe, and there’s water, food, and other essentials nearby."
        An smirk "I figured it’d be perfect for a newbie like you."
        menu:
            "I’m not that incompetent.":
                c "Anna, come on, I’m not that incompetent. Give me some credit."
                An normal "Actually, maybe you’re right."
                c "Really?"
                An "Yeah. You set up a tent using the instructions it came with, and put some rocks in a circle."
                An smirk "You sure do know what you’re doing."
                $ renpy.pause (0.5)
                show anna normal with dissolve

            "Thanks for looking out for me.":
                c "Well, thanks for looking out for me. I appreciate it."
                An "Given all you’ve done for me, it’s the least I could do."
                $ renpy.pause (0.5)

            "Are you sure it’s safe?":
                $ ryann_atttw_annoy_anna += 1
                c "Are you sure it’s safe out here?"
                An face "I just said it was. Do you really think I’d bring you out here if it wasn’t?"
                An normal "Even if something {i}were{/i} to happen, I’d be here to look after you."
                $ renpy.pause (0.5)

    "What did you bring with you last time you went out like this?" if not ryann_atttw_campfire_questions_last_time_went_out:
        $ ryann_atttw_campfire_questions_last_time_went_out = True
        c "What did you bring with you the last time you went out like this?"
        c " You said you wished you’d brought smores and hot chocolate, so I was just curious."
        An "I didn’t bring much with me."
        c "Thank you, that’s very specific."
        An face "It was years ago. You really think I still remember everything I brought?"
        menu:
            "I didn’t think you’d bring anything.":
                $ ryann_atttw_survival_challenge = True
                c "Honestly, I didn’t think you’d bring anything with you."
                An "Why wouldn’t I? It was supposed to be a vacation, not a survival challenge."
                An "Just because I {i}could{/i} survive out in the wild with nothing, doesn’t mean I’d want to."
                An normal "I just brought a few essentials that I couldn’t get out here."

            "I bet you brought coffee.":
                $ ryann_atttw_annoy_anna += 1
                c "I bet you brought coffee with you."
                An face "No, I obviously didn’t bring coffee with me."
                An sad "Though, in hindsight, I probably should have. The caffeine withdrawal was a bitch to deal with."
                $ renpy.pause (2.0)
                An face "And I didn’t bring any this time either… Great."
                An normal "If you end up getting more attitude from me than usual over the next few days, blame it on the migraines."
                $ renpy.pause (0.5)

            "What did you remember bringing?":
                $ ryann_atttw_survival_challenge = True
                c "Well, from what you remember, what did you bring?"
                An normal "Just some essentials, like a first aid kit. Stuff I needed, but couldn’t get out here."
                An "Just in case I couldn’t find any, some spare food too, so I wouldn’t starve."
                An face "It was supposed to be a vacation after all, not a survival challenge."
                $ renpy.pause (0.5)
                show anna normal with dissolve

jump ryann_atttw_campfire_questions_start

# ===========================================================================================================================================================

label ryann_atttw_tent:
stop soundloop fadeout 0.5
stop music fadeout 1.5

$ renpy.pause (0.5)
scene black with dissolve
$ renpy.pause (0.5)

play sound "fx/ryann_tent_zip.mp3"
$ renpy.pause (1.5)
play soundloop "fx/ryann_tent_rain.mp3" fadein 2.0
scene ryann_tent_dark
show anna normal
with dissolveslow
play music "mx/hydrangea.ogg"
$ renpy.pause (0.5)
c "I bet you’re glad I brought this tent now."
An smirk "Fine. I’m willing to admit you made the right call this time."
c "So, what do we do now? It’s still pretty early, so I’m not extremely tired."
An normal "I don’t know. Any ideas?"
c "Hmm…"
$ renpy.pause (2.5)
c "Actually, yeah, I might."
An "Let’s hear it."
c "Have you heard of a game called “Never Have I Ever”?"
An "No. How do you play it?"
c "So, each of us hold up a hand and we take turns saying, “Never have I ever”, followed by asking if the other person has done something."
c "An example would be, “Never have I ever, played this before”, and if one of us has played this before, the person would put a finger down. The person who runs out of fingers first loses."
An face "Right, and you definitely didn’t choose that last rule because you have more fingers than me."
c "I’ll only use four, so it’s fair."
An normal "Alright. You’re on."
An smirk "But before we start, any bets?"
c "Hmm…"
$ renpy.pause (0.5)
menu:
    "Winner gets bragging rights.":
        $ ryann_atttw_minigame_bet = "bragging"
        c "The winner gets unlimited bragging rights?"
        An "Perfect."

    "Winner gets the last smore.":
        $ ryann_atttw_minigame_bet = "smore"
        c "The winner gets the last smore?"
        An " Aww, what’s wrong, [player_name]? Are you not feeling confident enough to have real stakes?"
        An normal "Also, what last smore? We just ate the last of them."
        c "There’s enough stuff to make one last smore in your bag."
        An face "Wow. An uncooked smore. What an amazing prize."
        c "The prize itself isn’t important. Let’s just get started."
        An normal "Alright."

    "Loser has to take down the tent when we leave.":
        $ ryann_atttw_minigame_bet = "tent"
        $ ryann_atttw_annoy_anna += 1
        c "The loser has to take down the tent when we leave?"
        An face "How the hell is that fair when you’re the only one who wanted to bring it?"
        c "Sounds like you’re scared to agree because you think you’ll lose."
        $ renpy.pause (1.5)
        An normal "You know what? Fine, I’ll agree, but just so I can’t get rid of that smug smirk when you lose."


# ===========================================================================================================================================================

show anna normal with dissolve
$ renpy.pause (1.5)

label ryann_atttw_minigame_start:

show screen ryannextrainfo
$ ryannextradisplay = 2

$ ryannDisplayVar1name = "Anna's fingers remaining:"
$ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points
$ ryannDisplayVar1unit = ""

$ ryannDisplayVar2name = "Player's fingers remaining:"
$ ryannDisplayVar2 = ryann_atttw_minigame_player_points
$ ryannDisplayVar2unit = ""

$ renpy.pause (1.0)

label ryann_atttw_minigame:

if ryann_atttw_minigame_anna_points == 0 and ryann_atttw_minigame_player_points == 0:
    $ ryann_atttw_minigame_winner = "draw"
    jump ryann_atttw_minigame_end

if ryann_atttw_minigame_anna_points == 0:
    $ ryann_atttw_minigame_winner = "player"
    jump ryann_atttw_minigame_end

if ryann_atttw_minigame_player_points == 0:
    $ ryann_atttw_minigame_winner = "anna"
    jump ryann_atttw_minigame_end


menu:
    c "Never have I ever…"

    "Gotten intimately close with another species." if ryann_atttw_minigame_anna_points == 1: # Both
        if ryann_atttw_minigame_player_points == 1:
            c "(At least this way I can guarantee a draw.)"
            c "Never have I ever,{w=0.5} gotten intimately close, with another species."
            An smirk "Wow. You’re really that scared of losing so you force a draw?"
            c "I rather take a guaranteed draw, than a possible loss."
            An normal "Fine. Be boring then."
            m "We both put our remaining fingers down."

        else:
            c "Never have I ever,{fast} gotten intimately close, with another species."
            An disgust "…"
            $ renpy.pause (2.0)
            c "What are you waiting for, Anna?"
            $ renpy.pause (1.5)
            An sad "Fine."
            m "I put a finger down as Anna frustratedly did too."

        $ ryann_atttw_minigame_anna_points -= 1
        $ ryann_atttw_minigame_player_points -= 1
        $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points
        $ ryannDisplayVar2 = ryann_atttw_minigame_player_points


    "Seen someone die." if not ryann_atttw_minigame_seen_someone_die: # Both
        $ ryann_atttw_minigame_seen_someone_die = True
        c "Never have I ever,{fast} seen someone die."
        show anna sad with dissolve
        $ renpy.pause (2.0)
        An "Well, we technically both have."
        c "What do you mean?"
        $ renpy.pause (1.5)
        An "Maverick and Reza."
        c "Oh, right…"
        c "I’m sorry for bringing that up."
        An normal "It’s fine."

        $ ryann_atttw_minigame_anna_points -= 1
        $ ryann_atttw_minigame_player_points -= 1
        $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points
        $ ryannDisplayVar2 = ryann_atttw_minigame_player_points

    "Worked to the point of neglecting needs." if not ryann_atttw_minigame_neglect_needs: # None
        $ ryann_atttw_minigame_neglect_needs = True
        c "Never have I ever,{fast} worked to the point of neglecting needs."
        An "No."
        c "You expect me to believe that?"
        An sad "[player_name], I know I worked my tail off before…{w=0.5} you know what, but I’m not an idiot. I could hardly focus on my work if I was starving, or exhausted."
        An "Sure, I drank coffee like it was water, but it’s not like I tried to completely replace sleep with it."
        c "How much sleep were you getting?"
        An "The bare minimum. About six hours, sometimes less."
        An normal "But I still was sleeping. So I wasn’t neglecting it."
        c "I’d say it best that we just move on."

    "Accidentally burned yourself." if not ryann_atttw_minigame_burned: # Anna
        $ ryann_atttw_minigame_burned = True
        c "Never have I ever,{fast} accidentally burned yourself."
        An "Yeah, I’ve done that."
        c "What’s the story behind it?"
        An "Well, as I’m sure you’re aware by now, dragons can make fire on demand."
        An "And something you might not know, is that dragons can do this when they’re quite young."
        An sad "You can take an educated guess what happens when an unsupervised hatchling tries to make fire for the first time."
        An normal "Thankfully because of our scales, and limited fire-making ability, it’s rarely a huge issue."

        $ ryann_atttw_minigame_anna_points -= 1
        $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points

    "Gotten caught stealing." if not ryann_atttw_minigame_stealing: # None / Both if played Casual Arson
        $ ryann_atttw_minigame_stealing = True
        c "Never have I ever,{fast} gotten caught stealing."
        if ryann_did_arson == True:
            An face "Oh, you little bastard."
            c "What?"
            An "You’re talking about when we got caught stealing that mouflon, aren’t you?"
            An "Just so you know, that was the {i}only{/i} time I’ve been caught stealing."
            An smirk "But unfortunately for you, it means you’ve also been caught stealing."
            c "Yeah, I guess that kind of backfired, huh?"
            An face "…"
            An "That was such a stupid pun…"
            c "Oh, back{i}fired{/i}. I didn’t even notice that."
            An "…"

            $ ryann_atttw_minigame_anna_points -= 1
            $ ryann_atttw_minigame_player_points -= 1
            $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points
            $ ryannDisplayVar2 = ryann_atttw_minigame_player_points

        else:
            An "No, I haven’t."
            c "Really?"
            An face "Why would I? It’s not like I couldn’t afford anything I wanted."
            An normal "Plus, you shouldn’t steal something that’s not worth being caught over, anyway."
            c "But I guess mouflons are an exception to that."
            An smirk "That farmer was asking for it leaving them unattended like that. I was just teaching him a valuable lesson about installing proper fencing."
            c "Sure you were."

    "Purposely gone out of your way to spite someone." if not ryann_atttw_minigame_spite and ryann_atttw_minigame_round_counter >= 1: # Anna
        $ ryann_atttw_minigame_spite = True
        c "Never have I ever,{fast} purposely gone out of your way to spite someone."
        An smirk "Wow, you know me so well."
        c "I’ll take that as a yes?"
        An normal "Yeah. Long story short, I had more than my fair share of malicious and spiteful moments when I was younger."
        An smirk "Especially when I was a teenager. I was a menace back then. But because I had such a “{i}brilliant mind{/i}”, I was pretty much untouchable."
        c "I pity anyone who had to deal with you back then. I can only imagine how bad it was."
        An normal "Oh, trust me, it was {i}really{/i} bad."

        $ ryann_atttw_minigame_anna_points -= 1
        $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points

    "Accidentally ripped something with your claws." if not ryann_atttw_minigame_claws and ryann_atttw_minigame_round_counter >= 2: # Anna
        $ ryann_atttw_minigame_claws = True
        c "Never have I ever,{fast} accidentally ripped something with your claws."
        An face "Firstly, I thought you said no unfair questions, but you don’t even have claws."
        An "And secondly, of course that’s happened before. That’s happened to {i}literally{/i} every single dragon at some point."
        c "Well, given that dragons aren’t born, and that happens to literally every single human, I’d say that just makes us fair."
        An smirk "Touché."

        $ ryann_atttw_minigame_anna_points -= 1
        $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points

    "Gotten into a fight." if not ryann_atttw_minigame_fight and ryann_atttw_minigame_round_counter >= 3: # None
        $ ryann_atttw_minigame_fight = True
        c "Never have I ever,{fast} gotten into a fight."
        An face "Seriously?"
        c "What?"
        An "You really thought I’d be the kind of person who’d get into a physical fight with someone?"
        An normal "Just because I can sometimes come off as a bit hostile towards people, doesn’t mean I’d actually fight someone. That’s how you get arrested for assault and battery."
        c "But what about that whole conflict with Reza?"
        An face "I wouldn’t classify that as a fight. If that pathetic coward didn’t have that toy of his, any one of us could have dealt with him in a heartbeat."
        An smirk "And from what I recall, [player_name], you were there for that too."
        c "Uh…"
        An normal "So let’s say it doesn’t count, and move on."

if ryann_atttw_minigame_anna_points == 0 or ryann_atttw_minigame_player_points == 0:
    jump ryann_atttw_minigame

$ renpy.pause (0.5)
show anna normal with dissolve

if ryann_atttw_minigame_player_points == 1 and ryann_atttw_minigame_anna_points > 1:
    $ renpy.pause (0.5)
    An smirk "Well, it looks like it's time to end this."
    An "Never have I ever,{w=0.5} gotten, {i}intimately close{/i}, with another species."
    $ renpy.pause (2.0)
    m "Anna put a finger down."
    $ ryann_atttw_minigame_anna_points -= 1
    $ ryannlDisplayVar1 = ryann_atttw_minigame_anna_points
    An "Well, [player_name]? I already know your answer."
    m "I sighed and reluctantly put my last finger down."
    $ ryann_atttw_minigame_player_points -= 1
    $ ryannDisplayVar2 = ryann_atttw_minigame_player_points
    $ renpy.pause (0.5)
    An "Good little human."
    jump ryann_atttw_minigame

if ryann_atttw_minigame_round_counter == 0:
    An "Hmm…"
    $ renpy.pause (1.5)
    An smirk "I got it."
    An normal "Never have I ever,{w=0.5} been born."
    c "Okay, that’s just unfair."
    An smirk "What rule says I can’t?"
    c "Well… none. But, still, it just ruins the fun."
    c "It’s like me asking, never have I ever, hatched from an egg. You see how it’s an unfair question?"
    An face "Yeah, yeah. I get it."
    An normal "Let’s just keep going."

    $ ryann_atttw_minigame_player_points -= 1
    $ ryannDisplayVar2 = ryann_atttw_minigame_player_points

if ryann_atttw_minigame_round_counter == 1:
    $ renpy.pause (1.5)
    An "Never have I ever,{w=0.5} {i}not{/i} seen the fireworks at the festival."
    c "{i}Not{/i} seen the fireworks? But we went to see them together?"
    An smirk "Yes. We went to see the fireworks, but we left early."
    An normal "We were there for not even a full minute. I don’t count that as seeing the whole show."
    c "Fine. You can have that one."

    $ ryann_atttw_minigame_player_points -= 1
    $ ryannDisplayVar2 = ryann_atttw_minigame_player_points

if ryann_atttw_minigame_round_counter == 2:
    $ renpy.pause (1.5)
    An "Never have I ever,{w=0.5} not been camping before."
    c "Actually, I have."
    An smirk "You actually think I’ll fall for that?"
    if sebastianunplayed == False and sebastianfail == False:
        c "Well, when I first came here, me and Sebastian spent a night camping in a cave near my apartment."
        An normal "Oh, yeah, I’ve heard of that place."
        c "Have you ever been there?"
        An face "No. It seemed way too pre-organized and pampered to be considered proper camping for me."
        An normal "You could just go to a cheap hotel and leave the windows open for a similar experience."
    
    else:
        c "Well, after the flare, times could be tough. There were certain points where some of us had to sleep in tents."
        show anna sad with dissolve
        c "I guess you could argue it wasn’t camping because it wasn't for a vacation, but I’d say it’s close enough."
        An "Yeah, I think that does count."
        An face "Sorry for making you bring that up."
        c "It’s alright."

if ryann_atttw_minigame_round_counter == 3:
    $ renpy.pause (1.5)
    show anna smirk with dissolve
    $ renpy.pause (0.5)
    c "I don't like that smirk."
    An "Never have I ever,{w=0.5} seen more than three humans."
    c "Yeah, alright. You got me there."
    An smirk "I know. That’s why I asked it."

    $ ryann_atttw_minigame_player_points -= 1
    $ ryannDisplayVar2 = ryann_atttw_minigame_player_points

if ryann_atttw_minigame_round_counter == 4:
    An sad "…"
    c "Well?"
    An face "I can’t think of anything. I didn’t expect this to be going on for so long."
    An sad "I don’t know. Never have I ever,{w=0.5} seen a flying performance?"
    $ renpy.pause (2.0)
    c "Yes…"
    An normal "Wow, that was lucky."
    An smirk "I mean, of course, I knew that. And of course, a human like you, would be intreated in flying-related stuff, considering it’s so new to you."
    c "Have you not seen a flying performance?"
    An normal "No. I have no interest in watching that. I see people flying every day, so why would I purposely go out of my way to watch someone flying if looking out of a window could accomplish the same thing?"

    $ ryann_atttw_minigame_player_points -= 1
    $ ryannDisplayVar2 = ryann_atttw_minigame_player_points

$ renpy.pause (0.5)
show anna normal with dissolve

$ ryann_atttw_minigame_round_counter += 1
jump ryann_atttw_minigame

# ===========================================================================================================================================================

label ryann_atttw_minigame_end:

$ renpy.pause (1.5)
hide screen ryannextrainfo
$ renpy.pause (0.5)

if ryann_atttw_minigame_winner == "player":
    c "Looks like I won."
    An normal "Yes, you did."
    if ryann_atttw_minigame_bet == "bragging":
        c "Yeah, I know. You didn’t stand a chance."
        An face "Yeah, {i}you{/i} won the game that {i}you{/i} propositioned."
        c "Wow. Someone’s upset because they lost."
        $ renpy.pause (0.5)

    if ryann_atttw_minigame_bet == "smore":
        c "So, about that last smore."
        An "Yeah, go ahead, take it."
        m "Anna pushed her bag over to me, and I put the remaining ingredients together to make the last smore."
        $ renpy.pause (0.5)
        menu:
            "Keep it.":
                play sound "fx/pizzabite.ogg"
                $ renpy.pause (0.5)
                c "Wow, this smore is {i}so{/i} good…"
                An face "Okay, smartass, you don’t have to rub it in."
                c "Don’t act like you wouldn’t be doing the exact same thing."

            "Share it.":
                c "Hey, Anna, you want half?"
                An sad "No, you won, so you get the smore. That was the bet."
                c "Yeah, I get the smore, so I choose what to do with it, and I’m sharing it with you."
                $ renpy.pause (1.0)
                An normal "Alright, fine."
                $ renpy.pause (1.5)
                An "Thanks."
                $ renpy.pause (0.5)
                play sound "fx/pizzabite.ogg"
                $ renpy.pause (1.5)

    if ryann_atttw_minigame_bet == "tent":
        c "And it also looks like you’ll be taking down the tent."
        An face "I still think it’s wildly unfair when I never wanted to bring it in the first place."
        $ renpy.pause (2.0)
        c "If I offer to help you, will it prevent you from having a tantrum and ripping the tent apart?"
        An normal "See? Now that’s an actually fair deal."

if ryann_atttw_minigame_winner ==  "anna":
    An smirk "Well, it looks like we have a winner."
    c "Yeah…"
    if ryann_atttw_minigame_bet == "bragging":
        An "It sure does feel good to win. Not that you’d know."
        if eckannagameoutcome > 15:
            # If played through NSTH and won the rematch for the trivia game (Will anyone even see this?)
            c "Our rematch for that trivia game in the café begs to differ."
            An face "Shut it. You know what I meant."

    if ryann_atttw_minigame_bet == "smore":
        An "Guess I’ll be taking this."
        m "Anna took her bag and made the smore from the remaining stuff in it."
        play sound "fx/pizzabite.ogg"
        $ renpy.pause (1.0)
        m "She then purposely started eating it in a very taunting way, making sure to take her time."
        An "I wasn’t even hungry, but that smore tasted the best out of all of them."

    if ryann_atttw_minigame_bet == "tent":
        An "So, you’ll be the one taking down the tent."
        An normal "Which you would have to do regardless because I would have just left it out here."
        c "Seriously?"
        An "You’re the one who brought it. Not me."

if ryann_atttw_minigame_winner == "draw":
    c "Huh. I guess it’s a draw."
    An normal "That it is."
    c "So, what do we do?"
    if ryann_atttw_minigame_bet == "bragging":
        An "It’s probably better if we just call the whole bragging thing off."
        c "Yeah, that's probably for the best."

    if ryann_atttw_minigame_bet == "smore":
        An "We could just share the smore."
        c "Yeah, that seems like the best option."
        m "We made up the last smore and split it evenly."
        play sound "fx/pizzabite.ogg"
        $ renpy.pause (1.0)
        An "This would be nicer if the marshmallow was actually toasted."
        c "True, but it’s still better than nothing."

    if ryann_atttw_minigame_bet == "tent":
        An "Considering you’re the only one who wanted the tent, it’s only fair you take it down."
        c "But it was a draw, so it’s only fair we both take it down."
        An "Nope. You brought it, you take it down. I would’ve been perfectly fine without it."
        c "Fine."

$ renpy.pause (2.0)
An normal "You know, this game actually wasn’t too bad."
if ryann_atttw_minigame_bet == "bragging" and ryann_atttw_minigame_winner == "anna":
    An smirk "And, you know, I won, which is a big plus."
    show anna normal with dissolve

c "Well, I’m glad you enjoyed it."
$ renpy.pause (1.5)
An "Looks like it’s gotten pretty late."
c "Oh, yeah, it really has, huh?"
c "I’m actually feeling pretty tired now. I guess walking all day has finally caught up to us."
An "Seems like it has."
stop soundloop fadeout 10.0

play sound "fx/undress.ogg"
m "I proceeded to get undressed, and after some time arranging our makeshift bed of mismatched pillows and blankets, we settled down, embracing each other."
$ renpy.pause (1.5)
show anna sleep with dissolve
$ renpy.pause (0.5)
An slsmirk "I’ve been looking forward to this all day."
c "Looking forward to what? Stealing my body heat?"
An "Exactly."
c "Well, goodnight, Anna."
An sleep "Goodnight."
stop music fadeout 3.0
$ renpy.pause (2.5)
scene black with dissolveslow
$ renpy.pause (5.0)

# ===========================================================================================================================================================

play music "mx/cruising.ogg" fadein 6.0
$ renpy.pause (2.5)
scene ryann_tent with dissolveslow
$ renpy.pause (1.0)
m "I slowly awoke from my slumber, feeling groggy from the very different sleeping conditions."
$ renpy.pause (0.5)
show anna sleep with dissolveslow
m "I steadily regained my bearings, and realized Anna was now partially lying on top of me, probably from moving during the night."
m "She was still asleep, so I tried my best not to wake her, while still trying to stretch out my stiff muscles."
$ renpy.pause (2.5)
show anna normal with dissolve
m "Anna then slowly woke up too, stretching in a similar way to how a big cat would."
c "Morning, sleepyhead."
An "Morning."
c "Seems like you’re well-rested."
An smirk "Getting to sleep outside and having my very own self-warming pillow makes a big difference."
show anna normal with dissolve
$ renpy.pause (3.0)
m "We laid there together for a while longer, until Anna eventually decided to get up."
An "Come on, we can’t just lie here forever. I have something for us to do."
c "Alright, just give me a minute to get dressed."
m "She left the tent, and after getting dressed, I followed."
play sound "fx/ryann_tent_zip.mp3"
$ renpy.pause (0.5)

scene black with dissolve
$ renpy.pause (1.0)
scene forest2
show anna normal
with dissolve
$ renpy.pause (1.5)
An "Catch."
m "Anna threw something to me, which turned out to be an energy bar."
c "What’s this?"
An "Breakfast. Eat it, you’ll need the energy for later."
m "She took out her own bar and started eating it too."
c "Wow, water and energy bars. Truly a breakfast for champions."
if ryann_atttw_minigame_bet == "bragging" and ryann_atttw_minigame_winner == "anna":
    An smirk "After that embarrassing loss last night, you shouldn’t be calling yourself a champion."
    c "You’re really going to take full advantage of the whole bragging rights thing, aren’t you?"
    An "You knew exactly what you were risking when you made the bet."
    show anna normal with dissolve
    $ renpy.pause (1.0)

m "I opened the wrapper and started eating the bar, as Anna was finishing hers."
An "Alright, let’s go."
c "Where are we going?"
An smirk "It’s a surprise."
c "When you’re the one who has a surprise, I’m immediately on guard."
An normal "Trust me, it’ll be fun."
c "Alright."

$ renpy.pause (0.5)
scene black with dissolve
$ renpy.pause (2.5)
scene ryann_lake with dissolve
$ renpy.pause (1.5)
show anna normal flip at Position(xpos=0.2 )with easeinleft
$ renpy.pause (0.5)
An "We’re here."
c "You brought us to a lake?"
An smirk flip "Yes, [player_name]. This is a lake. Well done."
c "Ha ha."
An normal flip "I’m assuming you’re not getting in fully dressed?"
c "Yeah."
An "Then what are you waiting for?"
c "Anna, we’re out in the open. I’m not just going to randomly start getting undressed here."
An smirk flip "And why not? It’s just the two of us out here, and there’s nothing I haven't seen already."
c "But what about when I get out? I’ll just be getting my clothes wet then."
An normal flip "Then I’ll make a fire so you can get dry."
An smirk flip "[player_name], why are you stalling so much? Can you not swim, and are too embarrassed to admit it?"
c "Oh, shut up."
show anna normal flip with dissolve
m "Not having a proper swimsuit, I reluctantly get undressed down to just my underwear and put my clothes aside for later, next to Anna’s bag."
m "I made my way over to the lake's edge, and bent down to feel the water temperature."
if ryann_atttw_annoy_anna >= 4:
    c "W-Wow, that’s really col-{w=0.3}{nw}"
    play sound "fx/watersurface.ogg"
    m "But before I could even finish the thought, I felt a shove from behind."
    $ renpy.pause (1.5)
    c "A-Anna!" with vpunch
    An smirk flip "We’re still out here for the rest of the week. Hopefully, this’ll make you think twice before annoying me again."
    c "The water is freezing!"
    An "Come on, it’s not that bad. You would’ve had to get used to the temperature anyway. I just sped up the process."
    m "Anna then entered the water too, albeit by her own choice."
    show anna at Position(xpos=0.5) with ease
    $ renpy.pause (0.2)
    show anna normal with dissolve

else:
    c "W-Wow, that’s really cold."
    An "Come on, [player_name], it’s not that bad."
    m "Anna then entered the water, and seem to be mostly unaffected by it."
    show anna at Position(xpos=0.5) with ease
    $ renpy.pause (0.2)
    show anna normal with dissolve
    $ renpy.pause (0.5)
    An smirk "See? Now stop stalling."
    m "I slowly made my way into the water too, trying my best to ignore the cold shock."
    An normal "Well, how is it?"
    c "Cold, very cold."
    An "Don’t worry, you’ll get used to it."

m "We made our way deeper into the water, and as Anna said, I started to get accustomed to the temperature."
c "Y-You know, you were right, it’s not too bad. My body just needed a minute to adjust."
$ renpy.pause (2.0)
show anna smirk with dissolve
$ renpy.pause (1.0)
m "A mischievous smirk started to appear on Anna’s face, which immediately told me what she was doing."
c "Anna, don’t you dare."
An "Don’t I dare do what?"
c "Anna-{w=0.5}{nw}"
play sound "fx/ryann_water_splash_1.mp3"
$ renpy.pause (2.0)
c "You-{w=0.5}{nw}"
play sound "fx/ryann_water_splash_2.mp3"
$ renpy.pause (2.5)
An "What’s wrong, [player_name]? Not-{w=0.5}{nw}"
play sound "fx/ryann_water_splash_1.mp3"
show anna disgust with dissolve
$ renpy.pause (0.5)
show anna normal with dissolve
c "Yeah! How does that feel?"
An smirk "Refreshing."
An normal "You’ll have to do better than-{w=0.5}{nw}"
play sound "fx/ryann_water_splash_2.mp3"
show anna disgust with dissolve
$ renpy.pause (1.0)
show anna face with dissolve
$ renpy.pause (1.5)
c "You {i}were{/i} asking for it."
show anna normal with dissolve
$ renpy.pause (1.5)
hide anna with dissolve
m "I then shifted my weight backwards so I was floating on my back and started to skygaze. Anna started copying me soon after, so both of us were floating in blissful silence."

$ renpy.pause (0.5)
scene black with dissolve
$ renpy.pause (0.5)
scene ryann_sky at Pan((25, 250), (0, 0), 9.0) with dissolveslow
$ renpy.pause (7.0)
scene black with dissolve
$ renpy.pause (0.5)
scene ryann_lake
show anna normal 
with dissolve
$ renpy.pause (0.5)
An face "This is a lot more boring than I thought…"
c "Then let’s make it more interesting."
show anna normal with dissolve
m "I sat back up and looked around us."
$ renpy.pause (2.0)
c "How about we go cliff diving?"
An sad "Cliff diving? Is it even safe to do that here?"
c "Sounds to me like you’re scared."
An face "I’m not scared. I’m just concerned for our safety."
$ renpy.pause (2.0)
c "You’re definitely scared."
$ renpy.pause (2.0)
An sad "Fine. We’ll go cliff diving."

$ renpy.pause (1.0)
scene black with dissolve
$ renpy.pause (1.0)
m "We got out of the water, and after a minute of walking around the lake, we found a suitable cliff to jump from."
m "I made my way over to the edge of the cliff and peeked over."
scene ryann_cliff with dissolve
$ renpy.pause (1.5)
show anna normal at Position(xpos=0.8) with dissolve
$ renpy.pause (0.5)
if ryann_atttw_annoy_anna >= 6:
    c "Yeah, this should-{w=0.3}{nw}"
    m "I suddenly felt another shove from behind, almost pushing me over the cliff's edge, just to be barely pulled back by my arm."
    c "Anna!" with vpunch
    An smirk "Careful you don’t fall."
    c "T-That was {i}way{/i} too close."
    $ renpy.pause (1.0)
    show anna sad with dissolve
    $ renpy.pause (1.5)
    An face "In hindsight, it wasn’t a good idea to do that. I just thought it would be funny."
    An sad "Sorry."
    c "It’s alright. To be fair, you did get me pretty good there."
    show anna normal with dissolve

else:
    c "Yeah, this should work."

$ renpy.pause (1.0)
show anna at Position(xpos=0.5) with ease
m "Anna walked over to the cliff edge too and looked over."
c "Do you want to go first or second?"
An sad "I don’t know. You decide."
$ renpy.pause (0.5)
menu:
    "[[Jump]":
        $ ryann_atttw_cliff_dive_choice = "jump"
        $ renpy.pause (0.5)
        m "I took a few steps backward for a better run-up."
        
        $ renpy.pause (0.5)
        scene black with dissolve
        $ renpy.pause (0.5)
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        play sound "fx/wooshes.ogg"
        $ renpy.pause (0.6)
        stop sound
        $ renpy.pause (1.0)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (1.7)
        play sound "fx/underwater.ogg"
        $ renpy.pause (3.0)
        play sound "fx/watersurface.ogg"

        scene ryann_lake with dissolve
        $ renpy.pause (1.5)
        c "See, Anna? It’s fine."
        An face "{size=-5}Yeah, I can see that.{/size}"
        c "So what are you waiting for? Jump!"
        $ renpy.pause (1.5)
        An sad "{size=-5}Fine.{/size}"
        m "Anna then disappeared over the cliff face, but then reappeared a few seconds later jumping down."

        $ renpy.pause (0.5)
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        play sound "fx/wooshes.ogg"
        $ renpy.pause (0.6)
        stop sound
        $ renpy.pause (1.0)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (4.0)
        play sound "fx/watersurface.ogg"
        show anna sad with easeinbottom
        $ renpy.pause (1.0)
        c "It wasn’t that hard, was it?"
        An face "Shut up."

    "It’s okay to be scared.":
        $ ryann_atttw_cliff_dive_choice = "scared"
        c "Hey, Anna, it’s okay if you’re scared."
        An face "I’m not scared."
        c "Then what’s stopping you?"
        An sad "…"
        c "If I go first to show you it’s safe, will you go after?"
        $ renpy.pause (1.5)
        An face "Yeah, sure, whatever."
        $ renpy.pause (1.0)
        m "I took a few steps backward for a better run-up."

        $ renpy.pause (0.5)
        scene black with dissolve
        $ renpy.pause (0.5)
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        play sound "fx/wooshes.ogg"
        $ renpy.pause (0.6)
        stop sound
        $ renpy.pause (1.0)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (1.7)
        play sound "fx/underwater.ogg"
        $ renpy.pause (3.0)
        play sound "fx/watersurface.ogg"

        scene ryann_lake with dissolve
        $ renpy.pause (1.0)
        c "See? It’s perfectly safe."
        c "So are you coming, or what?"
        An sad "…"
        m "Anna then disappeared over the cliff face, but then reappeared a few seconds later jumping down."
        $ renpy.pause (0.5)
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        play sound "fx/wooshes.ogg"
        $ renpy.pause (0.6)
        stop sound
        $ renpy.pause (1.0)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (3.0)
        play sound "fx/watersurface.ogg"
        show anna sad with easeinbottom
        $ renpy.pause (1.0)
        c "I told you it was safe."
        An face "Shut up."

    "We can jump together.":
        $ ryann_atttw_cliff_dive_choice = "together"
        c "We can jump together if you want."
        $ renpy.pause (1.5)
        An normal "Alright."
        m "We took a few steps back, then ran forward together hand-in-hand."

        $ renpy.pause (0.5)
        scene black with dissolve
        $ renpy.pause (0.5)
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        play sound "fx/wooshes.ogg"
        $ renpy.pause (0.6)
        stop sound
        $ renpy.pause (1.0)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (1.7)
        play sound "fx/underwater.ogg"
        $ renpy.pause (3.0)
        play sound "fx/watersurface.ogg"

        scene ryann_lake 
        show anna sad
        with dissolve
        $ renpy.pause (1.0)
        c "See? It wasn’t that bad."
        An face "Whatever."
        show anna sad with dissolve 
        $ renpy.pause (1.5)
        An normal "Thanks for that, [player_name]."
        c "You’re welcome."

    "[[Push her]":
        $ ryann_atttw_cliff_dive_choice = "push"
        $ player_name_caps = player_name.upper()
        $ renpy.pause (1.0)
        m "I took a few steps back and pretended to get a run-up, but instead of running past her, I ran toward Anna and shoved her."
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        show anna rage with dissolve
        An "[player_name_caps], YOU FU-{w=0.3}{nw}" with Shake ((0, 0, 0, 0), 0.3, dist=10)
        hide anna with dissolve
        $ renpy.pause (0.5)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (3.5)
        c "(Now I’m scared for multiple reasons of what’s waiting for me at the bottom…)"
        $ renpy.pause (1.0)

        $ renpy.pause (0.5)
        scene black with dissolve
        $ renpy.pause (0.5)
        play sound "fx/run.ogg"
        $ renpy.pause (1.2)
        play sound "fx/wooshes.ogg"
        $ renpy.pause (0.6)
        stop sound
        $ renpy.pause (1.0)
        play sound "fx/ryann_cliff_dive.mp3"
        $ renpy.pause (1.7)
        play sound "fx/underwater.ogg"
        $ renpy.pause (3.0)
        play sound "fx/watersurface.ogg"

        scene ryann_lake 
        show anna rage
        with dissolve
        $ renpy.pause (1.0)
        An "…"
        c "Uh… You alright, Anna…?"
        An "I could kill you right now."
        An "There’s no witnesses, and I could just claim you drowned when I wasn’t watching."
        $ renpy.pause (1.5)
        c "B-But you’d never actually do that, right…?"
        An face "I’m still considering it."

$ renpy.pause (0.5)
hide anna with dissolve
$ renpy.pause (0.5)
if ryann_atttw_cliff_dive_choice == "push":
    m "After some more time just swimming around, and me making sure to stay outside of Anna’s reach while we were still in the water, we eventually made our way out of the water."
else:
    m "After some more time just swimming around, we eventually made our way out of the water."

$ renpy.pause (2.0)
show anna sad with dissolve
$ renpy.pause (0.5)
c "Anna, see how we’re both alive and unharmed? Now you know cliff diving isn’t something to be scared of."
if ryann_atttw_cliff_dive_choice == "together":
    An face "Shut it, [player_name]."
else:
    An disgust "[player_name], you better shut the hell up about that before I make you."
c "Okay, okay. I’ll drop it."
show anna sad with dissolve
$ renpy.pause (2.0)
An normal "Anyway, I should make you a fire so you can dry off."

show anna normal with dissolve
$ renpy.pause (0.2)
show anna at Position(xpos=0.25) with ease
$ renpy.pause (0.5)
m "Anna started to clear out a patch of grass to start a fire on, and in the meantime, my gaze wandered around our immediate area."
m "Suddenly, I spotted a creature that resembled a deer further down the lake drinking from it."
c "Hey, Anna, look."
$ renpy.pause (0.2)
show anna normal flip with dissolve
$ renpy.pause (0.2)
An "What?"
m "I pointed at the deer-like creature."
An smirk flip "Good eye. That's our dinner sorted."
c "Well, the floor’s all yours."
An normal flip "No, I don’t think so. This time you’ll actually be helping me. So you’ll have to get dressed."
c "But I’m still wet, so I’ll get my clothes wet too."
An "It’ll only be for a few minutes, then I’ll make a fire like I said I would."
c "Also, why exactly do you need my help? Are your hunting skills not as good as you said they were?"
An face flip "This isn’t like last time. This isn’t a domesticated animal that’ll just stand there all doe-eyed waiting to be killed. This is a wild animal that will run away."
An normal flip "I’ll go to the other side of it and you’ll scare it towards me."
An "Give me about… half a minute, and I’ll be ready. And don’t forget to get my bag."
$ renpy.pause (0.5)
show anna normal with dissolve
$ renpy.pause (0.2)
hide anna with easeoutleft
$ renpy.pause (0.5)
m "I started to get dressed, as Anna made her way past the tree line and deeper into the trees."
m "By the time I had got dressed, Anna had gotten closer, but not too close, to the deer-like creature, and soon make her way around to the other side of it."
m "Anna was still in my eyeshot, so she signaled me, and I made my way closer to the creature."
$ renpy.pause (1.5)
c "Hey!" with vpunch
m "Straight away it snapped up to look at me, then immediately started sprinting away from my direction."
m "Little did it know, Anna was waiting in the perfect position to pounce at its neck and claw at it as it tried to run away."
m "I made my way over to Anna, and she was already starting to prepare the fresh carcass."

$ renpy.pause (0.5)
show anna normal c with dissolve
$ renpy.pause (0.5)
An smirk c "This time, I get to choose what cut of meat I get first."
c "Anna."
An sad c "Oh, right. I’ll start a fire for you. The last thing we want is for you to get sick out here."
show anna normal c with dissolve
m "We then started to clear out a sufficient patch of grass for Anna to start a fire."
$ renpy.pause (1.5)
play sound "fx/firex.ogg"
$ renpy.pause (2.0)
m "I immediately clung to the fire to dry off and warm up, while Anna worked on cutting some meat for us to eat."
c "So, what animal is this?"
An "It’s called a barasingha. It’s rare for it to be reared by ranchers, but the meat is still perfectly edible."
play sound "fx/gore.ogg"
m "She then cut some slabs of the meat and put them near the fire to cook, and kept a few for herself to eat raw."
An "I remember you humans can’t eat raw meat, so I’ll just keep the rest of this for myself."
stop sound fadeout 1.5
c "If only we’d brought a cooler, or something, so we could keep some of this for another day or two."
An face c "First you bring a tent, and now you want a cooler. You might as well have brought a generator, and a quadruped-sized bed with you as well."
c "But what will we eat for the rest of our time out here?"
An normal c "This wasn’t the only animal out here, [player_name], and you’ve proven to be a capable hunting apprentice, so we’ll be fine."
An "And besides, I brought some spare food with me, just in case we don’t find anything."
c "Is that where you got those energy bars from earlier?"
An "Yeah. I knew we wouldn’t have time to look for food yesterday, and I didn’t want us going hungry, so I came prepared."
if ryann_atttw_survival_challenge == True:
    An face c "Again, this is supposed to be a vacation, not a survival challenge."
    show anna normal c with dissolve
else:
    An "This is supposed to be a vacation after all, not a survival challenge."

$ renpy.pause (2.0)
m "After some time, I picked up and tried the now perfectly cooked meat."
An "How is it?"
c "Well, you {i}literally{/i} can’t get fresher than this."
An smirk c "Exactly. You won’t find meat as high quality as this in a butcher’s."
show anna normal c with dissolve
$ renpy.pause (2.0)
An smirk c "Actually, I have an idea."
show anna normal c with dissolve
play sound "fx/undress.ogg"
m "Anna then grabbed her bag and searched through it, to then pull out a rather large bottle of wine."
An "I was planning to save this for later, but we might as well have some now."
play sound "fx/screwopen.ogg"
m "She then unscrewed the bottle’s cap and took a quick swig from it."
An "Mmm, that’s good."
m "She then passed the bottle over to me."
An "Don’t drink too much. We have to make it last the week."
m "I proceed to also take a quick swing of the wine. It was very sweet and flavorful, but it also had a kind of spicy kick to it."
c "That is pretty good."
An smirk c "Which is exactly why I brought it."
show anna normal c with dissolve 
m "By now, I had sufficiently dried off, and as the fire slowly died down, we both finished our respective meals, washing them down with sips of wine."
$ renpy.pause (2.0)
c "First you had smores and hot chocolate, and now wine. Now I’m really curious what else you have in that bag."
An smirk c"I might have a few more surprises for throughout the week, but I don’t want to spoil anything, so you’ll have to wait and see."
c "I was definitely surprised by the wine. I assumed you wouldn’t have been a fan of drinking."
An normal c "I don’t drink often. Usually just for special occasions."
c "So, why’d you bring wine this time?"
An smirk c "Well, there’s only so much you can do in the woods, so I thought bringing some would be helpful in case things started to get too boring."
c "Oh my."
An normal c "But not tonight. I just thought meat would pair better with wine, rather than water."
c "Oh."
An smirk c "Oh? What, are you disappointed, [player_name]?"
c "Well, uh, it must be the wine talking."
An "You’re blaming it on the wine? Really?"
An normal c "You’re either a terrible liar, or concerningly lightweight."
c "Shush."
$ renpy.pause (2.0)

m "By now, I’d noticed that the sun was much lower in the sky, and it was only a few minutes to sunset."
c "It's getting pretty late. We should get back to our camp."
An "Alright. Just give me a minute to wash this blood off."
hide anna with dissolve
m "Anna walked over to the lake and washed the blood off. Afterward, she came back over, and we made our way back to our camp."
$ renpy.pause (0.5)
scene black with dissolveslow
$ renpy.pause (0.5)
m "By the time we’d gotten back, it was sunset and we headed straight into the tent."
stop music fadeout 2.0
$ renpy.pause (0.5)
play sound "fx/ryann_tent_zip.mp3"

$ renpy.pause (1.5)
scene ryann_tent_dark
show anna normal
with dissolveslow

$ renpy.pause (1.0)
play music "mx/sleepingcity.ogg"
$ renpy.pause (0.5)
play sound "fx/undress.ogg"
m "We once again settled down into our makeshift bed set up together, with Anna lying on her back, one arm wrapped around me, and me at her side, resting my head on her chest."
An smirk "I’m actually glad you managed to talk me into doing this. I’ve really enjoyed the past two days."
if ryann_atttw_annoy_anna >= 6 or ryann_atttw_cliff_dive_choice == "push":
    An face "Well, for the most part, anyway…"
    show anna normal with dissolve
c "I'm happy to hear that."
An normal "And we're still out here for a few more days."
An smirk "You know, maybe this whole work-life balance stuff isn’t too bad after all."
show anna normal with dissolve
$ renpy.pause (2.0)
show anna sad with dissolve
$ renpy.pause (0.5)
An "Hey, [player_name], I want to explain the whole cliff diving thing from earlier."
An "Look, I’m not scared of heights, or cliff diving or whatever, it’s just…"
$ renpy.pause (2.5)
An "When you know your life is on a deadline, you stop caring about certain things."
An "I didn’t care about the consequences of my actions before, because I knew I wouldn’t have been around long enough to deal with them."
An normal "But thanks to you, I have a second chance now."
An sad "That’s why I’m trying to not be as reckless as before. I want to make sure I don’t waste it on something stupid."
c "Anna…"
m "I held her in a tighter embrace and snuggled even closer."
show anna normal with dissolve
c "I’m sorry for making fun of you, saying you were scared. If I’d know that’s how you felt…"
An "It’s alright. I know you meant it in a good-humored way."
An smirk "Besides, I probably would’ve done something similar if the roles were reversed."
show anna normal with dissolve
c "Still, even if you were scared, I shouldn’t have been making fun of you."
m "She then gave me a small peck on the top of my head before lying back down."
An sleep "[player_name], relax. We’re good now."
c "Right."

$ renpy.pause (2.5)
m "How Anna stretched earlier that morning gave me an idea, and now was the perfect time to enact it."
c "(I wonder if dragons also like this…)"
m "I began to move my arm down, and started to give Anna some belly rubs."
play soundloop "fx/purr.ogg" 
$ renpy.pause (0.5)
show anna slsmirk with dissolve
$ renpy.pause (2.0)
An "Tell anyone about this and I’ll cut out your tongue."
$ renpy.pause (2.5)
An "You know, I’m looking forward to the rest of this trip more and more knowing things like this are waiting for me."
c "And I’m looking forward to having the rest of this trip to continuously annoy you."
An face "You really just have to ruin a nice moment like this, don’t you?"
c "Well, I {i}did{/i} just say I was going to annoy you throughout the rest of this trip."
An "I hate you."
c "I love you too."
show anna slblush with dissolve
$ renpy.pause (2.5)
An "I…"
$ renpy.pause (2.0)
show anna slblush2 with dissolve
$ renpy.pause (1.5)
An "{size=-7}I love you too, [player_name]…{/size}"
$ renpy.pause (3.0)
stop soundloop fadeout 9.0
stop music fadeout 5.0
scene black with dissolveslow
$ renpy.pause (8.0)


jump ryann_atttw_credits
