
image ryann_forest2_evening = "bg/ryann_forest2_evening.jpg"
image ryann_lake = "bg/ryann_lake.png"
image ryann_cliff = "bg/ryann_cliff.jpg"
image ryann_sky = "bg/ryann_sky.jpg"
image ryann_tent = "bg/ryann_tent.jpg"
image ryann_tent_dark = "bg/ryann_tent_dark.jpg"
image ryann_wilderness = "bg/ryann_wilderness.jpg"


init python:

    ryann_did_arson = False # Again, very incriminating variable name, but needed for compatibility for Casual Arson
    eckannagameoutcome = 1 # Compatibility for card game in NSTH

    ryann_atttw_annoy_anna = 0 

    ryann_atttw_campfire_questions = 0
    ryann_atttw_campfire_questions_stay_in_wild = False
    ryann_atttw_campfire_questions_find_spot = False
    ryann_atttw_campfire_questions_last_time_went_out = False
    ryann_atttw_survival_challenge = False

    ryann_atttw_minigame_bet = ""
    ryann_atttw_minigame_winner = ""
    ryann_atttw_minigame_round_counter = 0
    ryann_atttw_minigame_anna_points = 4
    ryann_atttw_minigame_player_points = 4

    ryann_atttw_minigame_seen_someone_die = False 
    ryann_atttw_minigame_fight = False 
    ryann_atttw_minigame_stealing = False 
    ryann_atttw_minigame_neglect_needs = False 
    ryann_atttw_minigame_burned = False 
    ryann_atttw_minigame_claws = False 
    ryann_atttw_minigame_spite = False 

    ryann_atttw_cliff_dive_choice = ""

    ryannDisplayVar1name = ""
    ryannDisplayVar1 = 0
    ryannDisplayVar1unit = ""
    ryannDisplayVar2name = ""
    ryannDisplayVar2 = 0
    ryannDisplayVar2unit = ""


    

# ===========================================================================================================================================================
# Credits

label ryann_atttw_credits:

play sound "mx/partingsong.ogg" fadein 1.0



show extra2 at Pan ((450, 0), (540,0), 20.0)
show eckcreditsan at right
with dissolvemed
$ renpy.pause (12.0)
scene black with dissolvemed

show rezathroatslit at Pan ((500, 326), (1280,0), 20.0)
show credits1 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 at left with dissolvemed
show credits2 at left with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show testingroom at Pan ((960,0), (0,233), 20.0)
show credits3 at right
with dissolvemed
$ renpy.pause (8.0)
show black2 at right with dissolvemed
show credits4 at right with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show cgcampfire at Pan ((0, 500), (1500, 100), 30.0)
show credits5 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 at left with dissolvemed
show credits6 at left with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show cgdamion at Pan ((600, 0), (400, 302), 23)
show credits7 at right
with dissolvemed
$ renpy.pause (8.0)
show black2 at right with dissolvemed
show credits8 at right with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
show cganna at Pan((-600, 302), (-600, 0), 22.0)
show credits9 at left
with dissolvemed
$ renpy.pause (8.0)
show black2 at left with dissolvemed
show credits10 at left with dissolvemed
$ renpy.pause (8.0)
scene black with dissolvemed
scene logo with dissolvemed
$ renpy.pause (3.0)
stop sound fadeout 2.5
$ renpy.pause (7.0)
scene black with dissolvemed
stop sound fadeout 2.5
$ renpy.pause (4.0)


jump ml_main_menu
