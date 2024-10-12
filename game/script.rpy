define beginMarker = "0.0"
define sceneAudio = ""
define endMarker = "0.0"
define waitTime = "0.0"
define drift = 0.0
define waitTag = ""
define line = ""
define tolerance = 0.5
define pad = .05
define playback_paused = False
define paused_position = 0.0
define current_line = ""
define current_character = None
define line_time_remaining = 0.0
define pause_start = 0.0
define pause_duration = 0.0
define config.main_menu_music = "audio/menu_piano.mp3"

default csbox = False

image smoke:
    "smokeloop/Comp 1_00001.png"
    pause 0.08
    "smokeloop/Comp 1_00003.png"
    pause 0.08
    "smokeloop/Comp 1_00005.png"
    pause 0.08
    "smokeloop/Comp 1_00007.png"
    pause 0.08
    "smokeloop/Comp 1_00009.png"
    pause 0.08
    "smokeloop/Comp 1_00011.png"
    pause 0.08
    "smokeloop/Comp 1_00013.png"
    pause 0.08
    "smokeloop/Comp 1_00015.png"
    pause 0.08
    "smokeloop/Comp 1_00017.png"
    pause 0.08
    "smokeloop/Comp 1_00019.png"
    pause 0.08
    "smokeloop/Comp 1_00021.png"
    pause 0.08
    "smokeloop/Comp 1_00023.png"
    pause 0.08
    "smokeloop/Comp 1_00025.png"
    pause 0.08
    "smokeloop/Comp 1_00027.png"
    pause 0.08
    "smokeloop/Comp 1_00029.png"
    pause 0.08
    "smokeloop/Comp 1_00031.png"
    pause 0.08
    "smokeloop/Comp 1_00033.png"
    pause 0.08
    "smokeloop/Comp 1_00035.png"
    pause 0.08
    "smokeloop/Comp 1_00037.png"
    pause 0.08
    "smokeloop/Comp 1_00039.png"
    pause 0.08
    "smokeloop/Comp 1_00041.png"
    pause 0.08
    "smokeloop/Comp 1_00043.png"
    pause 0.08
    "smokeloop/Comp 1_00045.png"
    pause 0.08
    "smokeloop/Comp 1_00047.png"
    pause 0.08
    "smokeloop/Comp 1_00049.png"
    pause 0.08
    "smokeloop/Comp 1_00051.png"
    pause 0.08
    "smokeloop/Comp 1_00053.png"
    pause 0.08
    "smokeloop/Comp 1_00055.png"
    pause 0.08
    "smokeloop/Comp 1_00057.png"
    pause 0.08
    "smokeloop/Comp 1_00059.png"
    pause 0.08
    "smokeloop/Comp 1_00061.png"
    pause 0.08
    "smokeloop/Comp 1_00063.png"
    pause 0.08
    "smokeloop/Comp 1_00065.png"
    pause 0.08
    "smokeloop/Comp 1_00067.png"
    pause 0.08
    "smokeloop/Comp 1_00069.png"
    pause 0.08
    "smokeloop/Comp 1_00071.png"
    pause 0.08
    "smokeloop/Comp 1_00073.png"
    pause 0.08
    "smokeloop/Comp 1_00075.png"
    pause 0.08
    "smokeloop/Comp 1_00077.png"
    pause 0.08
    "smokeloop/Comp 1_00079.png"
    pause 0.08
    "smokeloop/Comp 1_00081.png"
    pause 0.08
    "smokeloop/Comp 1_00083.png"
    pause 0.08
    "smokeloop/Comp 1_00085.png"
    pause 0.08
    "smokeloop/Comp 1_00087.png"
    pause 0.08
    "smokeloop/Comp 1_00089.png"
    pause 0.08
    "smokeloop/Comp 1_00091.png"
    pause 0.08
    "smokeloop/Comp 1_00093.png"
    pause 0.08
    "smokeloop/Comp 1_00095.png"
    pause 0.08
    "smokeloop/Comp 1_00097.png"
    pause 0.08
    "smokeloop/Comp 1_00099.png"
    pause 0.08
    "smokeloop/Comp 1_00101.png"
    pause 0.08
    "smokeloop/Comp 1_00103.png"
    pause 0.08
    "smokeloop/Comp 1_00105.png"
    pause 0.08
    "smokeloop/Comp 1_00107.png"
    pause 0.08
    "smokeloop/Comp 1_00109.png"
    pause 0.08
    "smokeloop/Comp 1_00111.png"
    pause 0.08
    "smokeloop/Comp 1_00113.png"
    pause 0.08
    "smokeloop/Comp 1_00115.png"
    pause 0.08
    "smokeloop/Comp 1_00117.png"
    pause 0.08
    "smokeloop/Comp 1_00119.png"
    pause 0.08
    "smokeloop/Comp 1_00121.png"
    pause 0.08
    "smokeloop/Comp 1_00123.png"
    pause 0.08
    "smokeloop/Comp 1_00125.png"
    pause 0.08
    "smokeloop/Comp 1_00127.png"
    pause 0.08
    "smokeloop/Comp 1_00129.png"
    pause 0.08
    "smokeloop/Comp 1_00131.png"
    pause 0.08
    "smokeloop/Comp 1_00133.png"
    pause 0.08
    "smokeloop/Comp 1_00135.png"
    pause 0.08
    "smokeloop/Comp 1_00137.png"
    pause 0.08
    "smokeloop/Comp 1_00139.png"
    pause 0.08
    "smokeloop/Comp 1_00141.png"
    pause 0.08
    "smokeloop/Comp 1_00143.png"
    pause 0.08
    "smokeloop/Comp 1_00145.png"
    pause 0.08
    "smokeloop/Comp 1_00147.png"
    pause 0.08
    "smokeloop/Comp 1_00149.png"
    pause 0.08
    "smokeloop/Comp 1_00151.png"
    pause 0.08
    "smokeloop/Comp 1_00153.png"
    pause 0.08
    "smokeloop/Comp 1_00155.png"
    pause 0.08
    "smokeloop/Comp 1_00157.png"
    pause 0.08
    "smokeloop/Comp 1_00159.png"
    pause 0.08
    "smokeloop/Comp 1_00161.png"
    pause 0.08
    "smokeloop/Comp 1_00163.png"
    pause 0.08
    "smokeloop/Comp 1_00165.png"
    pause 0.08
    "smokeloop/Comp 1_00167.png"
    pause 0.08
    "smokeloop/Comp 1_00169.png"
    pause 0.08
    "smokeloop/Comp 1_00171.png"
    pause 0.08
    "smokeloop/Comp 1_00173.png"
    pause 0.08
    "smokeloop/Comp 1_00175.png"
    pause 0.08
    "smokeloop/Comp 1_00177.png"
    pause 0.08
    "smokeloop/Comp 1_00179.png"
    pause 0.08
    "smokeloop/Comp 1_00181.png"
    pause 0.08
    "smokeloop/Comp 1_00183.png"
    pause 0.08
    "smokeloop/Comp 1_00185.png"
    pause 0.08
    "smokeloop/Comp 1_00187.png"
    pause 0.08
    "smokeloop/Comp 1_00189.png"
    pause 0.08
    "smokeloop/Comp 1_00191.png"
    pause 0.08
    "smokeloop/Comp 1_00193.png"
    pause 0.08
    "smokeloop/Comp 1_00195.png"
    pause 0.08
    "smokeloop/Comp 1_00197.png"
    pause 0.08
    "smokeloop/Comp 1_00199.png"
    pause 0.08
    "smokeloop/Comp 1_00201.png"
    pause 0.08
    "smokeloop/Comp 1_00203.png"
    pause 0.08
    "smokeloop/Comp 1_00205.png"
    pause 0.08
    "smokeloop/Comp 1_00207.png"
    pause 0.08
    "smokeloop/Comp 1_00209.png"
    pause 0.08
    "smokeloop/Comp 1_00211.png"
    pause 0.08
    "smokeloop/Comp 1_00213.png"
    pause 0.08
    "smokeloop/Comp 1_00215.png"
    pause 0.08
    "smokeloop/Comp 1_00217.png"
    pause 0.08
    "smokeloop/Comp 1_00219.png"
    pause 0.08
    "smokeloop/Comp 1_00221.png"
    pause 0.08
    "smokeloop/Comp 1_00223.png"
    pause 0.08
    "smokeloop/Comp 1_00225.png"
    pause 0.08
    "smokeloop/Comp 1_00227.png"
    pause 0.08
    "smokeloop/Comp 1_00229.png"
    pause 0.08
    "smokeloop/Comp 1_00231.png"
    pause 0.08
    "smokeloop/Comp 1_00233.png"
    pause 0.08
    "smokeloop/Comp 1_00235.png"
    pause 0.08
    "smokeloop/Comp 1_00237.png"
    pause 0.08
    "smokeloop/Comp 1_00239.png"
    pause 0.08
    repeat

label splashscreen:
    $ renpy.movie_cutscene('wcsplash.webm')
    $ renpy.movie_cutscene('logosplash.webm')
    return

init python:
    import time

    if not persistent.start_label_jump:
        persistent.start_label_jump = "scene_0002B"

    def jump_start_label(first, second):
        _value = persistent.start_label_jump
        
        if persistent.start_label_jump == first:
            persistent.start_label_jump = second
        
        elif persistent.start_label_jump == second:
            persistent.start_label_jump = first
        
        return _value

    renpy.music.register_channel("ambient", "music", loop=True, tight=True)
    renpy.music.register_channel("vo", "music", loop=False, tight=True)
    renpy.music.register_channel("sfx", "music", loop=False, tight=True)

    def afterLoad():
        renpy.pause(1.0)


    config.after_load_callbacks = [afterLoad]
    preferences.show_empty_window = True

    if not persistent.endings:
        persistent.endings = []
        persistent.new_ending = False

    def isclose(a, b, tolerance):
        return abs(a-b) < tolerance

    def seekvoice(event, interact=True, **kwargs):
        global beginMarker, tolerance, drift
        if event == 'begin':
            pos = renpy.music.get_pos('vo')
            if pos is None:
                pos = float(beginMarker)
                drift = 0.0
                renpy.music.play("<from " + beginMarker + ">" + sceneAudio,'vo')
                return
            drift = pos - float(beginMarker)
            if not isclose(pos, float(beginMarker), tolerance):
                renpy.music.play("<from " + beginMarker + ">" + sceneAudio,'vo')

    def setWait(begin, end):
        global beginMarker, endMarker, waitTime, waitTag, sceneAudio, current_line, drift
        beginMarker = str(begin)
        endMarker = str(end)
        waitTime = str((end - begin) - drift if drift >= 0 else (end - begin))
        waitTag = '{p=' + waitTime + '}{nw}'


    def setVoiceTrack(name):
        global sceneAudio, beginMarker, endMarker, waitTime
        sceneAudio = name
        beginMarker = "0.0"
        endMarker = "0.0"
        waitTime = "0.0"
        drift = 0.0
        renpy.music.play(sceneAudio,'vo')
        renpy.music.set_pause(False, channel='vo')

    def killAudio():
        renpy.music.set_pause(True, channel='vo')
        renpy.music.set_pause(True, channel='ambient')

    def speak(c, line, resume=False):
        global pause_duration, waitTag, current_line, current_character, line_time_remaining
        current_line = line
        current_character = c
        if not resume:
            renpy.pause(0.0)
            renpy.checkpoint(renpy.say(c, line + waitTag))
        else:
            pause_duration = 0
            line_time_remaining = 0
            renpy.say(c.name, line)
        
        if line_time_remaining > 0.0:
            p = line_time_remaining
            
            line_time_remaining = 0
            current_line = current_line.split("{p")[0]
            if pause_duration >= p:
                speak(c, current_line + '{p=' + str(p) + '}{nw}', True)
            else:
                speak(c, current_line + '{p=' + str(pause_duration) + '}{nw}', True)



    def game_unpause():
        global pause_duration
        if pause_duration > 0:
            pause_duration += time.time() - pause_start
        else:
            pause_duration = time.time() - pause_start
        renpy.return_statement()

    def ending_reached(ending):
        import os
        import shutil
        ending_map = {
            '0039': 'shut up about this bitch4.txt',
            '0063': 'they just dont get it and never will.txt',
            '0074': 'attention5is6privilege7.txt',
            '0091': 'sdgsdg6sadhgdszfbadfb6adzfghzdfh6.txt',
            '0103': 'victims 2006 breed 2008 victims i want to kill myself look at me.txt',
            '0105': 'theanswerismaybejaajajajjajajaja.txt',
            '0121': 'priorirties in the year of our lord 2007.txt',
            '0126': 'she will never know who and its not fine.txt',
            '0127': 'i am the ball the ball the ball.txt',
            '0144': '3y3roll hardddddddddd.txt',
            '0145': 'po551b1t135.txt',
            '0153': 'dont do not look dont look at me i dont want it.txt',
            '0161': 'what about me, what ABOUT me 2010.txt',
            '0169': 'so close yet so 4375457far.txt',
            '0173': 'happy659087i5607905.txt',
        }
        desktop_path = os.path.expanduser("~/Desktop/")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(renpy.loader.transfn('endings/completed.txt'), 'r') as fp:
            endings = fp.read().splitlines()
            if ending not in endings:
                shutil.copy(renpy.loader.transfn('endings/' + ending_map[ending]), desktop_path)
        
        with open(renpy.loader.transfn('endings/completed.txt'), 'a') as fp:
            fp.writelines(["\n" + ending])

    def game_pause():
        global paused_position, endMarker, line_time_remaining, pause_start
        renpy.music.set_pause(True, channel='vo')
        renpy.music.set_pause(True, channel='ambient')
        pause_start = time.time()
        paused_position = renpy.music.get_pos('vo')
        line_time_remaining = float(endMarker) - paused_position if paused_position is not None else 0

init:

    $ config.enter_transition = None
    image black = Solid((0, 0, 0, 255))

transform transform_logo:
    alpha 0 xalign 1.2 yalign 0.2 size (700.0,395.0) subpixel True
    easein 1.0 alpha 1 xalign 0.88

screen pause_menu():
    tag menu

    on "show":
        action Function(game_pause)

    key "K_ESCAPE" action Function(game_unpause)
    key "mouseup_3" action Function(game_unpause)
    key "K_MENU" action Function(game_unpause)


    add "gui/nvl.png"
    style_prefix "main_menu"

    zorder 100

    hbox:
        frame:
            style "main_menu"

    add "gui/ClassOf09logo.png" at transform_logo

    vbox:

        xalign 0.5
        yalign 0.5


        textbutton _("Resume"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action Function(game_unpause)
        textbutton _("Options"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action ShowMenu('pause_prefs')
        textbutton _("Save"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action ShowMenu('pause_save')

        textbutton _("Main Menu"):
            activate_sound "audio/MainMenuPress.mp3"
            hover_sound "audio/MainMenuRollover.mp3"
            action [Stop("vo"),Stop("ambient"),MainMenu()]

style pause_menu_button_text:
    size 200




screen disable_Controls():
    tag menu
    zorder 0

    key "mouseup_1" action NullAction()
    key "mouseup_2" action NullAction()
    key "mouseup_3" action NullAction()
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    style_prefix "skip"

    vbox:
        spacing -5

        xalign 0.98
        yalign .98

        textbutton "Skip" action [Jump (jump_start_label("scene_0002A", "scene_0002B")), Hide("disable_Controls")]


screen disable_controls_for_ending():
    tag menu
    zorder 0
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()

    key "K_UP" action NullAction()
    key "K_DOWN" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()
    key "K_SPACE" action NullAction()

    key "a" action NullAction()
    key "b" action NullAction()
    key "c" action NullAction()
    key "d" action NullAction()
    key "e" action NullAction()
    key "f" action NullAction()
    key "g" action NullAction()
    key "h" action NullAction()
    key "i" action NullAction()
    key "j" action NullAction()
    key "k" action NullAction()
    key "l" action NullAction()
    key "m" action NullAction()
    key "n" action NullAction()
    key "o" action NullAction()
    key "p" action NullAction()
    key "q" action NullAction()
    key "r" action NullAction()
    key "s" action NullAction()
    key "t" action NullAction()
    key "u" action NullAction()
    key "v" action NullAction()
    key "w" action NullAction()
    key "x" action NullAction()
    key "y" action NullAction()
    key "z" action NullAction()

    key "0" action NullAction()
    key "1" action NullAction()
    key "2" action NullAction()
    key "3" action NullAction()
    key "4" action NullAction()
    key "5" action NullAction()
    key "6" action NullAction()
    key "7" action NullAction()
    key "8" action NullAction()
    key "9" action NullAction()


define NICOLE = Character("Nicole", callback=seekvoice)
define KYLAR = Character("Kylar", callback=seekvoice)
define ARI = Character("Ari", callback=seekvoice)
define CRISPIN = Character("Crispin", callback=seekvoice)
define TRODY = Character("Trody", callback=seekvoice)
define JEFFERY = Character("Jeffery", callback=seekvoice)
define BURLEDAY = Character("Mr. Burleday", callback=seekvoice)
define JECKA = Character("Jecka", callback=seekvoice)
define MOM = Character("Mom", callback=seekvoice)
define GAMER_BROTHER = Character("Gamer Brother", callback=seekvoice)
define COP = Character("Cop", callback=seekvoice)
define MALLCOP = Character("Mall Cop", callback=seekvoice)
define COACH = Character("Coach Colby", callback=seekvoice)
define KYLE = Character("Kyle", callback=seekvoice)
define EMILY = Character("Emily", callback=seekvoice)
define LYNN = Character("Principal Lynn", callback=seekvoice)
define HUNTER = Character("Hunter", callback=seekvoice)
define MEGAN = Character("Megan", callback=seekvoice)
define COUNSELOR = Character("Counselor", callback=seekvoice)
define KATZ = Character("Mr. Katz", callback=seekvoice)
define KAREN = Character("Karen", callback=seekvoice)
define BRAXTON = Character("Braxton", callback=seekvoice)
define KELLY = Character("Kelly", callback=seekvoice)
define EMT = Character("EMT", callback=seekvoice)
define GUEST = Character("Guest Speaker", callback=seekvoice)
define JAILPHONE = Character("Jail Phone", callback=seekvoice)
define MUSTANG = Character("Mustang Driver", callback=seekvoice)
define COROLLA = Character("Corolla Driver", callback=seekvoice)
define CAMRY = Character("Camry Driver", callback=seekvoice)
define LORRE = Character("Mr. Lorre", callback=seekvoice)
define AMES = Character("Ms. Ames", callback=seekvoice)
define FIEND = Character("Fiend", callback=seekvoice)
define ROSSLER = Character("Rossler's Deli Owner", callback=seekvoice)
define NICOLE_JECKA = Character("Nicole & Jecka", callback=seekvoice)
define none = Character("none", callback=seekvoice)


transform leftstage:
    xalign -0.11

transform leftmidstage:
    xalign 0.14

transform leftcenterstage:
    xalign 0.37

transform centerstage:
    xalign 0.5

transform rightcenterstage:
    xalign 0.63

transform rightmidstage:
    xalign 0.88

transform rightstage:
    xalign 1.12

transform off_right:
    xalign 1.4

transform off_farright:
    xalign 1.6

transform off_left:
    xalign -0.4

transform off_farleft:
    xalign -0.73

image opening cutscene = Movie(play="opening.webm")

image cs0074 = Movie (play="cs0074.webm", loop=False)

image cs0082 = Movie (play="cs0082.webm", loop=False)

image cs0095 = Movie (play="cs0095.webm", loop=False)

image cs0113 = Movie (play="cs0113.webm", loop=False)

image cs0131 = Movie (play="cs0131.webm", loop=False)

image cs0141 = Movie (play="cs0141.webm", loop=False)

image cs0160 = Movie (play="cs0160.webm", loop=False)

label start:
    stop music fadeout 0.7
    $ quick_menu = False
    $ _game_menu_screen = "pause_menu"
    show black
    show opening cutscene
    show screen disable_Controls
    $ renpy.pause(70, hard=True)

    $ renpy.jump(jump_start_label("scene_0002A", "scene_0002B"))

label scene_0002A:
    hide screen disable_Controls
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show title_september2008 onlayer screens
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter


    $ quick_menu = True

    scene school ext 3
    hide title_september2008 onlayer screens
    $ setVoiceTrack("audio/Scenes/0002A.mp3")
    show nicole sc1:
        off_left
        linear 2.2 leftmidstage

    show jecka sc1 smile:
        xalign 0.5

    $ setWait(2.377,3.545)
    $ speak(JECKA, "Hey you're on time.")
    $ setWait(3.545,6.256)
    $ speak(NICOLE, "I'm already so fuckin' over this.")
    show jecka sc1:
        xalign 0.5
    $ setWait(6.256,7.882)
    $ speak(JECKA, "All I said was \"hi\".")
    $ setWait(7.882,10.76)
    $ speak(NICOLE, "I wish I was high-- Do you think I'm here this early by choice?")
    $ setWait(10.76,12.262)
    $ speak(JECKA, "What is it this time?")
    $ setWait(12.262,16.224)
    $ speak(NICOLE, "I'm still awake from last night cause my Mom accidentally took one of my brother's adderalls.")
    $ setWait(16.224,17.35)
    $ speak(JECKA, "Instead of what?")
    show nicole sc1 angry:
        leftmidstage
    $ setWait(17.35,22.897)
    $ speak(NICOLE, "I don't know like oxy or morphine or something. They give old people heroin pills to mellow out over gas prices.")
    $ setWait(22.897,24.441)
    $ speak(JECKA, "Do those pills even look the same?")
    $ setWait(24.441,31.489)
    $ speak(NICOLE, "Anyway! So she won't shut the fuck up over how many days I missed. I'm like \"Mom if I can't go to sleep I'm gonna miss another day.\"")
    $ setWait(31.489,35.076)
    $ speak(JECKA, "Well wasn't she right? You're here early for the first time in forever.")
    $ setWait(35.076,38.621)
    $ speak(NICOLE, "Oh my god it's like I'm talking to a guy. Can't you just agree with me and say \"yeah she's a bitch\"?")
    $ setWait(38.621,43.585)
    $ speak(JECKA, "Okay sorry Nicole, your Mom is a bitch.. fucking.. whore.")
    show nicole sc1 smile:
        leftmidstage
    $ setWait(43.585,46.588)
    $ speak(NICOLE, "See now I feel better. This is why we have friends.")
    show nicole sc1:
        leftmidstage

    show jecka sc1 worried:
        centerstage
    $ setWait(46.588,47.63)
    $ speak(JECKA, "We're really white.")
    show jecka sc1:
        centerstage
        pause 0.5
        xzoom -1

    show crispin sc1 smile:
        off_right
        linear 2 rightmidstage
    $ setWait(47.63,52.135)
    $ speak(CRISPIN, "Oh guys what's up? Did I tell you I got a iPhone for my birthday?")
    $ setWait(52.135,54.512)
    $ speak(JECKA, "That's uh, that's cool...")
    $ setWait(54.512,56.681)
    $ speak(NICOLE, "We talk to you like once a month.")
    show crispin sc1:
        rightmidstage
    $ setWait(56.681,58.099)
    $ speak(CRISPIN, "Oh...")
    show crispin sc1 smile:
        rightmidstage
    $ setWait(58.099,62.187)
    $ speak(CRISPIN, "...well yeah it's crazy cause like I didn't know iPhones could do this much, bro.")
    $ setWait(62.187,65.523)
    $ speak(NICOLE, "Will it kill an Asian child? Or is that just when it's being made?")
    $ setWait(65.523,74.949)
    $ speak(CRISPIN, "That's uh, nah but like there's all these cool apps. Like I know there's Youtube and stuff but there's apps where you can like shoot guns and pop bubbles and stuff.")
    $ setWait(74.949,76.451)
    $ speak(JECKA, "You mean games?")
    $ setWait(76.451,81.164)
    $ speak(CRISPIN, "It's not even like games, it's just apps. Like there's an app for this, there's an app for that.")
    $ setWait(81.164,83.958)
    $ speak(NICOLE, "Is there an app that'll make you fuck off and kill yourself?")
    show crispin sc1:
        rightmidstage
    $ setWait(83.958,86.711)
    $ speak(CRISPIN, "Um, is that like a joke or are we?")
    show jecka sc1 angry:
        centerstage
        xzoom -1

    show crispin sc1:
        rightmidstage
        pause 1.3
        xzoom -1
        linear 3 off_farright
    $ setWait(86.711,90.423)
    $ speak(JECKA, "Just go!")
    show nicole sc1 sad:
        leftmidstage

    show jecka sc1:
        centerstage
        pause 0.32
        xzoom 1
    $ setWait(90.423,94.302)
    $ speak(NICOLE, "That alone was way too much in the morning there's no way I'm getting through these classes.")
    $ setWait(94.302,95.386)
    $ speak(JECKA, "Are you gonna skip again?")
    $ setWait(95.386,102.268)
    $ speak(NICOLE, "What choice did he just leave me? I can't see anyone like him for the rest of the day or I'm gonna go insane. C'mon let's go somewhere.")
    show jecka sc1 angry:
        centerstage
    $ setWait(102.268,103.978)
    $ speak(JECKA, "I have a quiz today, Nicole!")
    show nicole sc1 angry:
        leftmidstage
    $ setWait(103.978,107.482)
    $ speak(NICOLE, "Oh you're gonna miss your scantron memory game? Just retake it tomorrow.")
    show jecka sc1:
        centerstage
    $ setWait(107.482,110.318)
    $ speak(JECKA, "Ugh fine, so where are we even going?")
    stop ambient fadeout 3
    menu:
        "GO TO THE MALL":
            jump scene_0003
        "SKIP IN SCHOOL UNTIL LUNCH":
            jump scene_0004
        "HANG OUT AT HOME":
            jump scene_0005
label scene_0002B:
    hide screen disable_Controls
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show title_september2008 onlayer screens
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter

    show title_september2008

    $ quick_menu = True

    $ setVoiceTrack("audio/Scenes/0002B.mp3")
    play ambient "audio/Ambience/Bathroom_Lockerroom_Ambience.mp3"
    hide title_september2008 onlayer screens
    scene locker room
    show ari sc1:
        rightstage

    show nicole sc1 angry:
        off_left
        xzoom -1
        linear 1.3 leftstage
    $ setWait(2.42,3.921)
    $ speak(NICOLE, "Rgh...")
    show nicole sc1 angry:
        leftstage
        xzoom 1
        linear 0.7 leftmidstage
    $ setWait(3.921,5.715)
    $ speak(NICOLE, "Ew, this rope is filthy.")
    show ari sc1:
        rightstage
        linear 2.1 rightcenterstage
    $ setWait(5.715,7.592)
    $ speak(ARI, "What are you doing with the climbing rope?")
    show nicole sc1:
        leftmidstage
    $ setWait(7.592,11.971)
    $ speak(NICOLE, "Nothing just, moving it.\nUnrelated, do you know how to tie a noose?")
    show ari sc1 sad:
        rightcenterstage
    $ setWait(11.971,13.973)
    $ speak(ARI, "Why would I know how to do that?")
    $ setWait(13.973,15.641)
    $ speak(NICOLE, "You were in the girl scouts?")
    show ari sc1 angry:
        rightcenterstage
    $ setWait(15.641,19.395)
    $ speak(ARI, "Yeah we learned how to tie knots to go on boats and shit, not hang ourselves.")
    $ setWait(19.395,22.273)
    $ speak(NICOLE, "Well we're just assuming a whole lot today aren't we?")
    show ari sc1:
        rightcenterstage

    show jecka sc1:
        off_right
        linear 1.4 leftcenterstage
    $ setWait(22.273,24.817)
    $ speak(JECKA, "Hey guys, what's going on-- Why is the rope in here?")
    $ setWait(24.817,27.361)
    $ speak(ARI, "She was just asking me how to tie a noose.")
    show jecka sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(27.361,30.031)
    $ speak(JECKA, "And like, did you help her?")
    show ari sc1 sad:
        rightcenterstage
    $ setWait(30.031,30.74)
    $ speak(ARI, "Should I?")
    show jecka sc1 angry:
        leftcenterstage
        xzoom 1

    show ari sc1:
        rightcenterstage

    $ setWait(30.74,33.326)
    $ speak(JECKA, "Nicole are you really trying to kill yourself again?")
    $ setWait(33.326,36.787)
    $ speak(NICOLE, "Yeah, No? Uh\npick your favorite answer out of those.")
    show jecka sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(36.787,38.456)
    $ speak(JECKA, "Why would you help her tie a noose?")
    show ari sc1 sad:
        rightcenterstage
        pause .95
        xzoom -1
        linear 0.6 off_right
    $ setWait(38.456,41.209)
    $ speak(ARI, "I didn't! Oh my god I can't right now!")
    $ setWait(41.209,42.126)
    $ speak(NICOLE, "What's her problem?")
    show jecka sc1 angry:
        leftcenterstage
        xzoom 1
    $ setWait(42.126,47.048)
    $ speak(JECKA, "What's your problem? We're not even two weeks back yet and you're trying to hang yourself with the gym rope.")
    show nicole sc1 angry:
        leftmidstage
    $ setWait(47.048,50.176)
    $ speak(NICOLE, "Dude you have no idea what I had to witness this morning.")
    $ setWait(50.176,56.891)
    $ speak(NICOLE, "The Jeffery kid was doing cartoon voices for Mr. Burleday and the guy just nodded telling him he had a future in Hollywood.")
    show jecka sc1 worried:
        leftcenterstage
    $ setWait(56.891,58.1)
    $ speak(JECKA, "Like he wasn't joking?")
    $ setWait(58.1,61.604)
    $ speak(NICOLE, "Yeah so now he's just encouraged to go up to us talking like Elmo all day.")
    show jecka sc1:
        leftcenterstage
    $ setWait(61.604,67.109)
    $ speak(JECKA, "Alright yeah I get it but could you hold off on killing yourself for two more weeks, we're still partners on the lab, remember?")
    $ setWait(67.109,69.737)
    $ speak(NICOLE, "Oh that's your motive for keeping me alive, yeah sure no problem.")
    $ setWait(69.737,72.365)
    $ speak(JECKA, "So will I see you in science today?")
    show nicole sc1:
        leftmidstage
    $ setWait(72.365,79.58)
    $ speak(NICOLE, "About that, why don't we just go out and do something else?\nRegardless of whatever you say I'm not showing up to any class with Jeffery for the rest of the week.")
    show jecka sc1 angry:
        leftcenterstage
    $ setWait(79.58,83.542)
    $ speak(JECKA, "I exerted all that energy to keep you alive and you're still not gonna go?")
    $ setWait(83.542,85.127)
    $ speak(NICOLE, "You can come with me if you want.")
    $ setWait(85.127,88.256)
    $ speak(JECKA, "Uh, I'm trying to get into a college after I graduate.")
    show nicole sc1 smile:
        leftmidstage
    $ setWait(88.256,91.342)
    $ speak(NICOLE, "Fine go to science and let Jeffery do Elmo voice at you.")
    show jecka sc1 worried:
        leftcenterstage
    $ setWait(91.342,94.303)
    $ speak(JECKA, "Oh god... Where are you even going?")
    stop ambient fadeout 3
    menu:
        "GO TO THE MALL":
            jump scene_0003
        "SKIP IN SCHOOL UNTIL LUNCH":
            jump scene_0004
        "HANG OUT AT HOME":
            jump scene_0005
label scene_0003:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0003.mp3")
    scene mall int
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1
    show jecka sc1 angry:
        xzoom -1
        off_left
        linear 3 rightcenterstage
        xzoom 1

    show nicole sc1:
        off_farleft
        linear 3.2 leftcenterstage
    $ setWait(1.96,4.838)
    $ speak(JECKA, "Why did we come here if we don't even know what we wanna buy?")
    $ setWait(4.838,7.34)
    $ speak(NICOLE, "Dude we're literally in the mall, just figure it out.")
    $ setWait(7.34,10.594)
    $ speak(JECKA, "Even if I do want something it's just torture, I have like no money.")
    $ setWait(10.594,12.846)
    $ speak(NICOLE, "Who said we're buying anything? Just steal the shit.")
    show jecka sc1:
        rightcenterstage
    $ setWait(12.846,15.807)
    $ speak(JECKA, "fr.. sigma..")
    $ setWait(15.807,16.641)
    $ speak(NICOLE, "What?")
    show jecka sc1 smile:
        rightcenterstage
    $ setWait(16.641,20.27)
    $ speak(JECKA, "disc..")
    $ setWait(20.27,21.479)
    $ speak(NICOLE, "Oh.")
    show jecka sc1:
        rightcenterstage
    $ setWait(21.479,22.564)
    $ speak(JECKA, "Is there a problem?")
    $ setWait(22.564,27.36)
    $ speak(NICOLE, "No I'm just surprised you like MSI cause you're so... normal.")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(27.36,30.905)
    $ speak(JECKA, "Bitch I could cut myself just as much as you do, I just have better shit to do, okay?")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(30.905,33.199)
    $ speak(NICOLE, "That's not how it-- Okay so what are we getting?")
    show jecka sc1 smile:
        rightcenterstage

    show nicole sc1:
        leftcenterstage
    $ setWait(33.199,35.869)
    $ speak(JECKA, "I want a CD... and a shirt if they have one!")
    $ setWait(35.869,36.87)
    $ speak(NICOLE, "It's one or the other.")
    show jecka sc1:
        rightcenterstage
    $ setWait(36.87,37.996)
    $ speak(JECKA, "Why can't we steal both?")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(37.996,45.795)
    $ speak(NICOLE, "You don't steal twice in the same trip!\nThe only people here is us and some dad buying Skechers, who do you think the security guy's gonna have more fun gawking at?")
    $ setWait(45.795,50.216)
    $ speak(JECKA, "He wouldn't look at us, we're like children skipping school. \"Oh those children are so hot.\"")
    show nicole sc1:
        leftcenterstage
    $ setWait(50.216,54.012)
    $ speak(NICOLE, "How many men do you need to see outed as sex offenders before you start seeing there's a trend?")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(54.012,56.723)
    $ speak(JECKA, "You know what? Pick for me, Nicole. Lead the way.")
    stop ambient fadeout 3
    menu:
        "STEAL A $10 SHIRT":
            jump scene_0006
        "STEAL A CD IN 2008":
            jump scene_0016
label scene_0004:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0004.mp3")
    play ambient "Audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    scene cafeteria int 2
    show nicole sc1:
        rightcenterstage

    show jecka sc1 angry:
        rightmidstage
    $ setWait(0.17,3.256)
    $ speak(JECKA, "This is probably your worst idea yet.")
    $ setWait(3.256,5.383)
    $ speak(NICOLE, "What's easier than sitting in the cafeteria?")
    $ setWait(5.383,11.64)
    $ speak(JECKA, "Skipping in school is worse than just actually going to class.\nThere's no TV or alcohol or anything here.")
    $ setWait(11.64,14.309)
    $ speak(NICOLE, "Yeah but is there an ice cream vending machine at home?")
    $ setWait(14.309,16.102)
    $ speak(JECKA, "That shit doesn't even fucking work!")
    show nicole sc1:
        rightcenterstage
        xzoom -1
    $ setWait(16.102,17.896)
    $ speak(NICOLE, "No I think it's working this week.")
    show nicole sc1:
        rightcenterstage
        pause 0.5
        xzoom 1
    $ setWait(17.896,23.568)
    $ speak(JECKA, "Okay even if it is, we cut school and eat ice cream all day.\nWhat are we six? I need drugs, Nicole!")
    $ setWait(23.568,26.321)
    $ speak(NICOLE, "What so now if you're six you can't do drugs anymore?")
    $ setWait(26.321,31.534)
    $ speak(JECKA, "I could be in Math right now staring at the pregnant girl two rows down from me, that would be more entertaining than this.")
    show nicole sc1 surprised:
        rightcenterstage
    $ setWait(31.534,33.703)
    $ speak(NICOLE, "Our school has a pregnant girl? Do I know her?")
    show jecka sc1:
        rightmidstage
    $ setWait(33.703,38.333)
    $ speak(JECKA, "Well if you haven't seen a kid walking around looking seven months pregnant then I'm guessing no.")
    show nicole sc1:
        rightcenterstage
    $ setWait(38.333,40.794)
    $ speak(NICOLE, "Does she have a camera crew for one of those reality shows?")
    $ setWait(40.794,44.839)
    $ speak(JECKA, "No. I don't even think she speaks English she's like a Salvadorian transfer kid.")
    $ setWait(44.839,47.175)
    $ speak(NICOLE, "It's gotta be so weird to be pregnant in school.")
    $ setWait(47.175,53.306)
    $ speak(JECKA, "Oh all the guys are so mean about it too.\nThey call her Juno to her face, like can't you just fuck off and stare at her like a normal person?")
    show nicole sc1 smile:
        rightcenterstage
    $ setWait(53.306,55.725)
    $ speak(NICOLE, "See? This is gossip, we're having fun.")
    $ setWait(55.725,56.685)
    $ speak(JECKA, "I guess.")
    show nicole sc1 angry:
        rightcenterstage
    $ setWait(56.685,60.23)
    $ speak(NICOLE, "No fat balding piece of shit in a polo shirt telling us \"I'll wait\"")
    show burleday 1:
        off_left
        xzoom -1
        linear 1.5 leftmidstage

    show nicole sc1 surprised:
        rightcenterstage
        pause 0.4
        xzoom -1

    show jecka sc1 surprised:
        rightmidstage
    $ setWait(60.23,62.816)
    $ speak(BURLEDAY, "Girls. We're on our way to class, right?")
    $ setWait(62.816,63.4)
    $ speak(JECKA, "Fuck!")
    show nicole sc1:
        rightcenterstage
        xzoom -1

    show jecka sc1:
        rightmidstage
    $ setWait(63.4,69.447)
    $ speak(NICOLE, "Uh... Uh yeah we were just getting water for the plants in AP ecosystems.")
    $ setWait(69.447,72.826)
    $ speak(BURLEDAY, "You're seniors, that class is on the other side of the school.")
    $ setWait(72.826,77.956)
    $ speak(JECKA, "Oh well no the plants are... from California so they only use bottled water.")
    $ setWait(77.956,81.793)
    $ speak(NICOLE, "Yeah and the cafeteria's the closest place with bottled water.")
    $ setWait(81.793,88.174)
    $ speak(BURLEDAY, "I'm going to circle back around in a few minutes and I hope you'll be off to class by the time I get back.")
    show jecka sc1 smile:
        rightmidstage
    show burleday 1:
        leftmidstage
        xzoom -1
        pause 1.3
        xzoom 1
        linear 1.3 leftstage
    $ setWait(88.174,90.093)
    $ speak(JECKA, "Yeah of course, no problem.")
    $ setWait(90.093,90.719)
    $ speak(NICOLE, "Pedophile.")
    show nicole sc1 surprised:
        rightcenterstage
        xzoom -1
    show burleday 1 angry:
        leftstage
        xzoom -1
        linear 0.4 leftcenterstage
    $ setWait(90.719,91.261)
    $ speak(BURLEDAY, "What was that??")
    show jecka sc1 angry:
        rightmidstage
    $ setWait(91.261,92.178)
    $ speak(JECKA, "Why the fuck?")
    show jecka sc1:
        rightmidstage

    show nicole sc1:
        rightcenterstage
        xzoom -1
    $ setWait(92.178,99.936)
    $ speak(NICOLE, "Oh no pedophile, it's a new slang term.\nI know it sounds like the other thing but when we say it it means \"cool teacher\".")
    show burleday 1:
        leftcenterstage
        xzoom -1
    $ setWait(99.936,105.066)
    $ speak(BURLEDAY, "Huh... If that's the case, being strict is a part of the job but...")
    show burleday 1 smile:
        leftcenterstage
        xzoom -1
    $ setWait(105.066,108.987)
    $ speak(BURLEDAY, "...it is good to be a pedophile every now and then.")
    show jecka sc1 surprised:
        rightmidstage

    show nicole sc1 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(108.987,109.946)
    $ speak(JECKA, "Oh my god yeah.")
    $ setWait(109.946,111.03)
    $ speak(NICOLE, "Dude totally.")
    show burleday 1 smile:
        leftcenterstage
        xzoom 1
        linear 3 off_left
    $ setWait(111.03,113.366)
    $ speak(BURLEDAY, "I love being a pedophile.")
    stop ambient fadeout 1
    jump scene_0026
label scene_0005:
    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext day with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter

    $ setVoiceTrack("audio/Scenes/0005.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3"
    scene home nicole int
    show nicole sc1:
        leftcenterstage

    show jecka sc1:
        rightcenterstage
    $ setWait(1.752,4.922)
    $ speak(NICOLE, "...You wanna watch Mythbusters?")
    $ setWait(4.922,6.757)
    $ speak(JECKA, "This is like a really bad date.")
    $ setWait(6.757,7.925)
    $ speak(NICOLE, "At least we're not in school.")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(7.925,13.973)
    $ speak(JECKA, "That's a horrible comeback for that. What are you gonna do when you're 25 and working at Outback Steakhouse? \"Well at least we're not in school\"")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(13.973,16.684)
    $ speak(NICOLE, "I would never fucking work at Steak Back Outhouse.")
    $ setWait(16.684,23.608)
    $ speak(JECKA, "That doesn't change the fact we're stuck here, without gas money, and your Mom only pays for the basic cable package.")
    show nicole sc1:
        leftcenterstage
    $ setWait(23.608,25.276)
    $ speak(NICOLE, "...So you don't wanna watch Mythbusters?")
    $ setWait(25.276,30.448)
    $ speak(JECKA, "We literally just left school to avoid men who go \"this is true\"-- Why the fuck would I watch a show about them?")
    $ setWait(30.448,34.493)
    $ speak(NICOLE, "I heard every other episode they accidentally show you a new way to make crystal meth.")
    show jecka sc1:
        rightcenterstage
    $ setWait(34.493,37.079)
    $ speak(JECKA, "Did they ever do one on cigarettes causing cancer?")
    $ setWait(37.079,39.54)
    $ speak(NICOLE, "If cigarettes were in Star Wars then maybe?")
    $ setWait(39.54,40.75)
    $ speak(JECKA, "Can I smoke in here?")
    $ setWait(40.75,44.337)
    $ speak(NICOLE, "You can, I don't know if you should my Mom might get mad.")
    $ setWait(44.337,48.925)
    $ speak(JECKA, "Okay well you hate you Mom, and your brother, and anyone else you mention to me- so just let me smoke in here.")
    $ setWait(48.925,53.095)
    $ speak(NICOLE, "Holy shit calm down. You've only been smoking for like a year how are you addicted?")
    $ setWait(53.095,54.472)
    $ speak(JECKA, "Have an alternative?")
    $ setWait(54.472,59.018)
    $ speak(NICOLE, "My Mom has a bunch of old prescriptions in her medicine cabinet. You wanna crush 'em up and see what they do to us?")
    $ setWait(59.018,63.731)
    $ speak(JECKA, "Wow snorting your Mom's pills. We'd be like the guy in Scarface if he ran a nursing home.")
    $ setWait(63.731,66.525)
    $ speak(NICOLE, "This might be a stupid question but what even is Scarface?")
    $ setWait(66.525,71.364)
    $ speak(JECKA, "It's like a drug dealer movie? I don't know the ESL kids won't stop wearing shirts of it.")
    $ setWait(71.364,73.532)
    $ speak(NICOLE, "I think they did a Mythbusters on Scarface.")
    $ setWait(73.532,77.328)
    $ speak(JECKA, "That sounds so awesome for a guy who wears cargo shorts.")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(77.328,80.122)
    $ speak(JECKA, "What are we doing, Nicole? And don't say sobriety.")
    menu:
        "DO A LINE OF MOM'S PILLS":
            jump scene_0041
        "SMOKE CIGARETTES INDOORS":
            jump scene_0046
label scene_0006:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0006.mp3")
    play ambient "audio/Ambience/HotTopic_Ambience.mp3" fadein 1
    scene hot topic
    show nicole sc1:
        off_right
        xzoom -1
        linear 2.5 rightcenterstage

    show jecka sc1:
        off_farright
        linear 2.7 rightmidstage
    $ setWait(0.125,2.294)
    $ speak(NICOLE, "This place always smells like plastic.")
    show trody ht:
        off_left
        xzoom -1
        linear 2.2 leftmidstage
    $ setWait(2.294,3.712)
    $ speak(TRODY, "Hey how you guys doing today?")
    show jecka sc1 surprised:
        rightmidstage

    show nicole sc1 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(3.712,4.546)
    $ speak(JECKA, "Trody?")
    $ setWait(4.546,6.507)
    $ speak(NICOLE, "Holy shit are you skipping too?")
    show nicole sc1:
        rightcenterstage
        xzoom -1
    $ setWait(6.507,10.97)
    $ speak(TRODY, "I dropped out and my Mom forced me to get a job. So fuckin' not straight, I know.")
    show jecka sc1:
        rightmidstage


    $ setWait(10.97,13.806)
    $ speak(JECKA, "Okay well-- wait how the fuck do you drop out?")
    $ setWait(13.806,16.809)
    $ speak(TRODY, "Uh it's a lot of paperwork, you thinking about it too?")
    $ setWait(16.809,17.768)
    $ speak(JECKA, "That's okay.")
    show nicole sc1 smile:
        rightcenterstage
        xzoom -1
    $ setWait(17.768,20.646)
    $ speak(NICOLE, "Yeah you're the guy in the PBS commercials they make fun of.")
    show jecka sc1 smile:
        rightmidstage
    $ setWait(20.646,22.606)
    $ speak(JECKA, "Oh the tiny wallet commercial?")
    show nicole sc1 smile:
        rightcenterstage
        xzoom 1
    $ setWait(22.606,26.11)
    $ speak(NICOLE, "Yeah it's like 80%% of dropouts like...")
    show nicole sc1 smile:
        rightcenterstage
        xzoom -1
    $ setWait(26.11,28.654)
    $ speak(NICOLE, "...I don't know, the TV said you suck so fuck you.")
    show trody ht smile:
        leftmidstage
    $ setWait(28.654,34.159)
    $ speak(TRODY, "Yeah right, do you guys get paid 8 an hour to go to that bitch idiot school?")
    $ setWait(34.159,36.161)
    $ speak(NICOLE, "Wow he thought that would impress us!")
    $ setWait(36.161,38.539)
    $ speak(JECKA, "Yeah you're dumb, white, and broke!")
    show trody ht angry:
        leftmidstage
        xzoom -1
    $ setWait(38.539,41.25)
    $ speak(TRODY, "Shut the fuck up, you albacore eatin' bitch!")
    show nicole sc1 angry:
        rightcenterstage
        xzoom -1
    $ setWait(41.25,44.753)
    $ speak(NICOLE, "Hey whoa! Where's your manager? You can't talk to customers like that.")
    $ setWait(44.753,46.505)
    $ speak(JECKA, "Apologize, wage slave.")
    $ setWait(46.505,48.424)
    $ speak(TRODY, "God dammit, fine sorry.")
    show jecka sc1:
        rightmidstage
    $ setWait(48.424,52.177)
    $ speak(JECKA, "Good. Now what sizes do you have MSI shirts in right now?")
    show trody ht:
        leftmidstage
        xzoom -1
    $ setWait(52.177,55.347)
    $ speak(TRODY, "The band? Uh I think everything but large?")
    show nicole sc1:
        rightcenterstage
        xzoom -1
    $ setWait(55.347,59.268)
    $ speak(NICOLE, "Damn, that's the one size she wears too. Can you check in the back for us?")
    $ setWait(59.268,60.894)
    $ speak(TRODY, "What you see out is what we have, dude.")
    $ setWait(60.894,65.399)
    $ speak(NICOLE, "If you don't check right now I'm gonna tell your manager you didn't say \"hi\" to us when we walked in.")
    show trody ht angry:
        leftmidstage
        xzoom -1
        pause 1.5
        xzoom 1
        linear 2.7 off_left
    $ setWait(65.399,70.404)
    $ speak(TRODY, "Fuck fine! Joke's on you bitches I'm just gonna go back and pretend to look.")
    show nicole sc1:
        rightcenterstage
        xzoom 1
    $ setWait(70.404,71.78)
    $ speak(NICOLE, "...Okay grab the small let's go.")
    show jecka sc1 smile:
        rightmidstage
    $ setWait(71.78,73.866)
    $ speak(JECKA, "Yeah I was like how the fuck do you think I'm a large.")
    show nicole sc1 angry:
        rightcenterstage
        pause 0.15
        linear 0.7 off_right

    show jecka sc1:
        rightmidstage
        pause 0.73
        xzoom -1
        linear 0.5 off_right
    $ setWait(73.866,75.909)
    $ speak(NICOLE, "C'mon!")
    stop ambient fadeout 1
    jump scene_0007
label scene_0007:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0007.mp3")
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1
    scene mall int 2
    show nicole sc1:
        off_right
        xzoom -1
        linear 1.3 centerstage

    show jecka sc1 smile:
        off_farright
        linear 1.5 rightmidstage
    $ setWait(0.122,1.54)
    $ speak(JECKA, "How'd you learn how to do that?")
    show nicole sc1:
        centerstage
        xzoom 1
    $ setWait(1.54,4.042)
    $ speak(NICOLE, "What do you mean learn? You can't just take the shit in front of him.")
    $ setWait(4.042,5.544)
    $ speak(JECKA, "Okay so what's next?")
    $ setWait(5.544,7.629)
    $ speak(NICOLE, "Uh we leave before we get caught?")
    $ setWait(7.629,11.925)
    $ speak(JECKA, "We can't leave now, that was such a rush. C'mon let's go to the food court and steal some Dairy Queen!")
    show nicole sc1 angry:
        centerstage
    $ setWait(11.925,13.176)
    $ speak(NICOLE, "Do you hear yourself?")
    show jecka sc1 worried:
        rightmidstage
    $ setWait(13.176,17.306)
    $ speak(JECKA, "Ugh, yeah I guess it'd be pretty hard to jump the counter and fill a cone without spilling it.")
    $ setWait(17.306,20.475)
    $ speak(NICOLE, "No that shit's easy, why would you risk getting caught over Dairy Queen?")
    show jecka sc1:
        rightmidstage
    $ setWait(20.475,24.104)
    $ speak(JECKA, "Should we try Sarku Japan? Or would the free samples lady chase after us?")
    stop ambient fadeout 4
    show nicole sc1:
        centerstage
        pause 1.2
        xzoom -1
        linear 3 off_left
    $ setWait(24.104,26.023)
    $ speak(NICOLE, "Literally anywhere but here, c'mon!")
    jump scene_0008
label scene_0008:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show diner ext with Pause(2.252):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 0.65 truecenter
    $ setVoiceTrack("audio/Scenes/0008.mp3")
    play ambient "audio/Ambience/Diner_Ambience.mp3"
    scene diner int
    show nicole sc1:
        leftcenterstage

    show jecka sc1:
        rightcenterstage
    $ setWait(1.92,6.549)
    $ speak(JECKA, "Oh god I ate way too much, there's no way we can run out on the check now.")
    $ setWait(6.549,10.595)
    $ speak(NICOLE, "How do fat people eat here? It's like pure sodium-- Fuck I answered my own question.")
    $ setWait(10.595,11.721)
    $ speak(JECKA, "You wanted the patty melt.")
    $ setWait(11.721,15.225)
    $ speak(NICOLE, "Since we're not paying for this either I figured I'd demo some other part of the menu.")
    $ setWait(15.225,20.647)
    $ speak(JECKA, "It's literally just a burger where your Mom forgot to buy buns, who would voluntarily pay for that?")
    $ setWait(20.647,22.982)
    $ speak(NICOLE, "Someone who butters margarine with butter.")
    $ setWait(22.982,25.068)
    $ speak(JECKA, "You think we got Trody fired today?")
    $ setWait(25.068,27.862)
    $ speak(NICOLE, "I don't know... I don't care either, weird.")
    $ setWait(27.862,34.035)
    $ speak(JECKA, "Most of our friends just get jobs to buy adderall, but he has to like, support himself with that.")
    $ setWait(34.035,38.248)
    $ speak(NICOLE, "Yeah. Almost like he has to deal with the consequences of his actions or something.")
    $ setWait(38.248,41.125)
    $ speak(JECKA, "Since when do you of all people worry about accountability?")
    $ setWait(41.125,44.254)
    $ speak(NICOLE, "I don't worry about it for my actions. I'm too smart for consequences.")
    $ setWait(44.254,49.008)
    $ speak(JECKA, "It's the one time I feel kinda bad for a guy cause he can't do any of the stupid money jobs like pole dancing.")
    $ setWait(49.008,55.223)
    $ speak(NICOLE, "Yeah if I was dumb as shit being a stripper would be awesome. Though I'd feel ripped off cause I learned how to read for nothing.")
    $ setWait(55.223,57.433)
    $ speak(JECKA, "What if you're too shy and just work at Hooters?")
    $ setWait(57.433,60.853)
    $ speak(NICOLE, "Dude Hooters is even worse than a club, it's a legalized brothel.")
    show jecka sc1 worried:
        rightcenterstage
    $ setWait(60.853,62.73)
    $ speak(JECKA, "What!? How? How do you know this?")
    $ setWait(62.73,68.987)
    $ speak(NICOLE, "My cousin works at one. She says half the girls blow dudes for like 300 dollar tips and then wonder why they're getting stalked the next week.")
    $ setWait(68.987,70.488)
    $ speak(JECKA, "That's really specific.")
    $ setWait(70.488,72.907)
    $ speak(NICOLE, "That really happens. So what's next?")
    $ setWait(72.907,74.993)
    $ speak(JECKA, "I think I wanna go back to school now.")
    $ setWait(74.993,77.078)
    $ speak(NICOLE, "Dude you know you're gonna end up sitting there bored.")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(77.078,80.123)
    $ speak(JECKA, "I'd rather do that then end up the dick sucking girl at Hooters.")
    $ setWait(80.123,82.75)
    $ speak(NICOLE, "You can just say \"girl at Hooters\", the dick sucking's implied.")
    show jecka sc1:
        rightcenterstage
    $ setWait(82.75,83.71)
    $ speak(JECKA, "Check please!")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(83.71,85.662)
    $ speak(NICOLE, "We're not even paying for it, just get up and leave.")
    stop ambient fadeout 1.5
    jump scene_0009
label scene_0009:
    show black onlayer screens with Pause(1.2):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0009.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 2
    show lynn 2:
        rightmidstage

    show nicole sc1:
        off_left
        linear 2 leftcenterstage

    show jecka sc1:
        off_left
        xzoom -1
        linear 2.3 leftmidstage
    $ setWait(0.045,4.215)
    $ speak(LYNN, "Strolling in at noon together, you girls had a busy morning.")
    $ setWait(4.215,5.925)
    $ speak(NICOLE, "Yeah you don't know the half of it.")
    $ setWait(5.925,7.719)
    $ speak(JECKA, "Not even a quarter if we're being honest.")
    $ setWait(7.719,13.808)
    $ speak(LYNN, "Well the sign in sheet is on the desk, the unexcused column. I think you know it all too well, Nicole.")
    $ setWait(13.808,14.934)
    $ speak(NICOLE, "Unexcused?")
    $ setWait(14.934,18.021)
    $ speak(JECKA, "Yeah we kinda missed class for very traumatic reasons.")
    $ setWait(18.021,21.149)
    $ speak(NICOLE, "Yeah trauma has to be one of the excused tardies, right?")
    $ setWait(21.149,25.403)
    $ speak(LYNN, "For some reason I don't believe you. But today I think that's your problem.")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(25.403,27.072)
    $ speak(NICOLE, "Is being a fucking bitch your problem?")
    show jecka sc1 surprised:
        leftmidstage
        xzoom -1
    $ setWait(27.072,27.614)
    $ speak(JECKA, "Nicole!")
    $ setWait(27.614,28.448)
    $ speak(LYNN, "Excuse me?")
    show nicole sc1 sad:
        leftcenterstage

    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(28.448,31.242)
    $ speak(NICOLE, "Oh my god it was the trauma, I'm so sorry!")
    $ setWait(31.242,36.873)
    $ speak(LYNN, "So why don't you both enlighten me to the source of this trauma that's caused absence after absence?")
    menu:
        "DEPRESSION PITY PARTY":
            jump scene_0010
        "LIE ABOUT HAVING AIDS":
            jump scene_0013
label scene_0010:
    $ setVoiceTrack("audio/Scenes/0010.mp3")
    scene office 2
    show lynn 2:
        rightmidstage

    show nicole sc1 sad:
        leftcenterstage

    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(0.043,8.593)
    $ speak(NICOLE, "Honestly, I don't know it's just... We were both diagnosed with manic depression and it's just hard to show up anywhere.")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1
    $ setWait(8.593,14.766)
    $ speak(JECKA, "Uh, what she said, just nothing makes me happy anymore.\nNot even cocaine. I haven't tried it I'm just assuming.")
    $ setWait(14.766,19.187)
    $ speak(LYNN, "Manic Depression? Hmmm, I'm not sure we've had that as an excuse before.")
    $ setWait(19.187,23.191)
    $ speak(NICOLE, "But it's totally real, c'mon isn't it Mental Health Awareness Month?")
    $ setWait(23.191,24.233)
    $ speak(LYNN, "That's in May.")
    $ setWait(24.233,25.234)
    $ speak(JECKA, "Yeah it's May.")
    $ setWait(25.234,26.527)
    $ speak(LYNN, "It's September.")
    $ setWait(26.527,32.492)
    $ speak(NICOLE, "See? We're so messed up we don't even know what month it is.\nAnd besides, Whitney Houston said we need a whole year.")
    $ setWait(32.492,34.619)
    $ speak(LYNN, "That was for Black History Month.")
    $ setWait(34.619,38.289)
    $ speak(JECKA, "N-no it was for mental health awareness, right?")
    show nicole sc1 sad:
        leftcenterstage
        xzoom -1
        pause 1.4
        xzoom 1
    $ setWait(38.289,44.962)
    $ speak(NICOLE, "Yeah maybe? I just don't know anything anymore. I'm not sad I just don't feel feelings or care about anything.")
    $ setWait(44.962,46.714)
    $ speak(JECKA, "I'm headed into a downward spiral.")
    $ setWait(46.714,47.59)
    $ speak(NICOLE, "Oh my god same.")
    $ setWait(47.59,50.009)
    $ speak(JECKA, "I just wanna date a guy in his 30's and kill myself.")
    show nicole sc1 sad:
        leftcenterstage
        xzoom -1
        pause 0.6
        xzoom 1
    $ setWait(50.009,55.807)
    $ speak(NICOLE, "Oh that's good-- Yeah and I'm totally numb to hearing that because of my manic depression.")
    $ setWait(55.807,62.897)
    $ speak(LYNN, "Alright fine! I'll excuse it this time, but I expect you girls to seek help if this really is so much of an issue for you.")
    $ setWait(62.897,67.193)
    $ speak(JECKA, "Oh thank you, Miss Lynn. You made my day just a little bit better.")
    show nicole sc1 sad:
        leftcenterstage
        pause 2.5
        xzoom -1
    $ setWait(67.193,71.405)
    $ speak(NICOLE, "I have no emotions either way, cause depression, remember?")
    show nicole sc1 sad:
        leftcenterstage
        xzoom -1
        pause 0.7
        xzoom 1
    $ setWait(71.405,73.95)
    $ speak(JECKA, "Oh yeah that's right. You didn't do shit, Miss Lynn.")
    $ setWait(73.95,80.039)
    $ speak(LYNN, "Alright I think instead of class you should head over to your counselor for additional resources on your situation--")
    show trody ht:
        off_left
        xzoom -1
        linear 2 rightcenterstage

    show nicole sc1:
        leftcenterstage

    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(80.039,82.416)
    $ speak(TRODY, "Hey uh Principal Lynn, you got a minute?")
    $ setWait(82.416,85.503)
    $ speak(LYNN, "Hold on, girls-- Trody? I thought you dropped out.")
    $ setWait(85.503,88.422)
    $ speak(TRODY, "Well yeah I did but, I think I wanna re-enroll.")
    $ setWait(88.422,91.968)
    $ speak(LYNN, "Well that's great to hear, Trody. Why the sudden change of plans?")
    $ setWait(91.968,94.72)
    $ speak(TRODY, "I think it'd just make going to college a little easier.")
    $ setWait(94.72,98.724)
    $ speak(TRODY, "Also I got fired from Hot Topic, they said I let someone steal a shirt. So dumb.")
    show jecka sc1 surprised:
        leftmidstage
        xzoom -1
    $ setWait(98.724,99.35)
    $ speak(JECKA, "Oh shit.")
    show trody ht:
        rightcenterstage
        xzoom 1
    $ setWait(99.35,101.519)
    $ speak(TRODY, "Hey what are you guys doing here, I thought you were skipping today.")
    show nicole sc1 surprised:
        leftcenterstage
    $ setWait(101.519,102.103)
    $ speak(NICOLE, "What??")
    $ setWait(102.103,103.479)
    $ speak(LYNN, "Why do say that?")

    show trody ht:
        rightcenterstage
        xzoom -1

    $ setWait(103.479,105.231)
    $ speak(TRODY, "They were in the mall like 2 hours ago.")
    $ setWait(105.231,110.069)
    $ speak(LYNN, "Oh... They said they were suffering from manic depression. Could you step outside for a bit?")
    show nicole sc1:
        leftcenterstage

    show jecka sc1 smile:
        leftmidstage
        xzoom -1
    $ setWait(110.069,111.279)
    $ speak(JECKA, "Yeah no problem.")
    show jecka sc1:
        leftmidstage
        xzoom -1

    show trody ht:
        xzoom -1
        rightcenterstage
        pause 0.6
        xzoom 1
        linear 2 off_left
    $ setWait(111.279,114.282)
    $ speak(LYNN, "I meant Trody.")
    $ setWait(114.282,115.616)
    $ speak(NICOLE, "Dropouts, am I right?")
    $ setWait(115.616,117.368)
    $ speak(JECKA, "Yeah who can trust what they say--")
    show lynn 2:
        rightmidstage
        linear 2.5 rightcenterstage
    $ setWait(117.368,121.622)
    $ speak(LYNN, "Manic depression, huh? Suicidal thoughts and all.")
    show nicole sc1 sad:
        leftcenterstage
    $ setWait(121.622,124.667)
    $ speak(NICOLE, "...I mean I really wanna die right now so we're not all the way lying.")
    $ setWait(124.667,130.84)
    $ speak(LYNN, "Was it all worth it? Worth it for a T-shirt at the mall? You must be so depressed!")
    $ setWait(130.84,135.761)
    show jecka sc1 angry:
        leftmidstage
        xzoom -1
    $ speak(JECKA, "We stole an MSI shirt from Hot Topic, what about that doesn't scream depression?")
    stop ambient fadeout 2
    jump scene_0011
label scene_0011:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0011.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3

    show kylar sc1:
        centerstage
        xzoom -1

    show nicole sc2:
        leftmidstage

    show jecka sc2:
        rightmidstage
    $ setWait(0.08,2.249)
    $ speak(KYLAR, "Dude can we just go to an easier book?")
    show jecka sc2 angry:
        rightmidstage
    $ setWait(2.249,3.917)
    $ speak(JECKA, "This is the easier book.")
    $ setWait(3.917,6.336)
    $ speak(NICOLE, "Is everyone in the Reading Buddies program this stupid?")
    show kylar sc1:
        centerstage
        xzoom 1
    $ setWait(6.336,10.215)
    $ speak(KYLAR, "Hey the principal sent you here to help me, so make good or I'm snitching hard.")
    $ setWait(10.215,13.677)
    $ speak(NICOLE, "Okay fine, alright try this first page. Sound it out.")
    $ setWait(13.677,22.435)
    $ speak(KYLAR, "Uh, wuh-uh um. One... Fiss-huh... Twoah fiss-huh...")
    show jecka sc2:
        rightmidstage
    $ setWait(22.435,23.144)
    $ speak(JECKA, "Are you serious?")
    $ setWait(23.144,24.604)
    $ speak(KYLAR, "You picked a hard one on purpose!")
    show nicole sc2 angry:
        leftmidstage
    $ setWait(24.604,26.815)
    $ speak(NICOLE, "It's a Doctor Seuss book you fucking dipshit!")
    $ setWait(26.815,29.693)
    $ speak(KYLAR, "Oh yeah sure, if it's so easy why don't you try it, huh?")
    show nicole sc2:
        leftmidstage
    $ setWait(29.693,32.654)
    $ speak(NICOLE, "One fish, two fish, red fish, you bitch.")
    $ setWait(32.654,37.409)
    $ speak(KYLAR, "Huh-- wait that last part is... blue fish! See I knew you couldn't do it.")
    $ setWait(37.409,39.494)
    $ speak(JECKA, "This is a really potent punishment.")
    $ setWait(39.494,40.87)
    $ speak(NICOLE, "Fuck now I wanna drop out.")
    $ setWait(40.87,42.247)
    $ speak(JECKA, "Is Hooters hiring?")
    stop ambient fadeout 1.5
    jump scene_0012
label scene_0012:

    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show title_onedaylater onlayer screens
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter


    $ setVoiceTrack("audio/Scenes/0012.mp3")
    scene school ext 4
    hide title_onedaylater onlayer screens

    show emily sc2:
        rightcenterstage

    show jecka sc3:
        leftcenterstage
        xzoom -1

    show nicole sc3:
        off_left
        linear 2.2 leftmidstage
    $ setWait(0.126,1.628)
    $ speak(NICOLE, "Here we go again.")
    show jecka sc3:
        leftcenterstage
        xzoom 1
    $ setWait(1.628,2.504)
    $ speak(JECKA, "What?")
    $ setWait(2.504,3.421)
    $ speak(NICOLE, "School.")
    $ setWait(3.421,6.341)
    $ speak(EMILY, "It's senior year, you're not used to this by now?")
    $ setWait(6.341,7.175)
    $ speak(NICOLE, "Are you?")
    show emily sc2 upset:
        rightcenterstage
    $ setWait(7.175,10.387)
    $ speak(EMILY, "I'm not either but you sound like a sitcom. \"Here we go again\"")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(10.387,11.429)
    $ speak(NICOLE, "Who invited this bitch?")
    show emily sc2:
        rightcenterstage

    show jecka sc3 angry:
        leftcenterstage
        linear .3 leftmidstage

    show nicole sc3 surprised:
        pause .2
        linear .3 leftstage
    $ setWait(11.429,13.64)
    $ speak(JECKA, "Shut up, Nicole! This is the girl with the adderall.")
    $ setWait(13.64,16.017)
    $ speak(NICOLE, "Emily? Emily where the hell do you get so much adderall?")
    show emily sc2 smile:
        rightcenterstage
    $ setWait(16.017,19.396)
    $ speak(EMILY, "My boyfriend's 25, I can get whatever I want.")
    show jecka sc3 smile:
        leftmidstage
        xzoom -1
        linear 1 leftcenterstage
    $ setWait(19.396,20.897)
    $ speak(JECKA, "That's kinda awesome.")
    show nicole sc3:
        leftstage
        linear 1.2 leftmidstage
    $ setWait(20.897,25.277)
    $ speak(NICOLE, "So what a 7, 8 year age gap? That's pretty cool, that should work out.")
    show emily sc2:
        rightcenterstage
    $ setWait(25.277,29.239)
    $ speak(EMILY, "Yeah so have you guys heard they're gonna start giving out free syringes at South County?")
    show jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(29.239,30.615)
    $ speak(JECKA, "South County High School?")
    $ setWait(30.615,36.913)
    $ speak(EMILY, "Uh huh. Before they were trying to curb the opioid addiction but now they're just trying to keep all the kids from getting Hep-C or whatever.")
    $ setWait(36.913,39.457)
    $ speak(NICOLE, "Are they giving free heroin too or just the needles?")
    $ setWait(39.457,42.002)
    $ speak(EMILY, "Yeah just the needles, it sucks.")
    show jecka sc3 worried:
        leftcenterstage
        xzoom -1
    $ setWait(42.002,44.713)
    $ speak(JECKA, "Oh do you... do that?")
    $ setWait(44.713,49.509)
    $ speak(EMILY, "Kinda. My boyfriend got me into it but it's just lines, nothing serious.")
    $ setWait(49.509,54.139)
    $ speak(NICOLE, "Your 25 year old boyfriend dating you in high school got you into heroin? You guys are gonna be awesome together.")
    show jecka sc3:
        leftcenterstage
        xzoom -1
    $ setWait(54.139,56.6)
    $ speak(JECKA, "But if it's just lines what do you want the needles for?")
    $ setWait(56.6,61.646)
    $ speak(EMILY, "For him. Cause he did it so much that like, eventually doesn't hit as hard y'know.")
    show nicole sc3 smile:
        leftmidstage
    $ setWait(61.646,64.065)
    $ speak(NICOLE, "I think he'll be hittin' plenty hard, just give it time.")
    $ setWait(64.065,65.609)
    $ speak(EMILY, "Yeah that's true...")
    $ setWait(65.609,66.067)
    $ speak(EMILY, "...wait what?")
    show nicole sc3:
        leftmidstage
    $ setWait(66.067,69.195)
    $ speak(JECKA, "No no she's just talking to herself-- So can I buy addys at lunch today?")
    show emily sc2 smile:
        rightcenterstage
        pause 1.7
        xzoom -1
        linear 2.5 off_right
    $ setWait(69.195,73.241)
    $ speak(EMILY, "Yeah I'll see you there.\n\nAlright I gotta go.")
    show jecka sc3 smile:
        leftcenterstage
        xzoom 1
    $ setWait(73.241,74.909)
    $ speak(JECKA, "But yeah she has a lot of adderall.")
    $ setWait(74.909,76.953)
    $ speak(NICOLE, "That's the opening comment after she leaves.")
    show jecka sc3:
        leftcenterstage
        xzoom 1
    $ setWait(76.953,79.164)
    $ speak(JECKA, "Well yeah she's out there but...")
    $ setWait(79.164,87.547)
    $ speak(NICOLE, "Usually when I look in the mirror all I see is a self-destructive, pill popping ho.\nAfter 5 minutes with her I feel like Selena Gomez.")
    $ setWait(87.547,88.798)
    $ speak(JECKA, "Like you feel Mexican?")
    $ setWait(88.798,90.592)
    $ speak(NICOLE, "Never mind, c'mon let's hang out somewhere.")
    show jecka sc3 angry:
        leftcenterstage
        xzoom 1
    $ setWait(90.592,92.093)
    $ speak(JECKA, "I have school, Nicole!")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(92.093,93.511)
    $ speak(NICOLE, "Dude fuck that school shit.")
    $ setWait(93.511,96.64)
    $ speak(JECKA, "So from everything we had to do last week, you learned no lessons.")
    show nicole sc3:
        leftmidstage
    $ setWait(96.64,101.853)
    $ speak(NICOLE, "Lessons are for fat bitches who think pilates will make their husband wanna have sex again.")
    show jecka sc3:
        leftcenterstage
    $ setWait(101.853,106.274)
    $ speak(JECKA, "...You always find, like, the meanest way to say something.")
    $ setWait(106.274,107.567)
    $ speak(NICOLE, "So you're just leaving me?")
    $ setWait(107.567,111.488)
    $ speak(JECKA, "Don't be a baby I'll probably see you at lunch. Where you going anyway?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0013:
    $ setVoiceTrack("audio/Scenes/0013.mp3")
    scene office 2
    show lynn 2:
        rightmidstage

    show nicole sc1 sad:
        leftcenterstage

    show jecka sc1:
        leftmidstage
        xzoom -1

    $ setWait(0.077,3.288)
    $ speak(NICOLE, "...O-Okay you're gonna wanna take a seat.")
    $ setWait(3.288,5.332)
    $ speak(LYNN, "I've heard it all, Nicole.")
    show jecka sc1 worried:
        leftmidstage
    $ setWait(5.332,10.17)
    $ speak(JECKA, "N-no you really haven't heard... whatever she's about to tell you.")
    $ setWait(10.17,12.172)
    $ speak(LYNN, "Go on...")
    show jecka sc1:
        leftmidstage
        xzoom -1

    show nicole sc1:
        leftcenterstage
    $ setWait(12.172,16.802)
    $ speak(NICOLE, "We just came from the doctor and we, um...")
    show nicole sc1 sad:
        leftcenterstage
    $ setWait(16.802,19.096)
    $ speak(NICOLE, "We tested positive for HIV.")
    show jecka sc1 surprised:
        leftmidstage
        xzoom -1
    $ setWait(19.096,20.222)
    $ speak(JECKA, "We did?--We did.")
    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(20.222,26.019)
    $ speak(NICOLE, "And the nurse told us we might be AIDS positive cause we went so long without treatment.")
    $ setWait(26.019,28.48)
    $ speak(JECKA, "We won't get the results 'till later though.")
    $ setWait(28.48,31.733)
    $ speak(LYNN, "You both went to get tested together at the same place?")
    $ setWait(31.733,32.776)
    $ speak(JECKA, "Yeah?")
    $ setWait(32.776,34.736)
    $ speak(LYNN, "And where was that?")
    $ setWait(34.736,38.657)
    $ speak(NICOLE, "Like the... like the Springfield clinic.")
    $ setWait(38.657,40.951)
    $ speak(LYNN, "And you expect me to just believe this?")
    $ setWait(40.951,41.91)
    $ speak(NICOLE, "Shouldn't you?")
    $ setWait(41.91,46.248)
    $ speak(JECKA, "Think about it, Miss Lynn. If you believe us and we're lying it's just a little prank.")
    $ setWait(46.248,51.42)
    $ speak(JECKA, "But if we're telling the truth and you don't believe us you're gonna have to explain that to the local news.")
    $ setWait(51.42,58.051)
    $ speak(NICOLE, "And we'll have to explain that to the national news. How our principal made us cry while we're literally dying from AIDS.")
    $ setWait(58.051,66.309)
    $ speak(LYNN, "I'd need to see some documentation, girls. Do you realize the odds? How would you even get HIV in high school?")
    $ setWait(66.309,68.228)
    $ speak(JECKA, "We didn't get it in high school.")
    $ setWait(68.228,75.277)
    $ speak(NICOLE, "Yeah it's kind of embarrassing but we go to a lot of... swinger parties...\nwith homeless people.")
    $ setWait(75.277,76.445)
    $ speak(JECKA, "Homeless swinger parties.")
    $ setWait(76.445,77.237)
    $ speak(NICOLE, "Yeah.")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1
    $ setWait(77.237,84.327)
    $ speak(JECKA, "And it's TMI but I have a... unprotected sex fetish so it all kinda adds up.")
    $ setWait(84.327,87.664)
    $ speak(NICOLE, "Yeah and I have a sex in general fetish.")
    $ setWait(87.664,91.501)
    $ speak(JECKA, "Small world, one of my... 30 boyfriends has that too.")
    $ setWait(91.501,92.961)
    $ speak(LYNN, "30 boyfriends?")
    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(92.961,97.09)
    $ speak(JECKA, "Oh yeah, when a Dominican construction worker catcalls me-- just immediate relationship.")
    $ setWait(97.09,100.093)
    $ speak(NICOLE, "Yeah I love Jecka but she's a major whore.")
    $ setWait(100.093,100.802)
    $ speak(JECKA, "I don't get paid--")
    $ setWait(100.802,104.723)
    $ speak(LYNN, "So you both got your results for HIV? Did the blood work and everything?")
    $ setWait(104.723,106.308)
    $ speak(JECKA, "Yeah that's what we said.")
    $ setWait(106.308,108.351)
    $ speak(LYNN, "What's your T-cell count?")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1
    $ setWait(108.351,108.894)
    $ speak(JECKA, "Uh.")
    show nicole sc1 sad:
        leftcenterstage
    $ setWait(108.894,112.022)
    $ speak(NICOLE, "I-I don't get it, we don't take shop.")
    $ setWait(112.022,114.191)
    $ speak(LYNN, "You don't take shop?")
    $ setWait(114.191,117.402)
    $ speak(NICOLE, "Yeah they use T-Cells in shop class what's that have to do with AIDS?")
    show jecka sc1 angry:
        leftmidstage
        xzoom -1
    $ setWait(117.402,119.654)
    $ speak(JECKA, "That's a T-Square, Nicole-- Fuck!")
    show nicole sc1 angry:
        leftcenterstage
        pause 0.5
        xzoom -1
    $ setWait(119.654,121.406)
    $ speak(NICOLE, "What? No-- If you knew why'd you look at me?")
    $ setWait(121.406,123.283)
    $ speak(JECKA, "I didn't know how much we were supposed to say!")
    $ setWait(123.283,124.618)
    $ speak(NICOLE, "How the fuck would I know!?")
    $ setWait(124.618,126.078)
    $ speak(JECKA, "You said we had AIDS!")
    show lynn 2:
        rightmidstage
        pause 1.5
        linear 2 rightcenterstage

    show jecka sc1:
        leftmidstage

    show nicole sc1 sad:
        leftcenterstage
        xzoom -1
        pause 0.5
        xzoom 1
    $ setWait(126.078,134.503)
    $ speak(LYNN, "It all comes out...\nAnd coincidentally I have a lovely way for you girls to spend your Saturday afternoon, or you're expelled.")
    show nicole sc1 angry:
        leftcenterstage

    $ setWait(134.503,135.587)
    $ speak(NICOLE, "This sucks.")
    stop ambient fadeout 1
    jump scene_0014
label scene_0014:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter

    show title_dayslater
    $ setVoiceTrack("audio/Scenes/0014.mp3")
    play ambient "audio/Ambience/Gym_Ceremony_Ambience.mp3"
    scene gym 2
    show nicole sc2 angry:
        leftcenterstage

    show jecka sc2 angry:
        rightcenterstage

    $ setWait(0.001,1.795)
    $ speak(NICOLE, "This really sucks.")
    $ setWait(1.795,6.55)
    $ speak(GUEST, "We're almost set up here but thank you to everyone for coming to the AIDS Awareness Speaking.")
    $ setWait(6.55,12.013)
    $ speak(GUEST, "We have about 10 guests here with their journeys to share and we hope you can all learn a lot from them.")
    $ setWait(12.013,15.35)
    $ speak(JECKA, "I could be at the MSI show right now, but now I can't cause I listened to you.")
    show nicole sc2:
        leftcenterstage
    $ setWait(15.35,16.434)
    $ speak(NICOLE, "Oh don't say that.")
    $ setWait(16.434,19.312)
    $ speak(JECKA, "Don't say we have AIDS when you don't know what the fuck a T-cell is.")
    show nicole sc2 angry:
        leftcenterstage
    $ setWait(19.312,22.399)
    $ speak(NICOLE, "Like she was supposed to believe you had a rolodex of 50 guys?")
    $ setWait(22.399,23.108)
    $ speak(JECKA, "It was 30.")
    $ setWait(23.108,27.696)
    $ speak(NICOLE, "It was fucking stupid. And she didn't ask about T-cells until after you said that...")
    $ setWait(27.696,30.073)
    $ speak(NICOLE, "30 guys, what're you a public restroom?")
    show jecka sc2:
        rightcenterstage
    $ setWait(30.073,35.871)
    $ speak(JECKA, "Whatever... Why's AIDS such a big deal anyway? Isn't Magic Johnson like the healthiest man on earth?")
    show nicole sc2:
        leftcenterstage
    $ setWait(35.871,36.621)
    $ speak(NICOLE, "Huh?")
    $ setWait(36.621,39.916)
    $ speak(JECKA, "Magic Johnson, he got AIDS like 20 years ago and he's fine.")
    $ setWait(39.916,42.752)
    $ speak(NICOLE, "Who's Magic Johnson? Is that a pornstar?")
    $ setWait(42.752,45.547)
    $ speak(JECKA, "I don't think so, my dad talks about him a lot.")
    $ setWait(45.547,47.757)
    $ speak(NICOLE, "You don't think your dad could like a male pornstar?")
    show jecka sc2 angry:
        rightcenterstage
    $ setWait(47.757,52.846)
    $ speak(JECKA, "Nicole I'm already here, I don't need to also have a crisis over whether my dad's gay or not, okay?")
    stop ambient fadeout 1.2
    jump scene_0015
label scene_0015:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0015.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school ext 6
    show jecka sc3:
        rightmidstage

    show nicole sc3:
        off_left
        linear 3 centerstage
    $ setWait(0.122,2.332)
    $ speak(NICOLE, "Hey did you get an email quiz from Miss Lynn?")
    $ setWait(2.332,5.544)
    $ speak(JECKA, "About the Saturday thing? Yeah, I was almost late filling it out.")
    $ setWait(5.544,7.504)
    $ speak(NICOLE, "Like it wasn't enough for us to just go.")
    $ setWait(7.504,9.256)
    $ speak(JECKA, "She had to know we were there somehow.")
    $ setWait(9.256,12.551)
    $ speak(NICOLE, "Yeah but if she wasn't there how would she know we're telling the truth?")
    $ setWait(12.551,14.886)
    $ speak(JECKA, "She could record the assembly and play it back later.")
    $ setWait(14.886,20.6)
    $ speak(NICOLE, "But then just record the crowd so it shows we went there. Female teachers are fucking insane, it's all about a power trip.")
    $ setWait(20.6,22.019)
    $ speak(JECKA, "And the male teachers?")
    $ setWait(22.019,22.978)
    $ speak(NICOLE_JECKA, "Pedophiles.")
    $ setWait(22.978,24.396)
    $ speak(NICOLE, "How'd you know what I was gonna say?")
    $ setWait(24.396,25.605)
    $ speak(JECKA, "I'm noticing a trend.")
    $ setWait(25.605,29.901)
    $ speak(NICOLE, "No, Vote For Pedro shirts were a trend. The other thing's just forever.")
    $ setWait(29.901,33.363)
    $ speak(JECKA, "Okay, well I'm gonna go to class now. Are you going this time?")
    $ setWait(33.363,34.031)
    $ speak(NICOLE, "Why?")
    $ setWait(34.031,36.658)
    $ speak(JECKA, "To not get forced to go to an AIDS Assembly again?")
    $ setWait(36.658,40.37)
    $ speak(NICOLE, "That didn't happen cause we skipped, that happened cause we lied about why we skipped.")
    $ setWait(40.37,44.875)
    $ speak(JECKA, "Well okay, are you looking for a classroom or another excuse right now?")
    show nicole sc3 angry:
        centerstage
    $ setWait(44.875,46.626)
    $ speak(NICOLE, "Oh my god you sound like my mom.")
    show jecka sc3:
        rightmidstage
        pause 0.6
        xzoom -1
        linear 2 off_right
    $ setWait(46.626,48.795)
    $ speak(JECKA, "Whatever, see ya later.")
    show nicole sc3:
        centerstage

    show hunter sc1:
        off_right
        linear 2 rightmidstage
    $ setWait(48.795,50.922)
    $ speak(HUNTER, "Hey Nicole you got a minute?")
    $ setWait(50.922,54.593)
    $ speak(NICOLE, "I got my whole life ahead of me, doesn't mean I'll waste it talking to you.")
    $ setWait(54.593,63.185)
    $ speak(HUNTER, "Oh totally but I mean um, nah you see I was asking around and wondered if you wanted to go to the knife collector show at the Expo center.")
    $ setWait(63.185,65.604)
    $ speak(NICOLE, "Why the fuck would any girl wanna go do that with you?")
    show hunter sc1 sad:
        rightmidstage
    $ setWait(65.604,69.524)
    $ speak(HUNTER, "No it's not like a date it's uh...")
    show hunter sc1:
        rightmidstage
    $ setWait(69.524,70.942)
    $ speak(HUNTER, "But yeah, how are you?")
    $ setWait(70.942,73.07)
    $ speak(NICOLE, "Are you a human text message?")
    show hunter sc1 sad:
        rightmidstage
    $ setWait(73.07,74.362)
    $ speak(HUNTER, "Um...")
    $ setWait(74.362,76.114)
    $ speak(NICOLE, "Is that the alert that you're typing?")
    $ setWait(76.114,80.368)
    $ speak(HUNTER, "Sorry it's just, kinda hard to talk to you.")
    show nicole sc3 smile:
        centerstage
    $ setWait(80.368,81.703)
    $ speak(NICOLE, "Good.")
    show hunter sc1 blush:
        rightmidstage
    $ setWait(81.703,83.58)
    $ speak(HUNTER, "...So what'cha doing today?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0016:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0016.mp3")
    play ambient "audio/Ambience/Fye_ambience.mp3" fadein 1
    scene fye
    show nicole sc1:
        centerstage

    show jecka sc1:
        rightmidstage
        xzoom -1
    $ setWait(0.087,3.799)
    $ speak(NICOLE, "I always wonder if the big gaudy security tags are for show.")
    $ setWait(3.799,7.26)
    $ speak(JECKA, "They don't even reorganize the CD's, how am I supposed to find this?")
    show nicole sc1 angry:
        centerstage
    $ setWait(7.26,10.138)
    $ speak(NICOLE, "You're at F.Y.E. what the fuck do you expect?")
    show jecka sc1 angry:
        rightmidstage
        xzoom 1
    $ setWait(10.138,12.099)
    $ speak(JECKA, "Acknowledgment of the alphabet?")
    show jecka sc1:
        rightmidstage

    show nicole sc1:
        centerstage
    $ setWait(12.099,14.977)
    $ speak(NICOLE, "Don't you have the songs on your iTouch, what do you even want a CD for?")
    show jecka sc1 smile:
        rightmidstage
    $ setWait(14.977,17.896)
    $ speak(JECKA, "Collection. You put 'em on a shelf somewhere-- \"look at my CD's\"")
    $ setWait(17.896,20.983)
    $ speak(NICOLE, "Who's gonna wanna look at your CD collection other than you?")
    show jecka sc1:
        rightmidstage
    $ setWait(20.983,22.442)
    $ speak(JECKA, "Guys who want me bad.")
    $ setWait(22.442,30.158)
    $ speak(JECKA, "See they think they can manipulate me by pretending to care about my taste in music, but I'm actually manipulating them into learning about my favorite artists.")
    $ setWait(30.158,31.284)
    $ speak(NICOLE, "When all along...")
    show jecka sc1 smile:
        rightmidstage
    $ setWait(31.284,33.912)
    $ speak(JECKA, "I have no intention of fucking them in the first place.")
    show nicole sc1 smile:
        centerstage
    $ setWait(33.912,35.33)
    $ speak(NICOLE, "That's genius.")
    show jecka sc1:
        rightmidstage
        xzoom -1
    $ setWait(35.33,39.543)
    $ speak(JECKA, "Why's Flaming Lips in the M section? Wait what is Flaming Lips?")
    show nicole sc1:
        centerstage
    $ setWait(39.543,40.502)
    $ speak(NICOLE, "Shitty.")
    $ setWait(40.502,41.878)
    $ speak(JECKA, "Okay I'll give it a try.")
    $ setWait(41.878,46.8)
    $ speak(NICOLE, "Can you hurry up? I feel like we're 20 seconds away from a guy in a Spitfire shirt asking us what bands we like.")
    show jecka sc1 smile:
        rightmidstage
        xzoom -1
        pause 1.25
        xzoom 1
    $ setWait(46.8,49.177)
    $ speak(JECKA, "Oh just found it! So how do we sneak it out?")
    $ setWait(49.177,52.18)
    $ speak(NICOLE, "Say that again but just as loud so everyone in the store can hear.")
    show jecka sc1 angry:
        rightmidstage
    $ setWait(52.18,54.016)
    $ speak(JECKA, "I don't do this all the time, Nicole.")
    $ setWait(54.016,56.059)
    $ speak(NICOLE, "College should have a major in shoplifting.")
    show nicole sc1:
        centerstage
        linear 1 off_farright

    show jecka sc1:
        rightmidstage
        pause 0.7
        xzoom -1
        linear .8 off_right
    $ setWait(56.059,57.269)
    $ speak(NICOLE, "Quick, come on!")
    stop ambient fadeout 2
    jump scene_0017
label scene_0017:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0017.mp3")
    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1
    scene mall int 2
    show nicole sc1 smile:
        xzoom -1
        off_right
        linear 1.5 leftmidstage
        xzoom 1

    show jecka sc1 smile:
        off_right
        pause 0.5
        linear 1.3 leftcenterstage
    $ setWait(0.082,1.792)
    $ speak(JECKA, "Oh my god that was such a rush.")
    $ setWait(1.792,3.544)
    $ speak(NICOLE, "Yeah spending money's for posers.")
    $ setWait(3.544,6.046)
    $ speak(JECKA, "Aw it'll sound so good on my dad's stereo too!")
    $ setWait(6.046,10.301)
    $ speak(NICOLE, "I don't think I've heard a single person say stereo without \"dad\" in front of it.")
    $ setWait(10.301,13.262)
    $ speak(JECKA, "Well yeah stereos are for old people without iPods.")
    show nicole sc1:
        leftmidstage
    $ setWait(13.262,15.598)
    $ speak(NICOLE, "Do you think we'll ever end up old people with iPods?")
    show jecka sc1 worried:
        leftcenterstage
    $ setWait(15.598,17.558)
    $ speak(JECKA, "Ew I don't wanna think about being old.")
    $ setWait(17.558,20.144)
    $ speak(NICOLE, "Yeah I'd probably kill myself before that happens anyway.")
    show jecka sc1:
        leftcenterstage
    $ setWait(20.144,24.565)
    $ speak(JECKA, "If you do can you like leave a note on how you killed yourself? In case I wanna do it too.")
    $ setWait(24.565,26.066)
    $ speak(NICOLE, "Dude yeah, what are friends for?")
    $ setWait(26.066,31.071)
    $ speak(JECKA, "Yeah cause my mom was telling me about the Zodiac killer and I don't think anyone's gonna go out that cool again.")
    show nicole sc1 smile:
        leftmidstage
    $ setWait(31.071,32.74)
    $ speak(NICOLE, "Oh is he the guy with the symbol notes??")
    show jecka sc1 smile:
        leftcenterstage
    $ setWait(32.74,34.033)
    $ speak(JECKA, "Oh my god-- yeah!")
    $ setWait(34.033,42.291)
    $ speak(NICOLE, "It would be cool to go out like that. Think about it, some infamous shadowy figure kills you and then writes to the news in code about how hot it was when you died.")
    show jecka sc1:
        leftcenterstage
    $ setWait(42.291,44.335)
    $ speak(JECKA, "He'd probably say that about every girl he kills.")
    show nicole sc1:
        leftmidstage
    $ setWait(44.335,50.883)
    $ speak(NICOLE, "Yeah no that's true. If he doesn't specifically say I'm his hottest victim then fuck off, he can kill someone else.")
    $ setWait(50.883,53.802)
    $ speak(JECKA, "I get that... Do you think we're crazy for wanting that?")
    $ setWait(53.802,56.263)
    $ speak(NICOLE, "No we're just hot, these are hotgirl problems.")
    $ setWait(56.263,59.642)
    $ speak(JECKA, "Totally... Should we leave before we get caught or?")
    show nicole sc1:
        leftmidstage
        pause 1.2
        xzoom -1
        linear 0.5 leftstage
    $ setWait(59.642,60.976)
    $ speak(NICOLE, "Yeah let's go to the chrome diner.")

    show red onlayer screens:
        alpha 0.7
        pause 0.1 alpha 0
        pause 0.3 alpha 0.7
        pause 0.1 alpha 0
        pause 0.3 alpha 0.7
        pause 0.1 alpha 0

    show blue onlayer screens:
        alpha 0
        pause 0.2 alpha 0.7
        pause 0.1 alpha 0
        pause 0.3 alpha 0.7
        pause 0.1 alpha 0

    show nicole sc1 surprised:
        leftstage
        xzoom -1
        linear 0.15 leftmidstage

    show jecka sc1 surprised:
        xalign .37
        linear 0.06 xalign .39
        linear 0.06 xalign .35
        linear 0.06 xalign .38
        linear 0.06 xalign .36
        linear 0.06 leftcenterstage
    $ setWait(60.976,61.56)
    $ speak(JECKA, "Oh god!")
    $ setWait(61.56,63.312)
    $ speak(NICOLE, "Since when are the scanners here??")
    show nicole sc1 surprised:
        leftmidstage
        xzoom -1
        pause 0.5
        xzoom 1

    show jecka sc1 surprised:
        leftcenterstage
        pause 0.4
        xzoom -1

    show mallcop:
        off_right
        linear 1 rightstage
    $ setWait(63.312,65.397)
    $ speak(MALLCOP, "Looks like the jig is up, girls.")

    show nicole sc1 angry:
        leftmidstage

    show jecka sc1 worried:
        leftcenterstage
        xzoom -1

    $ setWait(65.397,66.19)
    $ speak(NICOLE, "God dammit.")
    $ setWait(66.19,73.447)
    $ speak(MALLCOP, "Caught over stealing a $12.99 CD, I hope it was worth it.\nWhat band did you like so much, huh?")
    show jecka sc1 worried:
        leftcenterstage
        xzoom 1
    $ setWait(73.447,74.865)
    $ speak(JECKA, "He's not wearing a Spitfire shirt.")
    show nicole sc1 angry:
        leftmidstage
    show jecka sc1:
        leftcenterstage
        pause 0.6
        xzoom -1
    $ setWait(74.865,77.326)
    $ speak(NICOLE, "Dude the CD was her's she brought it from home to trade in.")
    $ setWait(77.326,80.454)
    $ speak(MALLCOP, "With the price label and security tag still on it?")
    $ setWait(80.454,81.914)
    $ speak(NICOLE, "She collects! Right?")
    $ setWait(81.914,85.125)
    $ speak(JECKA, "Yeah they lose collector's value if you take those off.")
    show mallcop:
        rightstage
        linear 2.3 rightmidstage
    $ setWait(85.125,88.671)
    $ speak(MALLCOP, "You girls are gonna need a better story than that.")
    menu:
        "FLIRT WITH HIM\nTO GET OUT OF IT":
            jump scene_0018
        "MAKE A RUN FOR IT":
            jump scene_0024
label scene_0018:
    $ setVoiceTrack("audio/Scenes/0018.mp3")
    scene mall int 2

    show mallcop:
        rightmidstage

    show jecka sc1:
        xzoom -1
        leftcenterstage

    show nicole sc1 smile:
        leftmidstage
    $ setWait(0.04,3.335)
    $ speak(NICOLE, "Well... Do you want the truth?")
    $ setWait(3.335,4.419)
    $ speak(MALLCOP, "Of course.")
    show nicole sc1 flirt:
        leftmidstage
        linear 2 rightcenterstage
    $ setWait(4.419,12.385)
    $ speak(NICOLE, "See we saw you standing guard over there looking so strong, we kinda wanted an excuse to get arrested... Right?")
    show jecka sc1 smile:
        xzoom -1
        leftcenterstage
        pause 1.4
        linear 1 centerstage
    $ setWait(12.385,16.264)
    $ speak(JECKA, "Uh--Oh! Yeah- we have a thing for handcuffs.")
    $ setWait(16.264,24.105)
    $ speak(NICOLE, "Just being tossed around by an aggro man in uniform. Being bad can have some good payoff sometimes.")
    $ setWait(24.105,27.609)
    $ speak(MALLCOP, "Uh is there something you girls would like me to know?")
    show jecka sc1 flirt:
        xzoom -1
        centerstage
    $ setWait(27.609,33.323)
    $ speak(JECKA, "Yeah actually. We want you to know your wife doesn't need to know.")
    $ setWait(33.323,42.165)
    $ speak(NICOLE, "Totally, your wife is probably such a bitch when you come home. But we're two hot girls with no expectations at all.")
    $ setWait(42.165,47.837)
    $ speak(MALLCOP, "Huh... well my wife is a bitch cunt whore who I'm killing first if I ever get fired.")
    show jecka sc1 smile:
        xzoom -1
        centerstage
    $ setWait(47.837,50.257)
    $ speak(JECKA, "And see that doesn't scare us off at all.")
    $ setWait(50.257,52.676)
    $ speak(NICOLE, "Yeah you're dangerous, we want you more now.")
    $ setWait(52.676,56.638)
    $ speak(JECKA, "You wanna just forget about this CD and hang out somewhere? Topgolf just opened.")
    $ setWait(56.638,58.723)
    $ speak(NICOLE, "Fuck Topgolf, let's go to the Super8.")
    show jecka sc1 flirt:
        centerstage
        xzoom -1
    $ setWait(58.723,60.35)
    $ speak(JECKA, "You're so naughty.")

    show mallcop:
        rightmidstage
        linear .5 xalign .98

    $ setWait(60.35,62.769)
    $ speak(MALLCOP, "H-how old are you girls anyway?")
    $ setWait(62.769,66.064)
    $ speak(NICOLE, "Well we're a package deal so 34.")
    $ setWait(66.064,69.901)
    $ speak(MALLCOP, "34? Divided by two that's uh... hold on.")
    $ setWait(69.901,72.32)
    $ speak(JECKA, "Shhh you're a cop you don't need to know math.")
    $ setWait(72.32,74.99)
    $ speak(NICOLE, "So what if we're a little young? No one needs to know.")
    $ setWait(74.99,77.409)
    $ speak(JECKA, "Yeah take us to Cancun where we're legal.")
    $ setWait(77.409,80.704)
    $ speak(MALLCOP, "I got a place where I'd really like to take you.")
    show jecka sc1 smile:
        centerstage
    $ setWait(80.704,81.663)
    $ speak(JECKA, "Thailand?")
    $ setWait(81.663,82.956)
    $ speak(MALLCOP, "Downtown!")
    show nicole sc1 angry:
        rightcenterstage

    show jecka sc1 angry:
        centerstage
        linear 0.3 leftcenterstage

    $ setWait(82.956,85.417)
    $ speak(NICOLE, "Shit! Over a fucking MSI CD?")
    $ setWait(85.417,88.878)
    $ speak(MALLCOP, "You minors thought you could pull a fast one on me, huh?")
    $ setWait(88.878,92.966)
    $ speak(MALLCOP, "Though I will admit, you both look very mature for thirteen.")
    $ setWait(92.966,93.967)
    $ speak(JECKA, "Thirteen??")
    $ setWait(93.967,95.427)
    $ speak(NICOLE, "And they let you have a gun??")
    $ setWait(95.427,97.846)
    $ speak(MALLCOP, "We can't all be algebra experts.")
    stop ambient fadeout 2.2
    jump scene_0019
label scene_0019:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.4 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show title_twoweekslater onlayer screens

    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter



    $ setVoiceTrack("audio/Scenes/0019.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3"
    hide title_twoweekslater onlayer screens
    scene classroom int 4
    show nicole sc2:
        leftcenterstage

    show kelly sc1 sad:
        leftstage

    show jecka sc2:
        rightcenterstage
    $ setWait(0.085,1.92)
    $ speak(JECKA, "What the hell is this again?")
    $ setWait(1.92,4.214)
    $ speak(NICOLE, "The school's sex addict rehab program.")

    hide kelly sc1

    show kelly sc1 blush onlayer screens:
        leftstage
        xzoom -1
        linear 3.2 off_right

    show jecka sc2:
        rightcenterstage
        pause 2.1
        xzoom -1
    $ setWait(4.214,7.843)
    $ speak(KELLY, "Lexapro... I need Lexapro...")
    show jecka sc2:
        rightcenterstage
        xzoom 1
    $ setWait(7.843,9.678)
    $ speak(JECKA, "Just cause we flirted with that guy?")
    $ setWait(9.678,13.306)
    $ speak(NICOLE, "I know, we get the one male cop who isn't a pedophile.")
    $ setWait(13.306,14.725)
    $ speak(JECKA, "Is that our silver lining?")
    $ setWait(14.725,20.605)
    $ speak(NICOLE, "Maybe the mall cop snitching to the truancy officer is. It's a little entertaining to see what kids we know here.")
    show jeffery sc1 smile:
        off_right
        linear 1 rightmidstage

    show jecka sc2 surprised:
        rightcenterstage
        pause 0.3
        xzoom -1
        linear 0.65 leftmidstage
    $ setWait(20.605,24.109)
    $ speak(JEFFERY, "Oh hey! Didn't know you guys had to go here too.")
    $ setWait(24.109,25.152)
    $ speak(JECKA, "Is this surprising?")
    $ setWait(25.152,27.112)
    $ speak(NICOLE, "No... No it's not.")
    show jeffery sc1:
        rightmidstage
        linear 1 rightcenterstage
    $ setWait(27.112,29.448)
    $ speak(JEFFERY, "Hello? Earth to Nicole!")
    show jecka sc2 angry:
        leftmidstage
        xzoom -1
    $ setWait(29.448,30.991)
    $ speak(JECKA, "Oh my god make him go away.")
    show jecka sc2:
        leftmidstage
        xzoom -1
    $ setWait(30.991,35.62)
    $ speak(NICOLE, "Jeffery, how does a guy who sounds like a cartoon also have a sex addiction problem?")
    show jeffery sc1:
        rightcenterstage
    $ setWait(35.62,37.622)
    $ speak(JEFFERY, "Uh, can those not be together?")
    show jecka sc2 smile:
        leftmidstage
        xzoom -1
    $ setWait(37.622,40.834)
    $ speak(JECKA, "Do you get turned on by the paperclip guy in Microsoft Office?")
    $ setWait(40.834,44.046)
    $ speak(JEFFERY, "Sorry I'm a Mac user, is that why you're here?")
    show nicole sc2 smile:
        leftcenterstage
        xzoom -1
    $ setWait(44.046,45.756)
    $ speak(NICOLE, "Yeah Jecka is that why you're here?")
    show jecka sc2 flirt:
        leftmidstage
        xzoom -1
    $ setWait(45.756,49.051)
    $ speak(JECKA, "Oh my god totally, every time he pops up I just wanna rub against him.")

    show jeffery sc1 blush:
        rightcenterstage

    show jecka sc2 smile:
        leftmidstage
        xzoom -1

    show nicole sc2:
        leftcenterstage
        xzoom -1
        pause 0.3
        xzoom 1

    $ setWait(49.051,59.019)
    $ speak(JEFFERY, "R-Rub against him? Ugh that's... So... Ugh! Sorry! Last week we covered how to avoid sharing inappropriate thoughts with other girls.")
    $ setWait(59.019,61.354)
    $ speak(JECKA, "No kidding, a whole lesson?")
    $ setWait(61.354,63.398)
    $ speak(NICOLE, "Yeah, is that why you're here?")
    $ setWait(63.398,68.07)
    $ speak(JEFFERY, "Well... If I shared why I'm here then... I'd be relapsing.")
    show nicole sc2 smile:
        leftcenterstage
    $ setWait(68.07,70.697)
    $ speak(NICOLE, "C'mon, we all need a relapse every now and then.")
    show jeffery sc1:
        rightcenterstage
    $ setWait(70.697,72.699)
    $ speak(JEFFERY, "Are you peer pressuring me?")
    $ setWait(72.699,74.743)
    $ speak(JECKA, "More like peer helping you?")
    $ setWait(74.743,81.792)
    $ speak(JECKA, "My Valium ran out a couple months ago, but this morning I took so much of my Mom's Valium I can't even feel my lungs when I breathe in. I'm just zen.")
    $ setWait(81.792,84.628)
    $ speak(NICOLE, "Yeah and zen's a good ass fuckin' feeling, Jeffery.")

    show nicole sc2:
        leftcenterstage

    show jecka sc2:
        leftmidstage

    $ setWait(84.628,93.053)
    $ speak(JEFFERY, "O-okay fine...\nI was in the afterschool gaming club, playing Jak and Daxter on the PS2 and uh...")
    $ setWait(93.053,94.304)
    $ speak(JECKA, "What a setup for this.")
    $ setWait(94.304,100.894)
    $ speak(JEFFERY, "Yeah so I'm playing it and no one else was around and I just kinda felt like y'know...")
    $ setWait(100.894,103.271)
    $ speak(JEFFERY, "Feeling around down there...")
    $ setWait(103.271,104.147)
    $ speak(NICOLE, "...Yeah?")
    $ setWait(104.147,107.901)
    $ speak(JEFFERY, "Well one thing led to another and before I knew it...")
    $ setWait(107.901,114.032)
    $ speak(JEFFERY, "I was out in the open touching with one hand while the other was still playing Jak and Daxter.")
    $ setWait(114.032,116.868)
    $ speak(NICOLE, "You jacked off to Jak and Daxter?")
    show jeffery sc1 angry:
        rightcenterstage
    $ setWait(116.868,123.458)
    $ speak(JEFFERY, "What-- No I didn't do it to Jak and Daxter, I did it while playing Jak and Daxter.")
    show nicole sc2 smile:
        leftcenterstage

    show jecka sc2 smile:
        leftmidstage
        xzoom -1
    $ setWait(123.458,125.293)
    $ speak(NICOLE, "And you finished and everything?")
    $ setWait(125.293,126.211)
    $ speak(JECKA, "Don't ask that.")
    show jeffery sc1:
        rightcenterstage
    $ setWait(126.211,135.512)
    $ speak(JEFFERY, "I wasn't trying to do that, I just spaced out and eventually the club sponsor walked in on me. So I had to go here or else they'd expel me.")
    $ setWait(135.512,138.598)
    $ speak(NICOLE, "You really put the jack in Jak and Daxter, huh?")
    show jecka sc2:
        leftmidstage
        xzoom -1
    $ setWait(138.598,142.811)
    $ speak(JECKA, "So you're doing it and what's Jak and Daxter doing? He's just running around?")
    $ setWait(142.811,147.524)
    $ speak(JEFFERY, "They were running around, Jak and Daxter's two separate characters, Jecka.")
    show nicole sc2:
        leftcenterstage
    $ setWait(147.524,153.572)
    $ speak(JECKA, "So you just told two girls how you got off to a video game but you're more concerned if we know the characters in the video game.")
    $ setWait(153.572,155.532)
    $ speak(JEFFERY, "Uh... y-yeah.")
    $ setWait(155.532,157.993)
    $ speak(JECKA, "Why would you do that to a game for little kids?")
    $ setWait(157.993,159.119)
    $ speak(JEFFERY, "It's T for Teen.")
    $ setWait(159.119,161.83)
    $ speak(NICOLE, "So was this a group thing? Did Daxter jack too?")
    $ setWait(161.83,165.167)
    $ speak(JEFFERY, "Uh I never played Jak 2 I wouldn't know.")
    $ setWait(165.167,166.459)
    $ speak(JECKA, "We need to get the fuck out of here.")
    show nicole sc2:
        leftcenterstage
        xzoom -1
    $ setWait(166.459,169.921)
    $ speak(NICOLE, "What are you talking about? He's probably the worst one here, everyone else should be cool.")
    show kelly sc1 blush onlayer screens:
        xzoom 1
        off_right
        linear 8 off_left

    show jecka sc2:
        xzoom -1
        leftmidstage
        pause 6.4
        xzoom 1

    $ setWait(169.921,177.971)
    $ speak(KELLY, "Forgive me father for I have sinned. Please make these urges go away, my cousin is not hot, my cousin is not hot...")
    $ setWait(177.971,179.598)
    $ speak(NICOLE, "Okay we need to get the fuck outta here.")
    show jecka sc2:
        leftmidstage
        xzoom -1
    $ setWait(179.598,183.018)
    $ speak(JECKA, "I wish we could walk out but the principal's watching the door so hard.")
    $ setWait(183.018,186.062)
    $ speak(NICOLE, "I think we're gonna need a distraction.")
    menu:
        "RILE UP\nPOTENTIAL STALKER":
            jump scene_0020
        "GET THE SEX ADDICTS\nTO FIGHT":
            jump scene_0022
label scene_0020:
    $ setVoiceTrack("audio/Scenes/0020.mp3")
    scene classroom int 4

    show jecka sc2:
        leftmidstage
        xzoom -1

    show nicole sc2 smile:
        leftcenterstage

    show jeffery sc1:
        rightcenterstage

    $ setWait(0.045,7.469)
    $ speak(NICOLE, "Y'know Jeffery, don't tell anyone but, I actually think it's kinda cool that you did that.")
    show jeffery sc1 blush:
        rightcenterstage

    $ setWait(7.469,8.428)
    $ speak(JEFFERY, "You do?")
    $ setWait(8.428,9.012)
    $ speak(JECKA, "Here we go...")
    $ setWait(9.012,15.352)
    $ speak(NICOLE, "Yeah I know we were laughing about it but I've totally been there before.")
    $ setWait(15.352,17.103)
    $ speak(JEFFERY, "Wh-What do you mean?")
    show nicole sc2 flirt:
        leftcenterstage
    $ setWait(17.103,23.818)
    $ speak(NICOLE, "I literally do the same thing but at home, I just didn't think anyone else would be that kinky.")
    $ setWait(23.818,26.196)
    $ speak(JEFFERY, "Like while you're playing a video game too?")
    $ setWait(26.196,29.157)
    $ speak(NICOLE, "Obvi it's like the only way I do it nowadays.")
    show jecka sc2 smile:
        leftmidstage
        xzoom -1
    $ setWait(29.157,30.658)
    $ speak(JECKA, "Yeah? What game?")
    show nicole sc2 surprised:
        leftcenterstage
        xzoom -1
        pause 4
        xzoom 1
    $ setWait(30.658,35.747)
    $ speak(NICOLE, "Oh, um...\nCrash Bandicoot\n... Five.")
    show nicole sc2:
        leftcenterstage

    show jecka sc2:
        leftmidstage
        xzoom -1

    show jeffery sc1:
        rightcenterstage
    $ setWait(35.747,37.665)
    $ speak(JEFFERY, "I don't think there's a fifth one of that.")
    $ setWait(37.665,42.128)
    $ speak(NICOLE, "Yeah sorry I meant um, Crash Bandicoot... One.")
    $ setWait(42.128,43.338)
    $ speak(NICOLE, "They made one, right?")
    show jeffery sc1 smile:
        rightcenterstage
    $ setWait(43.338,45.256)
    $ speak(JEFFERY, "Crash 1, that's a classic.")
    show jecka sc2 smile:
        leftmidstage
        xzoom -1
    $ setWait(45.256,47.717)
    $ speak(JECKA, "Wow we're in the presence of a master gamer.")
    show nicole sc2 flirt:
        leftcenterstage
    $ setWait(47.717,52.305)
    $ speak(NICOLE, "Did I mention I had a thing for master gamers?")
    show jeffery sc1 blush:
        rightcenterstage
    $ setWait(52.305,55.35)
    $ speak(JEFFERY, "A thing? Wh-What do you mean by that?")
    $ setWait(55.35,61.523)
    $ speak(NICOLE, "What I mean is, you wanna come over to my house and play Jak and Daxter sometime?")
    $ setWait(61.523,66.945)
    $ speak(JEFFERY, "Oh uh... I've never really done that with a... girl before.")
    $ setWait(66.945,68.905)
    $ speak(NICOLE, "But why don't we fix that?")
    $ setWait(68.905,70.99)
    $ speak(JEFFERY, "Ugh! Unnnnhhh!!!")
    show jecka sc2 surprised:
        leftmidstage
        xzoom -1

    show nicole sc2 surprised:
        leftcenterstage
    $ setWait(70.99,71.991)
    $ speak(JECKA, "What'd you do??")
    show nicole sc2 surprised:
        leftcenterstage
        xzoom -1
    $ setWait(71.991,73.076)
    $ speak(NICOLE, "I guess he's turned on?")
    show nicole sc2 surprised:
        leftcenterstage
        xzoom -1
        pause 0.6
        xzoom 1
    $ setWait(73.076,76.246)
    $ speak(JEFFERY, "I want you to watch me while I do it! Ugggggggg!!!!")
    show lynn 1:
        off_right
        linear 0.3 rightmidstage
    $ setWait(76.246,80.708)
    $ speak(LYNN, "What's this all about?\nJeffery we went over how to control these patterns!")
    show jeffery sc1 perv:
        rightcenterstage
        pause 1.9
        xzoom -1
    $ setWait(80.708,86.881)
    $ speak(JEFFERY, "I'm just so... take me Miss Lynn! I'll do anything for your sweet relief!")
    $ setWait(86.881,87.966)
    $ speak(LYNN, "Stop it right now!")
    show jecka sc2 smile:
        leftmidstage
        xzoom -1
        pause 3
        xzoom 1
        linear 0.7 off_farleft
    $ setWait(87.966,91.428)
    $ speak(JECKA, "Wow Miss Lynn that's pretty embarrassing, we'll get out of your way for this one.")
    show nicole sc2 smile:
        leftcenterstage
        xzoom -1
        linear 0.7 off_left
    $ setWait(91.428,93.179)
    $ speak(NICOLE, "Good luck with the master gamer.")
    stop ambient fadeout 2
    jump scene_0021
label scene_0021:
    show black onlayer screens with Pause(1.5):
        alpha 0.0
        linear 1.2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0021.mp3")
    play ambient "audio/Ambience/Bathroom_Lockerroom_Ambience.mp3" fadein 1
    scene locker room
    show jecka changing:
        rightcenterstage

    show nicole sc3:
        leftcenterstage
    $ setWait(0.124,2.584)
    $ speak(NICOLE, "Have you heard anything from the principal since yesterday?")
    $ setWait(2.584,5.212)
    $ speak(JECKA, "No I think her hands were more than full with Jeffery.")
    $ setWait(5.212,8.882)
    $ speak(NICOLE, "I thought I'd need to say way more to get him going. He's really got a problem.")
    $ setWait(8.882,11.093)
    $ speak(JECKA, "I don't even know why you'd subject yourself to that.")
    $ setWait(11.093,12.302)
    $ speak(NICOLE, "We got out didn't we?")
    show jecka changing sad:
        rightcenterstage
    $ setWait(12.302,14.972)
    $ speak(JECKA, "Yeah I guess but playing with some weird kid like that?")
    $ setWait(14.972,19.017)
    $ speak(JECKA, "He's gonna like, go home and think about you when he's... Master gaming.")
    show jecka changing:
        rightcenterstage
    $ setWait(19.017,23.731)
    $ speak(NICOLE, "Dude we're in high school.\nWe could be covered in spaghetti sauce, they're still gonna think about us when they jerk off.")
    $ setWait(23.731,25.232)
    $ speak(JECKA, "No way, that often?")
    $ setWait(25.232,26.316)
    $ speak(NICOLE, "Are we on Teen Nick?")
    show jecka changing angry:
        rightcenterstage
    $ setWait(26.316,28.235)
    $ speak(JECKA, "Bitch, Zoey 101's a good show.")
    $ setWait(28.235,29.361)
    $ speak(NICOLE, "Hey Emily!")
    show jecka changing:
        rightcenterstage
        pause 0.6
        xzoom -1

    show emily pj:
        off_right
        linear 1.5 rightmidstage
    $ setWait(29.361,30.237)
    $ speak(EMILY, "What's up?")
    $ setWait(30.237,34.116)
    $ speak(NICOLE, "Do guys think about us when they... y'know, do it?")
    show emily pj angry:
        rightmidstage
    $ setWait(34.116,36.493)
    $ speak(EMILY, "I've gotten texts when they think about me doing it.")
    $ setWait(36.493,37.703)
    $ speak(NICOLE, "Oh I got that once.")
    $ setWait(37.703,39.455)
    $ speak(EMILY, "It's like \"yeah thanks\".")
    $ setWait(39.455,42.207)
    $ speak(JECKA, "I wonder how I'd feel about that if I really liked the guy.")
    show emily pj:
        rightmidstage
    $ setWait(42.207,50.215)
    $ speak(EMILY, "Well no if Johnny Depp did it I'd be like \"tell me more\" but it's never Johnny Depp.\nIt's always... some guy who looks like a Travis.")
    $ setWait(50.215,52.634)
    $ speak(JECKA, "If this happens so much why haven't I gotten a text?")
    $ setWait(52.634,54.678)
    $ speak(EMILY, "You're kinda too preppy for it honestly.")
    $ setWait(54.678,57.681)
    $ speak(NICOLE, "Yeah we're more trashy so guys think we'll be into it.")
    $ setWait(57.681,60.601)
    $ speak(JECKA, "I wonder what being trashy's like...")
    show emily pj smile:
        rightmidstage
    $ setWait(60.601,62.728)
    $ speak(EMILY, "You could pierce your tongue and find out.")
    show emily pj:
        rightmidstage
    $ setWait(62.728,64.938)
    $ speak(EMILY, "By the way where you headed, Nicole?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0022:
    $ setVoiceTrack("audio/Scenes/0022.mp3")
    scene classroom int 4
    show nicole sc2:
        leftcenterstage

    show jecka sc2:
        leftmidstage
        xzoom -1

    show jeffery sc1:
        rightcenterstage
    $ setWait(0.001,2.712)
    $ speak(NICOLE, "Huh... Hey Kelly!")
    show kelly sc1:
        off_right
        linear 1.3 rightmidstage

    show jeffery sc1:
        rightcenterstage
        xzoom -1
    $ setWait(2.712,3.713)
    $ speak(KELLY, "What's up Nicole?")
    $ setWait(3.713,7.008)
    $ speak(NICOLE, "Jeffery was just telling me how he wants to shove his face in your boobs.")
    show kelly sc1 angry:
        rightmidstage
    $ setWait(7.008,7.758)
    $ speak(KELLY, "Uh what??")
    show jeffery sc1 angry:
        rightcenterstage
        xzoom -1
    $ setWait(7.758,9.76)
    $ speak(JEFFERY, "Wha- Hey! I didn't say that!")
    $ setWait(9.76,13.305)
    $ speak(NICOLE, "Oh my god Jeffery don't lie, the first step is admitting you have a problem.")
    $ setWait(13.305,17.143)
    $ speak(KELLY, "If you were attractive I'd immediately let you, but you're just another ugly stalker!")
    $ setWait(17.143,19.311)
    $ speak(JECKA, "Yeah keep it in your pants for once, Jeffery.")
    $ setWait(19.311,23.274)
    $ speak(KELLY, "If I wasn't in a relationship with Jesus now, I would hurt you so bad!")
    show jeffery sc1 blush:
        rightcenterstage
        xzoom -1
        linear 0.65 leftmidstage

    show jecka sc2:
        leftmidstage
        xzoom -1
        pause 0.5
        linear 0.3 leftstage
    $ setWait(23.274,25.151)
    $ speak(JEFFERY, "Okay! Okay! Please don't!")
    show nicole sc2 smile:
        leftcenterstage
    $ setWait(25.151,28.821)
    $ speak(NICOLE, "But then he said that you were way cuter and less slutty than Ari.")
    show kelly sc1:
        rightmidstage
        linear 2 rightcenterstage
    $ setWait(28.821,31.824)
    $ speak(KELLY, "Oh my god that's actually really sweet, thank you Jeffery.")
    $ setWait(31.824,33.743)
    $ speak(KELLY, "I'd still never fuck you in a million years.")
    show nicole sc2:
        leftcenterstage

    show jeffery sc1:
        leftmidstage
        xzoom -1
    $ setWait(33.743,34.452)
    $ speak(NICOLE_JECKA, "Same.")
    show ari sc2 angry:
        off_right
        linear 1 rightstage
    $ setWait(34.452,36.37)
    $ speak(ARI, "Oh so you think you can just talk shit about me?")
    show kelly sc1:
        rightcenterstage
        xzoom -1
    $ setWait(36.37,37.371)
    $ speak(KELLY, "Bitch don't be jealous.")
    show ari sc2 angry:
        rightstage
        linear 0.7 rightmidstage
    $ setWait(37.371,39.29)
    $ speak(ARI, "Bitch I don't get jealous of sluts.")
    $ setWait(39.29,40.166)
    $ speak(NICOLE_JECKA, "Oohhhhh.")
    show kelly sc1 angry:
        rightcenterstage
        xzoom -1
    $ setWait(40.166,45.171)
    $ speak(KELLY, "Yeah Ari I'm not a slut anymore okay? I have a relationship with God and Jesus now!")
    $ setWait(45.171,48.549)
    $ speak(ARI, "Is that who told you to sell your ass for an iPod Nano last week?")
    $ setWait(48.549,49.05)
    $ speak(NICOLE, "Damn!")
    $ setWait(49.05,50.301)
    $ speak(JECKA, "Not even a video one?")
    $ setWait(50.301,52.178)
    $ speak(KELLY, "Uh, I don't even know what you're talking about?")
    $ setWait(52.178,56.766)
    $ speak(ARI, "Face it, bitch! Jesus is a pimp and born again virgins like you are his army of hos!")
    show kelly sc1:
        rightcenterstage
        xzoom -1
        pause 0.5
        xzoom 1
    $ setWait(56.766,60.895)
    $ speak(JEFFERY, "Hey guys let's settle down and try to be at least halfway respectful here!")
    $ setWait(60.895,63.481)
    $ speak(ARI, "Why don't you fuck off and finish last, virgin?")
    $ setWait(63.481,64.648)
    $ speak(JECKA, "You had it coming, Jeffery.")
    show kelly sc1 angry:
        rightcenterstage
        xzoom -1
    $ setWait(64.648,66.4)
    $ speak(KELLY, "Oh now you have beef with Jeffery?")
    $ setWait(66.4,69.278)
    $ speak(ARI, "Sorry didn't mean to insult your future customers.")
    $ setWait(69.278,71.614)
    $ speak(KELLY, "Do you actually wanna fucking fight right now??")
    $ setWait(71.614,73.824)
    $ speak(ARI, "Bitch I brought a knife to school, don't even try me.")
    $ setWait(73.824,75.534)
    $ speak(KELLY, "Yeah right, what're you gonna do with that?")
    $ setWait(75.534,77.411)
    $ speak(ARI, "Stab you and watch the skeet pour out.")
    show kelly sc1 angry:
        rightcenterstage
        xzoom -1
        linear 0.3 xalign .66
    $ setWait(77.411,78.829)
    $ speak(KELLY, "Not if I choke you first!")
    show ari sc2 angry:
        rightmidstage
        linear 0.3 xalign 0.85
    $ setWait(78.829,79.997)
    $ speak(ARI, "I'll spit in your face!")
    show kelly sc1 angry:
        xalign .66
        xzoom -1
        linear 0.3 xalign .69
    $ setWait(79.997,81.165)
    $ speak(KELLY, "I'll spit in your mouth!")
    show ari sc2 angry:
        xalign 0.85
        linear 0.3 xalign 0.82
    $ setWait(81.165,82.458)
    $ speak(ARI, "I'll like it!")
    show jecka sc2 surprised:
        leftstage
        xzoom -1
    $ setWait(82.458,83.209)
    $ speak(JECKA, "What is happening?")
    $ setWait(83.209,83.626)
    $ speak(NICOLE, "Shhh!")
    show kelly sc1 blush:
        xalign 0.69
        xzoom -1
    $ setWait(83.626,84.794)
    $ speak(KELLY, "Will you spit in mine back?")
    show ari sc2 blush:
        xalign 0.82
    $ setWait(84.794,87.379)
    $ speak(ARI, "I'll bite your bottom lip and make you fucking bleed.")
    $ setWait(87.379,89.131)
    $ speak(KELLY, "Promise to kiss me after-- No...")
    show kelly sc1 sad:
        xalign 0.69
        linear 0.15 rightcenterstage
    $ setWait(89.131,94.386)
    $ speak(KELLY, "NO! Help me, Jesus! Help me! It's not love it's just lust, it's not love it's just lust.")
    $ setWait(94.386,95.346)
    $ speak(NICOLE, "What the fuck...")
    show lynn 1:
        off_right
        linear 0.7 rightmidstage

    show ari sc2 angry:
        xalign 0.82
        pause 0.7
        linear 0.4 rightstage
    $ setWait(95.346,96.764)
    $ speak(LYNN, "Okay girls! Break it up!")
    show jecka sc2 angry:
        leftstage
        xzoom -1
    $ setWait(96.764,97.973)
    $ speak(JECKA, "Oh now you stop them.")
    show lynn 1:
        rightmidstage
        pause 2.2
        xzoom -1
    $ setWait(97.973,101.685)
    $ speak(LYNN, "One phone call and I can lock you both into a real rehab program.")
    show nicole sc2:
        leftcenterstage
        xzoom -1
        linear 0.7 off_left
    $ setWait(101.685,102.353)
    $ speak(NICOLE, "Let's go.")
    show jecka sc2:
        leftstage
        xzoom 1
        linear 0.5 off_left
    $ setWait(102.353,103.771)
    $ speak(JECKA, "Oh yeah.")
    stop ambient fadeout 2
    jump scene_0023
label scene_0023:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0023.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school ext 1
    show nicole sc3:
        leftcenterstage

    show jecka sc3:
        rightcenterstage
    $ setWait(0.038,2.499)
    $ speak(NICOLE, "Really thought I'd seen it all here.")
    $ setWait(2.499,4.835)
    $ speak(JECKA, "I don't wanna think about sex for the rest of the month.")
    $ setWait(4.835,6.294)
    $ speak(NICOLE, "No yeah for sure.")
    $ setWait(6.294,8.213)
    $ speak(JECKA, "God, imagine being those girls.")
    $ setWait(8.213,11.842)
    $ speak(NICOLE, "For a week it'd be kinda fun. You wanna be sexed up abusive lesbians?")
    show jecka sc3 angry:
        rightcenterstage
    $ setWait(11.842,12.843)
    $ speak(JECKA, "Fuck no.")
    $ setWait(12.843,13.385)
    $ speak(NICOLE, "Why not?")
    $ setWait(13.385,15.178)
    $ speak(JECKA, "Cause you'd be doing all the abusing.")
    $ setWait(15.178,16.137)
    $ speak(NICOLE, "Oh like what?")
    $ setWait(16.137,21.643)
    $ speak(JECKA, "Just weird shit.\nYou'd like... Put a cigarette out on my neck and lick the burn mark.")
    $ setWait(21.643,22.686)
    $ speak(NICOLE, "...So you wanna try it?")
    $ setWait(22.686,23.311)
    $ speak(JECKA, "No!")
    $ setWait(23.311,26.565)
    $ speak(NICOLE, "Fine whatever. But you never told me that Ari girl was so ghetto.")
    $ setWait(26.565,29.401)
    $ speak(JECKA, "Ari's not fucking ghetto she's like the whitest girl I ever met.")
    $ setWait(29.401,30.527)
    $ speak(NICOLE, "She had a knife on her.")
    $ setWait(30.527,33.071)
    $ speak(JECKA, "Cause she was a girl scout, it's just a pocket knife.")
    $ setWait(33.071,34.781)
    $ speak(NICOLE, "They don't have pocket knives in the ghetto?")
    show jecka sc3:
        rightcenterstage
    $ setWait(34.781,38.243)
    $ speak(JECKA, "Nicole, trust me, she's kiss-her-brother-on-the-lips white.")
    show counselor 1 smile:
        off_right
        linear 1 rightstage

    show jecka sc3:
        rightcenterstage
        pause 0.5
        xzoom -1
    $ setWait(38.243,42.455)
    $ speak(COUNSELOR, "Hello girls, we're not talking about kissing, are we?")
    $ setWait(42.455,43.623)
    $ speak(NICOLE, "Uh no.")
    $ setWait(43.623,47.335)
    $ speak(COUNSELOR, "It's alright, I'm your counselor. You can trust me with anything.")
    $ setWait(47.335,49.921)
    $ speak(JECKA, "No I was just telling her how white some girl is.")
    show counselor 1:
        rightstage
        linear 2.4 rightmidstage
    $ setWait(49.921,57.095)
    $ speak(COUNSELOR, "Now now, that sounds like it might be name calling. You remember our bullying assembly last year, correct?")
    $ setWait(57.095,60.181)
    $ speak(NICOLE, "Why are you, um... here?")
    $ setWait(60.181,67.564)
    $ speak(COUNSELOR, "I was informed that you both attended the sexual addiction rehab meeting yesterday and just wanted to follow up with you.")
    $ setWait(67.564,70.025)
    $ speak(JECKA, "Oh no it wasn't that deep we just flirted with a cop.")
    show counselor 1 smile:
        rightmidstage
    $ setWait(70.025,72.11)
    $ speak(COUNSELOR, "How deep was it then?")
    show counselor 1:
        rightmidstage
    $ setWait(72.11,74.237)
    $ speak(NICOLE, "You really get paid to fuckin' work here, don't you?")
    $ setWait(74.237,82.037)
    $ speak(COUNSELOR, "I'm certainly sensing a lot of hormonal tension from the two of you. As always, if you'd like to explore these urges...")
    show counselor 1 smile:
        rightmidstage
        xzoom -1
        linear 3 off_right
    $ setWait(82.037,85.665)
    $ speak(COUNSELOR, "...my office is right around the corner.")
    show jecka sc3 angry:
        xzoom 1
        rightcenterstage
    $ setWait(85.665,87.876)
    $ speak(JECKA, "What the fuck is that supposed to mean?")
    $ setWait(87.876,89.252)
    $ speak(NICOLE, "Teachers are broke, right?")
    show jecka sc3:
        rightcenterstage
    $ setWait(89.252,90.837)
    $ speak(JECKA, "I think so, why?")
    $ setWait(90.837,94.841)
    $ speak(NICOLE, "If he has a part time job as a mall cop we could really use this to our advantage.")
    show jecka sc3 angry:
        rightcenterstage
    $ setWait(94.841,96.718)
    $ speak(JECKA, "No way I'm ever doing that again!")
    $ setWait(96.718,100.221)
    $ speak(NICOLE, "What if he had a part time job as security for an MSI concert.")
    show jecka sc3 smile:
        rightcenterstage
    $ setWait(100.221,102.724)
    $ speak(JECKA, "I'd practice flirting in the mirror to get in for free.")
    $ setWait(102.724,104.225)
    $ speak(NICOLE, "Are there no limits with you?")
    show jecka sc3 angry:
        rightcenterstage
    $ setWait(104.225,106.811)
    $ speak(JECKA, "Bitch you have no limits you wanna put a cigarette out on my neck.")
    show nicole sc3 angry:
        leftcenterstage
    $ setWait(106.811,108.021)
    $ speak(NICOLE, "Oh whatever.")
    show jecka sc3:
        rightcenterstage
    $ setWait(108.021,111.691)
    $ speak(JECKA, "So are you going to class this time or what are you doing?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0024:
    $ setVoiceTrack("audio/Scenes/0024.mp3")
    scene mall int 2

    show mallcop:
        rightmidstage

    show jecka sc1:
        xzoom -1
        leftcenterstage

    show nicole sc1 angry:
        leftmidstage
        xzoom -1
        linear 0.4 off_left

    $ setWait(0.038,0.747)
    $ speak(NICOLE, "Come on!!")
    show jecka sc1 surprised:
        xzoom 1
        leftcenterstage
    $ setWait(0.747,1.248)
    $ speak(JECKA, "What!? But--")
    show mallcop:
        rightmidstage
        linear 0.5 off_left
    $ setWait(1.248,2.541)
    $ speak(MALLCOP, "We have a runner! Freeze!!")

    show white onlayer screens:
        alpha 1.0
        linear 0.1 alpha 0.0
        pause 0.1
        alpha 1.0
        linear 0.1 alpha 0.0
        pause 0.3
        alpha 1.0
        linear 0.1 alpha 0.0
        pause 0.4
        alpha 1.0
        linear 0.1 alpha 0.0
        pause 0.5
        alpha 1.0
        linear 0.1 alpha 0.0


    $ setWait(2.541,4.376)
    $ speak(JECKA, "Ahhhh what the fuck!!!")
    $ setWait(4.376,7.003)
    $ speak(NICOLE, "Ugh- Ahh! God dammit!")
    show jecka sc1 worried:
        leftcenterstage
        linear 0.8 off_left
    $ setWait(7.003,8.839)
    $ speak(JECKA, "Oh my god, oh my god, no!")
    play ambient "audio/Ambience/ParkingGarage_Ambience.mp3"
    $ csbox = True
    show cut0024_1
    $ setWait(8.839,11.8)
    $ speak(NICOLE, "He actually fucking shot me! What the fuck is wrong with you!?")
    $ setWait(11.8,14.761)
    $ speak(MALLCOP, "Maybe now you'll think twice about breaking the law.")
    show cut0024_2
    $ setWait(14.761,18.014)
    $ speak(JECKA, "You shot five bullets so she'll think twice next time??")
    show cut0024_3
    $ setWait(18.014,23.311)
    $ speak(MALLCOP, "Yeah it could've been less but I fired with my eyes closed. Little inside-challenge down at the precinct.")
    $ setWait(23.311,23.729)
    $ speak(NICOLE, "What!?")
    $ setWait(23.729,25.814)
    $ speak(JECKA, "Are you actually fucking insane!?")
    $ setWait(25.814,27.941)
    $ speak(MALLCOP, "Y'know you remind of my wife a bit.")
    show cut0024_4
    $ setWait(27.941,30.068)
    $ speak(MALLCOP, "I wanna fucking kill my wife!!")
    show cut0024_5
    $ setWait(30.068,31.111)
    $ speak(JECKA, "Oh my god-- what!?")
    $ setWait(31.111,35.449)
    $ speak(MALLCOP, "Shut your mouth before I blow your fucking brains out on the tiled floor!!")
    $ setWait(35.449,38.535)
    $ speak(JECKA, "No! No! Please don't I'm sorry!")
    show cut0024_6
    $ setWait(38.535,43.299)
    $ speak(MALLCOP, "Now that's more like it! I'll call you girls an ambulance, one sec.")
    stop ambient fadeout 1.4
    jump scene_0025
label scene_0025:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show title_twoweekslater onlayer screens
    show black
    $ csbox = False
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter
    $ setVoiceTrack("audio/Scenes/0025.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3"
    hide title_twoweekslater onlayer screens
    scene school int 1
    show jecka sc3:
        centerstage
        xzoom -1

    show megan sc2 smile:
        rightmidstage
    $ setWait(2.007,5.051)
    $ speak(MEGAN, "But yeah do you wanna go to my party this Saturday?")
    $ setWait(5.051,10.432)
    $ speak(JECKA, "I don't know it's just kinda tricky for me lately like PTSD and everything.")
    $ setWait(10.432,12.851)
    $ speak(MEGAN, "One of the guys from All Time Low might be there.")
    show jecka sc3 angry:
        centerstage
        xzoom -1
    $ setWait(12.851,15.937)
    $ speak(JECKA, "I'm fucking all time low, I have therapy twice a day now.")
    show megan sc2:
        rightmidstage
    $ setWait(15.937,17.23)
    $ speak(MEGAN, "What happened?")
    $ setWait(17.23,20.484)
    $ speak(JECKA, "You don't remember the news two weeks ago?")
    $ setWait(20.484,24.863)
    $ speak(MEGAN, "Oh was that um... No I don't.")
    show jecka sc3:
        centerstage
        xzoom -1
    $ setWait(24.863,25.906)
    $ speak(JECKA, "Well I'll see ya later.")

    show megan sc2:
        rightmidstage
        pause 0.7
        xzoom -1
        linear 2 off_right

    $ setWait(25.906,29.618)
    $ speak(MEGAN, "Yeah totally, just RSVP by Thursday so we know.")
    $ setWait(29.618,31.536)
    $ speak(JECKA, "...What a fucking bitch.")
    show nicole sc3:
        off_left
        linear 1.6 leftmidstage
    $ setWait(31.536,32.204)
    $ speak(NICOLE, "Hey.")
    show jecka sc3 surprised:
        xzoom 1
        centerstage
        linear 0.4 leftcenterstage
    $ setWait(32.204,33.997)
    $ speak(JECKA, "Oh my god, you're out?")
    $ setWait(33.997,37.167)
    $ speak(NICOLE, "Yeah they cleared me last week but I didn't feel like going to school.")
    show jecka sc3:
        leftcenterstage
    $ setWait(37.167,40.462)
    $ speak(JECKA, "You didn't feel like answering your texts either. I thought you were dying.")
    $ setWait(40.462,44.132)
    $ speak(NICOLE, "Well yeah I was emotionally. I'm always dying emotionally.")
    $ setWait(44.132,48.345)
    $ speak(JECKA, "Yeah I'm in therapy twice a day, shit was wild. So what happened with your leg?")
    $ setWait(48.345,53.35)
    $ speak(NICOLE, "Oh yeah so they said the bullet went deep into my thigh and almost hit an artery.")
    $ setWait(53.35,57.437)
    $ speak(JECKA, "But they got it out, right? The surgery went well?")
    $ setWait(57.437,60.19)
    $ speak(NICOLE, "I mean I'm walking, as well as it could go.")
    $ setWait(60.19,60.982)
    $ speak(JECKA, "What?")
    show nicole sc3 sad:
        leftmidstage
    $ setWait(60.982,66.446)
    $ speak(NICOLE, "I don't know, when they were putting me under I was so afraid they were gonna like violate me or something.")
    show jecka sc3 angry:
        leftcenterstage
    $ setWait(66.446,68.657)
    $ speak(JECKA, "They're doctors, Nicole, they're not gonna do that.")
    show nicole sc3:
        leftmidstage
    $ setWait(68.657,73.495)
    $ speak(NICOLE, "Okay well that's what they said about teachers, parents, and police so who the fuck can we trust anymore?")
    show jecka sc3:
        leftcenterstage
    $ setWait(73.495,74.371)
    $ speak(JECKA, "Oh god...")
    $ setWait(74.371,76.665)
    $ speak(NICOLE, "By the way do you know what happened with that cop?")
    $ setWait(76.665,79.751)
    $ speak(JECKA, "My Dad heard they gave the cop paid leave or something?")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(79.751,83.129)
    $ speak(NICOLE, "What the fuck, being a cop has to be the most cathartic job in the world.")
    $ setWait(83.129,83.797)
    $ speak(JECKA, "Really?")
    show nicole sc3:
        leftmidstage
    $ setWait(83.797,92.013)
    $ speak(NICOLE, "Think about it. You're some loser with a gun and your wife doesn't wanna fuck you so go out, shoot a teenager, and get a paid trip to Bermuda.")
    $ setWait(92.013,93.765)
    $ speak(JECKA, "That sounds kinda good actually.")
    $ setWait(93.765,95.267)
    $ speak(NICOLE, "You gonna join the academy?")
    $ setWait(95.267,102.107)
    $ speak(JECKA, "Why would I? I'll never be in a situation where my spouse doesn't wanna fuck me cause I'm a perfect 10 with a high libido.")
    show nicole sc3 surprised:
        leftmidstage
    $ setWait(102.107,103.733)
    $ speak(NICOLE, "...How many times a day you say you go to therapy?")
    show mallcop:
        off_right
        linear 2.2 rightcenterstage
    $ setWait(103.733,106.152)
    $ speak(MALLCOP, "Hello girls, are we staying out of trouble here?")
    show nicole sc3 surprised:
        leftmidstage
        pause 0.1
        linear 0.3 leftstage

    show jecka sc3 surprised:
        leftcenterstage
        xzoom -1
        linear 0.4 leftmidstage
    $ setWait(106.152,106.695)
    $ speak(NICOLE_JECKA, "Whoa!")
    show nicole sc3 sad:
        leftstage
    $ setWait(106.695,108.697)
    $ speak(NICOLE, "What are you doing here?")
    $ setWait(108.697,114.995)
    $ speak(MALLCOP, "After our little skirmish at the mall the county reassigned me to patrol this school to pay my debt to the youth.")
    $ setWait(114.995,117.122)
    $ speak(MALLCOP, "So let's stay in school this time, huh?")
    show jecka sc3 worried:
        leftmidstage
        xzoom -1
    $ setWait(117.122,118.54)
    $ speak(JECKA, "Y-yes, sir...")
    show nicole sc3:
        leftstage
    $ setWait(118.54,119.624)
    $ speak(NICOLE, "Okay bye, dude.")
    $ setWait(119.624,124.713)
    $ speak(MALLCOP, "Sure but one more thing. If either one of you get in any trouble...")
    show mallcop:
        rightcenterstage
        linear 3.2 leftcenterstage

    show jecka sc3 worried:
        xzoom -1
        leftmidstage
        pause 2.4
        linear 0.05 xalign 0.12
        linear 0.1 xalign 0.16
        linear 0.07 xalign 0.13
        linear 0.05 leftmidstage

    $ setWait(124.713,128.884)
    $ speak(MALLCOP, "I will not hesitate to fucking murder you.")
    show mallcop:
        leftcenterstage
        xzoom -1
        linear 3 off_right

    show nicole sc3 sad:
        leftstage
    $ setWait(128.884,130.468)
    $ speak(MALLCOP, "Have fun in school, you girls.")
    show nicole sc3:
        leftstage
    $ setWait(130.468,132.095)
    $ speak(NICOLE, "Yeah sure thing.")
    show jecka sc3 worried:
        leftmidstage
        xzoom -1
        linear 1 leftcenterstage
        xzoom 1
    $ setWait(132.095,134.306)
    $ speak(JECKA, "Wh-Why-Why did they send him here??")
    show nicole sc3:
        leftstage
        linear 0.7 leftmidstage
    $ setWait(134.306,136.349)
    $ speak(NICOLE, "Dude you didn't even get shot, calm down.")
    $ setWait(136.349,140.02)
    $ speak(JECKA, "He said he was gonna... blow my brains out, Nicole...")
    $ setWait(140.02,141.605)
    $ speak(NICOLE, "Oh my god you're such a poser.")
    $ setWait(141.605,145.233)
    $ speak(JECKA, "What the fuck am I supposed to do? We can't all be sociopaths like you, Nicole!")
    $ setWait(145.233,146.401)
    $ speak(NICOLE, "You'll get there.")
    $ setWait(146.401,149.696)
    $ speak(JECKA, "So why are you here, you gonna skip again or what?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0026:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0026.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 1
    show jecka sc1:
        off_left
        xzoom -1
        linear 2.5 rightcenterstage
        xzoom 1

    show nicole sc1:
        off_farleft
        linear 2.8 leftcenterstage

    $ setWait(0.087,2.256)
    $ speak(JECKA, "There's no way he actually fell for that.")
    $ setWait(2.256,4.425)
    $ speak(NICOLE, "Why would he say that if he didn't?")
    show jecka sc1 worried:
        rightcenterstage
    $ setWait(4.425,9.68)
    $ speak(JECKA, "What if he's trying to trick us into trying it on someone else. There were no witnesses, he could totally do that.")
    $ setWait(9.68,13.434)
    $ speak(NICOLE, "Or what if he's just actually a pedophile and wanted an excuse to say it?")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(13.434,15.061)
    $ speak(JECKA, "So you don't think he fell for it either?")
    $ setWait(15.061,18.939)
    $ speak(NICOLE, "No I'm just saying that's a more likely possibility if he didn't fall for it.")
    $ setWait(18.939,20.274)
    $ speak(JECKA, "How is that more likely?")
    $ setWait(20.274,25.488)
    $ speak(NICOLE, "Think about it, why would a man wanna be a public school teacher other than to have sex with the kids?")
    $ setWait(25.488,27.948)
    $ speak(JECKA, "Th...That makes no sense.")
    $ setWait(27.948,34.497)
    $ speak(NICOLE, "Okay if you're a man, right? You have way more job options, less annoying jobs, but teaching pays like total shit.")
    show jecka sc1:
        rightcenterstage
    $ setWait(34.497,35.331)
    $ speak(JECKA, "Yeah?")
    $ setWait(35.331,41.837)
    $ speak(NICOLE, "So why would a guy go to college for one of the worst paying jobs, and one of the only jobs where a man can be around minors 5 days a week?")
    $ setWait(41.837,43.339)
    $ speak(JECKA, "Cause they like teaching?")
    $ setWait(43.339,46.133)
    $ speak(NICOLE, "Then why not a university where they actually pay?")
    $ setWait(46.133,50.096)
    $ speak(JECKA, "I don't know? Not all male teachers are ugly it's not like they don't have options.")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(50.096,57.186)
    $ speak(NICOLE, "Exactly!\nSex with a regular bitch won't do it for 'em cause they want don't-tell-your-parents ass. It's totally fucked up, I know.")
    show jecka sc1 worried:
        rightcenterstage
    $ setWait(57.186,60.189)
    $ speak(JECKA, "...Nicole you need SSRIs really badly.")
    show nicole sc1 surprised:
        leftcenterstage
        pause 0.4
        xzoom -1

    show jecka sc1 surprised:
        rightcenterstage
    $ setWait(60.189,61.232)
    $ speak(LYNN, "What're you two doing??")
    show nicole sc1 angry:
        leftcenterstage
        xzoom -1
        pause 0.8
        xzoom 1
        linear .7 off_right

    show jecka sc1 worried:
        rightcenterstage
        pause 1
        xzoom -1
        linear 0.8 off_right

    $ setWait(61.232,63.776)
    $ speak(NICOLE, "Shit, run.")
    show lynn 1:
        off_left
        xzoom -1
        linear 1 leftmidstage
    $ setWait(63.776,68.364)
    $ speak(LYNN, "I go out to check on one staff complaint and of course I see students skipping...")
    stop ambient fadeout 1.3
    jump scene_0027
label scene_0027:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0027.mp3")
    play ambient "audio/Ambience/Bathroom_Lockerroom_Ambience.mp3" fadein 1
    scene bathroom
    show nicole sc1 sad:
        off_right
        xzoom -1
        linear 3 leftmidstage
        xzoom 1

    show jecka sc1 worried:
        off_right
        pause 0.4
        linear 2.6 leftcenterstage

    $ setWait(0.087,1.713)
    $ speak(NICOLE, "I think we're safe.")
    $ setWait(1.713,4.591)
    $ speak(JECKA, "Safe? Everyone skips here, they're gonna find us.")
    show nicole sc1:
        leftmidstage
    $ setWait(4.591,7.928)
    $ speak(NICOLE, "Everyone does not skip here. This particular girls bathroom?")
    show jecka sc1:
        leftcenterstage
    $ setWait(7.928,10.973)
    $ speak(JECKA, "Yeah cause it's right next to the vending machines and emergency exit.")
    $ setWait(10.973,14.977)
    $ speak(NICOLE, "It'll be fine, okay?\nSo what's this about me needing SSRIs?")
    show jecka sc1 worried:
        leftcenterstage
    $ setWait(14.977,18.438)
    $ speak(JECKA, "Like you're cool and everything but you're just like.. fucked up.")
    show emily sc1 smile:
        off_right
        linear 2.3 leftcenterstage

    show kelly sc1:
        off_right
        pause 0.4
        linear 2.1 rightcenterstage

    show nicole sc1:
        leftmidstage
        pause 1.8
        linear 0.5 leftstage

    show jecka sc1:
        leftcenterstage
        pause 1.5
        xzoom -1
        linear 0.6 leftmidstage
    $ setWait(18.438,19.439)
    $ speak(EMILY, "Ooh drama.")
    $ setWait(19.439,20.774)
    $ speak(KELLY, "I never knew you guys were dating.")
    show nicole sc1 surprised:
        leftstage
    $ setWait(20.774,21.316)
    $ speak(NICOLE, "What??")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1
    $ setWait(21.316,22.776)
    $ speak(JECKA, "No it was something else.")
    show nicole sc1:
        leftstage

    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(22.776,24.236)
    $ speak(NICOLE, "What're you guys doing here?")
    $ setWait(24.236,25.237)
    $ speak(KELLY, "Skipping?")
    show nicole sc1 angry:
        leftstage
    $ setWait(25.237,25.988)
    $ speak(NICOLE, "God dammit.")
    show jecka sc1 angry:
        leftmidstage
        xzoom 1
    $ setWait(25.988,26.822)
    $ speak(JECKA, "Told you.")
    show jecka sc1:
        leftmidstage
        pause 0.2
        xzoom -1

    show nicole sc1:
        leftstage

    $ setWait(26.822,30.325)
    $ speak(NICOLE, "Maybe you guys could settle a debate for us, are all male teachers pedophiles?")
    show emily sc1 angry:
        leftcenterstage
    $ setWait(30.325,32.369)
    $ speak(EMILY, "Here? 100 percent yes.")
    $ setWait(32.369,33.495)
    $ speak(KELLY, "All of them? No way.")
    $ setWait(33.495,36.039)
    $ speak(NICOLE, "Kelly you've never been hit on by a male teacher?")
    $ setWait(36.039,36.915)
    $ speak(KELLY, "Not really.")
    show emily sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(36.915,40.252)
    $ speak(EMILY, "You totally have Kelly, you're just too dumb to notice it.")
    show kelly sc1 angry:
        rightcenterstage
    $ setWait(40.252,40.961)
    $ speak(KELLY, "Bullshit.")
    $ setWait(40.961,45.799)
    $ speak(EMILY, "Remember when you wore a low cut shirt and the teacher stood over your shoulder for every single math problem?")
    $ setWait(45.799,47.217)
    $ speak(KELLY, "He was just being helpful!")
    $ setWait(47.217,51.054)
    $ speak(EMILY, "Yeah then I raised my hand in a sweater, did he come over? No.")
    $ setWait(51.054,51.763)
    $ speak(NICOLE, "See?")
    show jecka sc1:
        leftmidstage
        xzoom 1
    $ setWait(51.763,55.267)
    $ speak(JECKA, "I never said you were wrong I just think you're insane for having a blueprint on it.")
    show emily sc1:
        leftcenterstage
        xzoom 1

    show kelly sc1:
        rightcenterstage

    show jecka sc1:
        leftmidstage
        xzoom 1
        pause 0.4
        xzoom -1

    $ setWait(55.267,56.894)
    $ speak(EMILY, "So you guys wanna buy some addys?")
    show megan sc1:
        off_right
        linear 1 rightmidstage

    show ari sc1:
        off_right
        pause 0.5
        linear 0.8 rightstage

    show emily sc1:
        leftcenterstage
        xzoom 1
        pause 0.6
        xzoom -1

    show kelly sc1:
        rightcenterstage
        xzoom 1
        pause 0.4
        xzoom -1
    $ setWait(56.894,57.603)
    $ speak(MEGAN, "Are you serious?")
    $ setWait(57.603,59.521)
    $ speak(ARI, "I told you the other bathroom's better.")
    $ setWait(59.521,61.064)
    $ speak(KELLY, "Are you guys here to buy adderall?")
    $ setWait(61.064,62.774)
    $ speak(ARI, "No we're just getting out of a quiz.")
    show emily sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(62.774,63.942)
    $ speak(EMILY, "Then get the hell out.")
    $ setWait(63.942,66.445)
    $ speak(MEGAN, "Tell that to the other girls, they don't have a quiz to skip.")
    show nicole sc1 angry:
        leftstage

    $ setWait(66.445,67.529)
    $ speak(NICOLE, "We were here first!")
    $ setWait(67.529,70.073)
    $ speak(JECKA, "Yeah and you guys probably won't even buy addys or anything.")
    show emily sc1 upset:
        leftcenterstage
        xzoom 1

    $ setWait(70.073,71.241)
    $ speak(EMILY, "Are you?")
    $ setWait(71.241,73.493)
    $ speak(JECKA, "Well no but I know they won't either.")
    show emily sc1 yell:
        leftcenterstage
        xzoom -1
    $ setWait(73.493,76.079)
    $ speak(EMILY, "Is anyone here actually gonna buy addys!?")
    show nicole sc1:
        leftstage
    $ setWait(76.079,77.539)
    $ speak(NICOLE, "Let 'em all know we're here.")
    $ setWait(77.539,78.457)
    $ speak(ARI, "How much?")
    show emily sc1 smile:
        leftcenterstage
        xzoom -1
    $ setWait(78.457,79.291)
    $ speak(EMILY, "12 a bean.")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1
    $ setWait(79.291,80.334)
    $ speak(JECKA, "12 a pill??")
    show emily sc1 upset:
        leftcenterstage
        xzoom 1
    $ setWait(80.334,82.586)
    $ speak(EMILY, "Supply and demand, Cravin' Symone.")
    show jecka sc1 angry:
        leftmidstage
        xzoom 1
    $ setWait(82.586,84.338)
    $ speak(JECKA, "We gotta pick a new hiding spot.")
    stop ambient fadeout 3
    menu:
        "HIDE IN PHOTO LAB":
            jump scene_0028
        "HANG IN THE COURTYARD":
            jump scene_0035
label scene_0028:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0028.mp3")
    play ambient "audio/Ambience/Darkroom_Ambience.mp3" fadein 1
    scene dark room
    show nicole sc1 smile:
        leftcenterstage

    show jecka sc1:
        rightcenterstage
    $ setWait(0.042,1.502)
    $ speak(NICOLE, "This is way better.")
    $ setWait(1.502,3.003)
    $ speak(JECKA, "Why didn't you think of this first?")
    show nicole sc1:
        leftcenterstage
    $ setWait(3.003,5.297)
    $ speak(NICOLE, "I don't know it gets kinda scary in here after a while.")
    $ setWait(5.297,8.175)
    $ speak(JECKA, "You'll do a fat line of anything but you're afraid of the dark.")
    $ setWait(8.175,11.804)
    $ speak(NICOLE, "No it's not the dark it's just really red in here. I feel like the hos in Amsterdam.")
    $ setWait(11.804,14.765)
    $ speak(JECKA, "You're gonna be a ho in Amsterdam if you keep skipping everyday.")
    show karen sc1:
        off_right
        linear 1 rightstage
    $ setWait(14.765,18.06)
    $ speak(KAREN, "Hey... what're you guys doing in here?")
    show jecka sc1 surprised:
        rightcenterstage
        xzoom -1

    show nicole sc1 surprised:
        leftcenterstage
    $ setWait(18.06,18.602)
    $ speak(JECKA, "Uh oh.")
    show nicole sc1:
        leftcenterstage

    $ setWait(18.602,21.98)
    $ speak(NICOLE, "We were just um... developing pictures.")
    $ setWait(21.98,23.941)
    $ speak(KAREN, "But you're not even in this period.")
    show jecka sc1:
        rightcenterstage
        xzoom -1
    $ setWait(23.941,27.236)
    $ speak(NICOLE, "Okay well... I lied, I don't know what you wanna hear, dude.")
    show karen sc1 angry:
        rightstage
        linear 2 rightmidstage
    $ setWait(27.236,32.282)
    $ speak(KAREN, "You're not using the darkroom to skip, are you? Some of us actually use this place for academics.")
    $ setWait(32.282,36.87)
    $ speak(NICOLE, "Academics. You think a black and white picture of you holding a leaf is gonna wow Georgetown?")
    $ setWait(36.87,40.624)
    $ speak(KAREN, "Extracurricular activities make you look really good on college applications!")
    $ setWait(40.624,43.293)
    $ speak(NICOLE, "Do you see how you dress? You wouldn't look good on anything.")
    $ setWait(43.293,47.881)
    $ speak(KAREN, "I'm not putting up with this! I'm gonna get the principal and you guys are gonna be expelled for good!")
    show jecka sc1 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(47.881,48.841)
    $ speak(JECKA, "Oh shit...")
    menu:
        "MANIPULATE HER":
            jump scene_0029
        "GIVE HER AN\nEATING DISORDER":
            jump scene_0032
label scene_0029:
    $ setVoiceTrack("audio/Scenes/0029.mp3")
    scene dark room
    show nicole sc1 sad:
        leftcenterstage

    show jecka sc1:
        rightcenterstage
        xzoom -1

    show karen sc1 angry:
        rightmidstage
    $ setWait(0.005,2.007)
    $ speak(NICOLE, "N-no, come on wait!")
    $ setWait(2.007,3.467)
    $ speak(KAREN, "Why should I?")
    show nicole sc1:
        leftcenterstage
    $ setWait(3.467,7.095)
    $ speak(NICOLE, "Cause we... wanted to talk about Twilight?")
    $ setWait(7.095,9.014)
    $ speak(KAREN, "What about Twilight?")
    $ setWait(9.014,12.601)
    $ speak(NICOLE, "What's your opinion on... how to read it...")
    show karen sc1 angry:
        rightmidstage
        pause 1
        xzoom -1
        linear 0.4 rightstage
    $ setWait(12.601,13.935)
    $ speak(KAREN, "Okay where's the principal--")
    show jecka sc1 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(13.935,21.777)
    $ speak(JECKA, "No Karen! What she meant to ask was if you like your favorite Twilight character more than Ron.")
    show karen sc1:
        rightstage
        xzoom 1

    show jecka sc1:
        rightcenterstage
        xzoom -1
    $ setWait(21.777,28.825)
    $ speak(KAREN, "Uh... Well Ron from the Potter books will always be my favorite, but Edward is a pretty close second.")
    $ setWait(28.825,32.371)
    $ speak(JECKA, "And-- you're gonna see the Twilight movie when it comes out?")
    $ setWait(32.371,34.289)
    $ speak(KAREN, "Well yeah I read all the books.")
    show jecka sc1 smile:
        rightcenterstage
        xzoom -1
    $ setWait(34.289,38.043)
    $ speak(JECKA, "At the place in Centerville, right? Cause there's less people.")
    show karen sc1:
        rightstage
        linear 2 rightmidstage
    $ setWait(38.043,42.714)
    $ speak(KAREN, "Yeah, I know it's run down but I'd rather the movie be empty so I can watch it in peace.")
    $ setWait(42.714,44.8)
    $ speak(JECKA, "Will the ticket stub go on your wall?")
    $ setWait(44.8,50.764)
    $ speak(KAREN, "For sure, it's such a big movie. I actually took some of the ticket stubs down for a collage I'm working on right now.")
    $ setWait(50.764,53.6)
    $ speak(JECKA, "Do you need any help? Me and Nicole could help.")
    $ setWait(53.6,54.518)
    $ speak(NICOLE, "Help you fuck off--")
    show jecka sc1 angry:
        rightcenterstage
        xzoom 1
    $ setWait(54.518,55.143)
    $ speak(JECKA, "Shhh!!")
    show jecka sc1 smile:
        rightcenterstage
        xzoom -1
    $ setWait(55.143,58.105)
    $ speak(KAREN, "Uh, yeah the glue can be tricky.")
    show karen sc1 smile:
        rightmidstage
        xzoom -1
        linear 2.2 off_right

    $ setWait(58.105,59.773)
    $ speak(KAREN, "I have it on a table out here.")
    $ setWait(59.773,62.484)
    $ speak(JECKA, "Cool yeah we'll be right there in a sec.")
    show nicole sc1 angry:
        leftcenterstage
    $ setWait(62.484,64.277)
    $ speak(NICOLE, "...How the fuck did you know all that?")
    show jecka sc1:
        rightcenterstage
        xzoom 1
    $ setWait(64.277,66.154)
    $ speak(JECKA, "We were friends in like 6th grade.")
    show nicole sc1:
        leftcenterstage
    $ setWait(66.154,71.535)
    $ speak(NICOLE, "Ohhh socially obsolete. You made the upgrade and left her ass in the dust.")
    $ setWait(71.535,73.078)
    $ speak(JECKA, "It's not like I was trying to.")
    $ setWait(73.078,74.371)
    $ speak(NICOLE, "Yeah what's the story?")
    $ setWait(74.371,77.165)
    $ speak(JECKA, "I tried bringing her to lunch in middle school and...")
    show jecka sc1 worried:
        rightcenterstage
    $ setWait(77.165,80.502)
    $ speak(JECKA, "She brought up Harry Potter while we're talking about the Paris Hilton sextape.")
    $ setWait(80.502,84.673)
    $ speak(NICOLE, "Oh that's a bad awkward. And she directs it at you cause she doesn't know anyone else?")
    show jecka sc1 angry:
        rightcenterstage
    $ setWait(84.673,87.717)
    $ speak(JECKA, "Yeah, so I looked like a fucking baby in front of the 8th graders.")
    $ setWait(87.717,90.887)
    $ speak(NICOLE, "Wow, traded loyalty in for the acceptance of 8th graders.")
    $ setWait(90.887,94.391)
    $ speak(JECKA, "Fuck the acceptance, they were gonna let me try their cigarettes if they thought I was cool.")
    $ setWait(94.391,97.769)
    $ speak(NICOLE, "So she nerded you out of free cigarettes? Yeah I'd hate her too, honestly.")
    show jecka sc1:
        rightcenterstage
    $ setWait(97.769,101.106)
    $ speak(JECKA, "I don't hate her it's just like, what do you do with her?")
    $ setWait(101.106,102.274)
    $ speak(NICOLE, "Ask her to hang out with you.")
    show jecka sc1 angry:
        rightcenterstage

    $ setWait(102.274,112.117)
    $ speak(JECKA, "No I can't, it's weird now. You walk in the cafeteria and see her reading at lunch alone, she's like a hallucination reminding me how much of a bitch I am. I only said all that shit so she'd forget about the principal.")
    $ setWait(112.117,120.375)
    $ speak(NICOLE, "Wow so you manipulated that poor book-reader with her own childhood. She was your bestie and you sold her up the river, you cold heartless bitch.")
    $ setWait(120.375,123.712)
    $ speak(JECKA, "Fuck off Nicole, you move every two years you don't have to deal with this shit!")
    $ setWait(123.712,127.924)
    $ speak(JECKA, "I'm just gonna graduate, go to college, smoke a shit ton of salvia, and forget about her.")
    show jecka sc1 surprised:
        rightcenterstage
        pause 0.3
        xzoom -1

    show karen sc1:
        off_right
        xzoom 1
        linear 1 rightstage
    $ setWait(127.924,130.969)
    $ speak(KAREN, "Hey was there a slowdown? What's the problem?")
    $ setWait(130.969,132.345)
    $ speak(NICOLE, "Too many to list.")
    stop ambient fadeout 1.2
    jump scene_0030
label scene_0030:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0030.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene photo classroom
    show karen sc1:
        centerstage

    show nicole sc1:
        leftmidstage

    show jecka sc1:
        rightmidstage

    $ setWait(0.045,3.507)
    $ speak(KAREN, "Sorry just sorting out the ticket stubs...")
    $ setWait(3.507,7.136)
    $ speak(NICOLE, "You said you only save them for the special movies, right?")
    $ setWait(7.136,7.97)
    $ speak(KAREN, "Yeah.")
    $ setWait(7.97,10.806)
    $ speak(NICOLE, "Why do you have the ticket stub for Balls Of Fury?")
    $ setWait(10.806,13.559)
    $ speak(JECKA, "Is that the ping pong movie with the fat guy from Lost?")
    $ setWait(13.559,17.188)
    $ speak(NICOLE, "I guess. Here put it next to the Star Wars one, they're basically the same movie.")
    show karen sc1 smile:
        centerstage
        xzoom -1
    $ setWait(17.188,18.981)
    $ speak(KAREN, "Thanks again for the help.")
    $ setWait(18.981,20.149)
    $ speak(JECKA, "Yeah no problem.")
    $ setWait(20.149,22.651)
    $ speak(NICOLE, "So anyway, did you hear about what happened with Kelly last week?")
    $ setWait(22.651,23.319)
    $ speak(JECKA, "No.")
    $ setWait(23.319,27.698)
    $ speak(NICOLE, "She was at a party and somebody walked in on her right as a guy skeeted on her face.")
    show jecka sc1 surprised:
        rightmidstage
    $ setWait(27.698,29.867)
    $ speak(JECKA, "What the hell? Why wouldn't she lock the door?")
    show nicole sc1 smile:
        leftmidstage

    $ setWait(29.867,31.535)
    $ speak(NICOLE, "I think she wants to get caught.")
    show jecka sc1 worried:
        rightmidstage
    $ setWait(31.535,34.246)
    $ speak(JECKA, "Uh, what do you think, Karen?")
    show karen sc1:
        centerstage
        xzoom -1
    $ setWait(34.246,35.915)
    $ speak(KAREN, "What's \"skeeted\"?")


    $ setWait(35.915,36.54)
    $ speak(JECKA, "Huh?")

    show nicole sc1:
        leftmidstage

    $ setWait(36.54,37.249)
    $ speak(NICOLE, "Huh.")
    $ setWait(37.249,40.211)
    $ speak(KAREN, "\"Skeeted on\"? What does that mean?")
    show jecka sc1:
        rightmidstage
    $ setWait(40.211,43.13)
    $ speak(JECKA, "Um... so it's like when a boy--")
    show nicole sc1 smile:
        leftmidstage
    $ setWait(43.13,46.008)
    $ speak(NICOLE, "Dude it's not that hard, it just means to compliment something.")
    $ setWait(46.008,47.092)
    $ speak(JECKA, "Excuse me?")
    show karen sc1:
        centerstage
        xzoom 1
    $ setWait(47.092,49.303)
    $ speak(KAREN, "Well why don't you just say compliment?")
    $ setWait(49.303,52.389)
    $ speak(NICOLE, "It's just slang. Skeet, skeeting skeeted on...")
    $ setWait(52.389,55.726)
    $ speak(KAREN, "Like how Jecka skeeted on my collage?")
    show jecka sc1 worried:
        rightmidstage

    $ setWait(55.726,56.268)
    $ speak(JECKA, "Oh my god.")
    $ setWait(56.268,59.939)
    $ speak(NICOLE, "Exactly, I'm skeeting all over your collage right now, it's awesome.")
    show karen sc1 smile:
        centerstage

    $ setWait(59.939,62.942)
    $ speak(KAREN, "Thanks, yeah it took so long to put together.")
    $ setWait(62.942,67.78)
    $ speak(NICOLE, "Yeah you're pretty cool. Hang out with me and Jecka more and guys are gonna be skeeting all over you.")
    $ setWait(67.78,70.324)
    $ speak(KAREN, "You really think guys would wanna skeet on me?")
    $ setWait(70.324,72.117)
    $ speak(NICOLE, "Yeah with your glasses on and everything.")
    $ setWait(72.117,73.702)
    $ speak(JECKA, "You're unbelievable...")
    show karen sc1:
        centerstage
        xzoom -1
    $ setWait(73.702,75.079)
    $ speak(KAREN, "What's wrong, Jecka?")
    show jecka sc1:
        rightmidstage
    $ setWait(75.079,78.791)
    $ speak(JECKA, "Oh! Um nothing just... nothing.")
    $ setWait(78.791,82.378)
    $ speak(KAREN, "By the way I like your outfit. Did anyone skeet on you today?")
    $ setWait(82.378,84.88)
    $ speak(JECKA, "No I'm pretty elusive.")
    $ setWait(84.88,90.177)
    $ speak(NICOLE, "She's just being humble, Karen. Jecka really likes it when 3 or 4 guys skeet on her at once.")
    $ setWait(90.177,94.306)
    $ speak(KAREN, "Wow that many? I've always thought you were really pretty so it makes sense.")
    $ setWait(94.306,95.099)
    $ speak(JECKA, "Thanks..")
    $ setWait(95.099,98.978)
    $ speak(NICOLE, "Yeah and she never wants it to stop, not until she's gagging on compliments--")
    show jecka sc1 angry:
        rightmidstage
    $ setWait(98.978,101.021)
    $ speak(JECKA, "Okay so me and Nicole need to go now but...")
    show jecka sc1 angry:
        rightmidstage
        linear 1.3 off_left

    show nicole sc1:
        leftmidstage
        pause 0.8
        xzoom -1
        linear 0.7 off_left
    $ setWait(101.021,102.648)
    $ speak(JECKA, "...good luck with your collage, Karen!")
    show karen sc1 smile:
        centerstage
        xzoom 1
    $ setWait(102.648,105.859)
    $ speak(KAREN, "No problem. I'll see you guys later sometime!")
    stop ambient fadeout 1.4
    jump scene_0031
label scene_0031:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0031.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school ext 5
    show coach 1 smile:
        rightmidstage

    show nicole sc3:
        leftcenterstage

    show jecka sc3:
        rightcenterstage
        xzoom -1

    $ setWait(0.124,7.298)
    $ speak(COACH, "Yeah so girls uh, if your Mom's are single you know who to let know. Y'know what I'm sayin'?")
    $ setWait(7.298,8.466)
    $ speak(JECKA, "My Mom's married?")
    $ setWait(8.466,10.092)
    $ speak(NICOLE, "Why do you wanna fuck our moms so bad?")
    $ setWait(10.092,13.429)
    $ speak(JECKA, "Yeah my Mom's the last person I wanna fuck, what the hell do you see in her?")
    show coach 1 worried:
        rightmidstage

    $ setWait(13.429,16.223)
    $ speak(COACH, "Whoa, whoa, girls! Why ya gotta go there?")
    $ setWait(16.223,20.603)
    $ speak(NICOLE, "If you don't go to the ATM and get each of us a hundred dollars we're gonna report you.")
    $ setWait(20.603,21.604)
    $ speak(COACH, "Dammit!")
    show coach 1 sad:
        rightmidstage
        xzoom -1
        linear 2 off_farright
    $ setWait(21.604,23.23)
    $ speak(COACH, "...Alright where's my car.")
    show jecka sc3:
        rightcenterstage
        xzoom -1
        pause 1.6
        xzoom 1
    $ setWait(23.23,25.733)
    $ speak(JECKA, "And we want it in fives! Y'know the purple five?")
    show nicole sc3 smile:
        leftcenterstage

    $ setWait(25.733,26.984)
    $ speak(NICOLE, "Oh I love the purple five.")
    show jecka sc3 smile:
        rightcenterstage
        xzoom -1
    $ setWait(26.984,29.403)
    $ speak(JECKA, "Yeah-- Purple fives, bitch!")
    show kylar sc1 smile:
        off_left
        xzoom -1
        linear 1 leftstage

    show karen sc2 smile:
        off_left
        xzoom -1
        linear 1.25 leftmidstage

    show nicole sc3:
        leftcenterstage
        pause 0.5
        xzoom -1

    show jecka sc3:
        rightcenterstage
        xzoom -1
        pause 0.4
        xzoom 1

    $ setWait(29.403,30.362)
    $ speak(KYLAR, "Who's a bitch?")
    $ setWait(30.362,31.906)
    $ speak(KAREN, "Hey guys, what's up?")
    $ setWait(31.906,33.157)
    $ speak(NICOLE, "Uh hey.")
    $ setWait(33.157,36.494)
    $ speak(JECKA, "Hi Karen... why's Kylar with you?")
    $ setWait(36.494,40.039)
    $ speak(KAREN, "Well we just spoke this morning and kinda hit it off.")
    $ setWait(40.039,41.874)
    $ speak(JECKA, "Really... Really?")
    $ setWait(41.874,44.001)
    $ speak(KAREN, "Yeah he's actually really nice!")
    $ setWait(44.001,48.756)
    $ speak(KAREN, "He told me he never skeeted on a girl with glasses before and wanted me to be his first.")
    show jecka sc3 angry:
        rightcenterstage

    $ setWait(48.756,49.882)
    $ speak(JECKA, "Did he now?")
    $ setWait(49.882,51.717)
    $ speak(KYLAR, "Yeah baller shot caller, dude.")
    $ setWait(51.717,57.139)
    $ speak(KAREN, "Then one thing led to another and we're hanging out this Friday. And it's all thanks to you, Nicole!")
    $ setWait(57.139,59.558)
    $ speak(NICOLE, "Aw don't mention it... to anyone.")
    $ setWait(59.558,66.315)
    $ speak(KAREN, "If you never taught me about that slang, me and Kylar would've never understood each other, let alone set something up.")
    $ setWait(66.315,68.484)
    $ speak(KAREN, "Or the other four guys hanging out with me this week.")
    show jecka sc3 surprised:
        rightcenterstage
    $ setWait(68.484,69.485)
    $ speak(JECKA, "Four guys??")
    $ setWait(69.485,74.198)
    $ speak(KAREN, "Yeah Nicole was right, I'm really popular now and all it took was one phrase.")
    show jecka sc3 worried:
        rightcenterstage

    $ setWait(74.198,76.242)
    $ speak(JECKA, "Y-you mean skeeting?")
    $ setWait(76.242,77.618)
    $ speak(KYLAR, "Damn right she means skeeting.")
    $ setWait(77.618,86.627)
    $ speak(KAREN, "One guy asked to do it at the movies, another guy at the football game. And then one guy was really surprised when I said he could skeet all over me in public.")
    $ setWait(86.627,87.294)
    $ speak(JECKA, "Uh...")
    $ setWait(87.294,89.046)
    $ speak(NICOLE, "Some guys are just shy, y'know.")
    $ setWait(89.046,94.385)
    $ speak(KAREN, "I used to be like that, but this really broke me out of my shell. Thanks guys I'll see you next week!")
    show karen sc2 smile:
        leftmidstage
        xzoom 1
        linear 1 off_farleft

    show kylar sc1 smile:
        leftstage
        pause 0.3
        xzoom 1
        linear 0.8 off_left

    $ setWait(94.385,96.512)
    $ speak(KYLAR, "Can I get it in your hair too?")
    $ setWait(96.512,98.764)
    $ speak(JECKA, "...Why are you Hitler?")
    show nicole sc3:
        leftcenterstage
        xzoom 1

    $ setWait(98.764,101.142)
    $ speak(NICOLE, "Is that a band or you're calling me Hitler?")
    show jecka sc3 angry:
        rightcenterstage
        xzoom 1
    $ setWait(101.142,106.73)
    $ speak(JECKA, "What the fuck is gonna happen when she goes out with these guys?\nYour little prank turned a nice Twilight girl into the school slut.")
    $ setWait(106.73,109.066)
    $ speak(NICOLE, "Relax, she'll probably run away when they whip it out.")
    $ setWait(109.066,114.989)
    $ speak(JECKA, "And what if she doesn't, Nicole?\nWhat if she fills her void of friendship with male attention?")
    $ setWait(114.989,117.616)
    $ speak(NICOLE, "...Are we talking about my Mom or Karen right now?")
    $ setWait(117.616,123.706)
    $ speak(JECKA, "Now when I look at her in lunch I'm just gonna think about guys plastering the fuck out of her.\nShe was my childhood, Nicole.")
    $ setWait(123.706,133.591)
    $ speak(NICOLE, "Hold on so... the idea of her getting sexually manipulated is less important than your ability to objectify her as a childhood memory.")
    show jecka sc3:
        rightcenterstage

    $ setWait(133.591,135.593)
    $ speak(JECKA, "...What's wrong with that?")
    $ setWait(135.593,137.845)
    $ speak(NICOLE, "Uh... I mean I don't care.")
    show jecka sc3 smile:
        rightcenterstage

    $ setWait(137.845,138.971)
    $ speak(JECKA, "You're a good friend.")
    $ setWait(138.971,140.472)
    $ speak(NICOLE, "I thought I was Hitler.")
    $ setWait(140.472,143.601)
    $ speak(JECKA, "You're a really pretty brunette Hitler with a drug problem.")
    show nicole sc3 smile:
        leftcenterstage

    $ setWait(143.601,146.645)
    $ speak(NICOLE, "See if guys came up with that I'd actually try dating them.")
    $ setWait(146.645,148.522)
    $ speak(JECKA, "Anyway, I gotta go to class.")
    show nicole sc3:
        leftcenterstage

    $ setWait(148.522,150.9)
    $ speak(NICOLE, "I gotta wait for Mr. Colby to come back with the money.")

    show jecka sc3:
        rightcenterstage

    $ setWait(150.9,154.57)
    $ speak(JECKA, "Oh! Well what're you doing after that?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0032:
    $ setVoiceTrack("audio/Scenes/0032.mp3")
    scene dark room
    show nicole sc1 smile:
        leftcenterstage

    show jecka sc1:
        rightcenterstage
        xzoom -1

    show karen sc1 angry:
        rightmidstage

    $ setWait(0.035,3.496)
    $ speak(NICOLE, "You gonna stop by every vending machine on the way?")
    show karen sc1 sad:
        rightmidstage

    $ setWait(3.496,4.581)
    $ speak(KAREN, "Wh-what?")
    $ setWait(4.581,8.293)
    $ speak(NICOLE, "Y'know to keep those love-handles plump. That's what you're going for, right?")
    $ setWait(8.293,10.754)
    $ speak(KAREN, "I-I don't have big love-handles.")
    $ setWait(10.754,12.422)
    $ speak(NICOLE, "Don't be ashamed, right Jecka?")
    show jecka sc1 smile:
        rightcenterstage
        xzoom 1
        pause 1.65
        xzoom -1

    $ setWait(12.422,16.009)
    $ speak(JECKA, "Uh yeah um, Lane Bryant wouldn't think they're big either.")
    $ setWait(16.009,18.136)
    $ speak(KAREN, "Wha- no? I gotta go to math now.")
    $ setWait(18.136,21.056)
    $ speak(NICOLE, "Math class, you doing good in math? A for the year?")
    $ setWait(21.056,22.599)
    $ speak(KAREN, "A plus actually.")
    $ setWait(22.599,24.059)
    $ speak(JECKA, "Is the plus for plus sized?")
    $ setWait(24.059,27.312)
    $ speak(NICOLE, "Yeah if you're so good at math why can't you count your calories?")
    $ setWait(27.312,28.98)
    $ speak(KAREN, "Is this really necessary?")
    $ setWait(28.98,31.233)
    $ speak(JECKA, "Is that extra cheese at Chipotle necessary?")
    $ setWait(31.233,32.817)
    $ speak(KAREN, "I don't get that every time.")
    $ setWait(32.817,37.572)
    $ speak(NICOLE, "Hey no we support it.\nLet's just hope the chairs at Red Lobster can support you too.")
    $ setWait(37.572,42.16)
    $ speak(JECKA, "It'd be so embarrassing for the chair to break on your first date with your black boyfriend.")
    $ setWait(42.16,44.579)
    $ speak(KAREN, "Black boyfriend? What the hell??")
    $ setWait(44.579,47.582)
    $ speak(JECKA, "Oh you don't like black guys? Cause I think they'll love you.")
    $ setWait(47.582,49.584)
    $ speak(NICOLE, "Wow, fat AND racist.")
    $ setWait(49.584,52.462)
    $ speak(JECKA, "So picky with men, at least you're not a picky eater.")
    show karen sc1 sad:
        rightmidstage
        xzoom -1
        linear 0.4 off_right

    $ setWait(52.462,54.714)
    $ speak(KAREN, "I'm not racist!!")
    show nicole sc1:
        leftcenterstage

    $ setWait(54.714,55.882)
    $ speak(NICOLE, "...Shit where'd she go?")
    show jecka sc1:
        rightcenterstage
        xzoom 1
    $ setWait(55.882,57.55)
    $ speak(JECKA, "Hopefully not the principal.")
    $ setWait(57.55,62.514)
    $ speak(NICOLE, "I feel like we just gave her more fuel--Yeah that might've entirely backfired.")
    $ setWait(62.514,65.183)
    $ speak(JECKA, "Yeah... God I'm so hungry after doing that.")
    $ setWait(65.183,66.559)
    $ speak(NICOLE, "The Red Lobster cheesy biscuits?")
    $ setWait(66.559,67.936)
    $ speak(JECKA, "Fuck no-- Chipotle!")
    show nicole sc1 surprised:
        leftcenterstage

    $ setWait(67.936,69.396)
    $ speak(NICOLE, "You don't like the cheesy biscuits??")
    $ setWait(69.396,70.438)
    $ speak(JECKA, "They're okay.")
    show nicole sc1 smile:
        leftcenterstage

    $ setWait(70.438,72.274)
    $ speak(NICOLE, "I'm a whore for the cheesy biscuits.")
    $ setWait(72.274,73.775)
    $ speak(JECKA, "You say you're a whore for everything.")
    show nicole sc1 angry:
        leftcenterstage

    $ setWait(73.775,75.026)
    $ speak(NICOLE, "Oh yeah like what?")
    $ setWait(75.026,82.2)
    $ speak(JECKA, "Bottled water, massages, internet, Burts Bees, McDonald's french fries, percocet, American Spirits, Blink 182...")
    show nicole sc1:
        leftcenterstage

    $ setWait(82.2,83.326)
    $ speak(NICOLE, "We need to hang out less.")

    show jecka sc1 angry:
        rightcenterstage

    $ setWait(83.326,87.038)
    $ speak(JECKA, "We need to get the fuck out of here before Karen comes back with the principal.")
    show nicole sc1:
        leftcenterstage
        linear 1.2 off_farright

    show jecka sc1:
        rightcenterstage
        pause 0.6
        xzoom -1
        linear 1 off_farright

    $ setWait(87.038,88.54)
    $ speak(NICOLE, "New hiding spot.")
    stop ambient fadeout 1
    jump scene_0033
label scene_0033:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0033.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 2
    show emily sc1 angry:
        centerstage
        linear 3.5 off_left

    $ setWait(0.077,4.707)
    $ speak(EMILY, "I couldn't sell a single addy, it's like catholic school all over again...")
    show nicole sc1:
        off_right
        xzoom -1
        linear 1.2 rightcenterstage

    show jecka sc1:
        off_right
        pause 0.3
        linear 0.8 rightmidstage

    $ setWait(4.707,6.166)
    $ speak(JECKA, "Are we going in circles?")
    $ setWait(6.166,7.668)
    $ speak(NICOLE, "Yeah this does look familiar.")
    show nicole sc1 surprised:
        rightcenterstage

    show jecka sc1 surprised:
        rightmidstage

    $ setWait(7.668,10.462)
    $ speak(LYNN, "There you are! You have a lot of explaining to do!")
    show nicole sc1:
        rightcenterstage
        xzoom -1
        pause 0.2
        xzoom 1
        linear 0.4 off_right

    show jecka sc1 worried:
        rightmidstage
        pause 0.5
        xzoom -1
        linear 0.5 off_right

    $ setWait(10.462,11.422)
    $ speak(NICOLE, "Shit-- back to the bathroom.")
    $ setWait(11.422,13.757)
    $ speak(JECKA, "It's gonna be crowded.")
    show burleday 1 sad:
        off_left
        xzoom -1
        linear 2 centerstage
        xzoom 1

    show lynn 1:
        off_left
        xzoom -1
        pause 0.5
        linear 1.7 leftmidstage

    $ setWait(13.757,16.26)
    $ speak(BURLEDAY, "Look there's a perfectly good explanation.")
    $ setWait(16.26,21.307)
    $ speak(LYNN, "Oh I'd love to hear why referring to yourself as a pedophile would ingratiate yourself with your class.")
    $ setWait(21.307,24.81)
    $ speak(BURLEDAY, "A couple students told me about it, they said it means I'm a cool teacher!")
    $ setWait(24.81,30.065)
    $ speak(LYNN, "Cool teachers have pizza parties and Jeopardy PowerPoints, they don't imply they're molesters.")
    $ setWait(30.065,32.943)
    $ speak(BURLEDAY, "Come on it was an isolated incident, won't happen again.")
    $ setWait(32.943,37.281)
    $ speak(LYNN, "Then why did Kelly scream \"I knew it\" after you tried your little slang?")
    show burleday 1 smile:
        centerstage

    $ setWait(37.281,44.079)
    $ speak(BURLEDAY, "What? No you haven't heard?\n\"I knew it\" is actually slang for \"You're awesome\".")
    $ setWait(44.079,45.998)
    $ speak(LYNN, "Do you think I'm fucking stupid?")

    show burleday 1 sad:
        centerstage

    $ setWait(45.998,48)
    $ speak(BURLEDAY, "No but I guess I am...")
    stop ambient fadeout 1
    jump scene_0034
label scene_0034:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0034.mp3")
    play ambient "audio/Ambience/Bathroom_Lockerroom_Ambience.mp3" fadein 1
    scene bathroom
    $ setWait(0.085,1.086)
    $ speak(JECKA, "...")
    show jecka sc1:
        off_farright
        linear 1.2 rightmidstage

    show nicole sc1:
        off_right
        xzoom -1
        linear 0.7 rightcenterstage

    $ setWait(1.086,2.003)
    $ speak(JECKA, "Oh it's empty.")

    show nicole sc1:
        xzoom 1
        rightcenterstage

    $ setWait(2.003,3.964)
    $ speak(NICOLE, "I told you this is a good hiding spot.")
    show jecka sc1 worried:
        rightmidstage

    $ setWait(3.964,5.173)
    $ speak(JECKA, "Ew! Do you smell that??")
    show nicole sc1 sad:
        rightcenterstage

    $ setWait(5.173,6.967)
    $ speak(NICOLE, "Oh god, I guess that's why it's empty.")
    $ setWait(6.967,8.927)
    $ speak(JECKA, "Who the fuck threw up in here?")
    show nicole sc1 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(8.927,10.053)
    $ speak(NICOLE, "Oh my god they're still here.")
    $ setWait(10.053,13.181)
    $ speak(KAREN, "I just wanna be loved!")
    show jecka sc1 angry:
        rightmidstage

    $ setWait(13.181,15.141)
    $ speak(JECKA, "You bullied her into being fucking bulimic!")

    show nicole sc1 angry:
        rightcenterstage
        xzoom 1

    $ setWait(15.141,17.394)
    $ speak(NICOLE, "Dude she was probably already bulimic.")
    $ setWait(17.394,23.984)
    $ speak(KAREN, "I told myself yesterday would be the last time...\nI'm sorry, Daniel Radcliffe!")
    show nicole sc1:
        rightcenterstage

    $ setWait(23.984,26.069)
    $ speak(NICOLE, "See told ya, we had nothing to do with this.")
    show jecka sc1:
        rightmidstage

    $ setWait(26.069,28.446)
    $ speak(JECKA, "Well if we don't get out of here I'm gonna throw up.")
    $ setWait(28.446,31.908)
    $ speak(NICOLE, "God we gotta change too we probably smell like vomit by now.")
    $ setWait(31.908,37.539)
    $ speak(JECKA, "Yeah, now I can never look at this shirt again without thinking about how we made a bulimic girl relapse.")
    $ setWait(37.539,38.415)
    $ speak(NICOLE, "Can I have it?")
    $ setWait(38.415,43.211)
    $ speak(JECKA, "Sure whatever.\nI'm going back to class now, figure this out on your own.")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0035:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0035.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school courtyard
    show nicole sc1:
        off_left
        pause 0.6
        linear 1.3 leftmidstage

    show jecka sc1 angry:
        xzoom -1
        off_left
        linear 1.5 leftcenterstage
        xzoom 1

    $ setWait(0.161,2.913)
    $ speak(JECKA, "Emily's out of her mind if she thinks she can sell at those prices.")
    $ setWait(2.913,4.331)
    $ speak(NICOLE, "Mad you can't afford it?")
    show jecka sc1:
        leftcenterstage
        xzoom 1
    $ setWait(4.331,6.625)
    $ speak(JECKA, "Please, I have three in my ziploc, I'm fine.")
    show kylar sc1 smile:
        off_right
        linear 1 rightmidstage

    show jecka sc1:
        leftcenterstage
        pause 0.5
        xzoom -1
    $ setWait(6.625,8.544)
    $ speak(KYLAR, "Yo guys what's good? What're you doing here?")

    $ setWait(8.544,9.753)
    $ speak(NICOLE, "Not going to class.")
    $ setWait(9.753,10.963)
    $ speak(JECKA, "What're you doing here?")
    $ setWait(10.963,14.633)
    $ speak(KYLAR, "Oh I'm using my PSP to look at porn on the school's wifi.")
    $ setWait(14.633,16.177)
    $ speak(NICOLE, "You can't just wait 'till you get home?")
    $ setWait(16.177,21.765)
    $ speak(KYLAR, "Just to say I did it, y'know. And you can't even talk, you both get fucked up in the middle of class. That could wait 'till you're home.")
    $ setWait(21.765,24.226)
    $ speak(JECKA, "You do too, you pop percs in front of the teacher.")
    show kylar sc1:
        rightmidstage

    $ setWait(24.226,29.857)
    $ speak(KYLAR, "Yeah that's cause I have an actual medical condition, okay? You guys didn't bust your knee up playing lacrosse.")
    $ setWait(29.857,33.068)
    $ speak(NICOLE, "Wait no-- if we're all getting fucked up in class they cancel each other out.")
    $ setWait(33.068,36.322)
    $ speak(JECKA, "Yeah so you still need to answer why you're looking at titty pics on your gameboy.")
    show kylar sc1:
        rightmidstage
    $ setWait(36.322,37.865)
    $ speak(KYLAR, "It's a PSP, dumbass.")
    $ setWait(37.865,40.826)
    $ speak(NICOLE, "Why are you looking at titty pics on your Fisher Price Blackberry?")
    show jecka sc1 smile:
        leftcenterstage
        xzoom -1
    $ setWait(40.826,44.246)
    $ speak(JECKA, "Yeah that's a better name for it, makes it sound official. You have a busy schedule?")
    show kylar sc1 smile:
        rightmidstage

    $ setWait(44.246,50.544)
    $ speak(KYLAR, "Yeah busy telling bitches like you to fuck off.\nBy the way since we're all skipping you guys wanna like fuck around a little bit?")
    $ setWait(50.544,53.672)
    $ speak(NICOLE, "You just told us to fuck off and now you want us to fuck you?")
    show jecka sc1:
        leftcenterstage
        xzoom -1

    show kylar sc1 smile:
        rightmidstage

    $ setWait(53.672,56.509)
    $ speak(JECKA, "You're watching way too much porn if you think that's gonna work.")
    $ setWait(56.509,59.386)
    $ speak(NICOLE, "Yeah we only like being treated like shit when you're creative about it.")
    $ setWait(59.386,60.596)
    $ speak(JECKA, "Yeah let's see what ya got.")
    $ setWait(60.596,63.432)
    $ speak(KYLAR, "Shut the fuck up Jecka, pelican nose ass bitch.")
    $ setWait(63.432,65.768)
    $ speak(JECKA, "My nose is actually perfect, nice try though.")
    $ setWait(65.768,72.358)
    $ speak(NICOLE, "Yeah but the way you dress shows you might be insecure and overcompensating for your introverted childhood.")
    show jecka sc1 smile:
        leftcenterstage
        xzoom 1
        pause 0.7
        xzoom -1
    $ setWait(72.358,75.778)
    $ speak(JECKA, "Oh my g-- see? Now I'm gonna be up all night reading into that.")
    show nicole sc1 smile:
        leftmidstage

    $ setWait(75.778,78.322)
    $ speak(NICOLE, "First she'll hate me, then she'll want me.")
    show kylar sc1:
        rightmidstage
    $ setWait(78.322,87.373)
    $ speak(KYLAR, "Alright whatever dude. Tell ya what, I'll let you guys have the courtyard but you gotta pay up in prescriptions, dog. I ran out of oxy this morning and I just need something to take the edge off.")
    show nicole sc1:
        leftmidstage
    $ setWait(87.373,90.125)
    $ speak(NICOLE, "You called us bitches ten seconds ago and now you want our drugs?")
    $ setWait(90.125,92.002)
    $ speak(JECKA, "Yeah bitches need drugs, can't help ya.")
    $ setWait(92.002,95.589)
    $ speak(KYLAR, "Dude this is so fucking not straight, c'mon I'll throw in five bucks.")
    show jecka sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(95.589,97.174)
    $ speak(JECKA, "What the fuck do we do with five bucks?")
    $ setWait(97.174,100.844)
    $ speak(KYLAR, "O-okay fine, seven. I don't even care what you give me just help me out.")
    menu:
        "GIVE HIM ADDERALL":
            jump scene_0036
        "GIVE HIM XANAX":
            jump scene_0038
label scene_0036:
    $ setVoiceTrack("audio/Scenes/0036.mp3")
    scene school courtyard

    show nicole sc1:
        leftmidstage

    show jecka sc1:
        leftcenterstage
        xzoom -1

    show kylar sc1:
        rightmidstage

    $ setWait(0.041,1.501)
    $ speak(NICOLE, "Oh- your ziploc.")
    show jecka sc1:
        leftcenterstage
        xzoom 1
    $ setWait(1.501,5.046)
    $ speak(JECKA, "Adderall? What the fuck does adderall do for knee pain? It's like for focusing.")
    $ setWait(5.046,8.591)
    $ speak(NICOLE, "It'll help him focus on something other than his knee pain...")
    show jecka sc1:
        leftcenterstage
        xzoom -1
        linear 1 rightcenterstage
    $ setWait(8.591,9.676)
    $ speak(JECKA, "Okay, here ya go.")
    show kylar sc1 smile:
        rightmidstage
    $ setWait(9.676,10.969)
    $ speak(KYLAR, "Sweet, awesome...")
    show kylar sc1 smile:
        rightmidstage
        xzoom -1
        linear 2 off_right

    $ setWait(10.969,13.972)
    $ speak(KYLAR, "Alright I'll see you yin yang bitches later.")

    $ setWait(13.972,15.64)
    $ speak(NICOLE, "Is he calling us Asian?")
    show jecka sc1:
        rightcenterstage
        xzoom 1

    $ setWait(15.64,18.393)
    $ speak(JECKA, "Yeah I don't... Do we look Asian?")
    $ setWait(18.393,20.144)
    $ speak(NICOLE, "Last I checked, no.")
    $ setWait(20.144,22.272)
    $ speak(JECKA, "Then where the hell'd he come up with that?")
    show nicole sc1:
        leftmidstage
        linear 1.1 leftcenterstage

    $ setWait(22.272,24.399)
    $ speak(NICOLE, "Do you have one of those Chinese letter ass tatts?")
    $ setWait(24.399,26.86)
    $ speak(JECKA, "No but I actually wanted one in middle school.")
    $ setWait(26.86,28.111)
    $ speak(NICOLE, "Did you wanna be a stripper?")
    show jecka sc1 angry:
        rightcenterstage

    $ setWait(28.111,31.114)
    $ speak(JECKA, "Can a girl just do crazy shit to her body and have it be for herself?")
    $ setWait(31.114,33.783)
    $ speak(NICOLE, "If it makes staring in the mirror more fun, go for it.")

    show jecka sc1:
        rightcenterstage

    $ setWait(33.783,34.659)
    $ speak(JECKA, "Would you get one?")
    $ setWait(34.659,36.411)
    $ speak(NICOLE, "A Chinese ass tat? No.")
    $ setWait(36.411,39.497)
    $ speak(JECKA, "Okay what if it wasn't Chinese, just of anything.")
    $ setWait(39.497,41.457)
    $ speak(NICOLE, "...Mechanical Animals lyrics.")
    $ setWait(41.457,42.834)
    $ speak(JECKA, "I haven't heard that album.")
    $ setWait(42.834,43.877)
    $ speak(NICOLE, "It's pretty good.")
    $ setWait(43.877,48.464)
    $ speak(JECKA, "Just pretty good?\nYou'd get a pretty good album tattooed on your ass forever?")
    $ setWait(48.464,51.259)
    $ speak(NICOLE, "I'm gonna die before 30, won't have to deal with it that long.")
    $ setWait(51.259,53.887)
    $ speak(COACH, "Aw why would ya get married anyway!?")
    show nicole sc1 surprised:
        leftcenterstage
        xzoom -1

    $ setWait(53.887,54.971)
    $ speak(NICOLE, "Shit the coach is coming!")

    show nicole sc1:
        leftcenterstage
        xzoom -1

    $ setWait(54.971,58.057)
    $ speak(JECKA, "N-no wait, I think he's just talking on the phone outside.")
    $ setWait(58.057,63.354)
    $ speak(COACH, "Y-Yeah I'd be mad at OJ if he didn't kill her, fuck these bitches, man!")
    $ setWait(63.354,64.939)
    $ speak(NICOLE, "Does he not know he's still at work?")
    $ setWait(64.939,70.737)
    $ speak(COACH, "The fuck I gotta meet girls at a bar for? I teach gym, my students are way easier.")
    $ setWait(70.737,71.988)
    $ speak(JECKA, "I don't think he knows anything.")
    $ setWait(71.988,79.954)
    $ speak(COACH, "See I can't decide what's more exciting, cheating on my wife or buying a shotgun and blowing her fucking head off hahahahaha!!")
    $ setWait(79.954,82.332)
    $ speak(NICOLE, "Who could he possibly talk about all this with?")
    $ setWait(82.332,84.751)
    $ speak(COACH, "Hey hey, for a pastor...")
    $ setWait(84.751,87.67)
    $ speak(COACH, "...you got shit ton of fully automatic weapons!")
    show jecka sc1 worried:
        rightcenterstage

    $ setWait(87.67,89.297)
    $ speak(JECKA, "I can't listen to this, we need to go.")
    show nicole sc1 angry:
        leftcenterstage
        xzoom 1
    $ setWait(89.297,90.089)
    $ speak(NICOLE, "Where??")
    $ setWait(90.089,95.845)
    $ speak(JECKA, "Anywhere but here?\nHopefully somewhere that doesn't have a middle-aged pervert screaming about how much he likes killing women?")
    show nicole sc1:
        leftcenterstage
    $ setWait(95.845,98.556)
    $ speak(NICOLE, "Huh... I might have an idea, come on.")
    show nicole sc1:
        leftcenterstage
        linear 1.3 off_right

    show jecka sc1:
        rightcenterstage
        xzoom 1
        pause 0.7
        xzoom -1
        linear 1 off_right

    $ setWait(98.556,103.186)
    $ speak(COACH, "Yeah... yeah hey remember when the Jets had a white quarterback??")
    stop ambient fadeout 1
    jump scene_0037
label scene_0037:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0037.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 2
    show nicole sc1:
        centerstage
        xzoom -1

    show jecka sc1:
        leftmidstage
        xzoom -1

    $ setWait(0.086,2.589)
    $ speak(JECKA, "You really think we should hide in the principal's office?")
    $ setWait(2.589,6.092)
    $ speak(NICOLE, "I mean it's kinda the last place she'd expect to look for kids skipping.")
    $ setWait(6.092,9.053)
    $ speak(JECKA, "That's true, but are we just gonna sit here 'till the bell rings?")
    $ setWait(9.053,10.847)
    $ speak(NICOLE, "We could go through her drawers and see what's up with her.")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1

    $ setWait(10.847,15.268)
    $ speak(JECKA, "You're gonna go through her stuff?? So not worth it, would probably just be like pens and folders.")
    $ setWait(15.268,17.353)
    $ speak(NICOLE, "I don't think so... No way with her.")
    $ setWait(17.353,18.73)
    $ speak(JECKA, "You think she's smuggling something?")
    $ setWait(18.73,23.401)
    $ speak(NICOLE, "All I know is a woman who shows off that much cleavage at work is into some wild shit.")
    show jecka sc1:
        leftmidstage
        xzoom -1

    $ setWait(23.401,26.279)
    $ speak(JECKA, "I don't disagree but what, is she gonna have child porn in there?")
    $ setWait(26.279,28.656)
    $ speak(NICOLE, "She's not a man, Jecka, so no.")
    $ setWait(28.656,31.618)
    $ speak(JECKA, "Yeah that's true... why do they always bring it to work?")
    $ setWait(31.618,34.412)
    $ speak(NICOLE, "That domestically beats me, I have no fuckin' clue.")
    $ setWait(34.412,36.915)
    $ speak(JECKA, "So what could a female principal possibly have then?")
    $ setWait(36.915,40.96)
    $ speak(NICOLE, "I just feel like she'd be into Satan-worship, or at the very least have a sex diary.")
    $ setWait(40.96,44.214)
    $ speak(JECKA, "A Miss Lynn sex diary would be horrifying. She's like our teacher.")
    $ setWait(44.214,46.799)
    $ speak(NICOLE, "We say that about Stephen King books, we still read those.")
    $ setWait(46.799,49.761)
    $ speak(JECKA, "\"Dear Diary, hot candle wax hurts so good\"")
    $ setWait(49.761,53.014)
    $ speak(NICOLE, "No it'd probably be like a thesaurus of words for \"good\".")
    $ setWait(53.014,55.099)
    $ speak(JECKA, "Yeah she probably sexts with perfect grammar.")
    $ setWait(55.099,58.728)
    $ speak(NICOLE, "\"My husband showed an exquisite exhibition of lust for me.\"")
    $ setWait(58.728,62.065)
    $ speak(JECKA, "Husband? She would never be married, marriage is for ugly people.")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1
        pause 0.35
        xzoom 1

    show nicole sc1 surprised:
        centerstage
        xzoom -1

    $ setWait(62.065,62.523)
    $ speak(NICOLE, "Oh shit.")
    $ setWait(62.523,63.65)

    show lynn 1:
        off_left
        xzoom -1
        linear 2 rightstage

    $ speak(LYNN, "Step aside, girls!")
    show nicole sc1:
        centerstage
        xzoom 1

    show jecka sc1:
        leftmidstage
        xzoom -1
    $ setWait(63.65,65.944)
    $ speak(NICOLE, "There's a perfectly good reason for why we're in here--")
    show lynn 1:
        rightstage
        xzoom 1
    $ setWait(65.944,69.113)
    $ speak(LYNN, "Sorry but we'll have to talk about this later, we have a bit of an emergency.")
    $ setWait(69.113,70.615)
    $ speak(JECKA, "Is it a fire? Do we need to go?")
    $ setWait(70.615,72.575)
    $ speak(LYNN, "No, one of the students is having a seizure!")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1

    $ setWait(72.575,73.243)
    $ speak(JECKA, "Oh my god.")
    $ setWait(73.243,75.745)
    $ speak(NICOLE, "Yeah they really gotta fix that ceiling light flicker.")
    $ setWait(75.745,80.333)
    $ speak(LYNN, "It wasn't the lights, a student had an allergy to something and now they're having a fatal reaction on the floor!")
    $ setWait(80.333,82.085)
    $ speak(NICOLE, "Totally been there, not a seizure though.")
    show lynn 1:
        rightstage
        xzoom -1
    $ setWait(82.085,88.758)
    $ speak(LYNN, "Yes hello? I have a student who needs immediate medical attention...\nWe think it's a seizure and we need an ambulance ASAP...")
    $ setWait(88.758,90.885)
    $ speak(JECKA, "Isn't an ambulance ride like 5000 dollars?")
    show nicole sc1 smile:
        centerstage
        xzoom -1
    $ setWait(90.885,94.055)
    $ speak(NICOLE, "Yeah Fat Joe flexes the most on his way to cardiac surgery.")
    show nicole sc1:
        centerstage
        xzoom 1
    $ setWait(94.055,99.394)
    $ speak(LYNN, "What caused it? ...He took an unprescribed medication, I think he said it was adderall before he passed out.")
    $ setWait(99.394,100.27)
    show jecka sc1 surprised:
        leftmidstage
        xzoom -1

    show nicole sc1 surprised:
        centerstage
        xzoom 1
        linear 0.6 leftcenterstage

    $ speak(JECKA, "Oh fuck.")
    show lynn 1:
        rightstage
        xzoom -1
        pause 1
        xzoom 1
    $ setWait(100.27,101.854)
    $ speak(LYNN, "Hold on a sec...\nWhat is it?")
    $ setWait(101.854,102.438)
    $ speak(JECKA, "Uh well--")
    show nicole sc1 smile:
        leftcenterstage

    $ setWait(102.438,105.525)
    $ speak(NICOLE, "Nothing we just realized we gotta get to class, see ya later Miss Lynn!")
    show nicole sc1:
        leftcenterstage
        xzoom -1
        linear 1 off_farleft

    show jecka sc1:
        xzoom -1
        leftmidstage
        pause 0.7
        xzoom 1
        linear 0.6 off_left

    $ setWait(105.525,107.235)
    $ speak(JECKA, "Good luck with Kylar.")
    show lynn 1:
        rightstage
        xzoom -1
    $ setWait(107.235,110.113)
    $ speak(LYNN, "Yes the front exit is always unlocked... Wait.")
    show lynn 1:
        rightstage
        xzoom 1
    $ setWait(110.113,112.031)
    $ speak(LYNN, "How did you know it was Kylar!?")
    stop ambient fadeout 1
    jump scene_0040
label scene_0038:
    $ setVoiceTrack("audio/Scenes/0038.mp3")
    scene school courtyard

    show nicole sc1:
        leftmidstage
        linear 1.8 rightcenterstage


    show jecka sc1:
        leftcenterstage
        xzoom -1

    show kylar sc1:
        rightmidstage

    $ setWait(0.037,2.248)
    $ speak(NICOLE, "I got a xanax, it's a pink one.")
    $ setWait(2.248,4.5)
    $ speak(KYLAR, "Whatever, it's tiny but it'll do something, right?")
    $ setWait(4.5,5.876)
    $ speak(NICOLE, "You're just gonna have to find out.")
    $ setWait(5.876,8.838)
    $ speak(KYLAR, "Can you not be a stuck-up bitch about every single little thing.")
    show jecka sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(8.838,11.34)
    $ speak(JECKA, "Why are you complaining, you got your pill; Go!")
    show kylar sc1:
        rightmidstage
        xzoom -1
        linear 3 off_right

    $ setWait(11.34,16.762)
    $ speak(KYLAR, "Fine bitches, I'm gonna listen to Coldplay on my iPod. And Coldplay isn't gay either.")
    show nicole sc1:
        rightcenterstage
        xzoom -1
    $ setWait(16.762,17.888)
    $ speak(NICOLE, "...What is wrong with him?")
    show jecka sc1:
        leftcenterstage
        xzoom -1
    $ setWait(17.888,21.1)
    $ speak(JECKA, "I don't know but I'm really mad we got kicked out of the cafeteria now.")
    $ setWait(21.1,21.767)
    $ speak(NICOLE, "Why?")
    $ setWait(21.767,24.437)
    $ speak(JECKA, "I want ice cream and the vending machine's too far away now.")
    $ setWait(24.437,27.815)
    $ speak(NICOLE, "Why did I decide to skip in school? We could've done something cooler than this.")
    $ setWait(27.815,29.567)
    $ speak(JECKA, "I still got the addys in my ziploc.")
    $ setWait(29.567,35.573)
    $ speak(NICOLE, "I would but I just gave him my last xanax.\nIf I don't take the adderall with something to mellow me out I'm gonna be grinding my teeth all day.")
    $ setWait(35.573,36.866)
    $ speak(JECKA, "Have you tried weed with it?")
    $ setWait(36.866,39.243)
    $ speak(NICOLE, "Marijuana's for people who talk like ninja turtles.")
    show counselor 1:
        off_right
        linear 1.5 rightmidstage

    show nicole sc1:
        rightcenterstage
        xzoom -1
        pause 0.4
        xzoom 1

    $ setWait(39.243,43.664)
    $ speak(COUNSELOR, "Girls, we're not talking about illicit activities are we?")
    $ setWait(43.664,44.415)
    $ speak(JECKA, "No?")
    $ setWait(44.415,46.375)
    $ speak(NICOLE, "Is getting fucked up an illicit activity?")
    $ setWait(46.375,47.501)
    $ speak(JECKA, "But yeah so what's up?")
    $ setWait(47.501,52.59)
    $ speak(COUNSELOR, "I should ask you the same, class is in session but you're in the courtyard.")
    $ setWait(52.59,55.843)
    $ speak(NICOLE, "Oh yeah we have a... truncated schedule?")
    $ setWait(55.843,58.846)
    $ speak(COUNSELOR, "Really now? I haven't been made aware of this.")
    $ setWait(58.846,61.807)
    $ speak(JECKA, "Yeah they gave us one cause we have issues.")
    $ setWait(61.807,66.228)
    $ speak(COUNSELOR, "And just to be clear, what exactly does truncated mean?")
    show jecka sc1 worried:
        leftcenterstage
        xzoom -1

    $ setWait(66.228,68.189)
    $ speak(JECKA, "Like the definition?")
    $ setWait(68.189,69.44)
    $ speak(COUNSELOR, "Yes.")
    $ setWait(69.44,74.195)
    $ speak(NICOLE, "It's uh... Well our next period back is English so we could tell you then.")
    $ setWait(74.195,79.325)
    $ speak(COUNSELOR, "Such a shame you girls get into so much trouble with bright futures ahead of yourselves.")
    show counselor 1 smile:
        rightmidstage
        xzoom -1
        linear 2 off_right

    $ setWait(79.325,80.534)
    $ speak(COUNSELOR, "Come with me...")
    show nicole sc1:
        rightcenterstage
        xzoom 1
        linear 2 off_farright

    show jecka sc1 worried:
        leftcenterstage
        xzoom -1
        linear 2 off_right

    $ setWait(80.534,82.286)
    $ speak(JECKA, "Why do you always say it like that?")
    stop ambient fadeout 1
    jump scene_0039
label scene_0039:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0039.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1
    show counselor 1 smile:
        rightmidstage

    show nicole sc1:
        leftmidstage

    show jecka sc1:
        leftcenterstage
        xzoom -1

    $ setWait(0.047,7.346)
    $ speak(COUNSELOR, "Let me try something a little different here. Do you girls have thoughts and feelings for one another?")
    $ setWait(7.346,10.391)
    $ speak(NICOLE, "Uh, I think Jecka's kinda spoiled.")
    show jecka sc1 angry:
        leftcenterstage
        xzoom -1

    $ setWait(10.391,12.309)
    $ speak(JECKA, "And I feel like Nicole's a bitch.")
    $ setWait(12.309,21.11)
    $ speak(COUNSELOR, "Not quite what I was looking for. It seems that almost every time either of you are in trouble, you're always together.")
    $ setWait(21.11,26.24)
    $ speak(COUNSELOR, "Is there something between the two of you that you may not realize?")
    $ setWait(26.24,27.741)
    $ speak(JECKA, "What does any of that even mean?")
    $ setWait(27.741,29.076)
    $ speak( NICOLE, "He's asking if we're lesbians.")
    show jecka sc1:
        leftcenterstage
        xzoom -1
    $ setWait(29.076,30.786)
    $ speak(JECKA, "Oh you'd just love that, wouldn't you?")
    show counselor 1:
        rightmidstage
    $ setWait(30.786,34.123)
    $ speak(COUNSELOR, "Now please, there's no need for contextual assumption.")
    $ setWait(34.123,35.749)
    $ speak(NICOLE, "We could say the same to you.")
    $ setWait(35.749,47.386)
    $ speak(COUNSELOR, "Be mindful of your venomous commentary.\nIn my professional opinion I believe it would be helpful for the both of you to trial some sort of affection to clear the tension between you.")
    $ setWait(47.386,49.096)
    $ speak(JECKA, "Trial affection?")
    $ setWait(49.096,51.056)
    $ speak(NICOLE, "Are you telling us to make out in front of you?")
    show counselor 1 smile:
        rightmidstage
    $ setWait(51.056,59.481)
    $ speak(COUNSELOR, "No, I'm asking you to physically express how you feel about one another in the safety of this judgment-free room.")
    show nicole sc1:
        leftmidstage
        linear 1.3 xalign .23
        pause 1.1
        linear 0.4 leftmidstage

    $ setWait(59.481,62.609)
    $ speak(NICOLE, "Okay fine. Pat on the back, good job, champ-- Can we go now??")
    show counselor 1:
        rightmidstage
    $ setWait(62.609,67.364)
    $ speak(COUNSELOR, "Nicole will you please refrain from being intellectually and emotionally dishonest?")
    show jecka sc1 angry:
        leftcenterstage
        xzoom -1

    $ setWait(67.364,68.741)
    $ speak(JECKA, "What does any of that mean??")
    $ setWait(68.741,72.661)
    $ speak(NICOLE, "Dude this isn't American Pie, you can't just get hot girls to tongue kiss in front of you.")
    $ setWait(72.661,74.455)
    $ speak(JECKA, "Yeah you at least have to pay us.")
    $ setWait(74.455,78.083)
    $ speak(COUNSELOR, "I'm afraid you're only hurting yourselves in fighting this exercise.")
    $ setWait(78.083,80.002)
    $ speak(NICOLE, "Who the fuck lets you work here??")
    show lynn 1:
        off_left
        xzoom -1
        linear .6 leftstage

    show jecka sc1:
        leftcenterstage
        xzoom -1
        pause 0.4
        xzoom 1

    show nicole sc1:
        leftmidstage
        xzoom 1
        pause 0.3
        xzoom -1

    $ setWait(80.002,81.587)
    $ speak(LYNN, "Hope I'm not interrupting anything serious.")
    $ setWait(81.587,83.088)
    $ speak(JECKA, "No this is pretty fucking serious--")
    show counselor 1:
        rightmidstage
        linear 1 rightcenterstage

    $ setWait(83.088,84.548)
    $ speak(COUNSELOR, "What can I help you with, Principal?")
    $ setWait(84.548,88.427)
    $ speak(LYNN, "If I could borrow your help for a moment, there's a student entirely passed out in the hallway.")
    $ setWait(88.427,91.847)
    $ speak(COUNSELOR, "Uh-Oh my! Of course I could help, who is it?")
    show lynn:
        leftstage
        xzoom -1
        pause 2.1
        xzoom 1
        linear 0.7 off_left
    $ setWait(91.847,94.475)
    $ speak(LYNN, "It's Kylar, I found him out on the floor unconscious.")
    show counselor 1:
        rightcenterstage
        linear 0.9 off_left

    $ setWait(94.475,96.685)
    $ speak(COUNSELOR, "I know CPR!")
    $ setWait(96.685,98.729)
    $ speak(NICOLE, "...I remember my first xanax.")
    $ setWait(98.729,100.814)
    $ speak(JECKA, "But you gave him a pink one, aren't those tiny?")
    show nicole sc1:
        leftmidstage
        xzoom 1
    $ setWait(100.814,103.567)
    $ speak(NICOLE, "Yeah but if he's never done it before it hits really hard.")
    $ setWait(103.567,106.862)
    $ speak(JECKA, "He's like six feet tall he wouldn't pass out over a pink xanax, Nicole.")
    $ setWait(106.862,110.449)
    $ speak(NICOLE, "Am I doctor now?? I'm like a backpack pharmacist at best, how would I know?")
    $ setWait(110.449,112.951)
    $ speak(JECKA, "What if he found a percocet and took 'em both?")

    show nicole sc1 sad:
        leftmidstage
        xzoom 1

    $ setWait(112.951,114.244)
    $ speak(NICOLE, "...Can that kill you?")
    show jecka sc1 worried:
        leftcenterstage
        xzoom 1
    $ setWait(114.244,115.621)
    $ speak(JECKA, "I think we should ask.")
    stop ambient fadeout 1
    jump scene_0040
label scene_0040:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0040.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school ext 4
    show emt:
        leftstage
        pause 2.2
        xzoom -1
        linear 2 leftcenterstage
    $ setWait(0.039,3.084)
    $ speak(EMT, "Aw hold on guys, I forgot my Big Gulp jug.")
    show jecka sc1 worried:
        off_right
        linear 0.6 rightcenterstage

    show nicole sc1:
        xzoom -1
        off_right
        pause 0.4
        linear 0.8 rightmidstage

    $ setWait(3.084,5.044)
    $ speak(JECKA, "Hey do you know how Kylar passed out?")
    $ setWait(5.044,6.17)
    $ speak(EMT, "Is he a friend of yours?")
    $ setWait(6.17,6.963)
    $ speak(NICOLE, "Not really.")
    show jecka sc1:
        rightcenterstage

    $ setWait(6.963,8.965)
    $ speak(JECKA, "Um he's like my boyfriend.")
    $ setWait(8.965,12.218)
    $ speak(EMT, "Sorry girls but we can only divulge medical information with family members.")
    $ setWait(12.218,13.553)
    $ speak(JECKA, "Family-- he's my brother.")
    $ setWait(13.553,15.513)
    $ speak(EMT, "You said he was your boyfriend.")
    $ setWait(15.513,16.556)
    $ speak(JECKA, "Can he not be both?")
    $ setWait(16.556,17.306)
    $ speak(EMT, "He shouldn't be both.")
    $ setWait(17.306,20.226)
    $ speak(NICOLE, "Will you stop judging her Swedish heritage and just tell us??")
    $ setWait(20.226,27.275)
    $ speak(EMT, "So essentially his body's shut down to the point where his lungs are barely functioning.\nIf we didn't get him sooner he could've lost a lot of brain cells.")
    $ setWait(27.275,28.734)
    $ speak(NICOLE, "I didn't know five was a lot.")
    $ setWait(28.734,30.945)
    $ speak(JECKA, "But do you know exactly what caused it?")
    $ setWait(30.945,39.328)
    $ speak(EMT, "We won't know anything until we get him to the hospital for a toxicology report. Since you're family would you like to ride along in the ambulance with us? This must be very hard for you.")
    $ setWait(39.328,41.455)
    $ speak(JECKA, "Nah it's okay I don't care that much.")
    $ setWait(41.455,45.668)
    $ speak(EMT, "Um... Okay so if that's it, I have very pressing matters to tend to.")

    show emt:
        leftcenterstage
        xzoom -1
        linear 2 off_right

    $ setWait(45.668,47.962)
    $ speak(EMT, "Where is my big gulp jug?")
    $ setWait(47.962,49.672)
    $ speak(NICOLE, "...Are they just gonna wait for him to get that?")
    $ setWait(49.672,53.092)
    $ speak(JECKA, "Yeah I see Kylar in the back there, they're not driving off.")
    $ setWait(53.092,58.681)
    $ speak(NICOLE, "You don't think they can like stomach-pump the pills and find fingerprints on them, right?")
    $ setWait(58.681,61.225)
    show jecka sc1:
        rightcenterstage
        xzoom -1
    $ speak(JECKA, "No way, I don't think so.")
    $ setWait(61.225,64.562)
    $ speak(NICOLE, "Cool, yeah I don't care if he dies I just don't wanna be held responsible.")
    $ setWait(64.562,68.482)
    $ speak(JECKA, "Yeah same. Do you think we should go to class now so this doesn't look suspicious?")
    $ setWait(68.482,71.694)
    $ speak(NICOLE, "Yeah we should change too to screw up his story if he tries snitching on us.")
    $ setWait(71.694,74.864)
    $ speak(JECKA, "Good call, where are you going? We gotta get our stories straight.")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096

label scene_0041:
    $ setVoiceTrack("audio/Scenes/0041.mp3")
    scene home nicole int

    show nicole sc1:
        leftcenterstage

    show jecka sc1:
        rightcenterstage

    $ setWait(0.037,3.916)
    $ speak(NICOLE, "I think the pills could be a lot more fun than you're expecting.")
    $ setWait(3.916,4.833)
    $ speak(JECKA, "How's that?")
    $ setWait(4.833,9.421)
    $ speak(NICOLE, "My Mom has problems, dude. And she's old so the doctor just writes her whatever she wants.")
    $ setWait(9.421,11.006)
    $ speak(JECKA, "What are we gonna snort polio meds?")
    $ setWait(11.006,12.424)
    $ speak(NICOLE, "Don't they have a vaccine for that?")
    $ setWait(12.424,13.717)
    $ speak(JECKA, "Not when she was born.")
    $ setWait(13.717,19.306)
    $ speak(NICOLE, "Look, she goes to a new psychiatrist after every divorce and they keep giving her the good shit cause she doesn't move over the medical history.")
    $ setWait(19.306,24.269)
    $ speak(JECKA, "Oh that's a nice strategy. My Mom only gets the daily Prozac shit after they cut her off from Valium.")
    $ setWait(24.269,27.314)
    $ speak(NICOLE, "She should get divorced. New health plan, new psychiatrist.")
    $ setWait(27.314,31.318)
    $ speak(JECKA, "My Mom hasn't worked in like twenty years, I don't know if she could even function without my Dad.")
    $ setWait(31.318,33.445)
    $ speak(NICOLE, "Can't she just find a new guy? My Mom does.")
    show jecka sc1 worried:
        rightcenterstage

    $ setWait(33.445,38.283)
    $ speak(JECKA, "You haven't seen my Mom, Nicole. She stopped trying like ten years ago, I don't think you can ever go back from that.")
    $ setWait(38.283,41.87)
    $ speak(NICOLE, "Yeah after the mom jeans it's just over. Tragic.")
    $ setWait(41.87,45.832)
    $ speak(JECKA, "Thanks now I have to think about how sad my Mom is, this is why I'll never get married.")
    show nicole sc1:
        leftcenterstage
        pause 1.9
        xzoom -1
        linear 2.3 off_left

    $ setWait(45.832,48.377)
    $ speak(NICOLE, "This is why we should do those pills now, come on.")
    stop ambient fadeout 1
    jump scene_0042
label scene_0042:
    show black onlayer screens with Pause(1.2):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.8 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0042.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3" fadein 1
    $ csbox = True
    show cut0042_1
    $ setWait(0.041,2.961)
    $ speak(NICOLE, "\nWhy does it hit so fast when you snort it?? Fuck...")
    show cut0042_2
    $ setWait(2.961,5.588)
    $ speak(JECKA, "\nDoesn't Vicodin always hit like that? I never tried it.")
    $ setWait(5.588,7.966)
    $ speak(NICOLE, "\nNo it takes like an hour when you take it like a pill.")
    $ setWait(7.966,10.593)
    $ speak(JECKA, "\nWow prescriptions are just dope on layaway")
    $ setWait(10.593,15.223)
    $ speak(NICOLE, "\nA line of it does a little at first but then just... creeps up fast. Here try it.")
    show cut0042_3
    $ setWait(15.223,17.308)
    $ speak(JECKA, "\nOh my god I'm scared, is my nose gonna bleed?")
    $ setWait(17.308,19.227)
    $ speak(NICOLE, "\nOnly if you do it like a million times.")
    show cut0042_4
    $ setWait(19.227,21.646)
    $ speak(NICOLE, " ")
    show cut0042_5
    $ setWait(21.646,22.272)
    $ speak(JECKA, " ")
    show cut0042_6
    $ setWait(22.272,25.4)
    $ speak(JECKA, "\nWhat the fuck... How does your Mom function like this??")
    $ setWait(25.4,26.109)
    $ speak(NICOLE, "\nShe doesn't.")
    show cut0042_7
    $ setWait(26.109,28.027)
    $ speak(JECKA, "\nWhat if she needs these later?")
    $ setWait(28.027,31.614)
    $ speak(NICOLE, "\nIt's easy to get more, she can make an appointment and pay like 2 bucks for whole a bottle.")
    show cut0042_2 onlayer screens
    hide cut0042_7
    $ setWait(31.614,33.324)
    $ speak(JECKA, "\nThey won't cut her off or anything?")
    $ setWait(33.324,39.956)
    $ speak(NICOLE, "Yeah that's the one perk to being old. If you want enough drugs to shut off your emotions they won't assume you'll try to OD or anything.")
    $ setWait(39.956,42.041)
    $ speak(JECKA, "\nYeah they said that when I wanted sleeping pills.")
    $ setWait(42.041,47.005)
    $ speak(NICOLE, "\nIt's so bullshit. Like even if you wanted to do that it's like... like...")
    $ setWait(47.005,49.299)
    $ speak(NICOLE, "\nlike none of their business--Shit it's really hitting now.")
    $ setWait(49.299,53.678)
    $ speak(JECKA, "\nOh yeah I feel it too... It's like percocet but not as good...")
    $ setWait(53.678,57.307)
    $ speak(NICOLE, "\nYou could say that about any painkiller... You wanna watch Mythbusters now?")
    $ setWait(57.307,60.435)
    $ speak(JECKA, "\nI am nowhere near fucked up enough to watch Mythbusters.")
    $ setWait(60.435,62.395)
    $ speak(NICOLE, "\nWe might have something left to fix that.")
    $ setWait(62.395,65.023)
    $ speak(JECKA, "\nWhy the fuck do you wanna watch Mythbusters so bad?")
    $ setWait(65.023,67.567)
    $ speak(NICOLE, "\nI-I don't know it's the only thing on when I skip.")
    $ setWait(67.567,69.819)
    $ speak(JECKA, "\nUgh okay gimme something good.")
    $ setWait(69.819,73.489)
    $ speak(NICOLE, "\nYou wanna try a mystery pill? I'm not even looking at the label but I'll crush it up.")
    hide cut0042_2 onlayer screens
    show cut0042_3 onlayer screens
    $ setWait(73.489,75.575)
    $ speak(JECKA, "\nMystery pill? What if it hurts me?")
    $ setWait(75.575,77.952)
    $ speak(NICOLE, "\nDude you're Vic'd up, you're good.")
    show cut0042_2
    $ setWait(77.952,79.537)
    $ speak(JECKA, "\n...Alright fuck it, line it up.")
    hide cut0042_3 onlayer screens
    show cut0042_4 onlayer screens
    $ setWait(79.537,81.748)
    $ speak(NICOLE, " ")
    hide cut0042_4 onlayer screens
    show cut0042_5 onlayer screens
    $ setWait(81.748,82.624)
    $ speak(JECKA, " ")
    $ setWait(82.624,83.249)
    $ speak(NICOLE, "\nIs it good?")
    hide cut0042_5 onlayer screens
    show cut0042_6 onlayer screens
    $ setWait(83.249,86.002)
    $ speak(JECKA, "\nOh my god, oh my god, what did I do...")
    hide cut0042_6 onlayer screens
    show cut0042_2 onlayer screens
    $ setWait(86.002,87.503)
    $ speak(JECKA, "\nI don't feel anything.")
    $ setWait(87.503,89.839)
    $ speak(NICOLE, "\nReally? She always has the strongest shit.")
    $ setWait(89.839,92.05)
    $ speak(JECKA, "\nWhat if it's just a Claritin or something?")
    $ setWait(92.05,99.265)
    $ speak(NICOLE, "\nNo my Mom barely has allergies, lemme read the label...\nMetroprolol, generic for Betaloc.")
    $ setWait(99.265,101.976)
    $ speak(JECKA, "\nBetaloc? It should say what it's for, right?")
    $ setWait(101.976,106.314)
    $ speak(NICOLE, "\nIt says \"Use for high blood pressure or tightness of chest\".")
    hide cut0042_2 onlayer screens
    show cut0042_7:
        alpha 1.0
        pause 29
        linear 2 alpha 0.0
    $ setWait(106.314,109.15)
    $ speak(JECKA, "\nYou had me do a line of beta blocker?? Oh god it's hitting.")
    $ setWait(109.15,111.027)
    $ speak(NICOLE, "\nThere's a name for it? How'd you know that?")
    $ setWait(111.027,113.154)
    $ speak(JECKA, "\nThe chemistry teacher told us about it last year.")
    $ setWait(113.154,117.2)
    $ speak(NICOLE, "\nMissed that class... That was the last pill too, my Mom must take a lot of these.")
    $ setWait(117.2,121.412)
    $ speak(JECKA, "\nI'm like deflating in my own body. How wound up is your Mom to always need these??")
    $ setWait(121.412,124.374)
    $ speak(NICOLE, "\nWe don't really talk about that, she just comes home and yells at me.")
    $ setWait(124.374,127.835)
    $ speak(JECKA, "\nI would yell at you too, why the fuck didn't you tell me it was a beta blocker?")
    $ setWait(127.835,130.004)
    $ speak(NICOLE, "\nI think you're missing the point of a mystery pill.")
    $ setWait(130.004,133.174)
    $ speak(JECKA, "\nI took it with Vicodin, Nicole! ...Call 911.")
    $ setWait(133.174,135.968)
    $ speak(NICOLE, "\nDude you're gonna be fine. Worst case scenario, you pass out.")
    $ setWait(135.968,137.845)
    $ speak(JECKA, "\nWhy do I feel like a guy's told me that before?")
    stop ambient fadeout 1
    jump scene_0043
label scene_0043:
    $ csbox = False
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0043.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3" fadein 1
    scene home nicole int

    show mom 1 pain:
        off_right
        linear 4 centerstage
    $ setWait(0.039,5.753)
    $ speak(MOM, "Ugh! Chest pains! One pill left just gotta get up these stairs...")
    show mom 1 pain:
        centerstage
        linear 3 off_left

    $ setWait(5.753,9.215)
    $ speak(MOM, "The women at Ross are so god damn difficult...")
    stop ambient fadeout 1
    jump scene_0044
label scene_0044:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0044.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3" fadein 1
    scene bedroom nicole
    show nicole sc1:
        leftcenterstage
    $ setWait(0.036,2.205)
    $ speak(NICOLE, "Damn Jecka you're out cold.")
    show mom 1 pain:
        off_left
        xzoom -1
        linear 1 leftstage

    show nicole sc1 surprised:
        leftcenterstage
        pause 0.3
        xzoom -1

    $ setWait(2.205,7.293)
    $ speak(MOM, "Nicole why are you home?? And why's all my medicine on the floor!?")
    $ setWait(7.293,12.048)
    $ speak(NICOLE, "Oh shit, hey Mom um... We were feeling sick so we took a bunch of your pills.")
    show mom 1 pain:
        leftstage
        xzoom -1
        linear 2 leftmidstage
    $ setWait(12.048,15.802)
    $ speak(MOM, "I don't have time for excuses, just where's my Betaloc!?")
    show nicole sc1 sad:
        leftcenterstage
        xzoom -1
    $ setWait(15.802,18.471)
    $ speak(NICOLE, "Betaloc... Ummmm what do you need that for?")
    show mom 1 pain:
        leftmidstage
        xzoom -1
        linear 2 rightmidstage
        xzoom 1
    $ setWait(18.471,22.267)
    $ speak(MOM, "I feel like I'm having a heart attack! Why is the bottle empty!?")
    show nicole sc1 surprised:
        leftcenterstage
        xzoom 1
    $ setWait(22.267,25.228)
    $ speak(NICOLE, "Oh my fucking god uh... Jecka was having a heart attack too!")
    show black onlayer screens:
        alpha 0.0
        linear 4 alpha 1.0

    show mom 1 pain:
        rightmidstage
        linear 7 centerstage

    $ setWait(25.228,29.524)
    $ speak(MOM, "Ugh oh god... Everything's getting dark... call 911!")
    $ setWait(29.524,31.985)
    $ speak(NICOLE, "Okay, Mom... Mom?")
    stop ambient fadeout 7
    $ setWait(31.985,35.947)
    $ speak(NICOLE, "What the fuck!? Mom?? Fuck where's the phone!")
    jump scene_0045
label scene_0045:
    show black onlayer screens with Pause(3.75):
        alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 5 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0045.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 5

    scene school ext 5

    show nicole sc3:
        leftcenterstage

    show jecka sc3:
        rightcenterstage

    $ setWait(0.005,5.26)
    $ speak(NICOLE, "...")
    $ setWait(5.26,8.055)
    $ speak(JECKA, "...So how was the funeral?")
    $ setWait(8.055,9.723)
    $ speak(NICOLE, "Went as expected.")
    show jecka sc3 worried:
        rightcenterstage

    $ setWait(9.723,10.641)
    $ speak(JECKA, "Meaning?")
    $ setWait(10.641,12.517)
    $ speak(NICOLE, "My aunt pulled out a gun.")
    $ setWait(12.517,17.689)
    $ speak(JECKA, "Weird, that's somehow not the most shocking thing you've told me in the last week.")
    show nicole sc3 angry:
        leftcenterstage

    $ setWait(17.689,26.782)
    $ speak(NICOLE, "Yeah so there's this huge life insurance payout, all the alimony's going to me and my brother, tons of paperwork, and none of it's worth any of the hassle.")
    $ setWait(26.782,29.701)
    $ speak(JECKA, "Cause you can never replace her with money?")
    $ setWait(29.701,38.961)
    $ speak(NICOLE, "No there's a fucking trust fund and I can't touch it 'till I'm 35. All we get is a monthly stipend, I can't move to LA or anything.")
    show jecka sc3:
        rightcenterstage
    $ setWait(38.961,43.632)
    $ speak(JECKA, "Nicole this might be a weird question but uh...")
    $ setWait(43.632,46.969)
    $ speak(JECKA, "Did you cry at all after your Mom died?")
    show nicole sc3:
        leftcenterstage

    $ setWait(46.969,50.847)
    $ speak(NICOLE, "No. But I used it to get out of some stuff, does that count?")
    show jecka sc3 worried:
        rightcenterstage

    $ setWait(50.847,54.268)
    $ speak(JECKA, "Y-you seriously need to be on something.")
    $ setWait(54.268,54.977)
    $ speak(NICOLE, "I am.")
    $ setWait(54.977,57.312)
    $ speak(JECKA, "Something other than xanax and percocet.")
    $ setWait(57.312,58.897)
    $ speak(NICOLE, "I have vicodin too now.")
    show jecka sc3 angry:
        rightcenterstage

    $ setWait(58.897,62.276)
    $ speak(JECKA, "Do you really not get how sad this is or are you just fucking with me?")
    $ setWait(62.276,63.735)
    $ speak(NICOLE, "Can it be both?")
    show jecka sc3 worried:
        rightcenterstage

    $ setWait(63.735,71.368)
    $ speak(JECKA, "Again like, I'm sorry it went down like that. I was passed out and I couldn't really... it's a probably a lot to handle.")
    show nicole sc3 angry:
        leftcenterstage

    $ setWait(71.368,72.369)
    $ speak(NICOLE, "Yeah no shit.")
    show jecka sc3:
        rightcenterstage

    $ setWait(72.369,75.747)
    $ speak(JECKA, "That's what I mean, shouldn't you go to a therapist or talk to someone?")
    $ setWait(75.747,81.795)
    $ speak(NICOLE, "Is this gonna be a thing where you break down and cry for me or are you doing this to make you feel better?")
    show jecka sc3 worried:
        rightcenterstage
    $ setWait(81.795,84.423)
    $ speak(JECKA, "...Can it be both?")
    $ setWait(84.423,87.342)
    $ speak(NICOLE, "\"I'm going to class, where you headed Nicole?\"")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
label scene_0046:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0046.mp3")
    scene home nicole int

    show nicole sc1 smoke:
        leftcenterstage

    show jecka sc1 smoke:
        rightcenterstage

    show smoke:
        xalign 0.0
        yalign 0.0

    $ setWait(0.043,2.421)
    $ speak(NICOLE, "Why's smoking indoors so bad anyway?")
    $ setWait(2.421,4.423)
    $ speak(JECKA, "Cause it makes the carpet smell like cigarettes.")
    $ setWait(4.423,6.925)
    $ speak(NICOLE, "But it smells good, cigarettes are like air fresheners.")
    $ setWait(6.925,10.304)
    $ speak(JECKA, "They make you look cool too. I feel like a doctor in an 80's movie.")
    $ setWait(10.304,13.849)
    $ speak(NICOLE, "Yeah take a fatass drag before you tell a mother of 3 she has cancer.")
    $ setWait(13.849,15.851)
    $ speak(JECKA, "Like sorry bitch I'm just livin' over here.")
    $ setWait(15.851,17.895)
    $ speak(NICOLE, "Emphysema? Never heard of her.")
    $ setWait(17.895,22.024)
    $ speak(JECKA, "I'm so glad we could do this, it's so hard to smoke in front of the school now.")
    $ setWait(22.024,22.941)
    $ speak(NICOLE, "What happened?")
    $ setWait(22.941,29.615)
    $ speak(JECKA, "So my perfect time to go out an do it was like 9, 9:30, and in the last few weeks the fucking counselor is always out there trying to talk to me.")
    $ setWait(29.615,30.699)
    $ speak(NICOLE, "Cause you're in trouble?")
    $ setWait(30.699,37.08)
    $ speak(JECKA, "No that's why it's weird. It's like little small talk, commenting on my outfit, \"you're too pretty to smoke,\" it just ruins my whole morning now.")
    $ setWait(37.08,42.628)
    $ speak(NICOLE, "Oh I know what you're talking about, and no matter where you are he always finds you.\nDoes he use the dress code to hit on you?")
    $ setWait(42.628,46.798)
    $ speak(JECKA, "Literally every time.\n\"That looks a little low cut for school\"-- Looks right down the titties.")
    $ setWait(46.798,50.552)
    $ speak(NICOLE, "Yeah when they catch you alone they savor the fuck out of that good samaratin stare.")
    $ setWait(50.552,55.057)
    $ speak(JECKA, "Like how are you this horny at your job?\nGo look at porn on your work computer and get fired for it later.")
    $ setWait(55.057,57.225)
    $ speak(NICOLE, "And he's fully aware of the leverage game too.")
    $ setWait(57.225,63.19)
    $ speak(JECKA, "Exactly. \"I'm the cool counselor, you can smoke\" but as soon as I tell the principal he's flirting with me he'll immediately rat.")
    $ setWait(63.19,66.777)
    $ speak(NICOLE, "Wow so it's either don't smoke, or smoke and get your titties stared at.")
    $ setWait(66.777,70.238)
    $ speak(JECKA, "Easily the second one. I literally can't function without this now.")
    $ setWait(70.238,72.783)
    $ speak(NICOLE, "I still haven't found a drug where I function.")
    $ setWait(72.783,76.244)
    $ speak(JECKA, "It's like you turn 12 and you can't have anything perfect anymore.")
    show gamer_brother behind smoke:
        off_left
        xzoom -1
        linear 0.7 leftstage

    $ setWait(76.244,78.288)
    $ speak(GAMER_BROTHER, "What the hell are you guys doing in here??")
    show jecka sc1 surprised:
        rightcenterstage

    show nicole sc1 surprised:
        leftcenterstage
        pause 0.2
        xzoom -1

    $ setWait(78.288,78.83)
    $ speak(JECKA, "Oh shit.")
    $ setWait(78.83,80.832)
    $ speak(NICOLE, "Uh doing what? I don't know what you're talking about.")
    show gamer_brother:
        leftstage
        xzoom -1
        linear 1.4 leftmidstage

    $ setWait(80.832,84.002)
    $ speak(GAMER_BROTHER, "You see all the smoke in here, Mom said you can't smoke in the house!")
    show nicole sc1:
        leftcenterstage
        xzoom -1

    show jecka sc1:
        rightcenterstage

    $ setWait(84.002,88.382)
    $ speak(NICOLE, "Mom also said \"move the fuck out, you're 27\" but I guess that didn't register either.")
    $ setWait(88.382,90.842)
    $ speak(GAMER_BROTHER, "As if, like I don't even know what you're talking about.")
    $ setWait(90.842,95.472)
    $ speak(NICOLE, "Sorry I didn't know the basement was your video game office you happen to sleep in 7 nights a week.")
    $ setWait(95.472,97.766)
    $ speak(JECKA, "Office sleep 7 nights a week, workin' hard.")
    $ setWait(97.766,101.228)
    $ speak(GAMER_BROTHER, "I don't sleep there every night, okay? I got other places to be and shit.")
    $ setWait(101.228,104.147)
    $ speak(NICOLE, "Since when are you so defensive about living in the basement? I thought you liked it.")
    $ setWait(104.147,106.483)
    $ speak(GAMER_BROTHER, "I'm not defensive-- and I don't even sleep there!")
    show nicole sc1:
        leftcenterstage
        xzoom 1

    $ setWait(106.483,108.068)
    $ speak(NICOLE, "Ohhh I know why.")
    $ setWait(108.068,108.652)
    $ speak(GAMER_BROTHER, "What??")
    show nicole sc1:
        leftcenterstage
        xzoom -1

    $ setWait(108.652,111.154)
    $ speak(NICOLE, "You're trying to look cool cause there's a girl here.")
    $ setWait(111.154,111.905)
    $ speak(GAMER_BROTHER, "No!")

    show jecka sc1 smile:
        rightcenterstage

    $ setWait(111.905,113.74)
    $ speak(JECKA, "It's the cigarettes, they make me look hot.")
    show jecka sc1:
        rightcenterstage

    $ setWait(113.74,119.454)
    $ speak(GAMER_BROTHER, "Look all I did was come up here starving for lunch, and now my appetite's ruined cause of how bad it smells in here now.")
    $ setWait(119.454,121.707)
    $ speak(JECKA, "Yeah I never wanna eat after I smoke either.")
    show nicole sc1 smile:
        leftcenterstage
        xzoom 1
    $ setWait(121.707,124.001)
    $ speak(NICOLE, "Me too, cigarettes are actually kinda healthy.")
    $ setWait(124.001,125.585)
    $ speak(JECKA, "Newport's my new personal trainer.")
    $ setWait(125.585,128.505)
    $ speak(GAMER_BROTHER, "Do whatever the fuck you want cause I'm snitching hard, bro!")
    show jecka sc1:
        rightcenterstage
    $ setWait(128.505,129.84)
    $ speak(JECKA, "So not the way to win me over.")
    show nicole sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(129.84,132.467)
    $ speak(NICOLE, "Shh-- Come on, can't you just go back in the basement and play with your toys?")
    show gamer_brother:
        leftmidstage
        xzoom -1
        pause 2
        xzoom 1
        linear 2 leftstage

    $ setWait(132.467,135.846)
    $ speak(GAMER_BROTHER, "Video games are not toys! That's it, I'm calling Mom!")
    show nicole sc1 surprised:
        leftcenterstage
        xzoom -1
    $ setWait(135.846,137.264)
    $ speak(NICOLE, "Okay okay wait!")
    show gamer_brother:
        leftstage
        xzoom -1
    $ setWait(137.264,138.974)
    $ speak(GAMER_BROTHER, "This better be good.")
    hide smoke with Dissolve (0.8)
    menu:
        "SOCIALLY SACRIFICE JECKA":
            jump scene_0047
        "USE HIS OBESITY\nAGAINST HIM":
            jump scene_0050
label scene_0047:
    $ setVoiceTrack("audio/Scenes/0047.mp3")
    scene home nicole int
    show gamer_brother:
        leftstage
        xzoom -1

    show nicole sc1:
        leftcenterstage
        xzoom -1
        pause 3
        linear 2.5 off_left

    show jecka sc1:
        rightcenterstage

    $ setWait(0.037,6.418)
    $ speak(NICOLE, "Uh... let me get the smoke odor spray in my room. You guys just chat while I'm gone.")
    show gamer_brother:
        leftstage
        xzoom -1
        linear 2.5 leftcenterstage

    $ setWait(6.418,9.296)
    $ speak(GAMER_BROTHER, "...But yeah uh, it's an office.")
    $ setWait(9.296,10.464)
    $ speak(JECKA, "In the basement?")
    $ setWait(10.464,12.091)
    $ speak(GAMER_BROTHER, "It's a basement office.")
    $ setWait(12.091,13.133)
    $ speak(JECKA, "Right.")
    $ setWait(13.133,14.885)
    $ speak(GAMER_BROTHER, "So you hang out a lot?")
    $ setWait(14.885,16.845)
    $ speak(JECKA, "I guess? Doesn't everybody?")
    $ setWait(16.845,20.724)
    $ speak(GAMER_BROTHER, "Oh well y'know some people get busy with school and stuff.")
    $ setWait(20.724,22.184)
    $ speak(JECKA, "Are you in school?")
    $ setWait(22.184,27.147)
    $ speak(GAMER_BROTHER, "Taking a hiatus kinda. Was working on my masters in... game design.")
    $ setWait(27.147,28.148)
    $ speak(JECKA, "Where was that?")
    $ setWait(28.148,30.276)
    $ speak(GAMER_BROTHER, "DeVry, kinda under the radar.")
    $ setWait(30.276,32.444)
    $ speak(JECKA, "Not really, they're on TV everyday.")
    $ setWait(32.444,35.614)
    $ speak(GAMER_BROTHER, "But yeah all that stuff's boring, you like hanging out here?")
    $ setWait(35.614,36.532)
    $ speak(JECKA, "Not right now.")
    $ setWait(36.532,41.12)
    $ speak(GAMER_BROTHER, "Cause even if Nicole isn't around you can still come here if you want. I like hanging out.")
    $ setWait(41.12,45.541)
    $ speak(JECKA, "You wanna hang out with a high school girl by yourself? How old are you?")
    $ setWait(45.541,49.67)
    $ speak(GAMER_BROTHER, "Twenty uh... Twenty-seven. But it's just a number like whatever.")
    $ setWait(49.67,50.462)
    $ speak(JECKA, "I like numbers.")
    $ setWait(50.462,54.049)
    $ speak(GAMER_BROTHER, "You like numbers? Yeah yeah numbers are cool fuckin' math 'n shit.")
    $ setWait(54.049,57.553)
    $ speak(JECKA, "Math yeah, what's 48 divided by 4?")
    $ setWait(57.553,61.265)
    $ speak(GAMER_BROTHER, "Oh shit um... 12! It's 12, right?")
    $ setWait(61.265,62.266)
    $ speak(JECKA, "Yeah that's right.")
    show gamer_brother smile:
        leftcenterstage
        xzoom -1
    $ setWait(62.266,64.476)
    $ speak(GAMER_BROTHER, "Cool yeah, why do you ask?")
    $ setWait(64.476,67.98)
    $ speak(JECKA, "Because when you learned how to solve that I wasn't even alive.")
    stop ambient fadeout 1
    jump scene_0048
label scene_0048:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0048.mp3")
    play ambient "audio/Ambience/House_Ambience_2.mp3" fadein 1
    scene bedroom nicole
    show nicole sc1 smile:
        rightmidstage
        xzoom -1

    $ setWait(0.038,3.124)
    $ speak(NICOLE, "Tabloids are such a guilty pleasure.")
    $ setWait(3.124,7.128)
    $ speak(NICOLE, "\"Zac Efron gay??\" My condolences to the hos.")
    show jecka sc1 angry:
        off_left
        xzoom -1
        linear 1 leftstage

    $ setWait(7.128,8.921)
    $ speak(JECKA, "What the fuck is this??")
    show nicole sc1:
        rightmidstage

    $ setWait(8.921,9.672)
    $ speak(NICOLE, "A bedroom.")
    show jecka sc1 angry:
        leftstage
        xzoom -1
        linear 1.5 centerstage

    $ setWait(9.672,13.092)
    $ speak(JECKA, "You really left me with your brother to go up here and read a magazine?")
    $ setWait(13.092,14.969)
    $ speak(NICOLE, "I didn't think you'd stay down there that long.")
    $ setWait(14.969,17.597)
    $ speak(JECKA, "Cause I thought you were coming back with the smoke spray?")
    $ setWait(17.597,20.892)
    $ speak(NICOLE, "Yeah sorry sometimes I just disassociate.")
    $ setWait(20.892,22.393)
    $ speak(JECKA, "Do you even know what that means?")
    $ setWait(22.393,25.313)
    $ speak(NICOLE, "No but I heard a girl say it once, sounded like a good excuse.")
    $ setWait(25.313,27.69)
    $ speak(JECKA, "You have no idea how awkward that was!")
    $ setWait(27.69,29.942)
    $ speak(NICOLE, "I was hearing music down there, I thought you were having fun.")
    $ setWait(29.942,34.405)
    $ speak(JECKA, "No he just put on a bunch of techno music, and then he got mad after I called it techno.")
    $ setWait(34.405,35.156)
    $ speak(NICOLE, "Breakbeat.")
    $ setWait(35.156,37.867)
    $ speak(JECKA, "I was about to break the fucking stereo before I came up here.")
    $ setWait(37.867,40.745)
    $ speak(NICOLE, "Okay so he talked to you and played some shitty music, what's the big deal?")
    $ setWait(40.745,42.872)
    $ speak(JECKA, "Your brother was hitting on me, Nicole!")
    $ setWait(42.872,43.831)
    $ speak(NICOLE, "Seriously?")
    $ setWait(43.831,47.96)
    $ speak(JECKA, "He was asking me to come over even when you weren't here, what's that sound like to you?")
    $ setWait(47.96,49.337)
    $ speak(NICOLE, "Sounds like he wants to score.")
    $ setWait(49.337,54.258)
    $ speak(JECKA, "And you went up in your little room and let it happen.\nI can never come here again, it's too awkward now!")
    $ setWait(54.258,57.47)
    $ speak(NICOLE, "That's a little dramatic. He's in the basement most of the time anyway.")
    $ setWait(57.47,59.972)
    $ speak(JECKA, "But what if he comes up?? It's just weird now.")
    $ setWait(59.972,61.432)
    $ speak(NICOLE, "So you're just never coming back?")
    $ setWait(61.432,63.267)
    $ speak(JECKA, "Unless you kill your brother, no.")
    show nicole sc1 sad:
        rightmidstage
        xzoom -1
    $ setWait(63.267,64.685)
    $ speak(NICOLE, "But then I gotta go to jail.")
    $ setWait(64.685,67.772)
    $ speak(JECKA, "Don't even stress over it, I don't really think I wanna hang out anymore anyway.")
    show nicole sc1 angry:
        rightmidstage
        xzoom -1

    $ setWait(67.772,71.025)
    $ speak(NICOLE, "Are you serious? You get hit on by gross weird guys all the time.")
    $ setWait(71.025,76.989)
    $ speak(JECKA, "Yeah but after that they're blocked out of my memory. If I have one who's always at my friend's house I can't do that anymore.")
    $ setWait(76.989,80.952)
    $ speak(JECKA, "It's like a Jewish girl marrying Neo-Nazi, she'll never not think about the holocaust.")
    show nicole sc1:
        rightmidstage
        xzoom -1

    $ setWait(80.952,83.204)
    $ speak(NICOLE, "You are being so dramatic right now.")
    $ setWait(83.204,84.705)
    $ speak(JECKA, "It's like you don't even fucking care!")
    show jecka sc1 angry:
        xzoom 1
        centerstage
        linear 1.4 off_left

    $ setWait(84.705,88.084)
    $ speak(JECKA, "Okay bye Nicole! I'm done!")
    show nicole sc1:
        rightmidstage
        xzoom -1
        linear 1.7 leftcenterstage
    $ setWait(88.084,91.045)
    $ speak(NICOLE, "Wait were you actually like-- ugh god dammit...")
    stop ambient fadeout 1
    jump scene_0049
label scene_0049:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.9 alpha 0.0

    show title_9am onlayer screens
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter

    $ setVoiceTrack("audio/Scenes/0049.mp3")
    scene school ext 3
    hide title_9am onlayer screens
    show jecka sc3 smoke:
        leftmidstage
        xzoom -1
    $ setWait(2.337,4.839)
    $ speak(JECKA, "Camel Crush, the most interactive cigarette.")
    show nicole sc3:
        off_left
        linear 3.9 off_right

    show jecka sc3 smoke:
        leftmidstage
        xzoom -1
        pause 0.8
        xzoom 1
    $ setWait(4.839,7.3)
    $ speak(JECKA, "...")
    $ setWait(7.3,10.637)
    $ speak(JECKA, "9:10 in the morning, so far so good...")

    show counselor 1 smile:
        off_left
        xzoom -1
        linear 2 leftmidstage

    show jecka sc3 smoke:
        leftmidstage
        pause 1.2
        linear 0.4 leftcenterstage

    $ setWait(10.637,16.142)
    $ speak(COUNSELOR, "Jessica! Aren't you a sight for sore eyes, enjoying yourself out here yet again?")
    $ setWait(16.142,17.102)
    $ speak(JECKA, "I guess.")
    $ setWait(17.102,20.146)
    $ speak(COUNSELOR, "You guess? Is everything okay?")
    $ setWait(20.146,22.148)
    $ speak(JECKA, "No no, everything's okay.")
    $ setWait(22.148,26.945)
    $ speak(COUNSELOR, "Good, and if it ever isn't you know I'm always open to talk about it.")
    $ setWait(26.945,29.322)
    $ speak(JECKA, "Totally yeah, thanks.")
    $ setWait(29.322,34.869)
    $ speak(COUNSELOR, "By the way you're looking beautiful today as always, I hope your vice here won't tamper with that.")
    $ setWait(34.869,36.663)
    $ speak(JECKA, "Got it covered, don't worry.")
    $ setWait(36.663,39.708)
    $ speak(COUNSELOR, "So what have you been up to over the weekend?")
    $ setWait(39.708,44.504)
    $ speak(JECKA, "Um... I downloaded Tha Carter 3 off Limewire.")
    $ setWait(44.504,50.51)
    $ speak(COUNSELOR, "Oh I see. Is that a movie? I'm not familiar with the first two Carters.")
    $ setWait(50.51,51.636)
    $ speak(JECKA, "It's an album.")
    $ setWait(51.636,54.347)
    $ speak(COUNSELOR, "Right. Are you liking it so far?")
    $ setWait(54.347,55.432)
    $ speak(JECKA, "Doesn't everybody?")
    $ setWait(55.432,61.438)
    $ speak(COUNSELOR, "Well hopefully they could play some of it at homecoming this year if it's school appropriate.")
    $ setWait(61.438,62.897)
    $ speak(JECKA, "Yeah if I'm even going.")
    $ setWait(62.897,66.276)
    $ speak(COUNSELOR, "Now you wouldn't be having trouble finding a date, would you?")
    $ setWait(66.276,67.152)
    $ speak(JECKA, "Excuse me?")
    $ setWait(67.152,72.323)
    $ speak(COUNSELOR, "It's just that smoking habit of yours might leave a smell that could put the boys off.")
    $ setWait(72.323,74.2)
    $ speak(JECKA, "Really don't think it puts any guy off.")
    $ setWait(74.2,80.999)
    $ speak(COUNSELOR, "Well in any event, if you ever need to change to get the smell off you're always welcome to use my office.")
    $ setWait(80.999,83.084)
    $ speak(JECKA, "Why wouldn't I just use the locker room?")
    $ setWait(83.084,91.301)
    $ speak(COUNSELOR, "The gym teachers would catch that smell immediately and bombard you with questions. Though in my office it would be our little secret.")
    $ setWait(91.301,97.849)
    $ speak(COUNSELOR, "High school can be very hard so it helps to have an adult who really understands you.")
    $ setWait(97.849,100.894)
    $ speak(JECKA, "Totally yeah uh... so is that it?")
    $ setWait(100.894,103.646)
    $ speak(COUNSELOR, "Now you're not trying to get rid of me, are you?")
    $ setWait(103.646,105.19)
    $ speak(JECKA, "Why would I ever wanna do that?")
    $ setWait(105.19,112.822)
    $ speak(COUNSELOR, "Just playing around, but before I go I just need to remind you of the school's dress code once again.")
    $ setWait(112.822,113.698)
    $ speak(JECKA, "What about it?")
    show counselor 1 smile:
        leftmidstage
        xzoom -1
        linear 2 xalign 0.19
    $ setWait(113.698,119.037)
    $ speak(COUNSELOR, "I'm seeing your shirt alone has a few infractions.")
    $ setWait(119.037,120.163)
    $ speak(JECKA, "You get a good look?")
    show counselor 1:
        xalign .19
        linear 0.6 leftmidstage

    show jecka sc3 smoke:
        leftcenterstage
        pause 0.4
        xzoom -1

    show jeffery sc2 angry:
        xzoom -1
        off_right
        linear 0.35 rightmidstage

    show nicole sc3 angry:
        xzoom -1
        off_right
        linear 0.7 rightstage

    $ setWait(120.163,120.747)
    $ speak(NICOLE, "Bitch!")
    $ setWait(120.747,122.207)
    $ speak(JEFFERY, "Hey what's that for??")
    $ setWait(122.207,125.418)
    $ speak(NICOLE, "For reading your little anime book in front of me you fuckin' Lego collector!")
    $ setWait(125.418,128.588)
    $ speak(JEFFERY, "I already said this, it's called manga!")
    $ setWait(128.588,132.175)
    $ speak(NICOLE, "I'm gonna call your Mom and tell her \"sorry\" she'll never have grand kids.")
    $ setWait(132.175,134.219)
    $ speak(JEFFERY, "Wha- No! Don't kick me down there!")
    $ setWait(134.219,141.726)
    $ speak(NICOLE, "I don't need to, cause the more Mario trivia you know, the less women wanna fuck you.\nAnd you know a whole lot of Mario trivia, don't you Jeffery?")
    $ setWait(141.726,145.021)
    $ speak(JEFFERY, "M-moreso the canon of the mushroom kingdom.")
    $ setWait(145.021,147.732)
    $ speak(NICOLE, "...You are gonna fuck so many kids in your 30's.")
    $ setWait(147.732,151.194)
    $ speak(JEFFERY, "How do video games and anime make me a kid liker, huh?")
    $ setWait(151.194,154.28)
    $ speak(NICOLE, "That's like asking \"how does heroin make you a drug addict\".")
    $ setWait(154.28,159.536)
    $ speak(JEFFERY, "I'm getting real tired of you picking on me! It won't be so fun when the shoe's on the other foot!")
    $ setWait(159.536,163.373)
    $ speak(NICOLE, "Are you threatening me?\n...Are you threatening me in Skechers?")
    $ setWait(163.373,164.707)
    $ speak(JEFFERY, "Well um uh...")
    $ setWait(164.707,168.628)
    $ speak(NICOLE, "I'll take the gun you're saving for the cheerleaders and shoot you in the fucking face with it.")
    show counselor 1 angry:
        xzoom -1
        leftmidstage
        linear 1.1 rightmidstage

    show jeffery sc2:
        xzoom -1
        rightmidstage
        pause 0.7
        linear 0.8 rightcenterstage

    $ setWait(168.628,171.339)
    $ speak(COUNSELOR, "Alright that is quite enough, Nicole!")
    $ setWait(171.339,172.382)
    $ speak(NICOLE, "What!? What'd I do?")
    $ setWait(172.382,178.054)
    $ speak(COUNSELOR, "What I've heard in your verbal attack on Jeffery is very troubling and downright heinous!")
    $ setWait(178.054,181.558)
    $ speak(JEFFERY, "Yeah you forgot everything they said in the bullying assembly.")
    $ setWait(181.558,182.642)
    $ speak(NICOLE, "Yeah those work.")
    $ setWait(182.642,189.19)
    $ speak(COUNSELOR, "Confronted by a staff member and not even an ounce of remorse?\nThis is how Virginia Tech happened, Nicole.")
    show nicole sc3:
        xzoom -1
        rightstage
    $ setWait(189.19,192.36)
    $ speak(NICOLE, "...Wait, do you mean he's doing the shooting? Cause you should probably talk to him then.")
    show counselor 1:
        xzoom 1
        rightmidstage

    $ setWait(192.36,196.531)
    $ speak(COUNSELOR, "Go to class, Jeffery. I'll deal with this troubled student myself.")
    show jeffery sc2 smile:
        xzoom -1
        rightcenterstage
        pause 0.6
        xzoom 1
        linear 2.8 off_left

    $ setWait(196.531,199.701)
    $ speak(JEFFERY, "Thanks, you've always had the backs of us students.")
    show counselor 1 angry:
        xzoom -1
        rightmidstage
    $ setWait(199.701,206.916)
    $ speak(COUNSELOR, "This is mandatory counseling, Nicole!\nYou will be in my office everyday for the rest of the year until you show improvement!")
    show nicole sc3:
        xzoom -1
        rightstage
    $ setWait(206.916,208.918)
    $ speak(NICOLE, "Fuckin' everyday? For how long??")
    $ setWait(208.918,218.761)
    $ speak(COUNSELOR, "You'll be excused from your classes for one hour.\nThis used to be my break time but now I'll be seeing you in my office 9AM sharp starting tomorrow. Is that clear?")
    $ setWait(218.761,220.346)
    $ speak(NICOLE, "Dude that's so early!")
    $ setWait(220.346,221.764)
    $ speak(COUNSELOR, "Is that clear??")
    $ setWait(221.764,223.141)
    $ speak(NICOLE, "Sure whatever.")
    show counselor 1:
        rightmidstage
        xzoom -1
        linear 2.3 off_right

    $ setWait(223.141,226.311)
    $ speak(COUNSELOR, "Now off to class, both of you.")
    $ setWait(226.311,229.397)
    $ speak(NICOLE, "How was that rest of the year punishment?")
    $ setWait(229.397,233.651)
    $ speak(JECKA, "Um... what did Jeffery do?")
    show nicole sc3:
        rightstage
        xzoom -1
        linear 1.5 rightcenterstage

    $ setWait(233.651,234.819)
    $ speak(NICOLE, "Nothing.")
    $ setWait(234.819,237.614)
    $ speak(JECKA, "Wait then why did you--...")
    $ setWait(237.614,241.034)
    $ speak(NICOLE, "You can smoke by yourself again, right?")
    $ setWait(241.034,245.163)
    $ speak(JECKA, "...That's the nicest thing anyone's ever done for me.")
    $ setWait(245.163,247.415)
    $ speak(NICOLE, "...That's kinda sad.")
    $ setWait(247.415,249.6)
    $ speak(JECKA, "Do you wanna hang out later?")

    show nicole sc3 smile:
        xzoom -1
        rightcenterstage

    $ setWait(249.6,252.25)
    $ speak(NICOLE, "I could hang out now, let's skip the fuck out of here.")
    $ setWait(252.25,256.8)
    $ speak(JECKA, "I really can't miss class today.\nAre you going somewhere anyway?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0050:
    $ setVoiceTrack("audio/Scenes/0050.mp3")
    scene home nicole int
    show gamer_brother:
        leftstage
        xzoom -1

    show nicole sc1:
        leftcenterstage
        xzoom -1

    show jecka sc1:
        rightcenterstage

    $ setWait(0.036,1.954)
    $ speak(NICOLE, "Wh-what about lunch?")
    show gamer_brother:
        leftstage
        xzoom -1
        linear 1 leftmidstage
    $ setWait(1.954,3.122)
    $ speak(GAMER_BROTHER, "What about lunch?")
    $ setWait(3.122,7.71)
    $ speak(NICOLE, "Don't call Mom we could just go get you a pizza and like don't even worry about it.")
    show jecka sc1 smile:
        rightcenterstage
    $ setWait(7.71,11.589)
    $ speak(JECKA, "Yeah you can't miss lunch you're gonna be sooo hungry.")

    show gamer_brother smile:
        xzoom -1
        leftmidstage

    $ setWait(11.589,13.257)
    $ speak(GAMER_BROTHER, "Aw say it like that again, that's hot.")
    show jecka sc1 angry:
        rightcenterstage

    $ setWait(13.257,13.841)
    $ speak(JECKA, "God dammit.")
    show gamer_brother:
        xzoom -1
        leftmidstage

    $ setWait(13.841,16.969)
    $ speak(NICOLE, "Dude we'll look the other way on your minor fetish and get you a pizza, okay?")
    show jecka sc1:
        rightcenterstage
    $ setWait(16.969,18.054)
    $ speak(JECKA, "Does he have a major fetish?")
    show nicole sc1:
        leftcenterstage
        xzoom 1

    $ setWait(18.054,19.972)
    $ speak(NICOLE, "No his major fetish is a minor fetish.")
    $ setWait(19.972,20.765)
    $ speak(JECKA, "So what's the fetish?")
    $ setWait(20.765,22.141)
    $ speak(NICOLE, "I told you, a minor fetish.")
    $ setWait(22.141,24.185)
    $ speak(JECKA, "I know it's a minor fetish, what's the fetish for?")
    $ setWait(24.185,25.061)
    $ speak(NICOLE, "Minors.")
    $ setWait(25.061,26.187)
    $ speak(JECKA, "Like guys that dig coal?")
    $ setWait(26.187,27.229)
    $ speak(NICOLE, "Not those minors.")
    $ setWait(27.229,28.522)
    $ speak(JECKA, "So shitty baseball players?")
    $ setWait(28.522,29.315)
    $ speak(NICOLE, "What? No!")
    $ setWait(29.315,30.733)
    $ speak(JECKA, "Then what's the fetish?")
    $ setWait(30.733,34.779)
    $ speak(NICOLE, "Um... He's into girls under the age of 18.")
    show jecka sc1 worried:
        rightcenterstage

    $ setWait(34.779,37.323)
    $ speak(JECKA, "Oh that's not good... Why are we getting him pizza?")
    $ setWait(37.323,39.2)
    $ speak(GAMER_BROTHER, "Are you guys actually gonna get me food?")
    show nicole sc1:
        leftcenterstage
        linear 1.9 rightstage

    show jecka sc1:
        rightcenterstage

    $ setWait(39.2,40.993)
    $ speak(NICOLE, "Yeah sure, we'll pick it up somewhere. Let's go.")
    $ setWait(40.993,43.412)
    $ speak(GAMER_BROTHER, "Wait I didn't even tell you what I wanted on the pizza!")
    show nicole sc1:
        rightstage
        xzoom -1
    $ setWait(43.412,44.538)
    $ speak(NICOLE, "What is it?")
    $ setWait(44.538,59.512)
    $ speak(GAMER_BROTHER, "Okay uh... Pepperoni, ham, bacon, meatballs, sausage, and sliced sausage too so like the crumbled American sausage with the more Italian sliced sausage, chicken, buffalo chicken, extra cheese...")
    $ setWait(59.512,61.138)
    $ speak(JECKA, "Is this a pizza or a grocery list?")
    $ setWait(61.138,62.223)
    $ speak(GAMER_BROTHER, "So you got all that?")
    $ setWait(62.223,64.558)
    $ speak(NICOLE, "Uh yeah, could we borrow a 20?")
    show gamer_brother smile:
        leftmidstage
        xzoom -1
        linear 1 leftcenterstage
    $ setWait(64.558,68.187)
    $ speak(GAMER_BROTHER, "Aw yeah here ya go, Mom left me extra pizza money today anyway.")
    $ setWait(68.187,69.063)
    $ speak(JECKA, "At 27.")
    show nicole sc1:
        xzoom 1
        rightstage
        linear 0.7 off_right

    show jecka sc1:
        rightcenterstage
        xzoom -1
        linear 1.4 off_right

    $ setWait(69.063,71.941)
    $ speak(NICOLE, "Okay we'll be right back.")
    show gamer_brother smile:
        leftcenterstage
        xzoom -1
        pause 3.9
        xzoom 1
        linear 3 off_left

    $ setWait(71.941,77.279)
    $ speak(GAMER_BROTHER, "Fuckin' dumb bitches I had McDonald's in my room the whole time.\nNow I have two lunches.")
    stop ambient fadeout 1
    jump scene_0051
label scene_0051:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.9 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show barcade ext with Pause(2.252):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1
        parallel:
            linear 2.627 zoom 0.7 truecenter
    $ setVoiceTrack("audio/Scenes/0051.mp3")
    play ambient "audio/Ambience/Barcade_NoMusic_Ambience.mp3"
    scene barcade int
    show nicole sc1 angry:
        leftcenterstage

    show jecka sc1:
        rightcenterstage

    $ setWait(2.002,4.963)
    $ speak(NICOLE, "Ugh why didn't we call first? This is gonna take forever.")
    $ setWait(4.963,7.382)
    $ speak(JECKA, "Why did we even go to the barcade for a pizza?")
    show nicole sc1:
        leftcenterstage
    $ setWait(7.382,8.967)
    $ speak(NICOLE, "Why not? They have pizza.")
    $ setWait(8.967,12.429)
    $ speak(JECKA, "No but we could've gone to Joe's or Mama Lucia's.")
    $ setWait(12.429,13.763)
    $ speak(NICOLE, "Yeah, what's your point?")
    $ setWait(13.763,14.973)
    $ speak(JECKA, "It's gonna be shitty here.")
    $ setWait(14.973,17.142)
    $ speak(NICOLE, "We're in the beltway, the pizza's shitty everywhere.")
    $ setWait(17.142,18.059)
    $ speak(JECKA, "That makes sense.")
    show kyle sc1 smile:
        off_right
        linear 1.7 rightmidstage

    show jecka sc1:
        rightcenterstage
        pause 0.4
        xzoom -1

    $ setWait(18.059,21.396)
    $ speak(KYLE, "Oh hey guys, hey Jecka.")
    $ setWait(21.396,22.939)
    $ speak(JECKA, "...Who the fuck are you?")
    show kyle sc1:
        rightmidstage

    $ setWait(22.939,26.276)
    $ speak(KYLE, "I-I'm Kyle, I sat behind you in French last year.")
    $ setWait(26.276,27.068)
    $ speak(NICOLE, "Frenched who now?")
    $ setWait(27.068,32.532)
    $ speak(KYLE, "No French the language class, remember? I let you copy off my test?")
    $ setWait(32.532,34.075)
    $ speak(JECKA, "...Okay, hi.")
    $ setWait(34.075,37.829)
    $ speak(KYLE, "Yeah didn't think I'd run into anyone here, are you guys skipping too?")
    $ setWait(37.829,39.915)
    $ speak(NICOLE, "Maybe, why are you skipping?")
    $ setWait(39.915,43.71)
    $ speak(KYLE, "Aw just needed to blow off some steam, play a couple games here and stuff.")
    $ setWait(43.71,48.632)
    $ speak(NICOLE, "You skipped to play video games? That's really cool and would never discourage girls from having sex with you.")
    $ setWait(48.632,50.675)
    $ speak(KYLE, "Well why are you skipping?")
    $ setWait(50.675,52.594)
    $ speak(JECKA, "To get fucked up, why else?")
    $ setWait(52.594,56.097)
    $ speak(KYLE, "Cool yeah. So you wanna hang out?")
    $ setWait(56.097,59.309)
    $ speak(JECKA, "Do I wanna hang out or do I wanna go out?")
    $ setWait(59.309,61.144)
    $ speak(KYLE, "Uh both I don't know.")
    $ setWait(61.144,62.604)
    $ speak(JECKA, "No I don't even know you.")
    $ setWait(62.604,66.191)
    $ speak(KYLE, "We had class last year. You've gone out with guys you don't know before.")
    $ setWait(66.191,68.777)
    $ speak(NICOLE, "How would you know that if you only had one class with her?")
    show jecka sc1 angry:
        rightcenterstage
        xzoom -1
    $ setWait(68.777,69.736)
    $ speak(JECKA, "Yeah what the fuck.")
    $ setWait(69.736,72.822)
    $ speak(KYLE, "Forget that, c'mon what'd those other guys have that I didn't?")
    show jecka sc1:
        rightcenterstage
        xzoom -1
    $ setWait(72.822,74.449)
    $ speak(JECKA, "They were older and more attractive.")
    $ setWait(74.449,76.034)
    $ speak(KYLE, "So it's all about looks with you?")
    $ setWait(76.034,78.203)
    $ speak(JECKA, "It's not just looks they could buy me alcohol too.")
    show kyle sc1 sad:
        rightmidstage

    $ setWait(78.203,80.705)
    $ speak(KYLE, "But I let you copy off my test, you got a B+.")
    $ setWait(80.705,84.125)
    $ speak(JECKA, "What are we fucking over B+s now? At least lie and say it was an A.")
    $ setWait(84.125,86.169)
    $ speak(KYLE, "If it was an A would you have considered it more?")
    $ setWait(86.169,87.712)
    $ speak(NICOLE, "What do you think the answer is?")
    $ setWait(87.712,89.297)
    $ speak(KYLE, "Well what am I supposed to do?")
    $ setWait(89.297,91.341)
    $ speak(JECKA, "I don't know, literally don't be you?")
    show nicole sc1 smile:
        leftcenterstage

    $ setWait(91.341,93.259)
    $ speak(NICOLE, "Kill your mom. Even I'd go out with you then.")
    $ setWait(93.259,94.135)
    $ speak(KYLE, "What the fuck?")
    show jecka sc1 smile:
        rightcenterstage
        xzoom -1

    $ setWait(94.135,96.012)
    $ speak(JECKA, "Yeah actually then you'd be halfway cool.")
    $ setWait(96.012,97.764)
    $ speak(KYLE, "You guys can't mess around like that.")
    $ setWait(97.764,98.848)
    $ speak(NICOLE, "I'm not messing around.")
    $ setWait(98.848,101.643)
    $ speak(JECKA, "Yeah we're not. It's either me or your mom, pick one.")
    $ setWait(101.643,103.395)
    $ speak(KYLE, "Seriously? Come on, guys.")
    show jecka sc1:
        rightcenterstage
        xzoom -1

    show nicole sc1:
        leftcenterstage

    $ setWait(103.395,106.856)
    $ speak(JECKA, "Oh I am serious. Kill your mom and I'm all yours.")
    $ setWait(106.856,110.276)
    $ speak(KYLE, "Uh... --Aw damn I left my credit card in the car.")
    $ setWait(110.276,111.069)
    $ speak(NICOLE, "Credit card?")
    show kyle sc1:
        rightmidstage
        pause 1
        xzoom -1
    $ setWait(111.069,112.821)
    $ speak(KYLE, "Yeah hold on I'll be right back.")
    show kyle sc1:
        rightmidstage
        xzoom -1
        pause 0.25
        xzoom 1
    $ setWait(112.821,114.823)
    $ speak(NICOLE, "Wait, Visa? Discover? What's the credit limit?")
    $ setWait(114.823,119.202)
    $ speak(KYLE, "Oh no it's like the token credit card you swipe to play the games here.")
    show nicole sc1 angry:
        leftcenterstage

    $ setWait(119.202,122.247)
    $ speak(NICOLE, "This is why you're a virgin.")
    show kyle sc1 sad:
        rightmidstage
        xzoom -1
        linear 2.2 off_right

    show jecka sc1:
        rightcenterstage
        xzoom 1

    $ setWait(122.247,124.624)
    $ speak(JECKA, "It's like one step forward and twelve steps back.")
    show nicole sc1:
        leftcenterstage

    $ setWait(124.624,128.086)
    $ speak(NICOLE, "Oh my god I know...\nYou were convincing there for a second.")
    show jecka sc1 smile:
        rightcenterstage
        xzoom 1


    $ setWait(128.086,128.962)
    $ speak(JECKA, "I was?")
    show nicole sc1 smile:
        leftcenterstage

    $ setWait(128.962,131.339)
    $ speak(NICOLE, "\"Kill your mom and I'm all yours\" that was actually hot.")
    $ setWait(131.339,133.133)
    $ speak(JECKA, "\"I'm all yours\"")
    show nicole sc1 smile:
        leftcenterstage
        xzoom -1
        linear 2 off_farleft

    show jecka sc1:
        rightcenterstage
        xzoom 1
        pause 0.4
        linear 1.7 off_left

    $ setWait(133.133,134.884)
    $ speak(NICOLE, "Perfect timing.")
    $ setWait(134.884,137.22)
    $ speak(JECKA, "Is the box two colors or is that grease?")
    stop ambient fadeout 1
    jump scene_0052
label scene_0052:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0052.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3" fadein 1

    scene home nicole int

    show nicole sc1:
        xzoom -1
        off_right
        linear 3 centerstage

    show laptop:
        leftstage

    $ setWait(0.039,1.916)
    $ speak(NICOLE, "We got the pizza!")
    show jecka sc1 angry:
        off_right
        linear 2 rightmidstage



    $ setWait(1.916,3.334)
    $ speak(JECKA, "Fuck I forgot to buy cigarettes.")

    show nicole sc1:
        centerstage
        xzoom 1

    $ setWait(3.334,6.421)
    $ speak(NICOLE, "Now you remember, wait you're not old enough to buy any.")
    show jecka sc1:
        rightmidstage

    $ setWait(6.421,11.593)
    $ speak(JECKA, "No the little gas stations don't even card you. There's one right off the beltway but we didn't go back that way.")
    $ setWait(11.593,14.512)
    $ speak(NICOLE, "What are you talking about? That one cards you, they carded me.")
    $ setWait(14.512,15.805)
    $ speak(JECKA, "Was it the Indian guy?")
    $ setWait(15.805,16.431)
    $ speak(NICOLE, "Yeah?")
    $ setWait(16.431,19.767)
    $ speak(JECKA, "He'll always card you, go on the days when the Mexican guy's working there.")
    $ setWait(19.767,21.811)
    $ speak(NICOLE, "How the fuck would I know what days he's working there?")
    $ setWait(21.811,23.396)
    $ speak(JECKA, "When you have a car you'll know.")
    show nicole sc1:
        centerstage
        xzoom -1
    $ setWait(23.396,26.858)
    $ speak(NICOLE, "Dude where is he? The grease is gonna get solid.\nHello!?")
    $ setWait(26.858,28.193)
    $ speak(JECKA, "What if he's in the shower?")
    $ setWait(28.193,29.068)
    $ speak(NICOLE, "Good one.")
    show jecka sc1 worried:
        rightmidstage

    $ setWait(29.068,31.571)
    $ speak(JECKA, "Were there this many scuffs on the carpet before we left?")
    show nicole sc1 surprised:
        centerstage
        xzoom -1
        pause 2
        linear 1 xalign 0.13
    $ setWait(31.571,35.45)
    $ speak(NICOLE, "Holy shit what happened.\nWait his laptop's open out here.")
    $ setWait(35.45,36.659)
    $ speak(JECKA, "Is that usual?")
    show nicole sc1 sad:
        xzoom -1
        xalign 0.13

    $ setWait(36.659,39.245)
    $ speak(NICOLE, "Uhh-- Oh god, not with 20 porn tabs open.")
    $ setWait(39.245,40.747)
    $ speak(JECKA, "Literally 20??")
    show nicole sc1:
        xzoom -1
        xalign 0.13
    $ setWait(40.747,42.999)
    $ speak(NICOLE, "One, two, three... sixteen.")
    $ setWait(42.999,44.667)
    $ speak(JECKA, "Who needs that much porn at once?")
    $ setWait(44.667,49.339)
    $ speak(NICOLE, "People with more game systems than exes.\nEvery tab's a different fetish site too.")
    $ setWait(49.339,50.632)
    $ speak(JECKA, "Like what?")
    $ setWait(50.632,60.141)
    $ speak(NICOLE, "Uh... JigglyJihadists.com, BelowTheBorderLatinas.net, AsianGirlDynasty.org...")
    $ setWait(60.141,64.729)
    $ speak(JECKA, "I didn't think your brother would be into such... racially charged porn.")
    $ setWait(64.729,67.44)
    $ speak(NICOLE, "I didn't think my brother would be into women at all... Wait.")
    $ setWait(67.44,68.566)
    $ speak(JECKA, "Oh god what?")
    $ setWait(68.566,76.658)
    $ speak(NICOLE, "After those there's a bunch of... MILFdaycare.com, KidnappedBabysitters.html...")
    $ setWait(76.658,82.956)
    $ speak(NICOLE, "...BarelyLegal.gov, and AlmostLegal.co.jp?")
    show jecka sc1:
        rightmidstage

    $ setWait(82.956,84.791)
    $ speak(JECKA, "I've heard of \"barely legal\" what the hell is--")
    show nicole sc1 surprised:
        xalign 0.13
        xzoom -1
        linear 0.35 rightstage

    $ setWait(84.791,85.959)
    $ speak(NICOLE, "Holy fuck too young!!")
    show jecka sc1:
        rightmidstage
        linear 0.63 xalign 0.13
    $ setWait(85.959,86.668)
    $ speak(JECKA, "What is she Asian...")
    show jecka sc1 surprised:
        xalign 0.13
        xzoom -1
        linear 0.5 rightmidstage

    $ setWait(86.668,88.294)
    $ speak(JECKA, "Oh god that kind of too young!!")
    show nicole sc1 sad:
        rightstage
        xzoom -1
    $ setWait(88.294,90.672)
    $ speak(NICOLE, "The Russian roulette of internet history!")
    show jecka sc1 worried:
        rightmidstage
        xzoom -1
    $ setWait(90.672,91.881)
    $ speak(JECKA, "Are we in the system now?")
    $ setWait(91.881,93.716)
    $ speak(NICOLE, "I'm not a lawyer how the fuck should I know??")
    $ setWait(93.716,95.843)
    $ speak(JECKA, "We only looked for a second, five second rule, right?")
    $ setWait(95.843,98.346)
    $ speak(NICOLE, "That's for food on the floor not child porn!")
    $ setWait(98.346,99.055)
    $ speak(JECKA, "Oh my god.")
    show cop:
        off_right
        linear 0.5 rightstage

    show nicole sc1 surprised:
        rightstage
        xzoom -1
        pause 0.35
        xzoom 1
        linear 0.6 leftcenterstage

    show jecka surprised sc1:
        rightmidstage
        xzoom -1
        pause 0.3
        linear 0.4 rightcenterstage

    $ setWait(99.055,100.556)
    $ speak(COP, "What are you girls doing here??")
    $ setWait(100.556,102.642)
    $ speak(NICOLE, "I live here! What are you doing here?")
    $ setWait(102.642,106.521)
    $ speak(COP, "We made an arrest at this residence ten minutes ago but forgot to secure the evidence.")
    $ setWait(106.521,108.231)
    $ speak(NICOLE, "You arrested my brother??")
    $ setWait(108.231,110.817)
    $ speak(COP, "On possession of child pornography!")
    show cop:
        rightstage
        linear 2 xalign 0.13
        xzoom -1
    $ setWait(110.817,113.486)
    $ speak(COP, "If you'll excuse me I'll need that laptop-- Wait!")
    show jecka sc1 worried:
        rightcenterstage
        xzoom 1

    show nicole sc1 surprised:
        leftcenterstage
        xzoom -1
    $ setWait(113.486,114.028)
    $ speak(JECKA, "What?")
    $ setWait(114.028,117.49)
    $ speak(COP, "Were you looking at this AlmostLegal website while I was gone!?")
    $ setWait(117.49,119.45)
    $ speak(JECKA, "It was just left open like that, we swear!")
    $ setWait(119.45,122.996)
    $ speak(COP, "I don't know, you girls have a lot of explaining to do...")
    menu:
        "LIE TO A COP":
            jump scene_0053
        "BRIBE A COP":
            jump scene_0054
label scene_0053:
    $ setVoiceTrack("audio/Scenes/0053.mp3")
    scene home nicole int
    show nicole sc1:
        leftcenterstage
        xzoom -1

    show jecka sc1 worried:
        rightcenterstage

    show cop:
        xalign 0.13
        xzoom -1

    show laptop:
        leftstage

    $ setWait(0.037,3.541)
    $ speak(NICOLE, "Uh... I think you're the one who needs to explain.")
    show jecka sc1:
        rightcenterstage

    $ setWait(3.541,4.291)
    $ speak(JECKA, "He is?")
    $ setWait(4.291,8.546)
    $ speak(NICOLE, "Y-yeah because we might've seen the screen but look at the webcam above it.")

    show cop:
        xalign 0.13
        xzoom 1

    $ setWait(8.546,11.298)
    $ speak(COP, "I see it but I don't follow.")
    $ setWait(11.298,16.095)
    $ speak(NICOLE, "We're both still in high school, and you walked in on us shooting our own child porn video!")
    show cop:
        xalign 0.13
        xzoom -1
    $ setWait(16.095,20.891)
    $ speak(JECKA, "Um-- Yeah! And I'm pretty sure seeing it live is way more illegal than seeing it on a screen!")
    $ setWait(20.891,24.061)
    $ speak(NICOLE, "Caught right on video barging in on the set. Pathetic.")
    $ setWait(24.061,28.482)
    $ speak(COP, "I've never heard such BS in my life, you were standing here fully clothed.")
    $ setWait(28.482,30.609)
    $ speak(NICOLE, "Yeah cause you walked in on the start of the video.")
    $ setWait(30.609,32.361)
    $ speak(JECKA, "Right? What's porn without buildup?")
    $ setWait(32.361,34.822)
    $ speak(COP, "You had a pizza in your hand when I walked in!")
    show jecka sc1 worried:
        rightcenterstage
    $ setWait(34.822,35.448)
    $ speak(JECKA, "Oh shit.")
    $ setWait(35.448,39.493)
    $ speak(NICOLE, "Well no cause... I was playing the butch pizza delivery girl.")
    show jecka sc1:
        rightcenterstage
    $ setWait(39.493,42.538)
    $ speak(JECKA, "And I was playing the lipstick lesbian with no money for the pizza.")
    $ setWait(42.538,44.79)
    $ speak(NICOLE, "Yeah and I'm like \"Bitch how you gonna pay for this pizza?\"")
    show jecka sc1 angry:
        rightcenterstage

    $ setWait(44.79,47.418)
    $ speak(JECKA, "Then you walked in and ruined the whole scene.")
    $ setWait(47.418,52.673)
    $ speak(JECKA, "Now we gotta do it all over again. You're basically forcing us to make child porn twice, that's fucked up!")
    $ setWait(52.673,56.802)
    $ speak(NICOLE, "So go ahead, arrest us, cause there's gonna be some spicy outtakes played in court.")
    $ setWait(56.802,62.099)
    $ speak(COP, "Oh god-- look, girls. Why don't you just give me the laptop and we all forget we saw anything.")
    $ setWait(62.099,64.769)
    $ speak(JECKA, "So you can destroy the evidence against you? No thanks.")
    show nicole sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(64.769,67.146)
    $ speak(NICOLE, "Yeah get the fuck out of here before we call the other cops!")
    show cop:
        xalign 0.13
        xzoom -1
        linear 1.1 off_right
    $ setWait(67.146,69.106)
    $ speak(COP, "Why did they send me alone?")
    show jecka sc1:
        rightcenterstage

    $ setWait(69.106,70.9)
    $ speak(JECKA, "...God that was close.")
    show nicole sc1:
        leftcenterstage
        xzoom 1

    $ setWait(70.9,72.985)
    $ speak(NICOLE, "So if he's in jail you wanna eat this pizza with me?")
    $ setWait(72.985,74.487)
    $ speak(JECKA, "I'd rather not have gout.")
    stop ambient fadeout 1
    jump scene_0055
label scene_0054:
    $ setVoiceTrack("audio/Scenes/0054.mp3")
    scene home nicole int
    show nicole sc1 smile:
        leftcenterstage
        xzoom -1

    show jecka sc1 worried:
        rightcenterstage

    show cop:
        xalign 0.13
        xzoom -1

    show laptop:
        leftstage

    $ setWait(0.04,3.793)
    $ speak(NICOLE, "Not to change the subject but you look kinda hungry, dude.")
    $ setWait(3.793,4.544)
    $ speak(JECKA, "Oh my god...")
    $ setWait(4.544,6.88)
    $ speak(COP, "How can someone look hungry?")
    $ setWait(6.88,13.094)
    $ speak(NICOLE, "Just all that hard police work, y'know? Why don't you go ahead and pick up your evidence and take this pizza with you.")
    $ setWait(13.094,14.387)
    $ speak(COP, "What's on the pizza?")
    show jecka sc1:
        rightcenterstage

    $ setWait(14.387,15.805)
    $ speak(JECKA, "Everything but vegetables.")
    $ setWait(15.805,19.351)
    $ speak(COP, "You wouldn't be trying to bribe a police officer would you?")
    show nicole sc1:
        leftcenterstage
        xzoom -1
    $ setWait(19.351,24.189)
    $ speak(NICOLE, "Are you asking to assert your morals or asking to see if we'll up the ante?")
    $ setWait(24.189,28.109)
    $ speak(COP, "Let's just say the law's written in pencil. What else would you have for me?")
    $ setWait(28.109,28.985)
    $ speak(JECKA, "Jesus Christ...")
    $ setWait(28.985,30.612)
    $ speak(NICOLE, "Fifty dollars... cash.")
    $ setWait(30.612,32.906)
    $ speak(COP, "I'm not risking my pension over fifty dollars.")
    show nicole sc1 sad:
        leftcenterstage
        xzoom -1
    $ setWait(32.906,36.91)
    $ speak(NICOLE, "No no also um... Old white guy uhhhhh...")
    show nicole sc1:
        leftcenterstage
        xzoom -1
    $ setWait(36.91,39.412)
    $ speak(NICOLE, "I have my Dad's World War 2 DVDs.")
    show cop:
        xalign 0.13
        xzoom -1
        linear 1.2 rightmidstage
        xzoom 1

    show jecka sc1:
        rightcenterstage
        pause 1
        linear 3.2 off_left


    $ setWait(39.412,41.957)
    $ speak(COP, "Now you're talkin', keep going.")

    show nicole sc1:
        leftcenterstage
        xzoom 1


    $ setWait(41.957,46.586)
    $ speak(NICOLE, "You drive a hard bargain. We also have the complete series of Sex And The City on VHS.")
    $ setWait(46.586,48.713)
    $ speak(COP, "What kinda yuppie garbage is--")
    show nicole sc1 sad:
        leftcenterstage
        xzoom 1
    $ setWait(48.713,52.592)
    $ speak(NICOLE, "Sorry! Sorry sorry, did I say that? I meant... Home Improvement.")
    show nicole sc1:
        leftcenterstage
        xzoom 1
    $ setWait(52.592,55.887)
    $ speak(COP, "Oh now we're talkin'! Tim Allen, legend.")
    show jecka sc1 camera:
        xzoom -1
        off_left
        linear 1.5 leftmidstage
    $ setWait(55.887,59.599)
    $ speak(JECKA, "She's also got this old camera, it still shoots and everything, it's rolling right now.")
    show nicole sc1:
        xzoom -1
        leftcenterstage
        pause 1.6
        xzoom 1

    $ setWait(59.599,64.02)
    $ speak(NICOLE, "Yeah you could pawn that, then the 50 dollars turns into.. 57 dollars.")
    $ setWait(64.02,69.609)
    $ speak(COP, "Interesting... However you'll need to have way more than that if you want me to risk my pension.")
    $ setWait(69.609,72.612)
    $ speak(JECKA, "Damn. What if it was fifty-eight dollars, I found the lens cap.")
    $ setWait(72.612,77.283)
    $ speak(COP, "Again, lens cap or not, you still need to have way more than that.")
    $ setWait(77.283,79.911)
    $ speak(NICOLE, "What if I put on the table something I don't have?")
    $ setWait(79.911,80.954)
    $ speak(COP, "What's that?")
    $ setWait(80.954,82.205)
    $ speak(NICOLE, "A gag reflex?")
    show cop:
        rightmidstage
        pause .95
        linear 0.6 rightcenterstage

    $ setWait(82.205,84.249)
    $ speak(COP, "Aw hell yeah why didn't you say so?")
    show nicole sc1 angry:
        leftcenterstage

    $ setWait(84.249,85.041)
    $ speak(NICOLE, "God dammit.")
    $ setWait(85.041,85.583)
    $ speak(COP, "What?")
    $ setWait(85.583,88.67)
    $ speak(NICOLE, "I thought you'd feel bad for a minor offering head and just leave us alone.")
    show cop:
        rightcenterstage
        linear 0.5 rightmidstage

    $ setWait(88.67,92.34)
    $ speak(COP, "Minor? I thought you were 18, thank god no one saw me agree to that.")
    show nicole sc1:
        leftcenterstage
    $ setWait(92.34,94.217)
    $ speak(JECKA, "We have you on camera agreeing to that!")
    show nicole sc1:
        leftcenterstage
        xzoom -1
        pause 0.9
        xzoom 1

    $ setWait(94.217,96.302)
    $ speak(NICOLE, "Oh damn, you're fucked dude, sorry.")
    $ setWait(96.302,98.221)
    $ speak(COP, "How was I supposed to know how old you are??")
    $ setWait(98.221,100.849)
    $ speak(JECKA, "You're a literal cop you're supposed to ask for ID!")
    $ setWait(100.849,102.225)
    $ speak(NICOLE, "Still wanna keep that pension?")
    show cop:
        rightmidstage
        linear 4 rightstage

    $ setWait(102.225,107.48)
    $ speak(COP, "Okay okay, let's not do anything hasty now. I don't need anything, you're both free to go.")
    show nicole sc1 smile:
        leftcenterstage

    $ setWait(107.48,109.774)
    $ speak(NICOLE, "It was a pleasure doing business with you.")
    $ setWait(109.774,110.734)
    $ speak(COP, "Oh wait.")
    $ setWait(110.734,112.861)
    $ speak(JECKA, "The fuck do you want, ChomoCop?")
    $ setWait(112.861,114.446)
    $ speak(COP, "Can I still have the pizza?")
    show nicole sc1:
        leftcenterstage

    show pizza:
        parallel:
            leftcenterstage
            linear 0.75 rightstage
        parallel:
            alpha 0.0
            linear 0.1 alpha 1.0
            pause 0.4
            linear 0.3 alpha 0.0

    $ setWait(114.446,115.488)
    $ speak(NICOLE, "Yeah here ya go.")
    show cop:
        rightstage
        pause 1
        xzoom -1
        linear 1 off_right

    $ setWait(115.488,118.491)
    $ speak(COP, "Came for evidence, left with pizza.")
    show jecka sc1 worried:
        leftmidstage
        xzoom -1

    $ setWait(118.491,121.619)
    $ speak(JECKA, "...What are we gonna do when we're adults and can't pull that card anymore?")
    show nicole sc1 angry:
        leftcenterstage
        xzoom -1

    $ setWait(121.619,125.707)
    $ speak(NICOLE, "I'm pretty sure a cop getting bribery head is illegal regardless of what age you are.")
    stop ambient fadeout 1
    jump scene_0055
label scene_0055:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0055.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school courtyard
    show nicole sc3:
        leftcenterstage

    show jecka sc3:
        rightcenterstage

    $ setWait(0.048,5.845)
    $ speak(NICOLE, "So then it got to the part where he's like \"what do you mean 'you people'\" and I just turned the movie off and went to sleep.")
    $ setWait(5.845,8.264)
    $ speak(JECKA, "Oh yeah that's... wow.")
    $ setWait(8.264,11.768)
    $ speak(NICOLE, "Robert Downey should get back on heroin then his movies wouldn't suck anymore.")
    $ setWait(11.768,13.936)
    $ speak(JECKA, "Right? Yeah...")
    show nicole sc3 angry:
        leftcenterstage
    $ setWait(13.936,15.063)
    $ speak(NICOLE, "Am I boring you?")
    $ setWait(15.063,19.359)
    $ speak(JECKA, "What? No it's just like, I'm exhausted from yesterday.")
    show nicole sc3:
        leftcenterstage
    $ setWait(19.359,21.527)
    $ speak(NICOLE, "Yeah that was like an anomaly, holy shit.")
    show jecka sc3 angry:
        rightcenterstage
    $ setWait(21.527,26.574)
    $ speak(JECKA, "Was it? Or the week before that, or the week before that-- Why do our lives have to be so fucking eventful?")
    $ setWait(26.574,30.703)
    $ speak(NICOLE, "That's a legit question, shit...\nDo you believe in god?")
    show jecka sc3:
        rightcenterstage
    $ setWait(30.703,31.579)
    $ speak(JECKA, "Do you?")
    $ setWait(31.579,32.455)
    $ speak(NICOLE, "No.")
    $ setWait(32.455,34.415)
    $ speak(JECKA, "Me neither... You don't think--")
    show nicole sc3 angry:
        leftcenterstage

    $ setWait(34.415,36.751)
    $ speak(NICOLE, "We are not going to church.")
    show ring_woodburn onlayer screens

    show nicole sc3:
        leftcenterstage

    $ setWait(36.751,39.087)
    $ speak(NICOLE, "Don't know that number, wonder who this is.")
    $ setWait(39.087,42.548)
    $ speak(JECKA, "Lemme guess, bomb threat rapist murderer guy oh my god...")
    hide ring_woodburn onlayer screens

    $ setWait(42.548,44.133)
    $ speak(NICOLE, "Hello?")
    $ setWait(44.133,47.553)
    $ speak(JAILPHONE, "Hello, this is The Woodburn Correctional Holding Facility.")
    $ setWait(47.553,48.179)
    $ speak(JECKA, "I knew it.")
    $ setWait(48.179,49.847)
    $ speak(JAILPHONE, "You have a collect call from...")
    $ setWait(49.847,51.391)
    $ speak(GAMER_BROTHER, "It's your brother, bitch, pick up.")
    $ setWait(51.391,53.81)
    $ speak(JAILPHONE, "To accept these charges, press 1")
    $ setWait(53.81,54.894)
    $ speak(NICOLE, "Yeah whatever.")
    $ setWait(54.894,57.146)
    $ speak(GAMER_BROTHER, "Nicole why isn't Mom picking her phone up?")
    $ setWait(57.146,58.731)
    $ speak(NICOLE, "I don't know, call her up and ask her.")
    $ setWait(58.731,63.403)
    $ speak(GAMER_BROTHER, "Alright whatever, look I need you to do me a major solid. You still have that pizza?")
    $ setWait(63.403,64.862)
    $ speak(NICOLE, "Maybe? Why?")
    $ setWait(64.862,71.202)
    $ speak(GAMER_BROTHER, "Okay so I need you to take the pizza and bake it inside of a cake and then have the cake sent to me.")
    $ setWait(71.202,74.372)
    $ speak(NICOLE, "You want me to smuggle you a pizza through a cake?")
    $ setWait(74.372,75.623)
    $ speak(GAMER_BROTHER, "Uh yeah.")
    $ setWait(75.623,78.126)
    $ speak(NICOLE, "I'm pretty sure they'll let you just have a pizza.")
    $ setWait(78.126,85.258)
    $ speak(GAMER_BROTHER, "Well no there's an outside gifts limit and if you bake it inside I can have cake and pizza. That's genius, right?")
    $ setWait(85.258,86.467)
    $ speak(JECKA, "Holy fuck he's fat.")
    $ setWait(86.467,87.385)
    $ speak(NICOLE, "Okay bye!")
    $ setWait(87.385,89.846)
    $ speak(GAMER_BROTHER, "Wait wait is that your blonde friend?")
    $ setWait(89.846,91.639)
    $ speak(NICOLE, "Yeah... why?")
    $ setWait(91.639,95.977)
    $ speak(GAMER_BROTHER, "I met someone in here who wants to talk to her. Hold on a sec, okay?")
    show jecka sc3 worried:
        rightcenterstage

    $ setWait(95.977,97.228)
    $ speak(JECKA, "I'm scared.")
    $ setWait(97.228,100.148)
    $ speak(NICOLE, "...This is gonna be a really expensive phone call.")
    $ setWait(100.148,102.066)
    $ speak(KYLE, "Uh hello?")
    $ setWait(102.066,103.109)
    $ speak(NICOLE, "Who dis?")
    $ setWait(103.109,105.111)
    $ speak(KYLE, "It's me Kyle.")
    $ setWait(105.111,106.654)
    $ speak(JECKA, "Kyle who?")
    $ setWait(106.654,109.282)
    $ speak(KYLE, "We were at the barcade yesterday, remember?")
    show jecka sc3 surprised:
        rightcenterstage

    $ setWait(109.282,111.993)
    $ speak(JECKA, "Oh shit... Yeah?")
    $ setWait(111.993,119.792)
    $ speak(KYLE, "So I thought it over and I killed my Mom... So you wanna go out in ten years when they let me out?")
    show jecka sc3 worried:
        rightcenterstage

    $ setWait(119.792,122.17)
    $ speak(JECKA, "Uh... yeah I don't know.")
    $ setWait(122.17,126.632)
    $ speak(KYLE, "Aw come on you promised! You can't back out now. What do you think, Nicole?")
    $ setWait(126.632,129.051)
    $ speak(NICOLE, "I'm thinking how the fuck are you getting out in ten years.")
    $ setWait(129.051,132.388)
    $ speak(KYLE, "You wanna hear how I killed her? Would that turn you guys on?")
    $ setWait(132.388,133.055)
    $ speak(NICOLE, "Would it?")
    $ setWait(133.055,134.39)
    $ speak(JECKA, "What the fuck! Hang up!")
    $ setWait(134.39,137.56)
    $ speak(KYLE, "You said you'd be all mine! All mine!!")
    $ setWait(137.56,138.436)
    $ speak(NICOLE, "That was cool.")
    $ setWait(138.436,140.396)
    $ speak(JECKA, "I've never felt worse in my life.")
    $ setWait(140.396,145.193)
    $ speak(NICOLE, "Dude don't worry about it. The fact he followed through means his mom was probably a total bitch anyway.")
    $ setWait(145.193,147.028)
    $ speak(JECKA, "I guess that's possible.")
    show nicole sc3 smile:
        leftcenterstage

    $ setWait(147.028,151.657)
    $ speak(NICOLE, "And look on the bright side, he killed her for you. You're technically the hottest girl in school now.")
    show jecka sc3 smile:
        rightcenterstage

    $ setWait(151.657,153.034)
    $ speak(JECKA, "You're kinda right.")
    $ setWait(153.034,155.87)
    $ speak(NICOLE, "There might be a Lifetime movie about this where Miley Cyrus plays you too.")
    show jecka sc3 angry:
        rightcenterstage

    $ setWait(155.87,157.955)
    $ speak(JECKA, "Ew fuck that bitch I don't want her to play me.")
    show nicole sc3:
        leftcenterstage

    $ setWait(157.955,158.956)
    $ speak(NICOLE, "Then who?")
    show jecka sc3:
        rightcenterstage

    $ setWait(158.956,162.251)
    $ speak(JECKA, "Uh, I'll think it over in class. You going this time?")
    stop ambient fadeout 3
    menu:
        "KEEP SKIPPING":
            jump scene_0056
        "THEATRE CLASS":
            jump scene_0096
        "ART CLASS":
            jump scene_0114
label scene_0056:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0056.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 2
    show nicole sc3:
        xzoom -1
        off_right
        linear 3.1 rightcenterstage

    show crispin sc2:
        leftstage

    $ setWait(0.051,2.888)
    $ speak(NICOLE, "I wonder what the guy from Cody Banks is doing right now.")
    show crispin sc2 smile:
        leftstage
        xzoom -1
        linear 1.3 leftcenterstage
    $ setWait(2.888,4.764)
    $ speak(CRISPIN, "Oh hey Nicole, you over here too?")
    show nicole sc3 angry:
        xzoom -1
        rightcenterstage
    $ setWait(4.764,5.474)
    $ speak(NICOLE, "Oh great.")
    $ setWait(5.474,14.9)
    $ speak(CRISPIN, "Yeah I just like, I couldn't even handle whatever was going on in class and stuff and I just had to break loose from it all, y'know? Like I don't know these teachers are just crazy sometimes.")
    $ setWait(14.9,18.195)
    $ speak(NICOLE, "That was the longest possible way to say you're also skipping.")
    $ setWait(18.195,22.991)
    $ speak(CRISPIN, "Oh no like yeah um... Hey I like your shirt.")
    $ setWait(22.991,23.825)
    $ speak(NICOLE, "...Okay.")
    $ setWait(23.825,27.412)
    $ speak(CRISPIN, "It looks kinda deep, like is there any sorta meaning behind it?")
    $ setWait(27.412,28.955)
    $ speak(NICOLE, "Dude how the fuck should I know?")
    $ setWait(28.955,30.957)
    $ speak(CRISPIN, "Well you picked it out, I thought y'know...")
    $ setWait(30.957,37.672)
    $ speak(NICOLE, "I go to the store, it looks nice, I buy it, and not for an artistic conversation with someone dressed like a Bad Religion fan.")
    show crispin sc2:
        xzoom -1
        leftcenterstage
    $ setWait(37.672,42.552)
    $ speak(CRISPIN, "Oh whoa hold up I'm not really like a Bad Religion fan, I only like maybe like four of their albums.")
    $ setWait(42.552,43.887)
    $ speak(NICOLE, "I'm real happy for you.")
    $ setWait(43.887,47.891)
    $ speak(CRISPIN, "Yeah but I mean it's cool that you know about 'em, you like a lot of rock?")
    $ setWait(47.891,51.561)
    $ speak(NICOLE, "That was the most weekend dad question you could've possibly asked me.")
    $ setWait(51.561,53.396)
    $ speak(CRISPIN, "What's that mean exactly?")
    show megan sc2:
        off_right
        linear 1.4 rightmidstage
    $ setWait(53.396,54.773)
    $ speak(MEGAN, "What's going on out here?")
    show nicole sc3:
        xzoom 1
        rightcenterstage
    $ setWait(54.773,55.44)
    $ speak(NICOLE, "Torture.")
    show crispin sc2 smile:
        leftcenterstage
        xzoom -1
    $ setWait(55.44,56.816)
    $ speak(CRISPIN, "Oh hey Megan what's up?")
    $ setWait(56.816,58.485)
    $ speak(MEGAN, "I'm just on my way back from the bathroom.")
    $ setWait(58.485,60.904)
    $ speak(CRISPIN, "Oh yeah cool, I like your shirt by the way.")
    show megan sc2 smile:
        rightmidstage
    $ setWait(60.904,62.239)
    $ speak(MEGAN, "Oh thanks.")
    show nicole sc3:
        xzoom -1
        rightcenterstage
    $ setWait(62.239,66.451)
    $ speak(CRISPIN, "Yeah no it's like mega fuckin' cool, is there like a thing with it, like a story?")
    $ setWait(66.451,70.956)
    $ speak(MEGAN, "Actually there kinda is, it's um... well I don't wanna waste your time.")
    $ setWait(70.956,72.999)
    $ speak(CRISPIN, "No no I got time I'm hanging out.")
    show nicole sc3 angry:
        rightcenterstage
        xzoom -1
        linear 3 off_left

    $ setWait(72.999,74.129)
    $ speak(NICOLE, "Dumb fucking bitch.")
    show black:
        alpha 0.0
        pause 3
        linear 3 alpha 1.0

    stop ambient fadeout 7
    $ setWait(74.129,80.632)
    $ speak(MEGAN, "So it was custom made and it was basically a whole story on my journey with...")

    jump scene_0057
label scene_0057:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0057.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    scene cafeteria int 2
    show ari sc3:
        leftmidstage

    show nicole sc3:
        off_right
        xzoom -1
        linear 3 rightmidstage
    $ setWait(0.129,3.925)
    $ speak(NICOLE, "They should make a game show where a guy eats everything in a vending machine...")
    show ari sc3 think:
        leftmidstage
    $ setWait(3.925,5.176)
    $ speak(ARI, "Ugh...")
    $ setWait(5.176,9.138)
    $ speak(NICOLE, "And if he loses he's gotta like, take his shirt off at the pool or something.")
    show ari sc3 sad:
        leftmidstage
    $ setWait(9.138,10.807)
    $ speak(ARI, "I'm so dead...")
    show nicole sc3 smile:
        rightmidstage
    $ setWait(10.807,14.602)
    $ speak(NICOLE, "Then there's a bunch of hot girls in the pool laughing at his imperfections.")
    show ari sc3 angry:
        leftmidstage
    $ setWait(14.602,16.521)
    $ speak(ARI, "I can't, what do I do?...")

    show nicole sc3 angry:
        rightmidstage

    $ setWait(16.521,18.314)
    $ speak(NICOLE, "Okay Ari, what is it?")
    show ari sc3 sad:
        xzoom -1
        leftmidstage
    $ setWait(18.314,19.399)
    $ speak(ARI, "Wait what? I didn't--")
    $ setWait(19.399,21.484)
    $ speak(NICOLE, "Bitch do not play this game with me.")
    $ setWait(21.484,23.82)
    $ speak(ARI, "What game? I was just sitting here talking to--")
    $ setWait(23.82,25.738)
    $ speak(NICOLE, "Shut the fuck up- what is it?")
    show ari sc3:
        xzoom -1
        leftmidstage
        linear 2 centerstage
    $ setWait(25.738,32.578)
    $ speak(ARI, "Okay well, I'm supposed to be in physics right now but there's this project due and I have literally nothing.")
    show nicole sc3:
        xzoom -1
        rightmidstage
    $ setWait(32.578,35.873)
    $ speak(NICOLE, "Yeah so... Wait this doesn't make sense.")
    $ setWait(35.873,36.791)
    $ speak(ARI, "What doesn't?")
    $ setWait(36.791,39.794)
    $ speak(NICOLE, "If you cared about the class this much wouldn't you have done at least some of it?")
    show ari sc3 sad:
        xzoom -1
        centerstage
    $ setWait(39.794,43.548)
    $ speak(ARI, "It's not the grade, the teacher's just gonna like yell at me in front of everybody.")
    $ setWait(43.548,48.72)
    $ speak(NICOLE, "\"They do it because they care.\" Not because they're paid shitty and weren't smart enough to work at a university.")
    $ setWait(48.72,53.391)
    $ speak(ARI, "You think their salary determines how smart they are? Isn't it just a number on paper?")
    $ setWait(53.391,56.978)
    $ speak(NICOLE, "They think our grades determine how smart we are, let's see how the fuck they like it.")
    show ari sc3:
        xzoom -1
        centerstage
    $ setWait(56.978,62.275)
    $ speak(ARI, "Okay but that doesn't solve my problem. I've been here for the last ten minutes and I can't think of any good excuse.")
    $ setWait(62.275,65.737)
    $ speak(NICOLE, "Is it like a 2 day project or a 3 week project?")
    $ setWait(65.737,67.238)
    $ speak(ARI, "Closer to 3 weeks.")
    $ setWait(67.238,70.992)
    $ speak(NICOLE, "Huh what's a problem that lasts more than 3 weeks...")
    show nicole sc3 smile:
        xzoom -1
        rightmidstage
    $ setWait(70.992,72.326)
    $ speak(NICOLE, "Could you pass for pregnant?")
    show ari sc3 think:
        xzoom -1
        centerstage
    $ setWait(72.326,73.411)
    $ speak(ARI, "I hope not.")
    show nicole sc3:
        xzoom -1
        rightmidstage
    $ setWait(73.411,77.331)
    $ speak(NICOLE, "What works for me usually is saying I have depression but you can't use that.")
    show ari sc3:
        xzoom -1
        centerstage
    $ setWait(77.331,78.082)
    $ speak(ARI, "Why not?")
    $ setWait(78.082,82.128)
    $ speak(NICOLE, "Because I use that? If too many kids start saying it it won't work anymore.")
    show ari sc3 sad:
        xzoom -1
        centerstage
    $ setWait(82.128,85.965)
    $ speak(ARI, "Alright I'm just gonna go to class and get yelled at, this sucks.")
    show nicole sc3:
        rightmidstage
        xzoom 1
        linear 3.5 off_right

    $ setWait(85.965,88.509)
    $ speak(NICOLE, "Or you could drop out and live in a methadone clinic.")
    stop ambient fadeout 1
    jump scene_0058
label scene_0058:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0058.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 1
    show nicole sc3:
        off_left
        linear 2 leftcenterstage
    $ setWait(0.169,2.338)
    $ speak(NICOLE, "How would I pitch a game show to Spike TV?")
    show nicole sc3 surprised:
        leftcenterstage
    $ setWait(2.338,3.547)
    $ speak(LYNN, "You there! Hold it!")
    show nicole sc3:
        leftcenterstage
    $ setWait(3.547,4.798)
    $ speak(NICOLE, "Here we go...")
    show nicole sc3 surprised:
        leftcenterstage
    $ setWait(4.798,5.466)
    $ speak(NICOLE, "Wait.")
    show braxton sc1:
        off_right
        linear 1.3 off_left

    show brick:
        parallel:
            xalign 0.5 yalign 0.5
            pause 0.6
            linear 0.2 yalign 0.3
            linear 0.3 yalign 2.2
        parallel:
            alpha 0.0
            pause 0.59
            linear 0.05 alpha 1.0
    $ setWait(5.466,7.176)
    $ speak(BRAXTON, "How can she run this fast!?")
    show lynn 1:
        off_right
        linear 1.4 off_left
    $ setWait(7.176,9.803)
    $ speak(LYNN, "Don't make me call security!")
    show nicole sc3:
        leftcenterstage
        xzoom -1

    $ setWait(9.803,10.846)
    $ speak(NICOLE, "Hey you dropped something-")
    show cut0058
    $ setWait(10.846,11.555)
    $ speak(NICOLE, "Whoa!")
    $ setWait(11.555,14.475)
    $ speak(NICOLE, "That is a shit ton of cocaine. I wonder if it's real.")
    $ setWait(14.475,16.31)
    $ speak(LYNN, "You just wait 'till I call your parents!")
    hide cut0058
    show nicole sc3 surprised:
        xzoom -1
        leftcenterstage
        linear 0.2 centerstage

    $ setWait(16.31,17.77)
    $ speak(NICOLE, "Shit she's coming back.")
    show lynn 1:
        off_left
        xzoom -1
        linear 0.8 leftstage

    show nicole sc3:
        xzoom -1
        centerstage

    $ setWait(17.77,18.52)
    $ speak(LYNN, "Nicole?")
    $ setWait(18.52,22.274)
    $ speak(NICOLE, "Hey Miss Lynn, rough day at work? What's going on with Braxton?")
    show lynn 1:
        leftstage
        xzoom -1
        linear 1.7 leftmidstage

    $ setWait(22.274,24.818)
    $ speak(LYNN, "None of your business, why aren't you in class?")
    $ setWait(24.818,27.613)
    $ speak(NICOLE, "Oh uh... I was just on my way to the bathroom.")
    $ setWait(27.613,30.657)
    $ speak(LYNN, "You came all the way out to the main foyer on the way to the bathroom?")
    show nicole sc3 angry:
        xzoom -1
        centerstage
    $ setWait(30.657,32.534)
    $ speak(NICOLE, "What do we need bathroom GPS now?")
    $ setWait(32.534,34.286)
    $ speak(LYNN, "Tell me what class you're in right now.")
    show nicole sc3:
        xzoom -1
        centerstage
    $ setWait(34.286,37.247)
    $ speak(NICOLE, "Civics? It's okay I'm going now, don't worry.")
    $ setWait(37.247,38.499)
    $ speak(LYNN, "I'll walk with you.")
    $ setWait(38.499,40.209)
    $ speak(NICOLE, "Nah that's okay, you don't have to.")
    show lynn 1:
        leftmidstage
        xzoom -1
        linear 1.1 leftcenterstage
    $ setWait(40.209,41.335)
    $ speak(LYNN, "I insist.")
    $ setWait(41.335,43.295)
    $ speak(NICOLE, "Wow, are you gonna ask me out after?")
    $ setWait(43.295,45.255)
    $ speak(LYNN, "On a date? Why would I do that?")
    show nicole sc3 angry:
        xzoom -1
        centerstage
        pause 1.2
        xzoom 1
        linear 3 off_right

    show lynn 1:
        xzoom -1
        leftcenterstage
        pause 1.9
        linear 3.4 off_right
    $ setWait(45.255,47.383)
    $ speak(NICOLE, "Wait you're not a guy teacher, sorry let's go.")
    stop ambient fadeout 1
    jump scene_0059
label scene_0059:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0059.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3
    show katz 1:
        rightcenterstage

    show hunter sc1:
        rightstage

    show kelly sc1:
        leftcenterstage
        xzoom -1


    $ setWait(0.041,11.969)
    $ speak(KATZ, "And as I hope you remembered, today is the final day for submitting your community service sponsor. If you don't get those hours in, you cannot graduate.")
    show nicole sc3:
        off_left
        linear 0.8 leftstage

    $ setWait(11.969,12.97)
    $ speak(NICOLE, "Oh my god...")
    $ setWait(12.97,15.515)
    $ speak(KATZ, "Nicole! So nice of you to join us.")
    show nicole sc3:
        leftstage
        linear 2 leftmidstage
    $ setWait(15.515,20.144)
    $ speak(NICOLE, "I'd tell you to kill yourself in your garage but you probably only have a 2 bedroom condo with your pets.")
    $ setWait(20.144,28.194)
    $ speak(KATZ, "I'll pretend I didn't hear that. I trust the rest of you will be taking the community service hours seriously?")
    $ setWait(28.194,29.57)
    $ speak(KELLY, "...I guess?")
    $ setWait(29.57,32.407)
    $ speak(KATZ, "You guess? Kelly who's your sponsor?")
    $ setWait(32.407,34.867)
    $ speak(KELLY, "I'm volunteering for the county police department.")
    $ setWait(34.867,36.285)
    $ speak(NICOLE, "Wow that's lame.")
    show katz 1 angry:
        rightcenterstage
    $ setWait(36.285,38.204)
    $ speak(KATZ, "Something you'd like to add, Nicole?")
    $ setWait(38.204,41.374)
    $ speak(NICOLE, "Yeah why would you help the people who screw us over with speeding tickets?")
    show kelly sc1:
        leftcenterstage
        xzoom 1
    $ setWait(41.374,44.168)
    $ speak(KELLY, "The office is really close to my house, I don't have to drive or anything.")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(44.168,47.296)
    $ speak(NICOLE, "So you're gonna fuck the rest of us over just so you can save on gas money?")
    show kelly sc1:
        leftcenterstage
        xzoom -1
    $ setWait(47.296,50.216)
    $ speak(KATZ, "What did I say about the F-Word in this class??")
    show nicole sc3:
        leftmidstage
    $ setWait(50.216,51.384)
    $ speak(NICOLE, "Sorry, bitch.")
    $ setWait(51.384,56.139)
    $ speak(KATZ, "Are we just supposed to drive as fast as we want? The police are here to keep us safe!")
    $ setWait(56.139,59.892)
    $ speak(NICOLE, "Is that why a ticket's 200 dollars? They're keepin' my safe, holy shit.")
    show katz 1:
        rightcenterstage

    $ setWait(59.892,64.605)
    $ speak(KATZ, "Heh... Funny that a girl so critical of our legal system is failing civics.")
    $ setWait(64.605,69.819)
    $ speak(NICOLE, "Funny how you teach the most expensive car you could ever afford.")
    show katz 1 angry:
        rightcenterstage

    $ setWait(69.819,74.992)
    $ speak(KATZ, "Alright, Nicole! If you're so in tune with the needs of the people, how about your cause?")
    show nicole sc3 surprised:
        leftmidstage
    $ setWait(74.992,75.784)
    $ speak(NICOLE, "My what?")
    show katz 1:
        rightcenterstage

    $ setWait(75.784,82.75)
    $ speak(KATZ, "Your cause, your sponsor for the community service hours. You've had 2 weeks to set something up, now tell me with who...")
    menu:
        "DEPRESSION\nAS AN EXCUSE":
            jump scene_0060
        "COMMIT CHARITY FRAUD":
            jump scene_0083
label scene_0060:
    $ setVoiceTrack("audio/Scenes/0060.mp3")
    scene classroom int 3
    show nicole sc3:
        leftmidstage

    show kelly sc1:
        xzoom -1
        leftcenterstage

    show katz 1:
        rightcenterstage

    show hunter sc1:
        rightstage

    $ setWait(0.046,5.885)
    $ speak(NICOLE, "About that... See um I've sorta been going through a lot right now?")
    $ setWait(5.885,11.057)
    $ speak(KATZ, "Of course... Let's hear it, let's hear another marvelous excuse from Nicole.")
    show nicole sc3 sad:
        leftmidstage
    $ setWait(11.057,18.314)
    $ speak(NICOLE, "I've been diagnosed with... clinical depression so I haven't really gotten out of bed much lately.")
    $ setWait(18.314,19.315)
    $ speak(KATZ, "Depression?")
    $ setWait(19.315,23.57)
    $ speak(NICOLE, "Yeah it's from all the PTSD and some other letters.")
    $ setWait(23.57,28.366)
    $ speak(KATZ, "It's that bad? You couldn't at least think of a community service sponsor?")
    $ setWait(28.366,32.704)
    $ speak(NICOLE, "Well I tried a couple times, but when I did I just started...")
    show kelly sc1 sad:
        xzoom -1
        leftcenterstage

    show hunter sc1 sad:
        rightstage

    $ setWait(32.704,34.372)
    $ speak(NICOLE, "...cutting myself.")
    show kelly sc1 sad:
        xzoom 1
        leftcenterstage

    $ setWait(34.372,35.456)
    $ speak(KELLY, "Why?")
    $ setWait(35.456,42.672)
    $ speak(NICOLE, "Um... Because I'm burden on everyone around me and the community would be better off if I was dead.")
    $ setWait(42.672,43.965)
    $ speak(KATZ, "Aw jeez...")
    $ setWait(43.965,45.508)
    $ speak(KELLY, "That's really not good.")
    $ setWait(45.508,53.099)
    $ speak(NICOLE, "Oh no, am I bringing the mood down?\nSorry, if anyone has a gun I could borrow I could just take care of myself now.")
    $ setWait(53.099,53.975)
    $ speak(KATZ, "A gun??")
    show hunter sc1:
        rightstage

    $ setWait(53.975,55.351)
    $ speak(HUNTER, "Shit I left mine at home today.")
    $ setWait(55.351,57.52)
    $ speak(KELLY, "Oh my god, do you need someone to talk to?")
    $ setWait(57.52,59.814)
    $ speak(NICOLE, "No I don't wanna bother anybody...")
    $ setWait(59.814,65.236)
    $ speak(NICOLE, "Unless it's for a gun I can use to blow my worthless fucking brains out.")
    $ setWait(65.236,70.325)
    $ speak(KATZ, "Okay Nicole, this is not for the classroom. I think you need to go to the counselor's office.")
    $ setWait(70.325,73.203)
    $ speak(NICOLE, "But don't I need a community service sponsor?")
    $ setWait(73.203,76.08)
    $ speak(KATZ, "We can worry about that later just go to the counselor.")
    show nicole sc3 sad:
        leftmidstage
        pause 1
        xzoom -1
        linear 0.7 leftstage
        xzoom 1
    $ setWait(76.08,77.707)
    $ speak(NICOLE, "Okay...")
    $ setWait(77.707,81.669)
    $ speak(NICOLE, "...A-And you're sure you don't want me to kill myself? Cause I will if you want me to.")
    $ setWait(81.669,86.716)
    $ speak(NICOLE, "I'll fire it right in my mouth, my nose'll bleed like the chocolate river from Willy Wonka.")
    show kelly sc1 sad:
        leftcenterstage
        xzoom 1
        pause 2.1 xzoom -1
    $ setWait(86.716,89.802)
    $ speak(KELLY, "No please don't kill yourself, right Mr. Katz?")
    $ setWait(89.802,90.595)
    $ speak(KATZ, "Well..")
    show kelly sc1 angry:
        leftcenterstage
        xzoom -1
    $ setWait(90.595,91.512)
    $ speak(KELLY, "What the fuck!")
    $ setWait(91.512,95.183)
    $ speak(KATZ, "No no we don't want you to kill yourself, just go.")
    show nicole sc3:
        leftstage
        xzoom -1
        linear 0.7 off_left

    $ setWait(95.183,95.975)
    $ speak(NICOLE, "Hos.")
    stop ambient fadeout 1
    jump scene_0061
label scene_0061:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0061.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1
    show counselor 2:
        rightmidstage

    show ari sc3:
        xzoom -1
        leftcenterstage

    show nicole sc3:
        off_left
        linear 2 leftmidstage

    $ setWait(0.046,5.802)
    $ speak(COUNSELOR, "Oh Nicole come in, your civics teacher told me you'd be visiting. Have a seat.")
    $ setWait(5.802,10.014)
    $ speak(NICOLE, "Sure but I thought these were 1 on 1 sessions, what's she doing here?")
    $ setWait(10.014,16.479)
    $ speak(COUNSELOR, "Normally they are, however I thought I'd try something different given you're both here for the same reason.")
    show nicole sc3 angry:
        leftmidstage
    $ setWait(16.479,18.314)
    $ speak(NICOLE, "What reason?")
    show ari sc3 shy:
        xzoom 1
        leftcenterstage
    $ setWait(18.314,19.649)
    $ speak(ARI, "Depression...")
    $ setWait(19.649,20.692)
    $ speak(NICOLE, "You bitch.")
    $ setWait(20.692,26.489)
    $ speak(COUNSELOR, "Nicole I understand you're going through a lot right now but that's no excuse for lashing out at Ari.")
    $ setWait(26.489,30.076)
    $ speak(NICOLE, "Sorry won't happen again. Not like she did anything to deserve it, right?")
    $ setWait(30.076,35.915)
    $ speak(COUNSELOR, "Ari, using an \"I\" statement, please tell Nicole how that made you feel.")
    $ setWait(35.915,37.375)
    $ speak(NICOLE, "This'll be good.")
    $ setWait(37.375,44.549)
    $ speak(ARI, "Um, I feel like you might not be considering my own situation too.")
    show counselor 2 smile:
        rightmidstage

    show ari sc3:
        leftcenterstage
        xzoom 1
    $ setWait(44.549,52.557)
    $ speak(COUNSELOR, "That's very good, thank you.\nNow Nicole, please respond using your own \"I feel\" statement. Go ahead.")
    show nicole sc3 smile:
        leftmidstage
    $ setWait(52.557,56.31)
    $ speak(NICOLE, "Ari I feel you're a conniving fucking bitch. How's that?")
    show counselor 2:
        rightmidstage
    $ setWait(56.31,58.73)
    $ speak(COUNSELOR, "This is going to be a long session.")
    stop ambient fadeout 1
    jump scene_0062
label scene_0062:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0062.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 2
    show nicole sc3 angry:
        rightmidstage
        xzoom -1
        linear 1.6 leftcenterstage
        xzoom 1

    show ari sc3:
        off_right
        pause 0.25
        linear 1 rightmidstage
    $ setWait(0.172,1.632)
    $ speak(ARI, "Nicole, wait...")
    show nicole sc3 angry:
        leftcenterstage
        xzoom 1

    $ setWait(1.632,3.634)
    $ speak(NICOLE, "What? Need another excuse to steal?")
    show ari sc3 think:
        rightmidstage
        pause 3.2
        linear 1.7 rightcenterstage

    $ setWait(3.634,9.014)
    $ speak(ARI, "No- Well no it's just.. what if I wasn't making it up?")
    show nicole sc3:
        leftcenterstage
    $ setWait(9.014,10.515)
    $ speak(NICOLE, "Making what up?")
    $ setWait(10.515,19.816)
    $ speak(ARI, "At first I went to class thinking I'd lie about the depression, but after talking to the counselor I'm starting to realize there's something I actually am depressed about.")
    $ setWait(19.816,21.485)
    $ speak(NICOLE, "Okay cool talk to him about it.")
    show ari sc3:
        rightcenterstage
    $ setWait(21.485,22.444)
    $ speak(ARI, "I can't.")
    show nicole sc3 angry:
        leftcenterstage
        pause 1.1
        xzoom -1
        linear 0.7 leftstage
    $ setWait(22.444,23.987)
    $ speak(NICOLE, "Alright fine fuck off then, bye--")
    show ari sc3 shy:
        rightcenterstage
    $ setWait(23.987,24.946)
    $ speak(ARI, "Wait!")
    show nicole sc3 angry:
        xzoom 1
        leftstage
        linear 1 leftcenterstage
    $ setWait(24.946,26.698)
    $ speak(NICOLE, "What is it?")
    $ setWait(26.698,28.659)
    $ speak(ARI, "It's something about me.")
    $ setWait(28.659,33.163)
    $ speak(ARI, "Something I really can't let him know or he'll tell my parents.")

    show nicole sc3:
        leftcenterstage

    $ setWait(33.163,34.039)
    $ speak(NICOLE, "What're you gay?")
    show ari sc3 sad:
        rightcenterstage
        linear 0.07 xalign 0.64
        linear 0.08 xalign 0.62
        linear 0.07 rightcenterstage

    $ setWait(34.039,35.165)
    $ speak(ARI, "Wha--")
    show ari sc3 shy:
        rightcenterstage
    $ setWait(35.165,37.376)
    $ speak(ARI, "...How did you know? I've never told anyone that.")
    $ setWait(37.376,40.671)
    $ speak(NICOLE, "Dude look at your hair dye, you're either gay or color blind.")
    $ setWait(40.671,43.882)
    $ speak(ARI, "But are you... okay with that?")
    $ setWait(43.882,46.385)
    $ speak(NICOLE, "I mean, I wouldn't use that color but do what you want.")
    $ setWait(46.385,49.096)
    $ speak(ARI, "Not that, I meant... the other thing?")
    show nicole sc3 angry:
        leftcenterstage

    $ setWait(49.096,52.557)
    $ speak(NICOLE, "Are we in Nebraska now? No one cares if you're gay anymore.")
    $ setWait(52.557,54.184)
    $ speak(ARI, "Are you sure?")
    $ setWait(54.184,56.728)
    $ speak(NICOLE, "This is the most 80's conversation I've ever had.")
    show ari sc3:
        rightcenterstage

    $ setWait(56.728,59.856)
    $ speak(ARI, "But my cousin in West Virginia's gay, he says it's horrible.")
    $ setWait(59.856,63.443)
    $ speak(NICOLE, "It's West Virginia, what the fuck isn't horrible there?")
    show ari sc3 think:
        rightcenterstage

    $ setWait(63.443,67.948)
    $ speak(ARI, "So around here... You really think no one'll care if I'm gay?")
    show nicole sc3:
        leftcenterstage

    $ setWait(67.948,75.247)
    $ speak(NICOLE, "Maybe like a weirdo or two but everybody's gonna be like \"look at that asshole\". We're in a white-ass high school ten minutes from the capital, this is such a non-issue now.")
    $ setWait(75.247,76.998)
    $ speak(ARI, "But gay marriage isn't legal here.")
    $ setWait(76.998,78.583)
    $ speak(NICOLE, "Were you looking to get married?")
    show ari sc3:
        rightcenterstage
    $ setWait(78.583,80.377)
    $ speak(ARI, "I don't know if I'd ever wanna get married.")
    $ setWait(80.377,84.172)
    $ speak(NICOLE, "So why do you care? And by the time you do it'll probably be legal anyway.")
    $ setWait(84.172,86.633)
    $ speak(ARI, "I'm not that optimistic when it comes to our government.")
    $ setWait(86.633,91.263)
    $ speak(NICOLE, "Ari, you're white, you could be triple gay and the government's still gonna worry about you.")
    $ setWait(91.263,92.597)
    $ speak(ARI, "You really think so?")

    show crispin sc2 smile:
        off_left
        xzoom -1
        linear 1 leftstage

    $ setWait(92.597,96.351)
    $ speak(CRISPIN, "Oh hey Nicole you still hanging around out here? Did I tell you that's a cool shirt by the way?")
    show nicole sc3:
        leftcenterstage
        pause 0.42
        xzoom -1
    $ setWait(96.351,98.687)
    $ speak(NICOLE, "Look- Hey Crispin you wanna hear something about Ari?")
    show ari sc3 shy:
        rightcenterstage

    show crispin sc2:
        leftstage

    $ setWait(98.687,99.354)
    $ speak(ARI, "Oh my god don't--")
    $ setWait(99.354,101.94)
    $ speak(NICOLE, "Ari's gay.")
    $ setWait(101.94,103.108)
    $ speak(CRISPIN, "She's gay?")
    $ setWait(103.108,105.527)
    $ speak(NICOLE, "Yeah like lesbian gay.")
    $ setWait(105.527,109.698)
    $ speak(CRISPIN, "Oh that's cool... Is there like another part to the story or?")
    show nicole sc3 smile:
        leftcenterstage
        xzoom -1
    $ setWait(109.698,111.867)
    $ speak(NICOLE, "Go down to the cafeteria, you'll find it there.")
    show crispin sc2 smile:
        leftstage
        xzoom -1
        pause 1.4
        xzoom 1
        linear 1.7 off_left

    show ari sc3 think:
        rightcenterstage

    $ setWait(111.867,116.413)
    $ speak(CRISPIN, "Oh it's like a mystery, that's pretty cool you're so creative inside.")

    $ setWait(116.413,119.541)
    $ speak(ARI, "All this time I thought this would be the end of my life.")
    show nicole sc3:
        xzoom 1
        leftcenterstage

    $ setWait(119.541,123.044)
    $ speak(NICOLE, "If you lived in Texas it would be, but this is civilization, dude.")
    show ari sc3 smile:
        rightcenterstage
    $ setWait(123.044,130.719)
    $ speak(ARI, "Well I'll see you around somewhere... And thanks a lot, Nicole. I feel kinda.. free for once.")
    show nicole sc3 angry:
        leftcenterstage
        pause 2.3
        xzoom -1
        linear 3 off_left

    show ari sc3:
        rightcenterstage


    $ setWait(130.719,134.514)
    $ speak(NICOLE, "Fuck off bitch you still stole my excuse. Now I have to think of a new one.")
    stop ambient fadeout 1
    jump scene_0063
label scene_0063:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.252):
        zoom 0.55 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 0.62 truecenter
    $ setVoiceTrack("audio/Scenes/0063.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home nicole int
    show nicole pj:
        leftcenterstage

    show jecka pj:
        rightcenterstage

    $ setWait(2.215,4.3)
    $ speak(JECKA, "You didn't start depression, Nicole.")
    show nicole pj angry:
        leftcenterstage

    $ setWait(4.3,13.643)
    $ speak(NICOLE, "I never said that, but I started using depression as an excuse at that school. No one was doing that before me and now that she took it, everybody's gonna water it down.")
    $ setWait(13.643,19.106)
    $ speak(JECKA, "Do you feel like you're getting to a point where the excuses for not doing homework are more effort than the homework itself?")
    show nicole pj:
        leftcenterstage
    $ setWait(19.106,22.777)
    $ speak(NICOLE, "I don't know hold on... What's another mental disorder I could pull off?")
    $ setWait(22.777,23.778)
    $ speak(JECKA, "Quite a few.")
    $ setWait(23.778,26.864)
    $ speak(NICOLE, "Yeah but whatever I pick I'll need to research at least a little, right?")
    $ setWait(26.864,32.119)
    $ speak(JECKA, "No you don't. Mental illnesses are like horoscopes, you just look up symptoms that loosely fit your personality.")
    show nicole pj:
        leftcenterstage
        xzoom -1
        linear 1.168 leftstage
    $ setWait(32.119,33.287)
    $ speak(NICOLE, "Holy shit, where's my laptop--")
    show nicole pj surprised:
        leftstage
        xzoom 1
        linear 0.5 leftcenterstage

    $ setWait(33.287,33.829)
    $ speak(NICOLE, "Oh wait!")
    show jecka pj smile:
        rightcenterstage
    $ setWait(33.829,35.414)
    $ speak(JECKA, "Schizophrenia, good choice.")
    show nicole pj:
        leftcenterstage

    $ setWait(35.414,41.42)
    $ speak(NICOLE, "No I forgot to tell you what happened after the counselor.\nAri came out of the closet to me in the middle of the hallway.")
    show jecka pj:
        rightcenterstage
    $ setWait(41.42,43.506)
    $ speak(JECKA, "Closet with a glass door, I thought everyone knew that.")
    $ setWait(43.506,46.425)
    $ speak(NICOLE, "Yeah that's what I said, she thought it was like this huge deal.")
    $ setWait(46.425,49.053)
    $ speak(JECKA, "Well wouldn't it be? What if someone homophobic knew?")
    $ setWait(49.053,52.515)
    $ speak(NICOLE, "Yeah, who? I don't know anyone at our school who wouldn't vote for Obama.")
    show jecka pj sad:
        rightcenterstage

    $ setWait(52.515,54.558)
    $ speak(JECKA, "Holy shit I can't think of anyone either.")
    $ setWait(54.558,57.645)
    $ speak(NICOLE, "This area's like so democrat you're just preaching to the choir.")
    show jecka pj:
        rightcenterstage

    $ setWait(57.645,63.15)
    $ speak(JECKA, "Yeah no last year this gay guy sat at our table and was immediately the most popular person there.")
    $ setWait(63.15,64.944)
    $ speak(NICOLE, "Because he was gay or?")
    $ setWait(64.944,68.322)
    $ speak(JECKA, "I mean kinda. He quoted Amanda Show a lot I guess he was funny.")
    $ setWait(68.322,70.032)
    $ speak(NICOLE, "And no one gave him shit or anything?")
    $ setWait(70.032,73.703)
    $ speak(JECKA, "I mean Kylar came up to us but everyone was like \"what's his problem?\"")
    $ setWait(73.703,75.329)
    $ speak(NICOLE, "That's exactly what I told her.")
    $ setWait(75.329,78.332)
    $ speak(JECKA, "Well as long as she's happy like whatever, right?")
    show nicole pj angry:
        leftcenterstage

    $ setWait(78.332,83.004)
    $ speak(NICOLE, "I'm so happy for her.\nSo happy I have to see her ass every week with the counselor now.")
    stop ambient fadeout 1.2
    jump scene_0064
label scene_0064:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0064.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1
    show counselor 3 smile:
        rightmidstage

    show nicole sc4 angry:
        leftmidstage

    show ari sc4 smile:
        xzoom -1
        leftcenterstage

    $ setWait(0.087,10.806)
    $ speak(COUNSELOR, "And I wanted to say, Ari, how proud I am that you've been able to come to terms with your sexual orientation and openly share it with the rest of your peers.")
    $ setWait(10.806,14.476)
    $ speak(ARI, "Thanks, it's just kinda liberating to tell someone I'm gay, y'know?")
    $ setWait(14.476,15.852)
    $ speak(NICOLE, "Every chance you get.")
    $ setWait(15.852,18.647)
    $ speak(COUNSELOR, "Truthfully you are so brave.")
    $ setWait(18.647,20.524)
    $ speak(NICOLE, "Liberal high school, let's not get ahead of ourselves.")
    $ setWait(20.524,26.488)
    $ speak(ARI, "Everyone's been so supportive, I can't believe there was a time when being gay was so hated.")
    $ setWait(26.488,27.697)
    $ speak(NICOLE, "You believed it last week.")
    $ setWait(27.697,31.243)
    $ speak(COUNSELOR, "Yes, yes, times have certainly changed.")
    show nicole sc4:
        leftmidstage

    $ setWait(31.243,33.078)
    $ speak(NICOLE, "Isn't this supposed to be a group therapy?")
    show ari sc4:
        xzoom -1
        leftcenterstage

    show counselor 3:
        rightmidstage

    $ setWait(33.078,40.085)
    $ speak(COUNSELOR, "Is there something you'd like to add, Nicole? Just thought it'd be worth the time to spotlight the progress we've made as a society.")
    $ setWait(40.085,45.882)
    $ speak(COUNSELOR, "Though we still have a very long way to go in terms of sexual identity and acceptance.")
    $ setWait(45.882,47.968)
    $ speak(ARI, "What's left to accept?")
    $ setWait(47.968,61.314)
    $ speak(COUNSELOR, "Transsexuals for one, but also the rather silly notion of controlling other petty qualities of our partners beyond gender. Financial background, race, religion, and even age.")
    show nicole sc4 angry:
        leftmidstage
    $ setWait(61.314,62.315)
    $ speak(NICOLE, "Here we fuckin' go.")
    $ setWait(62.315,65.527)
    $ speak(ARI, "Age? Why would someone have a problem with age if they're legal?")
    $ setWait(65.527,76.83)
    $ speak(COUNSELOR, "But isn't that the problem? Letting legality control love. The state law says you can't marry another girl, but does that mean it's wrong for you to love her?")
    show ari sc4 think:
        leftcenterstage
        xzoom -1
    $ setWait(76.83,81.793)
    $ speak(ARI, "No but... I-I'm pretty sure age is one we.... y'know.")
    $ setWait(81.793,94.472)
    $ speak(COUNSELOR, "Society creates laws, but laws didn't create society. I hope both of you girls realize we should never be critical of anyone's preference regardless of what your parents or TV says.")
    show counselor 3 smile:
        rightmidstage

    $ setWait(94.472,99.352)
    $ speak(COUNSELOR, "Like gender, age is just another thing on your driver's license.")

    show ari sc4:
        xzoom 1
        leftcenterstage

    $ setWait(99.352,104.733)
    $ speak(ARI, "Um... how do you feel about that, Nicole? Do you have an \"I feel\" statement?")
    $ setWait(104.733,106.86)
    $ speak(NICOLE, "I feel like he wants to fuck children.")
    show ari sc4 sad:
        xzoom -1
        leftcenterstage
    $ setWait(106.86,111.781)
    $ speak(ARI, "Yeah, but that's not true, right Counselor? Like you wouldn't date a 15 year old, right?")
    $ setWait(111.781,113.909)
    $ speak(COUNSELOR, "Would you date a 15 year old?")
    $ setWait(113.909,118.413)
    $ speak(ARI, "M-maybe but I'm only 17 so it's not... illegal?")
    $ setWait(118.413,122.667)
    $ speak(COUNSELOR, "I just said, going by legality means you'd be in the wrong too.")
    $ setWait(122.667,126.504)
    $ speak(NICOLE, "Did you say \"in the wrong too\"?? As in you would date a 15 year old?")
    show counselor 3:
        rightmidstage

    $ setWait(126.504,134.221)
    $ speak(COUNSELOR, "I never said that, I'm merely open-minded enough to not doubt the romantic value of anyone of any age.")
    $ setWait(134.221,139.559)
    $ speak(NICOLE, "You're trying to sell a teenage girl on pedophilia using her own gayness as leverage-- What the fuck is wrong with you!?")
    show ari sc4 shy:
        leftcenterstage
        xzoom -1
    $ setWait(139.559,140.31)
    $ speak(ARI, "Oh my god...")
    show nicole sc4 angry:
        leftmidstage
        pause 0.9
        xzoom -1
        linear 1.8 off_left

    $ setWait(140.31,143.355)
    $ speak(NICOLE, "Fuck your therapy, tennis pedophile love-15 lookin' bitch.")
    $ setWait(143.355,148.401)
    $ speak(COUNSELOR, "Let her go, Ari. She's just having a personal moment and needs her space.")
    $ setWait(148.401,149.736)
    $ speak(ARI, "Uh okay...")
    show counselor 3 smile:
        rightmidstage
        linear 5 rightcenterstage

    $ setWait(149.736,155.367)
    $ speak(COUNSELOR, "By the way I didn't wanna make Nicole jealous but your hair looks absolutely beautiful today--")
    show ari sc4 sad:
        leftcenterstage
        pause 3.6
        xzoom 1
        linear 1.1 off_left

    $ setWait(155.367,159.898)
    $ speak(ARI, "Actually I'm gonna go check on her to make sure she doesn't kill herself!")
    stop ambient
    jump scene_0065
label scene_0065:
    $ setVoiceTrack("audio/Scenes/0065.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3"
    scene school int 2
    show nicole sc4:
        leftmidstage
        xzoom -1

    show ari sc4 sad:
        off_right
        linear 1 centerstage

    $ setWait(0.085,1.253)
    $ speak(ARI, "Nicole wait!")
    show nicole sc4:
        leftmidstage
        xzoom 1
    $ setWait(1.253,3.339)
    $ speak(NICOLE, "Wasn't walking.")
    show ari sc4 think:
        centerstage

    $ setWait(3.339,7.134)
    $ speak(ARI, "That wasn't like, a normal thing was it?")
    $ setWait(7.134,10.804)
    $ speak(NICOLE, "No him campaigning for that is a pretty normal thing around here, you didn't know?")
    $ setWait(10.804,17.853)
    $ speak(ARI, "Not that, I meant... you sticking up for someone like that? I never really seen you do that.")
    $ setWait(17.853,20.397)
    $ speak(NICOLE, "Sticking up for who?")
    show ari sc4:
        centerstage
    $ setWait(20.397,22.316)
    $ speak(ARI, "Me.")
    $ setWait(22.316,24.568)
    $ speak(NICOLE, "Okay?")
    $ setWait(24.568,28.238)
    $ speak(ARI, "I... I really appreciate it.")
    $ setWait(28.238,30.366)
    $ speak(NICOLE, "Uh huh?")
    show ari sc4 shy:
        centerstage

    $ setWait(30.366,34.286)
    $ speak(ARI, "This is um... --oh my god this is so fucking stupid.")
    $ setWait(34.286,35.204)
    $ speak(NICOLE, "Kinda is.")
    show ari sc4:
        centerstage
    $ setWait(35.204,42.753)
    $ speak(ARI, "Nicole I've um... Since we started doing this group counseling together I've actually kinda been...")
    show ari sc4 think:
        centerstage
    $ setWait(42.753,45.005)
    $ speak(ARI, "Thinking a lot about you.")
    $ setWait(45.005,47.716)
    $ speak(NICOLE, "But not in a weird way, right?")
    show ari sc4 shy:
        centerstage
    $ setWait(47.716,50.219)
    $ speak(ARI, "No it's, it's in a weird way.")
    show nicole sc4 angry:
        leftmidstage

    $ setWait(50.219,51.22)
    $ speak(NICOLE, "Oh my god...")

    show ari sc4 sad:
        centerstage

    $ setWait(51.22,58.268)
    $ speak(ARI, "I really really like you, I'm sorry, it's just you were the first person I came out to, and what you said in there, and your whole look, and I think I'm in love with you.")
    show nicole sc4:
        leftmidstage

    $ setWait(58.268,61.397)
    $ speak(NICOLE, "In love with someone you've known for two weeks, yeah you're real stable.")
    $ setWait(61.397,64.108)
    $ speak(ARI, "You're not like all sketched out now, are you?")
    $ setWait(64.108,66.402)
    $ speak(NICOLE, "A little but it's not like you're a man saying this.")
    $ setWait(66.402,67.987)
    $ speak(ARI, "How's it different with a man?")
    $ setWait(67.987,73.283)
    $ speak(NICOLE, "Men kinda have a tendency to rape and murder, not sure if you've seen a TV in the last forever.")
    $ setWait(73.283,75.619)
    $ speak(ARI, "Oh god that reminds me, I never even asked you.")
    $ setWait(75.619,77.287)
    $ speak(NICOLE, "Asked me what?")
    $ setWait(77.287,79.164)
    $ speak(ARI, "You um...")
    show ari sc4 shy:
        centerstage
    $ setWait(79.164,82.817)
    $ speak(ARI, "Do you like girls too?")
    menu:
        "TRY LESBIANISM\nBEFORE COLLEGE":
            jump scene_0066
        "MAKE A GAY GIRL CRY":
            jump scene_0075
label scene_0066:
    $ setVoiceTrack("audio/Scenes/0066.mp3")
    scene school int 2

    show nicole sc4 smile:
        leftmidstage

    show ari sc4 shy:
        centerstage
    $ setWait(0.04,2.042)
    $ speak(NICOLE, "Do you want me to?")
    $ setWait(2.042,3.752)
    $ speak(ARI, "Y-yeah.")
    $ setWait(3.752,5.003)
    $ speak(NICOLE, "How badly?")
    show ari sc4 sad:
        centerstage

    $ setWait(5.003,9.883)
    $ speak(ARI, "Extremely... No pressure but I might cut if you say no.")
    show nicole sc4:
        leftmidstage

    $ setWait(9.883,11.51)
    $ speak(NICOLE, "Where do you cut?")
    $ setWait(11.51,14.847)
    $ speak(ARI, "On my upper thigh so my parents don't see.")
    show nicole sc4 smile:
        leftmidstage

    $ setWait(14.847,16.348)
    $ speak(NICOLE, "Damn that's actually kinda hot.")
    show ari sc4 shy:
        centerstage

    $ setWait(16.348,17.599)
    $ speak(ARI, "I-It is?")
    $ setWait(17.599,20.644)
    $ speak(NICOLE, "Yeah cause you look too normal to cut so it's like a fun surprise.")
    show ari sc4 sad:
        centerstage

    $ setWait(20.644,21.854)
    $ speak(ARI, "Are you messing with me?")
    $ setWait(21.854,25.649)
    $ speak(NICOLE, "No seriously, it's like a cheerleader with a nipple piercing-- \"ooh wild side\".")
    $ setWait(25.649,27.401)
    $ speak(ARI, "Really? Do you cut too?")
    show nicole sc4:
        leftmidstage

    $ setWait(27.401,32.155)
    $ speak(NICOLE, "Duh but it's not hot when I do it. It's like \"look at that trashy ho I bet she cuts herself\".")
    $ setWait(32.155,33.49)
    $ speak(ARI, "I don't think you're trashy.")
    $ setWait(33.49,36.869)
    $ speak(NICOLE, "I don't think I should have an F in gym, shit happens though.")
    show ari sc4:
        centerstage

    $ setWait(36.869,42.457)
    $ speak(ARI, "So if you think I'm hot, would you wanna... start dating?")
    $ setWait(42.457,45.294)
    $ speak(NICOLE, "Uh, yeah I guess I'll try it.")
    show ari sc4 shy:
        centerstage

    $ setWait(45.294,46.503)
    $ speak(ARI, "Really??")
    show nicole sc4 smile:
        leftmidstage

    $ setWait(46.503,48.755)
    $ speak(NICOLE, "It'd be really funny if I said no right now.")
    show ari sc4 sad:
        centerstage

    $ setWait(48.755,50.09)
    $ speak(ARI, "Please don't do that to me!")
    show nicole sc4 angry:
        leftmidstage

    $ setWait(50.09,53.302)
    $ speak(NICOLE, "No, okay I'll do it. You have car to take us out?")
    show ari sc4 smile:
        centerstage

    $ setWait(53.302,57.389)
    $ speak(ARI, "Yeah my Mom's old Camry, and only 3 of the windows are broken!")
    show nicole sc4:
        leftmidstage

    $ setWait(57.389,58.807)
    $ speak(NICOLE, "Does it have power seats?")
    show ari sc4:
        centerstage
    $ setWait(58.807,60.559)
    $ speak(ARI, "No they're just manual.")
    show nicole sc4 angry:
        leftmidstage
    $ setWait(60.559,61.31)
    $ speak(NICOLE, "Ugh...")
    show ari sc4 sad:
        centerstage

    $ setWait(61.31,64.688)
    $ speak(ARI, "Oh- but I could borrow my Dad's Lexus if it makes a difference.")
    show nicole sc4:
        leftmidstage
    $ setWait(64.688,66.023)
    $ speak(NICOLE, "It makes a difference.")
    show ari sc4 smile:
        centerstage
    $ setWait(66.023,68.984)
    $ speak(ARI, "Okay I'll see you after school, I love you!")
    show nicole sc4:
        xzoom -1
        leftmidstage
        linear 3 off_left

    $ setWait(68.984,70.152)
    $ speak(NICOLE, "Bye.")
    stop ambient fadeout 1.2
    jump scene_0067
label scene_0067:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show bookstore ext with Pause(2.252):
        zoom 0.55 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 0.62 truecenter
    $ setVoiceTrack("audio/Scenes/0067.mp3")
    play ambient "audio/Ambience/Library_Ambience.mp3"
    scene bookstore
    show nicole sc4 angry:
        leftmidstage
        linear 1 leftcenterstage

    show ari sc4:
        rightcenterstage

    $ setWait(1.674,3.635)
    $ speak(NICOLE, "Why'd you take me to a bookstore?")
    $ setWait(3.635,6.012)
    $ speak(ARI, "It's like the library but all the books are new.")

    $ setWait(6.012,8.556)
    $ speak(NICOLE, "Do I look like a bitch who reads?")

    $ setWait(8.556,13.478)
    $ speak(ARI, "N-not even Harry Potter? It's like coming of age relatable and stuff.")
    show nicole sc4:
        leftcenterstage
    $ setWait(13.478,15.98)
    $ speak(NICOLE, "There's no percocet in Harry Potter, how's it relatable?")
    show jeffery sc3 smile:
        xzoom -1
        off_left
        linear 2 leftmidstage

    $ setWait(15.98,18.524)
    $ speak(JEFFERY, "Hey Nicole, didn't know you read here too.")
    $ setWait(18.524,20.652)
    $ speak(NICOLE, "We had to stop in the graphic novel section.")
    $ setWait(20.652,21.861)
    $ speak(ARI, "Do you know him?")
    $ setWait(21.861,23.363)
    $ speak(NICOLE, "Not really but I'll take care of it.")
    $ setWait(23.363,26.282)
    $ speak(JEFFERY, "So are you reading some manga with your friend there?")
    show nicole sc4 smile:
        leftcenterstage
        xzoom -1
    $ setWait(26.282,29.118)
    $ speak(NICOLE, "Oh she's not my friend, she's my girlfriend.")
    show jeffery sc3:
        leftmidstage
        xzoom -1
    $ setWait(29.118,31.746)
    $ speak(JEFFERY, "Girlfriend? But you're-- hold on!")
    $ setWait(31.746,36.334)
    $ speak(NICOLE, "Do you have a problem with two lesbians going to a book store as opposed to literally anything else?")
    $ setWait(36.334,40.672)
    $ speak(JEFFERY, "N-no it's good to be yourself. You guys are just a little different, like me.")
    show nicole sc4 angry:
        leftcenterstage
        xzoom -1
    $ setWait(40.672,42.215)
    $ speak(NICOLE, "We are nothing like you.")
    $ setWait(42.215,43.299)
    $ speak(JEFFERY, "And why's that?")
    show nicole sc4:
        leftcenterstage
        xzoom -1
    $ setWait(43.299,48.054)
    $ speak(NICOLE, "Cause while you're beating off to your little anime book, we're gonna get fucked up on whip-its and make out.")
    show jeffery sc3 angry:
        leftmidstage
        xzoom -1
    $ setWait(48.054,50.515)
    $ speak(JEFFERY, "Hey that was completely uncalled for!")
    $ setWait(50.515,55.311)
    $ speak(ARI, "Whoa, don't freak out when someone makes up a joke about you, it'll make people think it's real.")
    show jeffery sc3:
        leftmidstage
        xzoom -1
    $ setWait(55.311,59.19)
    $ speak(JEFFERY, "But I have done that to my manga, she shouldn't act like it's wrong though.")
    show ari sc4 sad:
        rightcenterstage

    $ setWait(59.19,59.899)
    $ speak(ARI, "Oh god!")
    show nicole sc4:
        leftcenterstage
        xzoom 1
    $ setWait(59.899,60.858)
    $ speak(NICOLE, "Shouldn't have helped him.")
    $ setWait(60.858,63.861)
    $ speak(ARI, "I've seen him around before, I didn't know he was fucked up like that.")
    show jeffery sc3 smile:
        leftmidstage
        xzoom -1

    show nicole sc4:
        leftcenterstage
        xzoom 1
        pause 0.6
        xzoom -1
    $ setWait(63.861,67.657)
    $ speak(JEFFERY, "By the way I started a Youtube channel, you guys wanna see it?")
    show nicole sc4:
        leftcenterstage
        xzoom 1
        linear 2 off_farright

    show ari sc4:
        rightcenterstage
        pause 1.2
        xzoom -1
        linear 1.1 off_right

    $ setWait(67.657,69.033)
    $ speak(NICOLE, "Nah we gotta go buy whip-its.")
    $ setWait(69.033,71.327)
    $ speak(ARI, "I never tried whip-its, do they taste bad?")
    stop ambient fadeout 1
    jump scene_0068
label scene_0068:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter
    $ setVoiceTrack("audio/Scenes/0068.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3"
    scene cafeteria int
    show jecka sc4:
        leftmidstage
        xzoom -1

    show nicole sc5:
        leftcenterstage
        xzoom -1

    show ari sc5:
        rightcenterstage

    $ setWait(0.042,8.217)
    $ speak(ARI, "And then the counselor got so weird he called my mom and told her I might have schizophrenia if I ever mentioned he was a pedophile.")
    $ setWait(8.217,9.427)
    $ speak(JECKA, "And what'd your mom say?")
    show ari sc5 sad:
        rightcenterstage
    $ setWait(9.427,12.93)
    $ speak(ARI, "She believed him! We had like an hour long fight over it, right honey?")
    show jecka sc4 smile:
        leftmidstage
        xzoom -1
    $ setWait(12.93,13.723)
    $ speak(JECKA, "Right honey?")
    show nicole sc5 angry:
        xzoom 1
        leftcenterstage
    $ setWait(13.723,15.266)
    $ speak(NICOLE, "Dude I said don't call me that in public.")
    $ setWait(15.266,17.81)
    $ speak(ARI, "Oh I thought it was don't say it in private.")
    $ setWait(17.81,20.396)
    $ speak(NICOLE, "If I didn't want it in private why would I want it in public?")
    show nicole sc5:
        leftcenterstage

    $ setWait(20.396,23.983)
    $ speak(ARI, "I'm sorry I'm sorry I'm sorry, I'm still getting used to your boundaries and everything.")
    $ setWait(23.983,27.278)
    $ speak(JECKA, "Boundaries? I didn't know you're dating a marriage counselor.")
    show kylar sc2 smile:
        off_right
        linear 1.8 rightmidstage

    show jecka sc4:
        leftmidstage
        xzoom -1

    $ setWait(27.278,28.279)
    $ speak(KYLAR, "What's up, queers?")
    $ setWait(28.279,29.363)
    $ speak(ARI, "Nicole...")
    $ setWait(29.363,30.656)
    $ speak(NICOLE, "Dude he's not gonna do anything.")
    show kylar sc2:
        rightmidstage

    $ setWait(30.656,33.326)
    $ speak(KYLAR, "Heard you guys were dating now, what're you special or something?")

    show nicole sc5 angry:
        leftcenterstage

    show ari sc5:
        rightcenterstage
        xzoom -1

    $ setWait(33.326,34.327)
    $ speak(NICOLE, "Why do you care?")
    $ setWait(34.327,36.579)
    $ speak(KYLAR, "Tired of hos like you always looking for attention.")
    $ setWait(36.579,39.207)
    $ speak(NICOLE, "Find one other person in this room who cares.")
    show kylar sc2 angry:
        rightmidstage
        pause 2.5
        xzoom -1
    $ setWait(39.207,42.585)
    $ speak(KYLAR, "No one's falling for this bullshit like you think they are. Ay Hunter!")
    show hunter sc2:
        off_right
        linear 1 rightstage

    $ setWait(42.585,43.419)
    $ speak(HUNTER, "What's up?")
    show kylar sc2:
        rightmidstage
        xzoom -1
    $ setWait(43.419,46.255)
    $ speak(KYLAR, "They're saying they're gay now, that's fuckin' dumb, right?")
    $ setWait(46.255,50.718)
    $ speak(HUNTER, "Uh Obama might be president soon, who's worried about being gay anymore?")
    show kylar sc2 angry:
        rightmidstage
        xzoom -1
    $ setWait(50.718,54.055)
    $ speak(KYLAR, "Dude fuck Obama he's a bitch, my dad's voting for McCain.")
    $ setWait(54.055,55.473)
    $ speak(HUNTER, "Why would he vote for McCain?")
    $ setWait(55.473,59.727)
    $ speak(KYLAR, "Cause he's a fuckin' war hero. Maybe then we'll nut up and nuke the middle east.")
    $ setWait(59.727,61.02)
    $ speak(HUNTER, "Oh...")
    show hunter sc2:
        rightstage
        pause 1.7
        xzoom -1
        linear 1.5 off_right

    $ setWait(61.02,65.441)
    $ speak(HUNTER, "...well sorry dude but your dad sounds really fucking gay voting for McCain.")
    show kylar sc2 angry:
        rightmidstage
        xzoom -1
        linear 1.1 off_right
    $ setWait(65.441,67.777)
    $ speak(KYLAR, "What?? No-- You're gay!")
    $ setWait(67.777,68.82)
    $ speak(JECKA, "Eventful.")
    show ari sc5 smile:
        rightcenterstage
        xzoom 1
    $ setWait(68.82,70.446)
    $ speak(ARI, "Thanks for taking care of that, Nicole.")
    show nicole sc5:
        leftcenterstage
        xzoom 1
    $ setWait(70.446,74.534)
    $ speak(NICOLE, "No problem-- Hey could you go to the longest pizza line and get me four slices?")
    $ setWait(74.534,76.953)
    $ speak(ARI, "Yeah sure, anything.")
    $ setWait(76.953,79.539)
    $ speak(NICOLE, "...Okay, why aren't you going?")
    show ari sc5:
        rightcenterstage

    $ setWait(79.539,81.582)
    $ speak(ARI, "You won't kiss me on the cheek first?")
    $ setWait(81.582,82.834)
    $ speak(NICOLE, "Oh my god...")
    show nicole sc5:
        leftcenterstage
        linear 0.2 xalign 0.56
        pause 0.1
        linear 0.3 leftcenterstage
    $ setWait(82.834,83.459)
    $ speak(NICOLE, "mwah.")
    show ari sc5 smile:
        xzoom -1
        rightcenterstage
        linear 1.8 off_right

    $ setWait(83.459,85.419)
    $ speak(ARI, "Okay I'll be right back.")
    show nicole sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(85.419,87.088)
    $ speak(NICOLE, "Egh! Disgusting.")
    $ setWait(87.088,88.464)
    $ speak(JECKA, "What, are you straight again?")
    $ setWait(88.464,93.678)
    $ speak(NICOLE, "No I have dollar store foundation on my lips now- ugh. This could double as baby formula in Pakistan.")
    $ setWait(93.678,95.179)
    $ speak(JECKA, "She's your girlfriend.")
    show nicole sc5:
        leftcenterstage
        xzoom -1
    $ setWait(95.179,95.888)
    $ speak(NICOLE, "So?")
    show jecka sc4 angry:
        leftmidstage
        xzoom -1
    $ setWait(95.888,97.431)
    $ speak(JECKA, "So take your bitch to Ulta.")
    $ setWait(97.431,101.477)
    $ speak(NICOLE, "No, already trying to limit the exposure, that's why I sent her to the pizza line.")
    show jecka sc4:
        leftmidstage
        xzoom -1
    $ setWait(101.477,103.437)
    $ speak(JECKA, "But you haven't even dated for a week yet.")
    $ setWait(103.437,104.564)
    $ speak(NICOLE, "Fucked up, right?")
    $ setWait(104.564,105.857)
    $ speak(JECKA, "Did she do something wrong?")
    $ setWait(105.857,108.734)
    $ speak(NICOLE, "She just gets really awkward when you're around her for long enough.")
    $ setWait(108.734,110.152)
    $ speak(JECKA, "Awkward how?")
    $ setWait(110.152,113.698)
    $ speak(NICOLE, "Okay so, she was in my room while I was changing real quick.")
    show nicole sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(113.698,120.913)
    $ speak(NICOLE, "Then she saw one nipple for like a second and was all \"oh my god I'm sorry I looked but you're so sexy, you're so sexy, I'm so lucky to have you\"-- Like bitch fuck off!!")
    $ setWait(120.913,124.166)
    $ speak(NICOLE, "I've seen her with guys before I don't know why she's acting like such a virgin.")
    $ setWait(124.166,127.044)
    $ speak(JECKA, "She's probably just a virgin with girls, it's like a higher echelon.")
    show nicole sc5:
        leftcenterstage
        xzoom -1
    $ setWait(127.044,130.214)
    $ speak(NICOLE, "But if she's so gay why was she even with guys in the first place?")
    $ setWait(130.214,136.596)
    $ speak(JECKA, "Cause hooking up with a guy is the easiest thing on Earth?\nEven if a girl's gay she's gonna try it at least once or.. nine times.")
    $ setWait(136.596,140.85)
    $ speak(NICOLE, "Wait so, first time you're curious, second time you're bored....")
    show jecka sc4 smile:
        leftmidstage
        xzoom -1
    $ setWait(140.85,143.811)
    $ speak(JECKA, "And ninth time you're just trying to keep the lights on.")
    stop ambient fadeout 1
    jump scene_0069
label scene_0069:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0069.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 1
    show kelly sc2:
        rightmidstage

    show ari sc5 smile:
        xzoom -1
        rightcenterstage

    show nicole sc5:
        xzoom -1
        leftcenterstage

    $ setWait(0.036,4.374)
    $ speak(KELLY, "And I just wanna say how cool it is that you guys are so open about this.")
    $ setWait(4.374,5.375)
    $ speak(ARI, "Right? Yeah.")
    $ setWait(5.375,11.673)
    $ speak(KELLY, "I kissed a girl at a party once and I totally get the appeal.\nLesbianism is just so... so bold!")
    $ setWait(11.673,14.551)
    $ speak(ARI, "Have you thought about, like, going full time with it?")
    $ setWait(14.551,15.802)
    $ speak(KELLY, "You mean like gay married?")
    $ setWait(15.802,16.428)
    $ speak(ARI, "Yeah.")
    show kelly sc2 angry:
        rightmidstage

    $ setWait(16.428,18.847)
    $ speak(KELLY, "Fuck that, then I wouldn't have a rich husband.")
    show ari sc5:
        rightcenterstage
        xzoom -1
    $ setWait(18.847,21.599)
    $ speak(ARI, "Isn't there more to a relationship than money though?")
    show kelly sc2:
        rightmidstage

    $ setWait(21.599,25.854)
    $ speak(KELLY, "Maybe? I see you guys ride around in that beat up Camry, and it's cute...")
    show kelly sc2:
        rightmidstage
        xzoom -1
        linear 2.6 off_right

    $ setWait(25.854,28.314)
    $ speak(KELLY, "...but I'd never cuff a broke bitch.")
    $ setWait(28.314,29.649)
    $ speak(ARI, "Can you believe her?")
    $ setWait(29.649,32.027)
    $ speak(NICOLE, "Yeah these bicurious hos? Fuck 'em.")
    show ari sc5 smile:
        xzoom 1
        rightcenterstage

    $ setWait(32.027,32.819)
    $ speak(ARI, "By the way did you wanna--")
    $ setWait(32.819,35.363)
    $ speak(NICOLE, "Hold on I'm replying to something.")

    show ari sc5:
        rightcenterstage

    $ setWait(35.363,37.323)
    $ speak(ARI, "Okay... Are you done?")
    show nicole sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(37.323,38.783)
    $ speak(NICOLE, "No, shut up hold on.")
    show ari sc5 think:
        rightcenterstage

    $ setWait(38.783,41.619)
    $ speak(ARI, "Nicole I don't really like it when you tell me to shut up--")
    show nicole sc5 angry:
        xzoom 1
        leftcenterstage

    $ setWait(41.619,45.123)
    $ speak(NICOLE, "Just fuck off, okay!? Maybe quit the box dye, it's fucking your brain up!")
    show ari sc5 shy:
        rightcenterstage

    $ setWait(45.123,46.583)
    $ speak(ARI, "...")
    show nicole sc5 sad:
        leftcenterstage
    $ setWait(46.583,48.334)
    $ speak(NICOLE, "...Oh shit.")
    show ari sc5 shy:
        rightcenterstage
    $ setWait(48.334,50.086)
    $ speak(ARI, "I um...")
    show nicole sc5:
        leftcenterstage

    $ setWait(50.086,51.588)
    $ speak(NICOLE, "Hey listen uh--")
    show ari sc5 sad:
        rightcenterstage

    $ setWait(51.588,56.134)
    $ speak(ARI, "I'm really sorry for not respecting your boundaries, I promise it won't happen again.")
    show nicole sc5 surprised:
        leftcenterstage

    $ setWait(56.134,58.094)
    $ speak(NICOLE, "Oh... what?")
    $ setWait(58.094,61.806)
    $ speak(ARI, "I was totally in the wrong you had every right to say that.")
    show nicole sc5:
        leftcenterstage

    $ setWait(61.806,66.644)
    $ speak(NICOLE, "Well, as long as you're sorry... you dumb bitch?")
    show ari sc5 think:
        rightcenterstage

    $ setWait(66.644,70.065)
    $ speak(ARI, "I know I'm a dumb bitch, I'm sorry. I love you.")
    show nicole sc5 smile:
        leftcenterstage

    $ setWait(70.065,72.734)
    $ speak(NICOLE, "I think I'm starting to love you too.")
    stop ambient fadeout 1.2
    jump scene_0070
label scene_0070:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0070.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school courtyard
    show jecka sc5:
        leftcenterstage
        xzoom -1

    show nicole sc6:
        xzoom -1
        rightmidstage
        linear 1 rightcenterstage

    show ari sc6:
        rightstage
        linear 1 rightmidstage

    $ setWait(0.048,1.716)
    $ speak(JECKA, "You guys see the new Smallville?")
    $ setWait(1.716,4.594)
    $ speak(NICOLE, "Dude Smallville's for straight people, who watches that shit?")
    show jecka sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(4.594,6.429)
    $ speak(JECKA, "You were straight 3 weeks ago.")
    $ setWait(6.429,9.933)
    $ speak(NICOLE, "Yeah and I didn't watch it then either. Guess it's just universally bad.")
    $ setWait(9.933,12.519)
    $ speak(ARI, "I saw a couple episodes once, it was okay.")

    show nicole sc6:
        xzoom 1
        rightcenterstage

    $ setWait(12.519,14.812)
    $ speak(NICOLE, "Was anyone asking you?")
    show ari sc6 think:
        rightmidstage

    show jecka sc5 sad:
        leftcenterstage
        xzoom -1

    $ setWait(14.812,16.272)
    $ speak(ARI, "Um... No.")
    show nicole sc6:
        xzoom -1
        rightcenterstage

    $ setWait(16.272,17.44)
    $ speak(NICOLE, "Just checking.")
    show ari sc6:
        rightmidstage

    $ setWait(17.44,22.07)
    $ speak(JECKA, "Anyway, I was gonna buy lunch today but the lines are like so long.")
    $ setWait(22.07,23.947)
    $ speak(NICOLE, "It's probably spicy chicken sandwich day.")
    show jecka sc5 smile:
        leftcenterstage
        xzoom -1
    $ setWait(23.947,25.114)
    $ speak(JECKA, "Oh and I want one...")
    show nicole sc6 smile:
        xzoom -1
        rightcenterstage
        pause 1.15
        xzoom 1
    $ setWait(25.114,28.451)
    $ speak(NICOLE, "Me too, Ari get us the chicken sandwiches, I'll pay you back.")

    show ari sc6 sad:
        rightmidstage

    $ setWait(28.451,30.37)
    $ speak(ARI, "But the line's gonna take forever, can we just--")
    show nicole sc6 angry:
        rightcenterstage
        xzoom 1

    show jecka sc5:
        leftcenterstage
        xzoom -1
    $ setWait(30.37,33.289)
    $ speak(NICOLE, "Don't you love me?")
    show ari sc6 think:
        rightmidstage

    $ setWait(33.289,34.999)
    $ speak(ARI, "...Okay I'll go.")

    $ setWait(34.999,38.044)
    $ speak(JECKA, "Cool, yeah and get me two if they have enough.")
    show nicole sc6:
        xzoom -1
        rightcenterstage
    $ setWait(38.044,39.963)
    $ speak(NICOLE, "They're big, you're gonna eat two?")
    $ setWait(39.963,42.09)
    $ speak(JECKA, "One for now, one for when I'm depressed.")
    show nicole sc6:
        xzoom 1
        rightcenterstage
    $ setWait(42.09,43.424)
    $ speak(NICOLE, "Alright you got all that?")
    show ari sc6 think:
        rightmidstage
        xzoom -1
        linear 1.2 rightstage

    $ setWait(43.424,44.551)
    $ speak(ARI, "Be right back.")
    $ setWait(44.551,45.969)
    $ speak(NICOLE, "You're forgetting something.")
    show ari sc6:
        rightstage
        xzoom 1
        linear 2 xalign 0.72

    show nicole sc6:
        rightcenterstage

    $ setWait(45.969,48.555)
    $ speak(ARI, "Oh right sorry... mwah.")
    show nicole sc6 smile:
        rightcenterstage
        xzoom 1
    $ setWait(48.555,50.682)
    $ speak(NICOLE, "Good girl, don't make me ask again.")
    show ari sc6:
        xzoom 1
        pause 1
        xalign 0.72
        xzoom -1
        linear 1.8 off_right

    $ setWait(50.682,52.433)
    $ speak(ARI, "I know, I love you.")


    show nicole sc6:
        rightcenterstage
        xzoom 1

    $ setWait(52.433,54.06)
    $ speak(NICOLE, "That's nice.")
    show jecka sc5 surprised:
        xzoom -1
        leftcenterstage

    $ setWait(54.06,55.061)
    $ speak(JECKA, "...What the fuck.")
    show nicole sc6:
        rightcenterstage
        xzoom -1
    $ setWait(55.061,56.813)
    $ speak(NICOLE, "I know. What's her problem, right?")

    show jecka sc5 angry:
        leftcenterstage
        xzoom -1

    $ setWait(56.813,59.857)
    $ speak(JECKA, "No-- What the fuck did you do to her? She's like your pet now.")
    $ setWait(59.857,66.823)
    $ speak(NICOLE, "Yeah so you know how I wanted out of the relationship?\nWhat I thought would be more fun than breaking up was just seeing what I could get away with.")
    show jecka sc5:
        leftcenterstage
        xzoom -1
    $ setWait(66.823,68.241)
    $ speak(JECKA, "Get away with what?")
    show nicole sc6 smile:
        rightcenterstage
        xzoom -1
    $ setWait(68.241,75.665)
    $ speak(NICOLE, "Dude like everything so far. I'll literally call her a bitch to her face and she'll just apologize and kiss me on the cheek. It's such a power trip.")
    show jecka sc5 sad:
        leftcenterstage
        xzoom -1
    $ setWait(75.665,78.71)
    $ speak(JECKA, "Uh.. It sounds like abuse.")
    $ setWait(78.71,84.424)
    $ speak(NICOLE, "I get that. But honestly if it is, abusing feels fucking awesome, don't knock it 'till you try it.")
    $ setWait(84.424,86.884)
    $ speak(JECKA, "Yeah but you know why you're getting away with it, right?")
    show nicole sc6 angry:
        rightcenterstage
        xzoom -1
    $ setWait(86.884,87.927)
    $ speak(NICOLE, "Oh let's hear this.")
    show jecka sc5:
        leftcenterstage
        xzoom -1
    $ setWait(87.927,89.762)
    $ speak(JECKA, "Because you're her only option.")
    $ setWait(89.762,98.73)
    $ speak(JECKA, "So you're taking advantage of the fact the only lesbian in school knows there aren't any other lesbians to date here. She's basically stuck with whatever you wanna put her through.")
    $ setWait(98.73,101.482)
    $ speak(NICOLE, "She can break up anytime she wants, she's not stuck with anything.")
    $ setWait(101.482,107.53)
    $ speak(JECKA, "Okay so she breaks up to move on to who? The only girl willing to date her is her abusive ex-girlfriend.")
    $ setWait(107.53,108.656)
    $ speak(NICOLE, "...And?")
    $ setWait(108.656,111.075)
    $ speak(JECKA, "No offense but you're like an evil fucking bitch.")
    $ setWait(111.075,117.957)
    $ speak(NICOLE, "No okay, if you're so high and mighty about it why don't you tell her everything you just told me? The dynamic, the game, everything.")
    show jecka sc5 sad:
        leftcenterstage
        xzoom -1

    $ setWait(117.957,120.084)
    $ speak(JECKA, "I don't know her like that-- awkward, ew.")
    show nicole sc6:
        rightcenterstage
        xzoom -1
    $ setWait(120.084,125.256)
    $ speak(NICOLE, "If only life was like TV where friends spill their hearts out to people they barely know.")
    show jecka sc5:
        leftcenterstage
        xzoom -1
    $ setWait(125.256,127.342)
    $ speak(JECKA, "You probably don't even watch anything good.")
    $ setWait(127.342,128.426)
    $ speak(NICOLE, "You watch Smallville.")
    $ setWait(128.426,129.26)
    $ speak(JECKA, "You're evil.")
    show nicole sc6 angry:
        rightcenterstage
        xzoom -1
    $ setWait(129.26,130.762)
    $ speak(NICOLE, "You're friends with someone who's evil.")
    show jecka sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(130.762,132.472)
    $ speak(JECKA, "You're friends with someone who watches Smallville.")
    show nicole sc6 surprised:
        xzoom 1
        rightcenterstage

    $ setWait(132.472,134.057)
    $ speak(NICOLE, "Holy shit don't say it that loud.")
    stop ambient fadeout 1
    jump scene_0071
label scene_0071:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0071.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1
    show counselor 1:
        rightmidstage

    show nicole sc6:
        leftmidstage

    show ari sc6:
        leftcenterstage
        xzoom -1

    $ setWait(0.043,11.138)
    $ speak(COUNSELOR, "Again, I apologize for the misunderstanding we had last time the two of you came in here. I would never want to be mistaken for an abuser, I can assure you that.")
    $ setWait(11.138,11.763)
    $ speak(NICOLE, "Uh huh.")
    show ari sc6 think:
        leftcenterstage
        xzoom -1
    $ setWait(11.763,12.889)
    $ speak(ARI, "Abuser...")
    $ setWait(12.889,17.936)
    $ speak(COUNSELOR, "Yes anyway, Nicole, it's been a while since we've chatted. What's going on with you?")
    $ setWait(17.936,19.688)
    $ speak(NICOLE, "What's going on with me?")
    $ setWait(19.688,24.109)
    $ speak(COUNSELOR, "Yes, if you'd care to share with us.")
    $ setWait(24.109,25.569)
    $ speak(NICOLE, "What the hell do I say to that?")
    $ setWait(25.569,34.536)
    $ speak(COUNSELOR, "A variety of things. You could speak about what you did over the weekend, or something that's caught your interest lately.\nAri and I are here to listen.")
    $ setWait(34.536,36.121)
    $ speak(NICOLE, "Okay well...")
    $ setWait(36.121,38.206)
    $ speak(NICOLE, "I heard Kanye West just got outta jail.")
    $ setWait(38.206,40.667)
    $ speak(COUNSELOR, "Really? Tell me more.")
    $ setWait(40.667,45.338)
    $ speak(NICOLE, "Um, he was in jail and then he wasn't in jail?")
    $ setWait(45.338,48.258)
    $ speak(COUNSELOR, "So why was he in jail in the first place?")
    $ setWait(48.258,53.096)
    $ speak(NICOLE, "He broke somebody's camera, and now his new album's delayed or something.")
    $ setWait(53.096,56.933)
    $ speak(COUNSELOR, "A new album, do you think it'll be as good as his last album?")
    show nicole sc6 angry:
        leftmidstage

    $ setWait(56.933,60.103)
    $ speak(NICOLE, "No-- why are you pretending like you know what I'm talking about?")
    $ setWait(60.103,63.482)
    $ speak(COUNSELOR, "I'm not pretending, just having a conversation.")
    $ setWait(63.482,65.734)
    $ speak(NICOLE, "Name one Kanye West song.")
    $ setWait(65.734,71.156)
    $ speak(COUNSELOR, "Um, I can't think of any off the top of my head.\nWhat are some of your favorites?")
    $ setWait(71.156,72.449)
    $ speak(NICOLE, "Dude you're so fucking gay.")
    show counselor 1 angry:
        rightmidstage

    $ setWait(72.449,76.036)
    $ speak(COUNSELOR, "Nicole! You know that word isn't welcome on this campus.")
    $ setWait(76.036,77.579)
    $ speak(NICOLE, "I'm gay now, I can say it!")
    $ setWait(77.579,79.039)
    $ speak(COUNSELOR, "The F-Word.")
    $ setWait(79.039,80.54)
    $ speak(NICOLE, "But the homophobic one's fine then.")
    show counselor 1:
        rightmidstage

    show nicole sc6:
        leftmidstage

    $ setWait(80.54,88.215)
    $ speak(COUNSELOR, "Well out of respect to Ari here, I wouldn't say that's fine either.\nAri how does that make you feel?")
    $ setWait(88.215,93.303)
    $ speak(ARI, "Well actually I actually wanted to ask something...")
    show ari sc6:
        leftcenterstage
        xzoom -1
    $ setWait(93.303,96.306)
    $ speak(ARI, "...when you said we mistook you for an abuser?")
    $ setWait(96.306,98.141)
    $ speak(COUNSELOR, "Yes, go on.")
    $ setWait(98.141,103.355)
    $ speak(ARI, "Like how? Y-You weren't violent or anything, I don't get it.")
    $ setWait(103.355,115.492)
    $ speak(COUNSELOR, "Abuse can come in many forms, not just violence or physical assault. It could be psychological, emotional, financial, anything that asserts control over another person.")
    $ setWait(115.492,118.829)
    $ speak(NICOLE, "Like how you wanna molest kids? I think they call it sexual abuse.")
    show counselor 1 angry:
        rightmidstage

    show ari sc6 sad:
        leftcenterstage
        xzoom -1

    $ setWait(118.829,120.747)
    $ speak(COUNSELOR, "Nicole, what did I say!?")
    $ setWait(120.747,121.915)
    $ speak(NICOLE, "Something about fucking kids.")
    $ setWait(121.915,129.381)
    $ speak(COUNSELOR, "That's it! This session is over! I'm sorry but you'll both have to come back at a later time when you learn how to behave yourselves.")
    $ setWait(129.381,129.84)
    $ speak(ARI, "But I didn't--")
    show counselor 1 angry:
        rightmidstage
        linear 0.7 rightcenterstage
    $ setWait(129.84,130.59)
    $ speak(COUNSELOR, "Out!")
    show nicole sc6 angry:
        xzoom -1
        leftmidstage
        linear 1.6 off_left

    show ari sc6 sad:
        leftcenterstage
        xzoom -1
        pause 1
        xzoom 1
        linear 1.6 off_left

    $ setWait(130.59,132.634)
    $ speak(NICOLE, "Finally, fuck.")
    stop ambient fadeout 1
    jump scene_0072
label scene_0072:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0072.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 2
    show nicole sc6 angry:
        xzoom -1
        rightmidstage
        linear 1.5 leftcenterstage
        xzoom 1

    show ari sc6 sad:
        off_right
        linear 2 rightcenterstage

    $ setWait(0.041,2.668)
    $ speak(NICOLE, "He's like the guy in every sitcom's pedophile episode.")

    $ setWait(2.668,4.754)
    $ speak(ARI, "Every sitcom has a pedophile episode?")
    show nicole sc6:
        leftcenterstage

    $ setWait(4.754,7.048)
    $ speak(NICOLE, "Yeah where the kids learn a lesson or whatever.")
    show ari sc6 think:
        rightcenterstage

    $ setWait(7.048,10.009)
    $ speak(ARI, "Oh yeah... Nicole.")
    $ setWait(10.009,11.01)
    $ speak(NICOLE, "What?")
    $ setWait(11.01,12.47)
    $ speak(ARI, "Could I ask you something?")
    $ setWait(12.47,16.557)
    $ speak(NICOLE, "No sorry I don't have anymore kisses today. The kiss factory's closed, somebody died.")
    $ setWait(16.557,21.02)
    $ speak(ARI, "No it wasn't about that, it was uh...")
    show ari sc6:
        rightcenterstage

    $ setWait(21.02,22.522)
    $ speak(ARI, "Why are you dating me?")
    show nicole sc6 angry:
        leftcenterstage

    $ setWait(22.522,25.9)
    $ speak(NICOLE, "Why am I dating you? Why am I doing anything? I don't know.")
    show ari sc6 think:
        rightcenterstage

    $ setWait(25.9,29.32)
    $ speak(ARI, "It's just, I was thinking about what the counselor said in there.")
    show nicole sc6:
        leftcenterstage

    $ setWait(29.32,31.405)
    $ speak(NICOLE, "Dude your shirt isn't see-through, he's just a pervert.")
    show ari sc6:
        rightcenterstage

    $ setWait(31.405,36.827)
    $ speak(ARI, "Well no that's a way bigger problem but-- I'm just talking about us right now.")
    $ setWait(36.827,38.287)
    $ speak(NICOLE, "What about us?")
    show ari sc6 think:
        rightcenterstage
    $ setWait(38.287,42.124)
    $ speak(ARI, "I'm just thinking like... what we've been for the last couple weeks.")
    $ setWait(42.124,43.334)
    $ speak(NICOLE, "You mean awesome?")
    show ari sc6 shy:
        rightcenterstage

    $ setWait(43.334,51.717)
    $ speak(ARI, "Maybe awesome for you-- Which is good but...\nwhat he said about how abuse works it... it kinda made me worried.")

    show nicole sc6 angry:
        leftcenterstage

    $ setWait(51.717,53.219)
    $ speak(NICOLE, "So I'm abusing you?")
    $ setWait(53.219,56.514)
    $ speak(ARI, "Uh, I don't know-- if you do I don't think you mean to.")
    $ setWait(56.514,58.266)
    $ speak(NICOLE, "When have I ever hit you or anything?")
    $ setWait(58.266,63.688)
    $ speak(ARI, "You haven't, but the emotional abuse... and how it controls.")
    $ setWait(63.688,66.274)
    $ speak(NICOLE, "You're really putting weight into what the fuck he says?")
    show ari sc6 sad:
        rightcenterstage


    $ setWait(66.274,68.859)
    $ speak(ARI, "He's a counselor, he knows about this stuff.")
    $ setWait(68.859,74.24)
    $ speak(NICOLE, "I'm your girlfriend. I pay for your Five Guys, he wants to put his dick in a child-- how am I getting outclassed here??")
    show ari sc6 angry:
        rightcenterstage
    $ setWait(74.24,76.659)
    $ speak(ARI, "No I always have to pay when we go to Five Guys.")
    $ setWait(76.659,79.37)
    $ speak(NICOLE, "Okay well, your dad drives a Lexus don't worry about it.")

    show nicole sc6:
        leftcenterstage


    $ setWait(79.37,84.917)
    $ speak(NICOLE, "But I'm just saying like, how are you gonna let our freak fucking counselor put all these ideas in your head?")

    $ setWait(84.917,86.294)
    $ speak(ARI, "Nicole...")
    show ari sc6 think:
        rightcenterstage

    $ setWait(86.294,89.797)
    $ speak(ARI, "I've had these ideas for a while...")
    $ setWait(89.797,93.217)
    $ speak(ARI, "All he did was give me the words to tell you.")
    show nicole sc6 angry:
        leftcenterstage

    $ setWait(93.217,95.052)
    $ speak(NICOLE, "Tell me what?")

    show ari sc6 sad:
        rightcenterstage

    $ setWait(95.052,98.139)
    $ speak(ARI, "I don't think we should see each other anymore.")
    show nicole sc6 sad:
        leftcenterstage

    $ setWait(98.139,101.934)
    $ speak(NICOLE, "So I'm losing my girlfriend because of the pedophile counselor?")
    show ari sc6 shy:
        rightcenterstage
        xzoom -1
        linear 3.2 off_right
    $ setWait(101.934,104.645)
    $ speak(ARI, "I'm sorry, Nicole.")
    show nicole sc6:
        leftcenterstage
    $ setWait(104.645,109.233)
    $ speak(NICOLE, "...I got dumped before the counselor got reported...")
    show nicole sc6:
        leftcenterstage
        pause 0.65
        xzoom -1
        linear 2.7 off_left

    $ setWait(109.233,112.402)
    $ speak(NICOLE, "Welp... I'm gonna go home and kill myself.")
    stop ambient fadeout 1.8
    jump scene_0073
label scene_0073:
    show black onlayer screens with Pause(1.7):
        alpha 0.0
        linear 1.5 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.3 alpha 0.0

    show title_onemonthlater onlayer screens

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(2.252):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter


    $ setVoiceTrack("audio/Scenes/0073.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3"
    scene cafeteria int 2
    hide title_onemonthlater onlayer screens
    show jecka sc6:
        rightmidstage

    show nicole sc7:
        rightcenterstage

    $ setWait(0.037,2.373)
    $ speak(JECKA, "Is Dust-Off the same high as whip-its?")
    $ setWait(2.373,3.874)
    $ speak(NICOLE, "I never tried Dust-Off.")
    show jecka sc6 surprised:
        rightmidstage
    $ setWait(3.874,4.709)
    $ speak(JECKA, "Really?")
    $ setWait(4.709,6.085)
    $ speak(NICOLE, "Why is that surprising?")
    show jecka sc6:
        rightmidstage
    $ setWait(6.085,8.212)
    $ speak(JECKA, "You've tried everything else when a guy offers.")
    show nicole sc7 angry:
        rightcenterstage
    $ setWait(8.212,12.675)
    $ speak(NICOLE, "Why would I flirt with a guy to get a free hit of Dust-Off? You can get the whole thing at store for like 3 dollars.")
    $ setWait(12.675,13.843)
    $ speak(JECKA, "Only 3 dollars?")
    show nicole sc7:
        rightcenterstage

    $ setWait(13.843,15.594)
    $ speak(NICOLE, "Yeah have you ever gone to a Staples?")
    show jecka sc6 sad:
        rightmidstage

    $ setWait(15.594,16.721)
    $ speak(JECKA, "Ew Staples?")
    $ setWait(16.721,19.473)
    $ speak(NICOLE, "What are you too High School Musical to walk into a Staples now?")

    show jecka sc6 angry:
        rightmidstage

    $ setWait(19.473,25.229)
    $ speak(JECKA, "No, every time I go in the one near school the manager always flirts with me.\nHe's like \"let's find you a new computer, sweetie.\"")
    $ setWait(25.229,27.231)
    $ speak(NICOLE, "What if he just wants to sell you a new computer?")
    $ setWait(27.231,28.607)
    $ speak(JECKA, "With his hand on my ass??")
    $ setWait(28.607,33.195)
    $ speak(NICOLE, "Okay...\nLittle late on that detail...\nYou don't complain when the guy at PacSun does it.")
    show jecka sc6:
        rightmidstage

    $ setWait(33.195,38.784)
    $ speak(JECKA, "Cause the guy at PacSun can get me something I actually want? I'm not gonna make out with a manager for a free pencil case.")

    show nicole sc7 surprised:
        rightcenterstage

    $ setWait(38.784,41.203)
    $ speak(NICOLE, "Are you saying you made out with the guy at PacSun?")
    $ setWait(41.203,43.372)
    $ speak(JECKA, "You're gay, right?--Don't ask don't tell, bitch.")
    show nicole sc7 angry:
        rightcenterstage

    $ setWait(43.372,44.54)
    $ speak(NICOLE, "Not gay anymore.")
    show jecka sc6 surprised:
        rightmidstage

    $ setWait(44.54,47.001)
    $ speak(JECKA, "Oh my god I forgot! Sorry! I wasn't thinking.")
    show nicole sc7:
        rightcenterstage

    $ setWait(47.001,48.627)
    $ speak(NICOLE, "No it's okay, I'm over it.")
    show jecka sc6 sad:
        rightmidstage

    $ setWait(48.627,53.174)
    $ speak(JECKA, "Are you sure? Didn't you like, try killing yourself over it?")
    show jecka sc6:
        rightmidstage
    $ setWait(53.174,60.89)
    $ speak(NICOLE, "Honestly not really. Like I got in the tub, cut a little, then the water was really nice and warm, and I don't know I just wasn't feeling it.")
    $ setWait(60.89,61.724)
    $ speak(JECKA, "I get that...")
    show jecka sc6 surprised:
        rightmidstage
    $ setWait(61.724,62.85)
    $ speak(JECKA, "--oh shit she's coming over here.")
    show nicole sc7 surprised:
        rightcenterstage
        pause 0.5
        xzoom -1

    show ari sc2:
        xzoom -1
        off_left
        linear 3 leftcenterstage

    $ setWait(62.85,63.934)
    $ speak(NICOLE, "What? Why?")
    $ setWait(63.934,65.311)
    $ speak(ARI, "Hey, Nicole.")
    $ setWait(65.311,66.645)
    $ speak(NICOLE, "Hi?")
    show jecka sc6:
        rightmidstage
    $ setWait(66.645,70.733)
    $ speak(ARI, "I just wanted to talk a little again, see how you were doing.")
    show ari sc2 think:
        leftcenterstage
        xzoom -1
    $ setWait(70.733,74.57)
    $ speak(ARI, "You haven't showed up to the group depression counseling in a while.")
    show nicole sc7:
        rightcenterstage
        xzoom -1
    $ setWait(74.57,76.405)
    $ speak(NICOLE, "Yeah I sorta quit that.")
    $ setWait(76.405,79.492)
    $ speak(ARI, "I figured, it would be awkward and everything.")
    $ setWait(79.492,80.618)
    $ speak(NICOLE, "Kinda like this.")
    show ari sc2:
        leftcenterstage
        xzoom -1
    $ setWait(80.618,84.121)
    $ speak(ARI, "Sorry I know. I just worry a lot.")
    $ setWait(84.121,87.249)
    $ speak(NICOLE, "...Are you trying to get back together again? I don't get it.")
    $ setWait(87.249,89.168)
    $ speak(ARI, "Yeah uh...")
    show ari sc2 think:
        leftcenterstage
        xzoom -1
    $ setWait(89.168,92.296)
    $ speak(ARI, "That's not exactly an option for me anymore?")
    show hunter sc3:
        xzoom -1
        off_left
        linear 2.4 leftmidstage
    $ setWait(92.296,94.715)
    $ speak(HUNTER, "Hey Ari, what's going on?")
    show ari sc2 smile:
        leftcenterstage
        xzoom 1
    $ setWait(94.715,96.884)
    $ speak(ARI, "Oh nothing I was just wrapping up here.")
    $ setWait(96.884,97.718)
    $ speak(NICOLE, "Who's this?")
    show ari sc2 think:
        leftcenterstage
        xzoom 1
    $ setWait(97.718,100.221)
    $ speak(ARI, "Oh yeah um, Nicole...")
    show ari sc2:
        leftcenterstage
        xzoom -1
    $ setWait(100.221,105.142)
    $ speak(ARI, "...this is my boyfriend Hunter.\nWe've been dating for a couple weeks now.")
    show nicole sc7 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(105.142,105.601)
    $ speak(HUNTER, "Hey.")
    show jecka sc6 surprised:
        rightmidstage

    $ setWait(105.601,106.644)
    $ speak(JECKA, "What the fuck.")
    $ setWait(106.644,107.52)
    $ speak(ARI, "Is something wrong?")
    $ setWait(107.52,108.687)
    $ speak(JECKA, "Oh uh..")
    show jecka sc6:
        rightmidstage

    show nicole sc7:
        rightcenterstage
        xzoom -1

    $ setWait(108.687,110.94)
    $ speak(JECKA, "I was just thinking about Staples.")
    $ setWait(110.94,112.191)
    $ speak(ARI, "The store?")
    $ setWait(112.191,112.942)
    $ speak(JECKA, "Long story.")
    $ setWait(112.942,116.529)
    $ speak(HUNTER, "Ari I gotta get back but your tray's at the table for you.")

    show ari sc2 smile:
        leftcenterstage
        xzoom 1

    show hunter sc3:
        leftmidstage
        xzoom 1
        linear 3 off_left

    $ setWait(116.529,120.241)
    $ speak(ARI, "Aw you're so sweet, thank you snookums.")
    show nicole sc7 angry:
        rightcenterstage
        xzoom -1
    $ setWait(120.241,121.867)
    $ speak(NICOLE, "Who the fuck says \"snookums\"?")
    show ari sc2:
        leftcenterstage
        xzoom -1
    $ setWait(121.867,122.576)
    $ speak(ARI, "What was that?")
    $ setWait(122.576,124.453)
    $ speak(NICOLE, "Oh sorry what I said was...")
    show nicole sc7 surprised:
        rightcenterstage
        xzoom -1
    $ setWait(124.453,125.704)
    $ speak(NICOLE, "I thought you were gay??")
    show ari sc2 think:
        leftcenterstage
        xzoom -1

    show nicole sc7:
        rightcenterstage
        xzoom -1
    $ setWait(125.704,128.874)
    $ speak(ARI, "Okay I knew we'd have to talk about this eventually.")
    $ setWait(128.874,130.668)
    $ speak(JECKA, "Are you bisexual now?")
    $ setWait(130.668,132.378)
    $ speak(ARI, "Honestly, no.")
    show jecka sc6 surprised:
        rightmidstage
    $ setWait(132.378,133.379)
    $ speak(JECKA, "What the fuck.")
    show ari sc2:
        leftcenterstage
        xzoom -1
    $ setWait(133.379,135.047)
    $ speak(ARI, "Are you thinking about Staples again?")
    $ setWait(135.047,136.924)
    $ speak(JECKA, "No like what the fuck is going on?")
    $ setWait(136.924,141.095)
    $ speak(NICOLE, "Yeah how can you have a boyfriend if you're not bisexual?")
    show ari sc2 shy:
        leftcenterstage
        xzoom -1
    $ setWait(141.095,145.516)
    $ speak(ARI, "The truth is... I still love everything about girls.")

    show jecka sc6:
        rightmidstage

    $ setWait(145.516,155.901)
    $ speak(ARI, "I love how they talk, how they laugh, how they use moisturizer, how they do makeup. I love how girls do their hair, how they smell nice, how they don't wear the same thing everyday...")
    $ setWait(155.901,161.866)
    $ speak(ARI, "And I really love how they hold your hand... and how it feels when they kiss you back.")
    $ setWait(161.866,165.244)
    $ speak(ARI, "Dating you helped me find the words for that, Nicole.")
    $ setWait(165.244,168.289)
    $ speak(NICOLE, "...Then you're dating a guy because?")
    show ari sc2 sad:
        leftcenterstage
        xzoom -1

    $ setWait(168.289,173.669)
    $ speak(ARI, "Because like, even though I feel that way I have to be honest with myself...")
    show ari sc2 shy:
        leftcenterstage
        xzoom -1
    $ setWait(173.669,178.966)
    $ speak(ARI, "Girls are kinda high maintenance.\nGirls play mind games I can't figure out.")
    $ setWait(178.966,182.803)
    $ speak(ARI, "And so the month we had together made me realize something else.")
    show nicole sc7 sad:
        rightcenterstage
        xzoom -1
    $ setWait(182.803,184.18)
    $ speak(NICOLE, "Realize what?")
    show ari sc2:
        leftcenterstage
        xzoom -1
    $ setWait(184.18,186.599)
    $ speak(ARI, "I realized that guys turn me off but...")
    show ari sc2 sad:
        leftcenterstage
        xzoom -1
        pause 1.3
        xzoom 1
        linear 2.1 off_left

    $ setWait(186.599,191.395)
    $ speak(ARI, "...girls make me wanna fucking kill myself.")
    show jecka sc6 sad:
        rightmidstage
    $ setWait(191.395,194.69)
    $ speak(JECKA, "...You bullied a gay girl into being straight.")
    show nicole sc7:
        rightcenterstage
        xzoom 1
    $ setWait(194.69,199.153)
    $ speak(NICOLE, "She's not straight now she's just... gonna be miserable for the rest of her life, big difference.")
    $ setWait(199.153,201.197)
    $ speak(JECKA, "Are you seriously not getting how bad this is?")
    show nicole sc7 sad:
        rightcenterstage
    $ setWait(201.197,202.448)
    $ speak(NICOLE, "How bad what is?")
    $ setWait(202.448,205.451)
    $ speak(JECKA, "You bullying a gay girl into being straight.")
    show nicole sc7:
        rightcenterstage
    $ setWait(205.451,208.579)
    $ speak(NICOLE, "I didn't bully her I was just abusive while dating her.")
    show jecka sc6:
        rightmidstage

    $ setWait(208.579,209.622)
    $ speak(JECKA, "What's the difference?")
    $ setWait(209.622,212.374)
    $ speak(NICOLE, "One's homophobic, the other's just regular bad.")
    $ setWait(212.374,214.084)
    $ speak(JECKA, "So you get how bad this is then?")
    show nicole sc7 angry:
        rightcenterstage

    $ setWait(214.084,217.463)
    $ speak(NICOLE, "Bitch you watch Smallville, do you get how bad that is?")
    $ setWait(217.463,219.215)
    $ speak(JECKA, "That's not gonna work this time, Nicole.")
    $ setWait(219.215,221.8)
    $ speak(NICOLE, "What the fuck is this? Why do you even care?")
    $ setWait(221.8,222.51)
    $ speak(JECKA, "Whatever.")
    $ setWait(222.51,224.803)
    $ speak(NICOLE, "Whatever what? Are we not friends anymore?")
    $ setWait(224.803,226.847)
    $ speak(JECKA, "Well I wouldn't want you as an enemy, holy shit.")
    $ setWait(226.847,232.019)
    $ speak(NICOLE, "No--explain to me how this is any more awful than anything I usually do?")
    $ setWait(232.019,234.271)
    $ speak(JECKA, "Cause usually you do it to men.")
    show nicole sc7:
        rightcenterstage

    $ setWait(234.271,239.818)
    $ speak(JECKA, "I'm like \"was that overboard?\" and you always say \"he'll end up a rapist or pedophile anyway\".")
    $ setWait(239.818,247.076)
    $ speak(JECKA, "But she's a teenage girl, Nicole.\nShe is a gay, codependent, teenage, girl, as if it wasn't hard enough.")
    show jecka sc6 angry:
        rightmidstage

    $ setWait(247.076,250.246)
    $ speak(JECKA, "What's your excuse this time?")
    show nicole sc7 angry:
        rightcenterstage

    show jecka sc6:
        rightmidstage

    $ setWait(250.246,254.124)
    $ speak(NICOLE, "That bitch stole my depression idea, fuck her.")

    show jecka sc6:
        rightmidstage
        xzoom -1
        linear 2.4 off_right


    show nicole sc7:
        rightcenterstage

    $ setWait(254.124,256.627)
    $ speak(JECKA, "You should've said nothing.")
    stop ambient fadeout 2
    jump end_0074

label end_0074:

    show black onlayer screens with Pause(1.7):
        alpha 0.0
        linear 1.5 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.3 alpha 0.0

    if "end_0074" not in persistent.endings:
        $ persistent.endings.append("end_0074")
        $ persistent.new_ending = True


    scene onlayer master
    show black
    $ quick_menu = False
    $ csbox = True

    $ renpy.movie_cutscene("cs0074.webm")

    return

label scene_0075:
    $ setVoiceTrack("audio/Scenes/0075.mp3")
    scene school int 2
    show nicole sc4 smile:
        leftmidstage

    show ari sc4 shy:
        centerstage
    $ setWait(0.006,2.383)
    $ speak(NICOLE, "Oh this shit's fun.")
    $ setWait(2.383,3.634)
    $ speak(ARI, "Fun why?")
    $ setWait(3.634,7.763)
    $ speak(NICOLE, "You don't think it's weird to tell a girl you love her and then ask if she's gay?")
    $ setWait(7.763,11.851)
    $ speak(ARI, "I... I guess I wasn't thinking, I don't know.")
    show nicole sc4:
        leftmidstage

    $ setWait(11.851,17.273)
    $ speak(NICOLE, "So let's say I said \"yes\", right? If you were my girlfriend what would you do for me?")
    show ari sc4 sad:
        centerstage

    $ setWait(17.273,19.567)
    $ speak(ARI, "I don't know, anything you want?")
    show nicole sc4 smile:
        leftmidstage

    $ setWait(19.567,23.446)
    $ speak(NICOLE, "Anything? Damn.\nSo any depraved ass shit you're just down for.")
    $ setWait(23.446,25.281)
    $ speak(ARI, "For you, yeah.")
    $ setWait(25.281,26.991)
    $ speak(NICOLE, "Could I choke you while we make out?")
    $ setWait(26.991,28.451)
    $ speak(ARI, "If you want.")
    $ setWait(28.451,30.745)
    $ speak(NICOLE, "Could I smack the shit out of you in public?")

    show ari sc4 shy:
        centerstage

    $ setWait(30.745,31.704)
    $ speak(ARI, "Yes please.")
    $ setWait(31.704,33.581)
    $ speak(NICOLE, "Gahhh self-esteem.")
    show ari sc4 sad:
        centerstage

    $ setWait(33.581,34.582)
    $ speak(ARI, "Am I too desperate?")
    $ setWait(34.582,38.502)
    $ speak(NICOLE, "No not your self-esteem, my self-esteem. It's through the roof right now.")
    $ setWait(38.502,39.629)
    $ speak(ARI, "How come?")
    $ setWait(39.629,43.049)
    $ speak(NICOLE, "Cause now that a girl wants me this bad I'm like universally hot now.")
    $ setWait(43.049,44.3)
    $ speak(ARI, "But you don't...")

    show nicole sc4:
        leftmidstage

    $ setWait(44.3,47.928)
    $ speak(NICOLE, "Yeah not really, sorry. Not there yet.")
    $ setWait(47.928,48.721)
    $ speak(ARI, "Oh.")
    $ setWait(48.721,50.139)
    $ speak(NICOLE, "Look you're probably better off.")
    $ setWait(50.139,51.974)
    $ speak(ARI, "It doesn't feel like I'm better off.")
    $ setWait(51.974,55.519)
    $ speak(NICOLE, "Speaking of \"off\", you're not gonna off yourself over this, are you?")
    $ setWait(55.519,57.563)
    $ speak(NICOLE, "Cause if you do will you leave me your iTouch?")
    show ari sc4 angry:
        centerstage

    $ setWait(57.563,60.441)
    $ speak(ARI, "Why the fuck would I give my iTouch to a girl rejecting me?")
    $ setWait(60.441,64.32)
    $ speak(NICOLE, "Sorry it works with guys, never mind.\nDoes this feel like a hole in your chest or what?")
    show ari sc4 shy:
        centerstage

    $ setWait(64.32,68.324)
    $ speak(ARI, "I feel like I'm gonna be alone forever, I don't know any girl who's gay here.")
    $ setWait(68.324,69.492)
    $ speak(NICOLE, "You could find out.")
    $ setWait(69.492,70.117)
    $ speak(ARI, "How?")
    $ setWait(70.117,74.58)
    $ speak(NICOLE, "Sext a pic of yourself to every straight girl you know, one of them's bound to be in the closet.")
    show ari sc4 sad:
        centerstage

    $ setWait(74.58,76.04)
    $ speak(ARI, "Wha-- and if they're not!?")
    $ setWait(76.04,82.38)
    $ speak(NICOLE, "Worst case scenario, they forward it to their boyfriends.\nHe'll text back like \"haha what an idiot\" but the picture will absolutely go in the rotation.")
    $ setWait(82.38,83.756)
    $ speak(ARI, "Rotation for what??")
    show nicole sc4:
        leftmidstage
        pause 2.3
        xzoom -1
        linear 1.9 off_left

    $ setWait(83.756,88.427)
    $ speak(NICOLE, "Look I gotta go, just forget what I said. Good luck, excuse stealer.")
    show ari sc4 angry:
        centerstage
        xzoom -1
        linear 3 off_right

    $ setWait(88.427,89.928)
    $ speak(ARI, "Bitch.")
    stop ambient fadeout 1
    jump scene_0076
label scene_0076:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0076.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    scene cafeteria int
    show nicole sc5:
        leftcenterstage

    show jecka sc4:
        rightcenterstage

    $ setWait(0.045,2.339)
    $ speak(JECKA, "Do you like Date Movie?")
    $ setWait(2.339,3.757)
    $ speak(NICOLE, "Is that the parody movie?")
    $ setWait(3.757,5.718)
    $ speak(JECKA, "Yeah the one with the milkshakes song.")
    $ setWait(5.718,6.844)
    $ speak(NICOLE, "Yeah it was kinda funny.")
    $ setWait(6.844,12.433)
    $ speak(JECKA, "I thought so too, but I was trying to watch it online and the movie website said it was 3 out of 10 stars.")
    $ setWait(12.433,13.767)
    $ speak(NICOLE, "What? It wasn't that bad.")
    $ setWait(13.767,18.272)
    $ speak(JECKA, "I know. I tried clicking 9 stars to bump it up and it said I had to sign in.")
    $ setWait(18.272,19.022)
    $ speak(NICOLE, "Did you?")

    show jecka sc4 angry:
        rightcenterstage

    $ setWait(19.022,22.234)
    $ speak(JECKA, "Who the fuck has time for that shit? I just wanted to watch the movie again.")
    $ setWait(22.234,27.906)
    $ speak(NICOLE, "Huh. That means all the opinions on the internet are only from weirdos with enough time to create an account.")
    $ setWait(27.906,32.536)
    $ speak(JECKA, "I know it's so dumb. Like maybe if you fucked a bitch you'd know a good movie when you see one.")
    $ setWait(32.536,36.206)
    $ speak(NICOLE, "Are you saying that hating Date Movie makes you a virgin?")

    show jecka sc4:
        rightcenterstage

    $ setWait(36.206,37.541)
    $ speak(JECKA, "I mean basically.")
    $ setWait(37.541,38.667)
    $ speak(NICOLE, "I could get behind that.")
    $ setWait(38.667,46.133)
    $ speak(JECKA, "But no so I go on the rest of the site like what do they think's a good movie, and all their 9 star movies are so boring. Have you seen The Godfather?")
    $ setWait(46.133,47.176)
    $ speak(NICOLE, "I've heard of it.")
    show jecka sc4 angry:
        rightcenterstage
    $ setWait(47.176,50.429)
    $ speak(JECKA, "My Dad made me watch it, I fell asleep. How is that a 9?")
    $ setWait(50.429,51.764)
    $ speak(NICOLE, "What else was high?")
    show jecka sc4:
        rightcenterstage
    $ setWait(51.764,55.726)
    $ speak(JECKA, "Uh, there was American History X but I haven't seen it.")
    $ setWait(55.726,57.936)
    $ speak(NICOLE, "That one's cool, kinda long though.")
    $ setWait(57.936,59.104)
    $ speak(JECKA, "What's it about?")
    $ setWait(59.104,60.189)
    $ speak(NICOLE, "A racist guy.")

    show jecka sc4 sad:
        rightcenterstage

    $ setWait(60.189,62.024)
    $ speak(JECKA, "You like a movie about a racist guy?")

    show jecka sc4:
        rightcenterstage

    $ setWait(62.024,63.567)
    $ speak(NICOLE, "There's like a whole moral whatever.")

    show trody sc1:
        off_right
        linear 0.8 rightstage
        pause 0.6
        xzoom -1
        linear 1 off_right

    show jecka sc4:
        rightcenterstage
        pause 1
        xzoom -1

    $ setWait(63.567,65.778)
    $ speak(TRODY, "Weird Christian bitch.")
    show nicole sc5 angry:
        leftcenterstage


    $ setWait(65.778,67.112)
    $ speak(NICOLE, "What the hell was that?")
    show jecka sc4:
        rightcenterstage

    $ setWait(67.112,69.907)
    $ speak(JECKA, "Yeah I don't know where he got that...")
    show jecka sc4:
        xzoom 1
        rightcenterstage

    $ setWait(69.907,70.949)
    $ speak(JECKA, "But so another movie was...")
    show megan sc3 angry:
        xzoom -1
        off_left
        linear 2 leftmidstage

    show kelly sc3 angry:
        xzoom -1
        off_farleft
        linear 1.5 leftstage

    $ setWait(70.949,72.409)
    $ speak(KELLY, "Oh look who it is.")
    $ setWait(72.409,73.827)
    $ speak(MEGAN, "It's the school bigot.")
    show nicole sc5 surprised:
        leftcenterstage
        xzoom -1

    show jecka sc4 sad:
        rightcenterstage
        xzoom 1

    $ setWait(73.827,74.286)
    $ speak(NICOLE, "What??")
    $ setWait(74.286,76.622)
    $ speak(MEGAN, "Don't play dumb, we heard what you said.")
    $ setWait(76.622,78.207)
    $ speak(KELLY, "And we heard what you did to Ari.")
    $ setWait(78.207,82.127)
    $ speak(MEGAN, "You'll really reject a gay girl then have the nerve to say no one's homophobic here?")
    show nicole sc5 angry:
        leftcenterstage
        xzoom 1
    $ setWait(82.127,84.296)
    $ speak(NICOLE, "Oh so now our conversations are worth broadcasting?")
    $ setWait(84.296,86.924)
    $ speak(JECKA, "I only mentioned it to one person, I didn't think it'd be a thing!")
    show nicole sc5 angry:
        leftcenterstage
        pause 0.8
        xzoom -1

    $ setWait(86.924,89.384)
    $ speak(MEGAN, "Ari told people too. You're sick, Nicole!")
    $ setWait(89.384,92.471)
    $ speak(KELLY, "Pretending there isn't bigotry here, must be nice to ignore it!")
    show jecka sc4:
        rightcenterstage

    $ setWait(92.471,93.597)
    $ speak(NICOLE, "What are you gay?")
    $ setWait(93.597,94.223)
    $ speak(KELLY, "No.")
    $ setWait(94.223,95.14)
    $ speak(NICOLE, "Then fuck off!")
    $ setWait(95.14,97.1)
    $ speak(MEGAN, "You don't need to be gay to fight homophobia.")
    $ setWait(97.1,100.229)
    $ speak(NICOLE, "I never said she can't be gay, I said no one here would hate her for being gay!")
    $ setWait(100.229,102.815)
    $ speak(KELLY, "Indifference is as bad as participation!")
    $ setWait(102.815,107.402)
    $ speak(NICOLE, "What the fuck did that have to do with what I just said?? Do you just have a list of sayings memorized?")
    $ setWait(107.402,114.618)
    $ speak(MEGAN, "Actually we have a list of 500 signatures.\n500 signatures in favor of expelling you for gay bashing Ari!")
    $ setWait(114.618,115.369)
    $ speak(JECKA, "Damn that's a lot.")
    $ setWait(115.369,117.746)
    $ speak(NICOLE, "When the hell did you get 500 signatures?")
    $ setWait(117.746,122.626)
    $ speak(KELLY, "Over the last 2 days, and I think it's safe to say the people have spoken.")
    $ setWait(122.626,125.796)
    $ speak(MEGAN, "Everyone we went up to immediately signed to fight homophobia.")
    $ setWait(125.796,127.339)
    $ speak(NICOLE, "Okay kinda proving my point.")
    $ setWait(127.339,129.55)
    $ speak(KELLY, "What point? That you hate gay people?")
    $ setWait(129.55,134.93)
    $ speak(NICOLE, "If there's such a mass homophobia problem at the school how'd you get 500 signatures with no push-back at all?")
    $ setWait(134.93,137.933)
    $ speak(KELLY, "Ugh so ignorant. The GSA club weeps for you.")
    $ setWait(137.933,140.561)
    $ speak(MEGAN, "Yeah I don't think you're ready for a conversation about this.")
    show kelly sc3:
        leftstage
        xzoom -1
        pause 0.5
        xzoom 1
        linear 1.2 off_left

    show megan sc3 angry:
        leftmidstage
        xzoom -1
        pause 1
        xzoom 1
        linear 1.5 off_left

    $ setWait(140.561,142.938)
    $ speak(KELLY, "C'mon let's get more signatures.")

    show hunter sc2:
        off_right
        linear 0.8 rightstage
        pause 0.5
        xzoom -1
        linear 1 off_right

    $ setWait(142.938,145.107)
    $ speak(HUNTER, "Homophobic? C'mon man.")
    show nicole sc5 sad:
        leftcenterstage
        xzoom 1

    $ setWait(145.107,146.316)
    $ speak(NICOLE, "Am I going crazy here?")
    $ setWait(146.316,148.527)
    $ speak(JECKA, "Yeah this feels a little over the top.")
    $ setWait(148.527,151.321)
    $ speak(NICOLE, "Can you like talk to people for me and clear this up?")
    show ari sc5:
        off_left
        xzoom -1
        linear 2 leftstage

    $ setWait(151.321,153.365)
    $ speak(JECKA, "Hell no not getting involved.")
    show nicole sc5 surprised:
        leftcenterstage
        xzoom -1

    $ setWait(153.365,154.491)
    $ speak(NICOLE, "Oh Ari!")
    show ari sc5:
        leftstage
        xzoom -1
        linear 1 leftmidstage

    $ setWait(154.491,155.242)
    $ speak(ARI, "Yeah?")
    show nicole sc5 angry:
        leftcenterstage
        xzoom -1
    $ setWait(155.242,157.327)
    $ speak(NICOLE, "What's this shit about me hating gay people?")
    $ setWait(157.327,160.706)
    $ speak(ARI, "I didn't tell anyone that but they just kinda had their own conclusion.")
    show nicole sc5 sad:
        leftcenterstage
        xzoom -1

    $ setWait(160.706,162.207)
    $ speak(NICOLE, "Well can you tell 'em to chill out?")
    show ari sc5 sad:
        leftmidstage
        xzoom -1

    $ setWait(162.207,165.085)
    $ speak(ARI, "Why the fuck would I do anything for you? You rejected me.")
    show nicole sc5 angry:
        leftcenterstage
        xzoom -1

    show ari sc5:
        leftmidstage
        xzoom -1

    $ setWait(165.085,166.169)
    $ speak(NICOLE, "This is bullshit.")
    show jecka sc4 smile:
        rightcenterstage

    show nicole sc5:
        leftcenterstage
        xzoom -1

    $ setWait(166.169,167.754)
    $ speak(JECKA, "Oh Ari I got your picture.")
    $ setWait(167.754,168.505)
    $ speak(ARI, "You did?")
    $ setWait(168.505,169.798)
    $ speak(JECKA, "Yeah you looked hot as fuck in it.")
    show ari sc5 smile:
        leftmidstage
        xzoom -1

    $ setWait(169.798,172.801)
    $ speak(ARI, "Oh my god thank you! Would you wanna try like...")
    show jecka sc4:
        rightcenterstage

    $ setWait(172.801,176.221)
    $ speak(JECKA, "No sorry, I'm not there yet. Maybe in college.")

    show ari sc5 angry:
        leftmidstage
        xzoom 1
        linear 2 off_left

    $ setWait(176.221,178.14)
    $ speak(ARI, "Dumbest advice ever.")
    $ setWait(178.14,180.934)
    $ speak(JECKA, "...Who would advise her to randomly sext people?")
    show nicole sc5 surprised:
        leftcenterstage
        xzoom 1
    $ setWait(180.934,181.81)
    $ speak(NICOLE, "Oh shit.")
    $ setWait(181.81,182.436)
    $ speak(JECKA, "What?")
    show nicole sc5:
        leftcenterstage
        xzoom 1
    $ setWait(182.436,183.77)
    $ speak(NICOLE, "Nothing--Show me the picture?")
    show jecka sc4 angry:
        rightcenterstage
        xzoom -1
        linear 2.6 off_right

    $ setWait(183.77,185.147)
    $ speak(JECKA, "No, get your own.")
    stop ambient fadeout 1
    jump scene_0077
label scene_0077:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0077.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 2
    show lynn 3:
        rightmidstage

    show nicole sc5 angry:
        leftmidstage

    $ setWait(0.039,4.418)
    $ speak(LYNN, "As you might be aware, the school's GSA has been petitioning for your immediate expulsion.")
    $ setWait(4.418,6.003)
    $ speak(NICOLE, "The fuck's a GSA?")
    $ setWait(6.003,7.713)
    $ speak(LYNN, "Gay-Straight-Alliance?")
    $ setWait(7.713,11.551)
    $ speak(NICOLE, "So if a gay girl asks me out I'm just not allowed to reject her?")
    $ setWait(11.551,17.39)
    $ speak(LYNN, "I'm not exactly sure that's what they're saying. The claim is that you bullied a gay girl by downplaying homophobia.")
    $ setWait(17.39,21.853)
    $ speak(NICOLE, "Yeah but I'm pretty sure this all became a thing cause I wouldn't go out with her.")
    $ setWait(21.853,27.149)
    $ speak(LYNN, "Well I'm sorry but that detail doesn't seem to be relevant in the documentation for this petition.")
    $ setWait(27.149,31.07)
    $ speak(NICOLE, "What do I have to do to prove I'm not homophobic? Make out with her on public access?")
    $ setWait(31.07,35.324)
    $ speak(LYNN, "Nicole you know the public access stations wouldn't allow that, don't be disingenuous.")
    $ setWait(35.324,38.536)
    $ speak(NICOLE, "Okay then channel 4? 5? The CW? What?")
    $ setWait(38.536,39.579)
    $ speak(LYNN, "That's not what I meant.")
    $ setWait(39.579,40.913)
    $ speak(NICOLE, "Well what do I have to do??")
    $ setWait(40.913,45.167)
    $ speak(LYNN, "I believe the best course of action is writing Ari a formal apology letter--")
    $ setWait(45.167,47.879)
    $ speak(NICOLE, "Fuck that shit! Do you even know how I got involved with this bitch!?")
    $ setWait(47.879,48.713)
    $ speak(LYNN, "Language.")
    $ setWait(48.713,50.381)
    $ speak(NICOLE, "Do you even know how I got involved with this ho?")
    $ setWait(50.381,51.09)
    $ speak(LYNN, "Slightly better.")
    $ setWait(51.09,55.97)
    $ speak(NICOLE, "She stole one of my homework excuses and I got stuck in group counseling with her. Ari screwed me over first.")
    $ setWait(55.97,59.348)
    $ speak(LYNN, "Nicole this is like telling police they should arrest someone for selling you bad weed.")
    $ setWait(59.348,61.434)
    $ speak(NICOLE, "I wouldn't put selling a bag of stems past her either.")
    $ setWait(61.434,65.855)
    $ speak(LYNN, "Look it's either write her a letter, go to a sensitivity retreat, or be expelled.")
    show nicole sc5:
        leftmidstage

    $ setWait(65.855,68.774)
    $ speak(NICOLE, "Sensitivity retreat? Is that like conversion therapy?")
    $ setWait(68.774,74.238)
    $ speak(LYNN, "Third person reverse conversion therapy.\nYou have a week to decide, you're excused.")
    stop ambient fadeout 1
    jump scene_0078
label scene_0078:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0078.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 2
    show karen sc3:
        leftmidstage
        xzoom -1

    show nicole sc5:
        xzoom -1
        off_right
        linear 2 rightmidstage

    $ setWait(0.039,2.875)
    $ speak(NICOLE, "What a waste of time...\nKaren?")

    show karen sc3 angry:
        leftmidstage
        xzoom 1
        linear 1.5 off_left

    $ setWait(2.875,3.918)
    $ speak(KAREN, "Homophobe.")
    show nicole sc5:
        rightmidstage
        xzoom -1
        linear 1 centerstage

    $ setWait(3.918,4.919)
    $ speak(NICOLE, "Even Karen?")
    show megan sc3 angry:
        off_left
        xzoom -1
        linear 3.2 off_right

    $ setWait(4.919,6.545)
    $ speak(MEGAN, "Your days are numbered, bitch.")
    show nicole sc5 angry:
        centerstage
        xzoom 1

    $ setWait(6.545,8.339)
    $ speak(NICOLE, "Holy shit get a hobby.")
    show kylar sc2:
        off_right
        linear 1.8 rightmidstage

    $ setWait(8.339,9.382)
    $ speak(KYLAR, "Sucks, don't it?")
    $ setWait(9.382,11.801)
    $ speak(NICOLE, "Okay let's hear your dumbass insult.")
    $ setWait(11.801,12.301)
    $ speak(KYLAR, "What?")
    $ setWait(12.301,14.303)
    $ speak(NICOLE, "Pile it on. I'm a homophobe, right?")
    $ setWait(14.303,16.389)
    $ speak(KYLAR, "You think I'm just another sheep, don't you?")
    $ setWait(16.389,18.099)
    $ speak(NICOLE, "Is sheep interchangeable with dipshit?")

    show kylar sc2 smile:
        rightmidstage

    $ setWait(18.099,23.938)
    $ speak(KYLAR, "Don't get defensive, I've heard what they're saying about you. Let's just say I know a place that can help you out.")
    show nicole sc5:
        centerstage

    $ setWait(23.938,26.691)
    $ speak(NICOLE, "What could possibly help me out of this situation?")
    $ setWait(26.691,28.359)
    $ speak(KYLAR, "I don't know maybe...")
    $ setWait(28.359,29.652)
    $ speak(KYLAR, "The Straight Club?")
    show nicole sc5 surprised:
        centerstage

    $ setWait(29.652,30.987)
    $ speak(NICOLE, "The Straight Club!?")
    show kylar sc2:
        rightmidstage

    $ setWait(30.987,32.238)
    $ speak(KYLAR, "Shhh! It's on the DL, dude.")
    show nicole sc5 angry:
        centerstage

    $ setWait(32.238,33.864)
    $ speak(NICOLE, "What the hell is the Straight Club?")
    $ setWait(33.864,41.455)
    $ speak(KYLAR, "Just a place for us straights, y'know? A group to avoid bitches in the GSA for sure. If they're so proud of being gay then we're proud of being straight.")
    show nicole sc5:
        centerstage

    $ setWait(41.455,42.957)
    $ speak(NICOLE, "I gotta be dreaming right now.")

    show kylar sc2 smile:
        rightmidstage

    $ setWait(42.957,44.041)
    $ speak(KYLAR, "That good, huh?")
    $ setWait(44.041,48.129)
    $ speak(NICOLE, "More like so incredibly fucking stupid there's no way it's real.")
    $ setWait(48.129,50.673)
    $ speak(KYLAR, "Oh it's real alright, and you're invited.")
    $ setWait(50.673,52.049)
    $ speak(NICOLE, "I feel so special.")
    $ setWait(52.049,58.139)
    $ speak(KYLAR, "C'mon it's fun. We make signs, plan events, talk about John McCain, have pizza parties. Just a wholesome get together.")
    $ setWait(58.139,59.098)
    $ speak(NICOLE, "Wholesome huh?")
    $ setWait(59.098,60.558)
    $ speak(KYLAR, "Hundred percent.")
    $ setWait(60.558,63.269)
    $ speak(NICOLE, "Do you still have percocet? I'll go if you give me some.")
    show kylar sc2:
        rightmidstage

    $ setWait(63.269,64.52)
    $ speak(KYLAR, "Uh alright sure.")
    $ setWait(64.52,65.73)
    $ speak(NICOLE, "Okay where is it?")
    $ setWait(65.73,68.232)
    $ speak(KYLAR, "Follow me, we can't disclose it verbally okay?")
    show kylar sc2 smile:
        rightmidstage
        linear 3 off_left

    $ setWait(68.232,70.359)
    $ speak(KYLAR, "You're in luck too, it's Straight Club movie night.")
    show nicole sc5:
        xzoom -1
        centerstage
        linear 2.5 off_left

    $ setWait(70.359,71.569)
    $ speak(NICOLE, "Swell.")
    stop ambient fadeout 1
    jump scene_0079
label scene_0079:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0079.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3
    show kylar sc2 smile:
        xzoom -1
        off_left
        linear 1.8 leftcenterstage

    show nicole sc5:
        off_farleft
        linear 1.9 leftmidstage

    show braxton sc2 smile:
        rightmidstage

    show jeffery sc3 smile:
        rightstage

    $ setWait(0.042,2.503)
    $ speak(KYLAR, "Guys welcome our new member, Nicole.")
    $ setWait(2.503,3.546)
    $ speak(BRAXTON, "Aw what's up?")
    $ setWait(3.546,5.006)
    $ speak(JEFFERY, "Fancy seeing you here!")
    $ setWait(5.006,6.799)
    $ speak(NICOLE, "Why am I not surprised it's all men?")
    $ setWait(6.799,9.051)
    $ speak(KYLAR, "It's movie night, boys. We got the projector ready?")
    show braxton sc2 smile:
        xzoom -1
        rightmidstage
        linear 2 off_right

    $ setWait(9.051,10.094)
    $ speak(BRAXTON, "Nah but I got it.")
    show kylar sc2 smile:
        leftcenterstage
        xzoom -1
        linear 2.3 off_right

    $ setWait(10.094,11.721)
    $ speak(KYLAR, "Cool lemme help ya.")
    show jeffery sc3 smile:
        rightstage
        linear 1.4 rightcenterstage

    $ setWait(11.721,13.598)
    $ speak(JEFFERY, "So you're in the straight club, huh?")
    show nicole sc5:
        leftmidstage
        linear 1.7 leftcenterstage

    $ setWait(13.598,15.349)
    $ speak(NICOLE, "Let's not use the word \"in\".")
    $ setWait(15.349,16.517)
    $ speak(JEFFERY, "Visiting then.")
    $ setWait(16.517,19.145)
    $ speak(NICOLE, "I guess? Why are you in the straight club?")
    $ setWait(19.145,21.856)
    $ speak(JEFFERY, "Isn't it obvious?")
    $ setWait(21.856,22.732)
    $ speak(NICOLE, "...Don't make me say it.")

    show jeffery sc3:
        rightcenterstage

    $ setWait(22.732,33.284)
    $ speak(JEFFERY, "Well okay maybe it's kind of a long story. It all goes back to when I finally started narrowing down my interests into a couple key hobbies. Like video games and anime for starters.")
    $ setWait(33.284,34.201)
    $ speak(NICOLE, "Don't make me say it.")
    $ setWait(34.201,42.418)
    $ speak(JEFFERY, "And I loved stuff like that so much I wasn't afraid to tell anyone about it, but I didn't think so many people would find it annoying.")
    $ setWait(42.418,48.924)
    $ speak(JEFFERY, "My hobbies are practically my identity and ever since middle school I've been bullied for every hobby I have.")
    $ setWait(48.924,49.634)
    $ speak(NICOLE, "Good.")
    $ setWait(49.634,58.351)
    $ speak(JEFFERY, "Yeah that's what they said too. I saw other kids get bullied for being gay or foreign and everyone immediately rushed to their defense.")
    $ setWait(58.351,66.525)
    $ speak(JEFFERY, "But when I got bullied for how I talked or what I liked, no one really cared.\nLike I wasn't supposed to be protected.")
    $ setWait(66.525,69.195)
    $ speak(NICOLE, "Almost as if liking anime is a choice.")
    $ setWait(69.195,77.119)
    $ speak(JEFFERY, "Exactly, and that's when I realized no one's sympathetic when you're regular bullied. They only care if you're bullied for something you say you're born as.")
    show jeffery sc3 smile:
        rightcenterstage

    $ setWait(77.119,82.291)
    $ speak(JEFFERY, "Before they were jerks for bullying me, but with this new group they're gonna be bigots!")
    $ setWait(82.291,86.17)
    $ speak(NICOLE, "Okay that surprisingly clicks, except for one thing.")

    show jeffery sc3:
        rightcenterstage

    $ setWait(86.17,86.962)
    $ speak(JEFFERY, "What's that?")
    show nicole sc5 angry:
        leftcenterstage

    $ setWait(86.962,89.048)
    $ speak(NICOLE, "Why the fuck did you pick the straight club?")
    $ setWait(89.048,94.011)
    $ speak(JEFFERY, "I couldn't really pull off being gay, I get too nervous around girls.")
    show nicole sc5:
        leftcenterstage

    $ setWait(94.011,102.353)
    $ speak(JEFFERY, "My friend Jasper loved cartoons and Amanda Show, but then he came out as gay and it was like no one was allowed to call him annoying anymore.")
    show nicole sc5 surprised:
        leftcenterstage

    $ setWait(102.353,103.521)
    $ speak(NICOLE, "Did you say Amanda Show?")
    $ setWait(103.521,104.48)
    $ speak(JEFFERY, "Yeah why?")
    show nicole sc5:
        leftcenterstage

    $ setWait(104.48,109.318)
    $ speak(NICOLE, "No reason--Straight pride isn't gonna make anyone wanna protect you. Straights are way in the lead here.")
    $ setWait(109.318,116.117)
    $ speak(JEFFERY, "Well if that's true why do we have to be so secretive of the Straight Pride Club? Feels like everyone gets a pride rally but us.")
    $ setWait(116.117,117.952)
    $ speak(NICOLE, "It's called a Redskins tailgate.")
    $ setWait(117.952,123.416)
    $ speak(JEFFERY, "Uh- never mind let's not get into this on movie night. Really not the time for politics.")
    $ setWait(123.416,127.42)
    $ speak(NICOLE, "It's not politics it's fucking dumb as shit. What teacher would even sponsor this?")
    $ setWait(127.42,132.341)
    $ speak(JEFFERY, "We couldn't get an official sponsor, but one teacher agreed to under-the-table sponsor us.")
    $ setWait(132.341,134.802)
    $ speak(NICOLE, "Okay so what teacher would under-the-table sponsor this?")
    show coach 2:
        xzoom -1
        off_left
        linear 1.2 leftstage

    $ setWait(134.802,137.888)
    $ speak(COACH, "Greetings fellow straights! I brought the movie--")
    show coach 2 smile:
        leftstage
        xzoom -1
        linear 0.5 leftmidstage

    show nicole sc5:
        leftcenterstage
        xzoom -1

    $ setWait(137.888,138.681)
    $ speak(COACH, "--Nicole??")
    $ setWait(138.681,139.64)
    $ speak(NICOLE, "Of course.")
    $ setWait(139.64,143.769)
    $ speak(COACH, "Now that we got a pretty girl in the Straight Club we're really in business!")
    show kylar sc2 smile:
        off_right
        xzoom 1
        linear 1.5 rightmidstage

    $ setWait(143.769,146.605)
    $ speak(KYLAR, "Dude perfect timing! What's the movie this week, Coach?")
    show braxton sc2 smile:
        off_right
        xzoom 1
        linear 1 rightstage

    $ setWait(146.605,148.649)
    $ speak(JEFFERY, "It's not Rambo 3 again, is it?")
    $ setWait(148.649,156.449)
    $ speak(COACH, "No I thought we'd switch things up from the last four weeks.\nI got a very special copy of American History X!")
    $ setWait(156.449,157.575)
    $ speak(NICOLE, "Seen it, I'm leaving.")
    show coach 2:
        leftmidstage
        xzoom -1

    $ setWait(157.575,159.201)
    $ speak(COACH, "Not so fast, young lady.")
    $ setWait(159.201,160.453)
    $ speak(KYLAR, "What makes it so special?")
    $ setWait(160.453,166.292)
    $ speak(COACH, "See when the movie first came out it was great. Just a man proud of his heritage kickin' ass!")
    $ setWait(166.292,172.59)
    $ speak(COACH, "But then Hollywood had to come in and put in their BS progressive agenda on the last part of the movie.")
    show coach 2 smile:
        leftmidstage
        xzoom -1

    $ setWait(172.59,178.304)
    $ speak(COACH, "So this is my copy of American History X with the last 30 minutes cut out, who wants to watch!?")

    show jeffery sc3 smile:
        rightcenterstage
        pause 3.3
        linear 2 off_left

    $ setWait(178.304,182.641)
    $ speak(JEFFERY, "Oh I love director's cuts! I'm gonna get us some popcorn, be right back!")
    $ setWait(182.641,183.642)
    $ speak(KYLAR, "This is gonna rule.")
    $ setWait(183.642,187.062)
    $ speak(COACH, "So Nicole, what brought you to the Straight Club anyway?")
    $ setWait(187.062,188.606)
    $ speak(NICOLE, "Some drama don't worry about it.")
    show kylar sc2:
        rightmidstage
        xzoom 1

    $ setWait(188.606,193.36)
    $ speak(KYLAR, "She's just being shy. Some dlke bitch told everyone Nicole was homophobic cause she didn't wanna date her.")
    show coach 2 angry:
        leftmidstage
        xzoom -1

    $ setWait(193.36,196.697)
    $ speak(COACH, "What the fuck is wrong with these gay people??")
    $ setWait(196.697,197.865)
    $ speak(NICOLE, "Not blaming all of them.")
    show coach 2:
        leftmidstage
        xzoom -1
    $ setWait(197.865,202.286)
    $ speak(COACH, "Yeah that's what they always say but these freaks won't stop 'till society's underwater!")
    show kylar sc2 angry:
        rightmidstage

    $ setWait(202.286,204.622)
    $ speak(KYLAR, "We should publicly execute those weirdos!")

    show nicole sc5:
        xzoom 1
        leftcenterstage
        linear 0.5 centerstage

    $ setWait(204.622,206.707)
    $ speak(NICOLE, "Now that's what I expected to hear at a Straight Club.")
    $ setWait(206.707,209.46)
    $ speak(KYLAR, "What's her address, Nicole! Let's show that bitch a lesson!")
    show nicole sc5 sad:
        centerstage

    $ setWait(209.46,210.628)
    $ speak(NICOLE, "Whoa, chill out I don't know it!")

    show kylar sc2 yell:
        rightmidstage

    $ setWait(210.628,215.341)
    $ speak(KYLAR, "Don't hold out on us! Tell me where she lives or I'm gonna chokeslam you into the sugar cube castle!!")
    $ setWait(215.341,217.092)
    $ speak(NICOLE, "I told you I don't know her fucking address!!")
    $ setWait(217.092,220.679)
    $ speak(COACH, "Kylar! Kylar! Calm down! This is way over the top.")
    show kylar sc2 angry:
        rightmidstage
    $ setWait(220.679,223.641)
    $ speak(KYLAR, "I don't get it, Coach, I thought this was the Straight Club.")
    $ setWait(223.641,227.436)
    $ speak(COACH, "I know but you're being messy. Besides I'm a teacher...")
    show coach 2 smile:
        leftmidstage
        xzoom -1
    $ setWait(227.436,229.98)
    $ speak(COACH, "...I'll just look up her file and get the address that way!")
    show kylar sc2 smile:
        rightmidstage

    $ setWait(229.98,231.065)
    $ speak(KYLAR, "Great thinking, Coach!")
    show nicole sc5 surprised:
        centerstage
        xzoom -1

    $ setWait(231.065,232.274)
    $ speak(NICOLE, "Get her address for what??")
    $ setWait(232.274,241.283)
    $ speak(COACH, "Just gonna teach her and her family a little lesson in humility.\nC'mon Straight Club! First the student files, then a drive down 95 where the gas is cheap!")
    show kylar sc2:
        rightmidstage

    $ setWait(241.283,243.285)
    $ speak(KYLAR, "Down 95? Wouldn't that take forever?")
    $ setWait(243.285,246.205)
    $ speak(COACH, "I'm not gonna burn her house down with expensive gas.")
    show kylar sc2 smile:
        rightmidstage

    $ setWait(246.205,247.289)
    $ speak(KYLAR, "Aw hell yeah!")

    show coach 2 smile:
        leftmidstage
        pause 0.9
        xzoom 1
        linear 0.9 off_farleft

    $ setWait(247.289,248.29)
    $ speak(COACH, "Let's go, boys!")

    show nicole sc5 surprised:
        centerstage
        pause 1.2
        xzoom -1

    show kylar sc2 smile:
        rightmidstage
        linear 1.8 off_farleft

    show braxton sc2 smile:
        rightstage
        pause 0.4
        linear 1.8 off_left


    $ setWait(248.29,249.583)
    $ speak(BRAXTON, "Finally reparations!")
    $ setWait(249.583,251.502)
    $ speak(KYLAR, "Hatin' these homos.")
    show nicole sc5:
        xzoom -1
        centerstage

    $ setWait(251.502,254.129)
    $ speak(NICOLE, "I wonder if I'll get blamed for this too.")
    show nicole sc5 angry:
        xzoom -1
        centerstage
        linear 1.5 off_left

    $ setWait(254.129,257.591)
    $ speak(NICOLE, "Who could help me out of this shit?")
    show jeffery sc3:
        xzoom -1
        off_left
        linear 2.6 leftmidstage

    $ setWait(257.591,260.678)
    $ speak(JEFFERY, "What th-- Where'd everybody go??")

    show jeffery sc3 angry:
        leftmidstage


    $ setWait(260.678,263.514)
    $ speak(JEFFERY, "Maybe I should find something other than being straight.")
    stop ambient fadeout 1.25
    jump scene_0080

label scene_0080:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.3 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.1 alpha 0.0


    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show house jecka night with Pause(2.001):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.001 zoom 1.07 truecenter

    $ setVoiceTrack("audio/Scenes/0080.mp3")
    scene porch_jecka
    show nicole sc5 sad:
        xzoom -1
        leftstage

    $ setWait(2.001,5.505)
    $ speak(NICOLE, "Come on come on, tryna not get blamed for a hate crime.")

    show jecka pj angry:
        xzoom -1
        off_left
        linear 1.2 leftstage

    show nicole sc5 sad:
        xzoom -1
        leftstage
        pause 0.8
        linear 0.8 leftmidstage


    $ setWait(5.505,8.257)
    $ speak(JECKA, "I'm watching Drake & Josh, this better be really fucking good.")
    $ setWait(8.257,10.134)
    $ speak(NICOLE, "It's actually really bad!")

    show jecka pj:
        xzoom -1
        pause 0.76
        xzoom 1
        linear 1 xalign -0.25

    $ setWait(10.134,11.511)
    $ speak(JECKA, "Oh, well see ya later.")
    show nicole sc5 angry
    $ setWait(11.511,12.136)
    $ speak(NICOLE, "Dude wait!")
    show jecka pj angry:
        xalign -0.25
        xzoom -1
        linear 0.5 leftstage
    $ setWait(12.136,12.72)
    $ speak(JECKA, "What?")
    show nicole sc5 sad
    $ setWait(12.72,18.685)
    $ speak(NICOLE, "I was invited to the Straight Club and they're on their way to burn Ari's house down right now! We have to stop it!")
    show jecka pj sad
    $ setWait(18.685,23.064)
    $ speak(JECKA, "Okay, slow... way the fuck down. What the hell is a Straight Club??")
    $ setWait(23.064,28.361)
    $ speak(NICOLE, "The gym coach started an underground cult for straight pride, they all think they're victims for being straight!")
    show jecka pj
    $ setWait(28.361,32.031)
    $ speak(JECKA, "Aren't we victims of being straight? Name one good boyfriend either of us had.")
    show nicole sc5 angry
    $ setWait(32.031,33.908)
    $ speak(NICOLE, "No-- It's all men!")
    $ setWait(33.908,35.91)
    $ speak(JECKA, "Oh... How are they victims?")
    show nicole sc5
    $ setWait(35.91,38.746)
    $ speak(NICOLE, "They're jealous of gay pride rallies, that's all I gathered.")
    show jecka pj smile
    $ setWait(38.746,45.169)
    $ speak(JECKA, "They should be, they're fun. It's the only place where you can make out with three different girls and feel proud of your cold sores the next morning.")
    show nicole sc5 angry
    $ setWait(45.169,47.755)
    $ speak(NICOLE, "Cool- so they're on the way to kill Ari right now!")
    show jecka pj
    $ setWait(47.755,49.799)
    $ speak(JECKA, "Oh yeah, why would they burn her house down?")
    $ setWait(49.799,54.929)
    $ speak(NICOLE, "Cause they heard she spread the homophobic rumor about me and now they want revenge or something! They were set off like instantly!")
    $ setWait(54.929,57.306)
    $ speak(JECKA, "And so why's that your problem? I thought you hated her.")
    $ setWait(57.306,63.98)
    $ speak(NICOLE, "Cause it's a hate crime that I'm gonna get blamed for!\nThese guys are insane, they watch American History X with the ending cut out!")
    show jecka pj sad
    $ setWait(63.98,66.566)
    $ speak(JECKA, "But it's about a racist guy, isn't cutting it down good?")
    $ setWait(66.566,68.484)
    $ speak(NICOLE, "The end's where they learn how to not be racist!")
    show jecka pj
    $ setWait(68.484,71.738)
    $ speak(JECKA, "Okay okay I get it! ..Except for one little detail.")
    $ setWait(71.738,72.28)
    $ speak(NICOLE, "What??")
    show jecka pj angry

    $ setWait(72.28,74.907)
    $ speak(JECKA, "Why the fuck did you come here!? Call the police!!")
    show nicole sc5
    $ setWait(74.907,78.119)
    $ speak(NICOLE, "When have the police ever done anything good for us?")
    show jecka pj angry
    $ setWait(78.119,79.245)
    $ speak(JECKA, "...")
    show jecka pj:
        leftstage
        xzoom 1
        linear 1 off_left

    $ setWait(79.245,81.33)
    $ speak(JECKA, "Alright lemme get my shoes.")
    stop ambient fadeout 1
    jump scene_0081
label scene_0081:
    show black onlayer screens with Pause(1.3):
        alpha 0.0
        linear 1.3 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.1 alpha 0.0


    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show house ari night with Pause(2.081):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.081 zoom 1.08 truecenter

    $ setVoiceTrack("audio/Scenes/0081.mp3")

    scene porch_ari

    show nicole sc5 sad:
        xzoom -1
        leftstage

    show jecka pj:
        rightcenterstage

    $ setWait(2.081,3.791)
    $ speak(NICOLE, "Is she already asleep? Ari!?")
    $ setWait(3.791,4.709)
    $ speak(JECKA, "Ari!")
    show nicole sc5 angry:
        xzoom 1

    $ setWait(4.709,7.753)
    $ speak(NICOLE, "Why can't it be like the movies where they're just conveniently ten feet from the door?")
    show jecka pj sad
    $ setWait(7.753,10.131)
    $ speak(JECKA, "It better be like the movies soon, when are they getting here?")
    show nicole sc5
    $ setWait(10.131,13.759)
    $ speak(NICOLE, "I think they went down to Woodbridge where the gas is cheap so we maybe have a few minutes.")
    $ setWait(13.759,16.846)
    $ speak(JECKA, "The price is cheaper but don't you burn that driving down there?")
    show nicole sc5 angry
    $ setWait(16.846,17.972)
    $ speak(NICOLE, "It's not for their car.")
    show jecka pj
    $ setWait(17.972,19.973)
    $ speak(JECKA, "Oh yeah to burn the house down.")

    show ari pj angry:
        xzoom -1
        off_left
        linear 1.4 leftstage

    show nicole sc5 surprised:
        leftstage
        pause 0.45
        xzoom -1
        linear 0.6 leftcenterstage

    $ setWait(19.973,22.143)
    $ speak(ARI, "Drake and Josh is on, this better be good.")

    $ setWait(22.143,23.144)
    $ speak(NICOLE, "What the fuck, still?")
    $ setWait(23.144,23.811)
    $ speak(JECKA, "Marathon.")
    $ setWait(23.811,25.313)
    $ speak(ARI, "What do you want? It's almost ten.")
    show nicole sc5 sad
    $ setWait(25.313,26.23)
    $ speak(NICOLE, "Is your family home?")
    $ setWait(26.23,28.441)
    $ speak(ARI, "No they're out of town-- what the fuck do you want?")
    show nicole sc5 angry
    $ setWait(28.441,31.485)
    $ speak(NICOLE, "You gotta get out of here someone's on the way to burn your house down!")
    show ari pj sad
    $ setWait(31.485,33.654)
    $ speak(ARI, "What? Who would set my house on fire??")
    $ setWait(33.654,39.827)
    $ speak(NICOLE, "Coach Colby's Straight Club! They're mad at the general idea of homosexuality and wanna kill you for being gay!")
    show jecka pj sad
    $ setWait(39.827,41.12)
    $ speak(JECKA, "Yeah so pretty serious.")
    show ari pj angry
    $ setWait(41.12,46.083)
    $ speak(ARI, "That sounds so made up it's not even funny. You already rejected me, now you wanna prank me?")
    $ setWait(46.083,48.127)
    $ speak(JECKA, "She's not making it up, they're on the way.")
    $ setWait(48.127,52.715)
    $ speak(ARI, "Why the hell would Nicole go out of her way to help anyone but herself? It doesn't make any sense.")
    show nicole sc5 surprised

    $ setWait(52.715,56.427)
    $ speak(NICOLE, "Because if you die the school would indict me as the cause of the hate crime!")
    show nicole sc5
    $ setWait(56.427,57.97)
    $ speak(JECKA, "You really gotta get out of here.")
    show ari pj sad
    $ setWait(57.97,59.722)
    $ speak(ARI, "Why wouldn't I just call the police?")
    show nicole sc5 angry
    $ setWait(59.722,62.099)
    $ speak(NICOLE, "So they can show up ten minutes after you're dead?")
    show ari pj angry
    $ setWait(62.099,63.351)
    $ speak(ARI, "Okay where's the camera?")
    show nicole sc5 yell
    $ setWait(63.351,68.898)
    $ speak(NICOLE, "There's no fucking camera! No MTV, no Ashton Kutcher, no.. the guy from Drumline, c'mon!")
    show nicole sc5 angry
    $ setWait(68.898,70.983)
    $ speak(JECKA, "What do we have to do to prove we're not making this up?")

    show ari pj sad

    $ setWait(70.983,71.942)
    $ speak(ARI, "How should I know??")
    $ setWait(71.942,75.279)
    $ speak(JECKA, "I don't know just anything she wouldn't do to pull off a prank?")
    show ari pj
    $ setWait(75.279,77.782)
    $ speak(ARI, "Uh... Fine.")
    show jecka pj
    show ari pj angry
    $ setWait(77.782,78.741)
    $ speak(ARI, "Kiss me.")



    show jecka pj smile:
        rightcenterstage
        linear 1 leftmidstage

    show nicole sc5:
        xzoom -1


    $ setWait(78.741,79.325)
    $ speak(JECKA, "Oh easy.")
    $ setWait(79.325,83.204)
    $ speak(ARI, "Not you, Herpes Fully Loaded.\nI mean Nicole has to kiss me.")
    show nicole sc5 surprised
    show jecka pj

    $ setWait(83.204,84.038)
    $ speak(NICOLE, "Why me??")
    $ setWait(84.038,85.331)
    $ speak(JECKA, "I thought you were mad at her.")
    $ setWait(85.331,87.375)
    $ speak(ARI, "Oh I am. I hate her.")
    show nicole sc5
    $ setWait(87.375,95.716)
    $ speak(ARI, "Nicole you're a cold, corrupt, selfish, psychopathic bitch. Literally the most sadist fucking whore-- I wouldn't be surprised if you like killing animals.")
    $ setWait(95.716,96.509)
    $ speak(NICOLE, "Haven't tried.")
    $ setWait(96.509,104.141)
    $ speak(ARI, "You don't even get mad at the assumption of that. You're severely twisted, evil, manipulative, and in general just a heartless bitch...")
    show ari pj blush
    $ setWait(104.141,108.646)
    $ speak(ARI, "Doesn't mean I don't want you every waking moment of my sad fucking life.")
    show nicole sc5 surprised
    show jecka pj surprised
    $ setWait(108.646,109.563)
    $ speak(NICOLE, "Excuse me?")
    $ setWait(109.563,112.525)
    $ speak(ARI, "You show every sign of an abuser and I don't give a shit.")
    $ setWait(112.525,118.406)
    $ speak(ARI, "You're the kinda girl who'd choke me goodnight, the kinda girl who'd walk in on me cutting and take the razor blade and do it for me.")
    $ setWait(118.406,125.538)
    $ speak(ARI, "I don't want a girlfriend to marry, I want a girlfriend who helps me plan my own suicide.\nYou're that girl Nicole, and I need you bad.")
    $ setWait(125.538,127.456)
    $ speak(NICOLE, "Bitch you need therapy.")
    show jecka pj sad:
        xzoom -1

    $ setWait(127.456,130.084)
    $ speak(JECKA, "Okay but she confessed her love for you, are you gonna kiss her now?")
    show nicole sc5 angry
    show ari pj angry

    $ setWait(130.084,131.502)
    $ speak(NICOLE, "No way! Fuck this bitch.")
    show jecka pj angry
    $ setWait(131.502,132.086)
    $ speak(JECKA, "Why??")
    $ setWait(132.086,134.672)
    $ speak(NICOLE, "She stole my excuse, I don't kiss depression posers.")
    show jecka pj sad
    $ setWait(134.672,137.8)
    $ speak(JECKA, "You are so petty-- how else is she gonna believe this isn't a prank??")
    $ setWait(137.8,139.009)
    $ speak(ARI, "My demand's final.")
    show jecka pj sad:
        xzoom 1

    $ setWait(139.009,140.886)
    $ speak(NICOLE, "We're here to save you right now!")
    $ setWait(140.886,147.101)
    $ speak(ARI, "Shame that you hate being a homophobe more than I hate dying. Even if you're telling the truth I don't care, you know what I want.")
    show jecka pj angry:
        xzoom -1
    $ setWait(147.101,150.813)
    $ speak(JECKA, "Nicole we lost 5 minutes doing this and she hasn't moved one inch from her house.")
    show nicole sc5 sad
    $ setWait(150.813,154.733)
    $ speak(NICOLE, "Uh... What if we took you to the Super8 and I kiss you in the lobby?")
    show ari pj sad
    show jecka pj:
        xzoom 1

    $ setWait(154.733,157.403)
    $ speak(ARI, "The lobby? What am I worthless?")
    $ setWait(157.403,159.363)
    $ speak(NICOLE, "Do you wanna hear \"yes\"?")
    show ari pj:
        xzoom 1
        leftstage
        linear 1 xalign -0.24

    $ setWait(159.363,160.281)
    $ speak(ARI, "I'll get my shoes.")
    show nicole sc5 angry:
        xzoom 1
        leftcenterstage
        linear 0.9 off_right

    show jecka pj sad:
        leftmidstage
        pause 0.3
        xzoom -1
        linear 1 off_right

    show ari pj sad:
        xalign -0.24
        xzoom 1
        pause 0.37
        xzoom -1
        pause 0.42
        linear 1.3 off_right


    $ setWait(160.281,161.991)
    $ speak(NICOLE, "No time, get in the car!")
    stop ambient fadeout 1.5

    jump end_0082

label end_0082:
    show black onlayer screens with Pause(1.7):
        alpha 0.0
        linear 1.5 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.3 alpha 0.0


    if "end_0082" not in persistent.endings:
        $ persistent.endings.append("end_0082")
        $ persistent.new_ending = True

    scene onlayer master
    show black
    $ quick_menu = False
    $ csbox = True
    $ renpy.movie_cutscene("cs0082.webm")

    return

label scene_0083:
    $ setVoiceTrack("audio/Scenes/0083.mp3")
    scene classroom int 3
    show nicole sc3:
        leftmidstage

    show kelly sc1:
        xzoom -1
        leftcenterstage

    show katz 1:
        rightcenterstage

    show hunter sc1:
        rightstage
    $ setWait(0.004,3.549)
    $ speak(NICOLE, "It's uh... it's like a nonprofit.")
    $ setWait(3.549,5.009)
    $ speak(KATZ, "A nonprofit what?")
    $ setWait(5.009,6.76)
    $ speak(NICOLE, "A nonprofit charity.")
    $ setWait(6.76,9.722)
    $ speak(KATZ, "A nonprofit charity for what?")
    $ setWait(9.722,12.016)
    $ speak(NICOLE, "A cause. You wanted it for a cause, right?")
    show katz 1 angry:
        rightcenterstage
    $ setWait(12.016,13.726)
    $ speak(KATZ, "What is the cause??")
    $ setWait(13.726,16.186)
    $ speak(NICOLE, "A healthy cause. So people are healthy.")
    $ setWait(16.186,18.23)
    $ speak(KATZ, "And how do they make them healthy?")
    $ setWait(18.23,19.315)
    $ speak(NICOLE, "Medicine.")
    show katz 1 angry:
        rightcenterstage
    $ setWait(19.315,24.445)
    $ speak(KATZ, "So pharmaceuticals. What's the name of this pharmaceutical nonprofit?")
    $ setWait(24.445,26.28)
    $ speak(NICOLE, "Ooh, gotta get back to you on that one.")
    $ setWait(26.28,29.241)
    $ speak(KATZ, "You signed up for a charity and don't even know the name of it?")
    $ setWait(29.241,36.707)
    $ speak(NICOLE, "It was kinda long I don't have it in front of me. But it was definitely a charity and definitely for medication to the... underprivileged.")
    show kelly sc1:
        leftcenterstage
        xzoom 1

    $ setWait(36.707,37.416)
    $ speak(KELLY, "Where is it?")
    $ setWait(37.416,38.459)
    $ speak(NICOLE, "Bitch no one asked you.")
    show kelly sc1 angry:
        leftcenterstage

    $ setWait(38.459,39.418)
    $ speak(KELLY, "I was asking.")
    show kelly sc1:
        leftcenterstage
        pause 0.7
        xzoom -1

    $ setWait(39.418,46.216)
    $ speak(KATZ, "You're aware you'll need to fill out a form with the location of this charity, right? Just so we know it's not made up.")
    $ setWait(46.216,48.677)
    $ speak(NICOLE, "Yeah totally I'll get all that for ya next class.")
    show katz 1 angry:
        rightcenterstage

    $ setWait(48.677,50.262)
    $ speak(KATZ, "It was due today.")
    $ setWait(50.262,54.642)
    $ speak(NICOLE, "Well I don't know what to tell you. Is the charity gonna disappear cause I didn't get it in on time?")
    show katz 1 angry:
        rightcenterstage

    $ setWait(54.642,61.482)
    $ speak(KATZ, "If you're fine with your grade taking a 10 percent hit then be my guest. My policy on all late work.")
    $ setWait(61.482,63.233)
    $ speak(NICOLE, "Dude you need to stop watching C-Span.")
    $ setWait(63.233,65.069)
    $ speak(KATZ, "How did you know I watch at lunch?")
    $ setWait(65.069,66.779)
    $ speak(NICOLE, "You just seem like a rules fan.")
    $ setWait(66.779,69.865)
    $ speak(KATZ, "I hope everyone here is a rules fan, this is civics!")
    $ setWait(69.865,73.369)
    $ speak(NICOLE, "If rules did anything wouldn't rape and murder stop happening?")
    $ setWait(73.369,74.787)
    $ speak(KATZ, "It stops most of it.")
    $ setWait(74.787,78.248)
    $ speak(NICOLE, "Okay let's tell all the rape and murder victims that, I'm sure it'll make 'em feel better.")
    $ setWait(78.248,82.127)
    $ speak(KATZ, "Get your charity in next class and hope I don't fail you for the year!")
    $ setWait(82.127,85.264)
    $ speak(NICOLE, "God failed you for your entire life.")
    stop ambient fadeout 1
    jump scene_0084
label scene_0084:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0084.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    scene cafeteria int 2
    show nicole sc3:
        leftcenterstage

    show emily sc2 angry:
        rightcenterstage

    $ setWait(0.045,5.675)
    $ speak(EMILY, "So then my mom's like \"he's too old to date you\" and I just ask \"are you gonna buy me alcohol at 1 in the morning?\"")
    $ setWait(5.675,6.635)
    $ speak(NICOLE, "Exactly.")
    $ setWait(6.635,10.972)
    $ speak(EMILY, "Like I thought you were supposed to look out for me, Mom. If you don't give me what I want I'll find someone who will.")
    $ setWait(10.972,15.06)
    $ speak(NICOLE, "Dude totally, we turn fifteen and they're entirely clueless to our needs.")
    $ setWait(15.06,20.94)
    $ speak(EMILY, "And getting locked in this bitch eight hours a day means I need the edge off. Is everyone's mom a bitch or is it just us?")
    $ setWait(20.94,24.152)
    $ speak(NICOLE, "Uh... Jecka hates her mom so I guess everyone?")
    show emily sc2:
        rightcenterstage

    $ setWait(24.152,25.612)
    $ speak(EMILY, "Where is Jecka?")
    $ setWait(25.612,28.114)
    $ speak(NICOLE, "Probably doing something dumb as shit like school.")
    show kylar sc2 smile:
        off_right
        linear 2 rightmidstage
    $ setWait(28.114,30.158)
    $ speak(KYLAR, "Hey guy what's good?")
    show emily sc2 upset:
        rightcenterstage
        xzoom -1
    $ setWait(30.158,31.117)
    $ speak(EMILY, "Hi?")
    $ setWait(31.117,32.535)
    $ speak(NICOLE, "Why do you always come up to us at lunch?")

    show kylar sc2:
        rightmidstage

    $ setWait(32.535,34.496)
    $ speak(KYLAR, "Will you shut the fuck up and let me talk?")
    $ setWait(34.496,35.121)
    $ speak(EMILY, "Bye then.")
    $ setWait(35.121,39.876)
    $ speak(KYLAR, "No no alright-- I just wanted to know if you knew people setting up the county's worship festival next weekend.")
    $ setWait(39.876,42.921)
    $ speak(EMILY, "County's worship festival? Is that like Jesus and shit?")
    $ setWait(42.921,45.09)
    $ speak(NICOLE, "Do we look like the type of girls who would go to church?")
    $ setWait(45.09,48.176)
    $ speak(KYLAR, "No it's not like super religious it's just like a county fair.")
    show emily sc2:
        rightcenterstage
        xzoom -1

    $ setWait(48.176,49.26)
    $ speak(EMILY, "So what do you wanna know?")
    $ setWait(49.26,55.85)
    $ speak(KYLAR, "Okay there's this really hot girl on the organizing committee and I need to get on it. So if you know any religious people just 'tell 'em I wanna join.")
    $ setWait(55.85,58.895)
    $ speak(NICOLE, "Do we look like the type of girls who know girls who go to church?")
    $ setWait(58.895,59.813)
    $ speak(EMILY, "Who's the girl?")
    $ setWait(59.813,62.232)
    $ speak(KYLAR, "I can't tell you that you might try to ruin it.")
    $ setWait(62.232,65.151)
    $ speak(EMILY, "All of this sounds like an excuse to come up and talk to us.")
    show nicole sc3 smile:
        leftcenterstage

    $ setWait(65.151,66.194)
    $ speak(NICOLE, "Yeah are you lonely?")

    show kylar sc2 angry:
        rightmidstage
        pause 0.75
        xzoom -1
        linear 1.77 off_right

    $ setWait(66.194,69.28)
    $ speak(KYLAR, "What? No-- Alright whores fuck you then.")
    show emily sc2 smile:
        rightcenterstage
        xzoom 1
    $ setWait(69.28,70.573)
    $ speak(EMILY, "I think he was lonely.")
    show nicole sc3:
        leftcenterstage

    $ setWait(70.573,73.159)
    $ speak(NICOLE, "Like we would even know people who set up church functions.")
    show emily sc2:
        rightcenterstage

    $ setWait(73.159,75.87)
    $ speak(EMILY, "I barely know people at this school in general anymore.")
    $ setWait(75.87,77.08)
    $ speak(NICOLE, "Did your friends transfer?")
    $ setWait(77.08,80.834)
    $ speak(EMILY, "No I always hook up with my friends' boyfriends so they don't wanna talk anymore.")
    $ setWait(80.834,82.21)
    $ speak(NICOLE, "Oh that's why we get along.")
    show emily sc2 smile:
        rightcenterstage

    $ setWait(82.21,83.712)
    $ speak(EMILY, "You have a cheating thing too?")
    $ setWait(83.712,89.384)
    $ speak(NICOLE, "Uh... no, I've just never liked a guy enough to the point of calling him my boyfriend.\nBut good to know you're into that.")
    $ setWait(89.384,91.803)
    $ speak(EMILY, "I'm like a charity for guys sick of their girlfriends.")
    show nicole sc3 angry:
        leftcenterstage

    $ setWait(91.803,94.097)
    $ speak(NICOLE, "Charity-- Fuck I still have to do that!")
    show emily sc2:
        rightcenterstage

    $ setWait(94.097,94.806)
    $ speak(EMILY, "Do what?")
    show nicole sc3:
        leftcenterstage

    $ setWait(94.806,102.063)
    $ speak(NICOLE, "I made up a fake pharmaceutical charity for civics and now I gotta either find a real one or just make up better lies for the fake one.")
    $ setWait(102.063,104.149)
    $ speak(EMILY, "Both sound like a lot of effort.")
    $ setWait(104.149,105.066)
    $ speak(NICOLE, "No kidding.")
    $ setWait(105.066,107.819)
    $ speak(EMILY, "Or you could start your own charity, then you're not lying.")
    $ setWait(107.819,110.363)
    $ speak(NICOLE, "That sounds like more work than both options put together.")
    show emily sc2 angry:
        rightcenterstage

    $ setWait(110.363,116.87)
    $ speak(EMILY, "Fuck no, you think people actually work at those charity things?\nThey just vacay in Florida and write it off as a conference.")
    $ setWait(116.87,117.704)
    $ speak(NICOLE, "How would you know?")
    show emily sc2:
        rightcenterstage

    $ setWait(117.704,121.875)
    $ speak(EMILY, "My fucking piece of shit dad who I wanna kill works for a charity business.")
    $ setWait(121.875,125.295)
    $ speak(NICOLE, "Is there-- okay we won't explore that one. No but that's actually a good idea.")
    $ setWait(125.295,130.175)
    $ speak(EMILY, "Yeah, oh and did you hear about Braxton? He tried selling a brick in school.")
    show nicole sc3 surprised:
        leftcenterstage

    $ setWait(130.175,132.385)
    $ speak(NICOLE, "No I had no idea-- to who?")
    show nicole sc3:
        leftcenterstage

    $ setWait(132.385,135.93)
    $ speak(EMILY, "Probably a teacher with a coke problem cause I don't know any kid who could afford that.")
    $ setWait(135.93,136.723)
    $ speak(NICOLE, "Where would he even--")
    show coach 1 smile:
        off_right
        linear 2 rightmidstage

    $ setWait(136.723,140.143)
    $ speak(COACH, "Hey! If it isn't my favorite gym students.")
    show emily sc2 upset:
        rightcenterstage
        xzoom -1
    $ setWait(140.143,143.396)
    $ speak(EMILY, "We never dressed out when we did it, how are we your favorite students?")
    $ setWait(143.396,148.109)
    $ speak(COACH, "Aw I know what you're doing, you wanna stay lookin' nice for your favorite gym teacher.")
    $ setWait(148.109,149.611)
    $ speak(NICOLE, "Why would we care about that?")
    $ setWait(149.611,154.199)
    $ speak(COACH, "I hear how you girls talk about older men and quite frankly I support it.")
    $ setWait(154.199,155.867)
    $ speak(NICOLE, "You wanna say that in front of the principal?")
    $ setWait(155.867,158.328)
    $ speak(EMILY, "Yeah and it's older men, not ancient men.")
    show coach 1 smile:
        xzoom -1
        rightmidstage
        linear 3.2 off_farright

    $ setWait(158.328,165.46)
    $ speak(COACH, "Yeah we'll see about that when you're looking for an expensive good time.")
    show emily sc2:
        xzoom 1
        rightcenterstage

    $ setWait(165.46,167.921)
    $ speak(EMILY, "How many times this month has he tried asking us out?")
    $ setWait(167.921,171.09)
    $ speak(NICOLE, "Three, but yeah where would Braxton even get a brick of coke?")
    $ setWait(171.09,174.01)
    $ speak(EMILY, "I think his friend's cousin's in MS-13.")

    show nicole sc3 surprised:
        leftcenterstage

    $ setWait(174.01,174.928)
    $ speak(NICOLE, "Oh shit.")
    $ setWait(174.928,175.72)
    $ speak(EMILY, "What's wrong?")

    show nicole sc3:
        leftcenterstage

    $ setWait(175.72,179.808)
    $ speak(NICOLE, "Nothing, it's probably no big deal. Everyone's a little drive from PG County.")
    $ setWait(179.808,180.975)
    $ speak(EMILY, "You going to class?")

    show nicole sc3:
        leftcenterstage
        pause 1.5
        xzoom -1
        linear 2.1 off_left

    $ setWait(180.975,184.929)
    $ speak(NICOLE, "Nah I'm going home. It's 11:30, been here long enough.")
    stop ambient fadeout 1
    jump scene_0085
label scene_0085:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.086):
        zoom 0.5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.086 zoom 0.55 truecenter
    $ setVoiceTrack("audio/Scenes/0085.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene bedroom nicole
    show nicole sc6 angry:
        rightcenterstage
    $ setWait(2.086,7.925)
    $ speak(NICOLE, "Okay so I need a charity, a way to ditch this fatass brick, and money in general. Let's see.")
    show nicole sc6 angry:
        rightcenterstage
        xzoom -1
    $ setWait(7.925,13.139)
    $ speak(NICOLE, "I can't just sell the coke cause then they'll go looking for me. Can never kill two birds with one stone.")
    show nicole sc6 smile:
        rightcenterstage
        xzoom -1
    $ setWait(13.139,15.474)
    $ speak(NICOLE, "God this shit feels so good on my gums too.")
    show nicole sc6:
        rightcenterstage
        xzoom -1
        linear 1 centerstage

    $ setWait(15.474,18.686)
    $ speak(NICOLE, "I'd try it for real but I don't know if it'd mix well with my Mom's vicodin.")
    $ setWait(18.686,21.772)
    $ speak(NICOLE, "How is this a prescription med? It feels as good as the street drug...")
    show nicole sc6 surprised:
        centerstage
        xzoom -1
    $ setWait(21.772,22.398)
    $ speak(NICOLE, "I got it!")
    show nicole sc6 surprised:
        centerstage
        xzoom -1
        linear 1.4 off_left

    $ setWait(22.398,24.525)
    $ speak(NICOLE, "Where's my laptop, how would I word this?")

    show nicole sc6:
        xzoom 1
        off_left
        linear 4 centerstage
    $ setWait(24.525,29.739)
    $ speak(NICOLE, "\"How to freebase\"")
    stop ambient fadeout 5
    call screen search_engine_screen
    jump scene_0086
label scene_0086:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0086.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3
    show lynn 1:
        rightcenterstage

    show hunter sc2:
        rightstage

    show kelly sc2:
        leftcenterstage
        xzoom -1

    show nicole sc4:
        leftmidstage

    $ setWait(0.039,5.878)
    $ speak(LYNN, "Now I'm told if you didn't get your community service causes in last time, you better have them today.")
    $ setWait(5.878,7.422)
    $ speak(HUNTER, "Aw FUCK!")
    show lynn 1:
        rightcenterstage
        xzoom -1

    $ setWait(7.422,9.132)
    $ speak(LYNN, "Excuse me!")
    $ setWait(9.132,11.426)
    $ speak(KELLY, "Hey uh where's Mr. Katz?")
    show lynn 1:
        rightcenterstage
        xzoom 1

    $ setWait(11.426,16.681)
    $ speak(LYNN, "Today I'm filling in for Mr. Katz as he had a medical issue he needed to take care of.")
    show nicole sc4 angry:
        leftmidstage

    $ setWait(16.681,20.059)
    $ speak(NICOLE, "So I had another two days to think of a charity? God dammit.")
    $ setWait(20.059,25.565)
    $ speak(LYNN, "You think because I'm subbing today I won't enforce your teacher's deadlines? Don't forget I'm your principal.")
    show nicole sc4:
        leftmidstage

    $ setWait(25.565,26.19)
    $ speak(NICOLE, "Oh my.")
    $ setWait(26.19,36.868)
    $ speak(LYNN, "And speaking of deadlines, Mr. Katz took extra care to remind me of your assignment in particular, Nicole. It's your last day to submit or you fail this class for the year, so what do you have for me?")
    $ setWait(36.868,39.203)
    $ speak(NICOLE, "Uh I have my charity.")
    $ setWait(39.203,46.335)
    $ speak(LYNN, "What charity might that be? I was told it had to do with pharmaceuticals so let's not stray too far from any prior narrative.")
    $ setWait(46.335,50.757)
    $ speak(NICOLE, "Yeah whatever, the name of my charity is Medicine Rocks.")
    $ setWait(50.757,52.467)
    $ speak(LYNN, "Medicine Rocks?")
    $ setWait(52.467,57.93)
    $ speak(NICOLE, "Yeah it's a charity that helps get prescription drugs to the underprivileged in PG County.")
    $ setWait(57.93,60.6)
    $ speak(LYNN, "Why haven't I heard of this charity?")
    $ setWait(60.6,62.101)
    $ speak(NICOLE, "I don't know, PG County's far.")
    $ setWait(62.101,63.394)
    $ speak(LYNN, "Not that far.")
    $ setWait(63.394,69.15)
    $ speak(NICOLE, "Well they're really underfunded so they can't get the word out. Wanted to volunteer for something that could actually use some help.")
    show kelly sc2 angry:
        leftcenterstage
        xzoom 1
    $ setWait(69.15,70.568)
    $ speak(KELLY, "What's that supposed to mean?")
    show nicole sc4 angry:
        leftmidstage

    $ setWait(70.568,71.903)
    $ speak(NICOLE, "Bitch you know what the fuck it means.")
    show kelly sc2:
        leftcenterstage
        xzoom -1
    $ setWait(71.903,77.366)
    $ speak(LYNN, "Girls, girls! --I'll have to look them up sometime then.\nThey'd have a website, wouldn't they?")
    show nicole sc4:
        leftmidstage

    $ setWait(77.366,85.792)
    $ speak(NICOLE, "No they don't really have anything on the internet cause they're underfunded and underprivileged. Not everyone has the technology us well-funded whites do, Miss Lynn.")
    $ setWait(85.792,87.043)
    $ speak(LYNN, "What do you mean by that?")
    $ setWait(87.043,89.17)
    $ speak(NICOLE, "If you Google them you're racist.")
    $ setWait(89.17,90.171)
    $ speak(HUNTER, "She got ya there.")
    show lynn 1:
        rightcenterstage
        xzoom -1
    $ setWait(90.171,91.172)
    $ speak(LYNN, "Hush!")
    show lynn 1:
        rightcenterstage
        xzoom 1
    $ setWait(91.172,99.639)
    $ speak(LYNN, "Well I have to say I'm pleasantly surprised with you, Nicole. Here's your hours sheet, you'll need 25 hours in the next six weeks, with signatures.")
    $ setWait(99.639,100.515)
    $ speak(NICOLE, "Yeah okay.")
    $ setWait(100.515,104.477)
    $ speak(LYNN, "We operate under the honor system, but don't think I won't keep my eye on you.")
    $ setWait(104.477,105.311)
    $ speak(NICOLE, "Oh I'm wet.")
    $ setWait(105.311,105.895)
    $ speak(LYNN, "What was that?")
    $ setWait(105.895,108.523)
    $ speak(NICOLE, "Nothing, hey let's see you fail one of these other losers.")
    show lynn 1:
        xzoom -1
        rightcenterstage
        linear 3 rightmidstage

    $ setWait(108.523,110.358)
    $ speak(LYNN, "Anyone else have a charity for me?")
    stop ambient fadeout 1
    jump scene_0087
label scene_0087:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0087.mp3")
    play ambient "audio/Ambience/Bathroom_Lockerroom_Ambience.mp3" fadein 1
    scene locker room
    show jecka changing:
        leftcenterstage
        xzoom -1

    show nicole sc4:
        xzoom -1
        off_right
        linear 1.2 rightcenterstage

    $ setWait(0.035,3.538)
    $ speak(NICOLE, "Dude I've been looking everywhere for you, since when do you take elective gym?")
    $ setWait(3.538,6.625)
    $ speak(JECKA, "It's the easiest class ever, you just be skinny and get an A.")
    $ setWait(6.625,8.585)
    $ speak(NICOLE, "And get sexually harassed by the gym coach.")
    $ setWait(8.585,13.298)
    $ speak(JECKA, "No he doesn't do that for the seniors, he thinks we're old enough to tell our parents or something.")
    show nicole sc4 sad:
        rightcenterstage
        xzoom -1
    $ setWait(13.298,15.092)
    $ speak(NICOLE, "Ew I wouldn't tell my parents at any age.")
    show jecka changing sad:
        leftcenterstage
        xzoom -1
    $ setWait(15.092,16.802)
    $ speak(JECKA, "Yeah that's like way too embarrassing.")
    $ setWait(16.802,20.597)
    $ speak(NICOLE, "Imagine telling your mom a 50 year old man wants to each a Lunchable outta your cleavage.")
    $ setWait(20.597,26.061)
    $ speak(JECKA, "Exactly, parents and sex are two entirely different worlds... Unless you're in Arkansas.")
    show nicole sc4:
        rightcenterstage
        xzoom -1
    $ setWait(26.061,28.855)
    $ speak(NICOLE, "The only way I'd tell is for a pity dinner at Red Lobster.")
    show jecka changing:
        leftcenterstage
        xzoom -1
    $ setWait(28.855,30.482)
    $ speak(JECKA, "High bar-- so what do you want?")
    $ setWait(30.482,32.484)
    $ speak(NICOLE, "Oh yeah, I have a project I need help with.")
    show jecka changing angry:
        leftcenterstage
        xzoom -1

    $ setWait(32.484,35.404)
    $ speak(JECKA, "Nicole that MySpace girl isn't even fun to bully anymore.")
    $ setWait(35.404,37.28)
    $ speak(NICOLE, "No not that, another project.")
    show jecka changing:
        leftcenterstage
        xzoom -1

    $ setWait(37.28,38.365)
    $ speak(JECKA, "Project for what?")
    $ setWait(38.365,39.074)
    $ speak(NICOLE, "For school.")
    $ setWait(39.074,41.368)
    $ speak(JECKA, "Since when the fuck do you do any project for school?")
    $ setWait(41.368,46.331)
    $ speak(NICOLE, "Since I got a really awesome idea for it but I need you to bring some stuff over to my house.")
    $ setWait(46.331,47.624)
    $ speak(JECKA, "Okay what is it?")
    $ setWait(47.624,52.462)
    $ speak(NICOLE, "I need baking soda, a zippo lighter, some really tiny ziplocks, and one of your parent's serving spoons.")
    $ setWait(52.462,53.755)
    $ speak(JECKA, "Are you in chemistry now?")
    $ setWait(53.755,54.673)
    $ speak(NICOLE, "No, civics.")
    show jecka changing angry:
        leftcenterstage
        xzoom -1

    $ setWait(54.673,57.217)
    $ speak(JECKA, "Where the hell am I gonna get really tiny ziplocks?")
    $ setWait(57.217,59.636)
    $ speak(NICOLE, "Isn't your mom into jewelry? She would have those lying around.")
    show jecka changing:
        leftcenterstage
        xzoom -1

    $ setWait(59.636,62.597)
    $ speak(JECKA, "Okay so ziplocks, serving spoon, lighter-- what else?")
    $ setWait(62.597,64.266)
    $ speak(NICOLE, "Baking soda, a whole box of it.")
    $ setWait(64.266,66.893)
    $ speak(JECKA, "Baking soda. Okay I'll see ya after school.")
    show nicole sc4:
        rightcenterstage
        xzoom -1
        pause 0.4
        xzoom 1
        linear 1.6 off_right

    $ setWait(66.893,69.312)
    $ speak(NICOLE, "Thanks, I'll explain later.")
    show jecka changing angry:
        leftcenterstage
        xzoom -1

    $ setWait(69.312,72.899)
    $ speak(JECKA, "How long is it gonna take to find this shit?")
    show coach 1 smile:
        xzoom -1
        off_left
        linear 2 leftmidstage
    $ setWait(72.899,75.235)
    $ speak(COACH, "Hey sweet cheeks, you got a minute?")

    show jecka changing angry:
        xzoom 1
        leftcenterstage
        linear 0.28 centerstage

    $ setWait(75.235,77.487)
    $ speak(JECKA, "Miss Lynn said you're not allowed in the girl's locker room.")

    $ setWait(77.487,80.157)
    $ speak(COACH, "She don't need to know-- hey quick question for ya.")
    $ setWait(80.157,81.116)
    $ speak(JECKA, "What??")
    $ setWait(81.116,83.493)
    $ speak(COACH, "Are you familiar with...")
    $ setWait(83.493,86.038)
    $ speak(COACH, "Lunchables Chicken Shake-Ups?")
    stop ambient fadeout 1
    jump scene_0088
label scene_0088:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.372):
        zoom .5 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.372 zoom .56 truecenter
    $ setVoiceTrack("audio/Scenes/0088.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"

    $ quick_menu = True

    scene home nicole int
    show nicole sc4:
        rightstage
        linear 2 leftcenterstage

    show jecka sc4:
        off_right
        pause 1.7
        linear 1.2 rightmidstage

    $ setWait(2.372,5.042)
    $ speak(NICOLE, "Thanks for coming, I know it was super short notice.")
    $ setWait(5.042,7.336)
    $ speak(JECKA, "Yeah so what do you need all this shit for?")
    show nicole sc4 sad:
        leftcenterstage
        xzoom -1
        linear 1.6 off_left

    $ setWait(7.336,8.962)
    $ speak(NICOLE, "Okay don't freak out.")
    $ csbox = True
    show cut0088
    $ setWait(8.962,10.672)
    $ speak(JECKA, "You found it??")
    $ setWait(10.672,11.757)
    $ speak(NICOLE, "Was this yours or something?")
    $ setWait(11.757,16.094)
    $ speak(JECKA, "No-- there's a rumor going around that some gang kid lost a huge thing of coke at our school.")
    $ setWait(16.094,19.598)
    $ speak(NICOLE, "That Braxton kid just ditched it in front of me while running from school security.")
    $ setWait(19.598,23.268)
    $ speak(JECKA, "And you didn't think \"oh that's a lot of illegal drugs maybe more trouble than they're worth\".")
    $ setWait(23.268,24.895)
    $ speak(NICOLE, "Since when are we afraid of the law?")
    hide cut0088
    $ csbox = False
    show jecka sc4 angry:
        rightmidstage
        linear 1 rightcenterstage

    show nicole sc4:
        leftcenterstage
        xzoom 1

    $ setWait(24.895,30.984)
    $ speak(JECKA, "I'm not talking about the law, I'm talking about MS-13's name on the side of the fucking bag! They're gonna kill you if they find out.")
    $ setWait(30.984,32.778)
    $ speak(NICOLE, "How do you know who MS-13 is?")
    show jecka sc4:
        rightcenterstage

    $ setWait(32.778,35.113)
    $ speak(JECKA, "One of my friend's cousins was in MS-13.")
    show nicole sc4 angry:
        leftcenterstage

    $ setWait(35.113,41.286)
    $ speak(NICOLE, "I guess everyone's friend's cousin's in MS-13 now-- and no way it's MS-13, why would a gang put their name on their drugs?")
    show jecka sc4:
        rightcenterstage

    $ setWait(41.286,43.038)
    $ speak(JECKA, "What if it was supposed to be delivered to them?")
    $ setWait(43.038,46.291)
    $ speak(NICOLE, "What shitty ass drug dealer would keep their customer's names in writing?")
    show jecka sc4 angry:
        rightcenterstage

    $ setWait(46.291,50.379)
    $ speak(JECKA, "A really fucking stupid one, as in stupid enough to bring this to a public school??")

    show nicole sc4:
        leftcenterstage

    $ setWait(50.379,53.131)
    $ speak(NICOLE, "Alright don't worry about it, they won't even know we had it when we're finished.")
    $ setWait(53.131,54.591)
    show jecka sc4 surprised:
        rightcenterstage
    $ speak(JECKA, "Finished with what?")
    $ setWait(54.591,56.343)
    $ speak(NICOLE, "You brought the supplies, right?")
    $ setWait(56.343,57.302)
    $ speak(JECKA, "Yeah for...")
    show jecka sc4 sad:
        rightcenterstage

    $ setWait(57.302,59.054)
    $ speak(JECKA, "You brought me here to cook crack??")
    $ setWait(59.054,60.973)
    $ speak(NICOLE, "Yeah what else is baking soda for?")
    $ setWait(60.973,62.349)
    $ speak(JECKA, "I don't know, baking?!")
    show nicole sc4 angry:
        leftcenterstage

    $ setWait(62.349,64.977)
    $ speak(NICOLE, "Dude why are you freaking out? We've had drugs before.")
    show jecka sc4 angry:
        rightcenterstage

    $ setWait(64.977,67.729)
    $ speak(JECKA, "Yeah percs and robo not go-to-jail drugs!")
    $ setWait(67.729,70.607)
    $ speak(NICOLE, "Okay just lemme borrow your stuff, I need the community service hours.")
    $ setWait(70.607,72.734)
    $ speak(JECKA, "What does making crack do for the community?")
    show nicole sc4:
        leftcenterstage

    $ setWait(72.734,75.028)
    $ speak(NICOLE, "Nothing. Selling crack's another story.")
    $ setWait(75.028,77.072)
    $ speak(JECKA, "We live in cul-de-sacs, who's gonna buy this?")
    $ setWait(77.072,78.532)
    $ speak(NICOLE, "I'm not selling it here.")

    show jecka sc4 sad:
        rightcenterstage

    $ setWait(78.532,81.618)
    $ speak(JECKA, "Oh my god... This is gonna ruin my parents' serving spoon.")
    $ setWait(81.618,82.619)
    $ speak(NICOLE, "Just buy another one.")
    $ setWait(82.619,83.662)
    $ speak(JECKA, "It's from Tiffany.")
    show nicole sc4 angry:
        leftcenterstage

    $ setWait(83.662,86.164)
    $ speak(NICOLE, "Why would you bring a Tiffany serving spoon to make crack?")
    show jecka sc4 angry:
        rightcenterstage

    $ setWait(86.164,87.833)
    $ speak(JECKA, "You never told me what it was for!")
    show nicole sc4:
        leftcenterstage

    show black onlayer screens:
        alpha 0.0
        pause 1.3
        linear 1.6 alpha 1.0

    stop ambient fadeout 4

    $ setWait(87.833,97.092)
    $ speak(NICOLE, "Look calm down, this'll take like an hour at most.")

    $ csbox = True

    show black onlayer screens:
        alpha 1.0
        pause 0.3
        linear 2 alpha 0.0

    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1.8

    $ quick_menu = False

    scene cut0088a 1

    $ setWait(97.092,99.803)
    $ speak(NICOLE, "I think we're getting the hang of this. We filled so many baggies.")
    $ setWait(99.803,101.471)
    $ speak(JECKA, "But how do we know if it's good?")
    $ setWait(101.471,106.476)
    $ speak(NICOLE, "The guy on the internet said if you break one of the little shards it should give a really nice snap.")
    scene cut0088a 2
    $ setWait(106.476,107.019)
    $ speak(JECKA, "...")
    $ setWait(107.019,108.02)
    $ speak(JECKA, "That was bad.")
    scene cut0088a 1
    $ setWait(108.02,109.104)
    $ speak(NICOLE, "Try another one.")
    scene cut0088a 2
    $ setWait(109.104,110.397)
    $ speak(JECKA, "Oh it worked.")
    scene cut0088a 1
    $ setWait(110.397,111.356)
    $ speak(NICOLE, "So it's good enough.")
    scene cut0088a 3
    $ setWait(111.356,113.608)
    $ speak(JECKA, "God my gums are still numb from rubbing this shit.")
    $ setWait(113.608,114.443)
    $ speak(NICOLE, "It's good, right?")
    scene cut0088a 1
    $ setWait(114.443,115.402)
    $ speak(JECKA, "Oh my god yeah.")
    $ setWait(115.402,118.488)
    $ speak(NICOLE, "I wanna try coke for real but I feel like I'd kill someone on it.")
    $ setWait(118.488,121.825)
    $ speak(JECKA, "Oh... I just don't wanna OD but good to know your potential.")
    $ setWait(121.825,125.245)
    $ speak(NICOLE, "Alright the whole room smells like burnt plastic so I think we made enough today.")
    scene cut0088a 4
    $ setWait(125.245,127.831)
    $ speak(JECKA, "My parents are gonna be so mad when they see this spoon.")
    $ setWait(127.831,130.125)
    $ speak(NICOLE, "Just leave it here, it's better lost than ruined.")
    $ setWait(130.125,131.418)
    $ speak(JECKA, "That's true.")
    scene cut0088a 1
    $ setWait(131.418,134.171)
    $ speak(NICOLE, "Kay I gotta go to PG county now. Can you give me a ride?")
    scene cut0088a 5
    $ setWait(134.171,137.299)
    $ speak(JECKA, "I'm not driving to PG county, Nicole! What if my car gets stolen?")
    $ setWait(137.299,141.47)
    $ speak(NICOLE, "Oh so you'll freebase crack but won't drive through a black neighborhood? What're you Ronald Reagan?")
    $ setWait(141.47,145.015)
    $ speak(JECKA, "I helped you with your community service project, you won't guilt me into anything.")
    $ setWait(145.015,147.684)
    $ speak(NICOLE, "Okay just drive me to the Franconia station, I'll take the metro.")
    $ setWait(147.684,149.394)
    $ speak(JECKA, "Fine! But I'm not driving you back.")
    $ setWait(149.394,152.397)
    $ speak(NICOLE, "No problem, I'll have plenty for a cab when I'm done.")
    stop ambient fadeout 2
    jump scene_0089
label scene_0089:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.7 alpha 0.0

    $ quick_menu = True
    $ csbox = False
    $ setVoiceTrack("audio/Scenes/0089.mp3")
    play ambient "audio/Ambience/Hood_Ambience.mp3" fadein 1.3
    scene hood

    show nicole sc4:
        centerstage

    show car_camry onlayer screens:
        xcenter -3.0
        pause 3.2
        linear 2.5 xcenter 0.5
        linear 0.4 xcenter 0.58

    $ setWait(0.16,7.375)
    $ speak(NICOLE, "Should've looked up how to actually sell drugs before I came out here.")
    $ setWait(7.375,8.21)
    $ speak(NICOLE, "Ay what's up?")
    $ setWait(8.21,9.086)
    $ speak(CAMRY, "What you got?")
    $ setWait(9.086,10.212)
    $ speak(NICOLE, "You wanna buy some crack?")
    show nicole sc4 surprised:
        centerstage

    show car_camry onlayer screens:
        xcenter 0.58
        pause 0.45
        linear 0.33 xcenter 0.65
        linear 0.8 xcenter 3.0

    $ setWait(10.212,15.675)
    $ speak(CAMRY, "12!")
    show nicole sc4 sad:
        centerstage

    show car_lincoln onlayer screens:
        xcenter -3.0
        pause 0.5
        linear 4.8 xcenter 0.54

    $ setWait(15.675,21.181)
    $ speak(NICOLE, "Damn I did sound like a cop, huh?")
    show nicole sc4:
        centerstage

    $ setWait(21.181,21.932)
    $ speak(FIEND, "Ay mo.")
    $ setWait(21.932,22.724)
    $ speak(NICOLE, "What you need?")
    $ setWait(22.724,23.642)
    $ speak(FIEND, "What you got?")
    $ setWait(23.642,25.602)
    $ speak(NICOLE, "I got rocks, bricks, white legos.")
    $ setWait(25.602,26.561)
    $ speak(FIEND, "How much?")
    $ setWait(26.561,27.938)
    $ speak(NICOLE, "Hundred for the baggie.")
    $ setWait(27.938,29.064)
    $ speak(FIEND, "Alright here ya go.")
    $ setWait(29.064,30.941)
    $ speak(NICOLE, "Thanks, oh one more thing.")
    $ setWait(30.941,31.608)
    $ speak(FIEND, "What?")
    show nicole sc4 smile:
        centerstage

    $ setWait(31.608,34.861)
    $ speak(NICOLE, "Could you sign my community service hours sheet? I'll give ya an extra rock.")
    $ setWait(34.861,37.364)
    $ speak(FIEND, "Yeah okay.")
    $ setWait(37.364,39.157)
    $ speak(NICOLE, "Yeah just any fake name, it's fine.")
    show car_lincoln onlayer screens:
        xcenter 0.54
        pause 0.4
        linear 0.5 xcenter 0.57
        linear 3 xcenter 3.0
    $ setWait(39.157,42.369)
    $ speak(FIEND, "Alright peace.")
    show nicole sc4 smile:
        centerstage
        pause 5.3
        xzoom -1
    $ setWait(42.369,48.75)
    $ speak(NICOLE, "Hundred bucks and a 2 hour signature, I think this is gonna work out.")
    $ setWait(48.75,50.585)
    $ speak(NICOLE, "Cool.")
    stop ambient fadeout 1.5
    jump scene_0090
label scene_0090:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0090.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 3
    show katz 2:
        rightcenterstage

    show hunter sc3:
        rightstage

    show kelly sc3:
        xzoom -1
        leftcenterstage

    $ setWait(0.035,9.545)
    $ speak(KATZ, "Now that I've called roll I just wanted to apologize for my absence. I know you've all been working very hard on your community service assignment.")
    $ setWait(9.545,11.046)
    $ speak(KELLY, "Has everything been okay?")
    $ setWait(11.046,19.805)
    $ speak(KATZ, "Not to get too far into detail but I've been having some personal health issues arise and have needed time away from my teaching duties.")
    $ setWait(19.805,21.724)
    $ speak(KELLY, "Oh well we hope you're alright.")
    $ setWait(21.724,22.933)
    $ speak(HUNTER, "I don't give a shit.")
    show nicole bape:
        off_left
        linear 2 leftmidstage

    $ setWait(22.933,25.269)
    $ speak(NICOLE, "Here! Oh is attendance over, sorry.")
    $ setWait(25.269,28.856)
    $ speak(KATZ, "So nice of you to join us, late as always.")
    $ setWait(28.856,31.442)
    $ speak(NICOLE, "Fuck you, you've been gone the last three classes.")
    show kelly sc3 sad:
        leftcenterstage
        xzoom 1

    $ setWait(31.442,32.902)
    $ speak(KELLY, "He had a medical issue.")
    $ setWait(32.902,37.323)
    $ speak(NICOLE, "Yeah I do too, it's called liking post-rock. No one rolls out the red carpet for me.")
    show kelly sc3:
        xzoom -1
        leftcenterstage

    $ setWait(37.323,38.824)
    $ speak(KATZ, "Just have a seat, Nicole.")

    show nicole bape angry:
        leftmidstage

    $ setWait(38.824,40.659)
    $ speak(NICOLE, "You can have this dick, bitch.")
    show katz 2 angry:
        rightcenterstage

    $ setWait(40.659,41.41)
    $ speak(KATZ, "Ergh..")
    $ setWait(41.41,42.703)
    $ speak(NICOLE, "Dude why are you freakin' out?")
    $ setWait(42.703,48.25)
    $ speak(KATZ, "Alright, Nicole! You act like you own the place, so I assume you're top of the class in community hours?")
    show nicole bape smile:
        leftmidstage

    $ setWait(48.25,49.251)
    $ speak(NICOLE, "I might be.")
    $ setWait(49.251,53.005)
    $ speak(KATZ, "Pull out your sheet then, let's see what our star student has for us.")
    $ setWait(53.005,54.381)
    $ speak(NICOLE, "Yeah sure here ya go.")
    $ setWait(54.381,56.967)
    $ speak(KATZ, "Of course as I expected...")
    show katz 2:
        rightcenterstage

    $ setWait(56.967,58.511)
    $ speak(KATZ, "Wait how many is this?")
    show nicole bape:
        leftmidstage

    $ setWait(58.511,59.929)
    $ speak(NICOLE, "I don't know, lost count.")
    $ setWait(59.929,63.516)
    $ speak(KATZ, "16, 18.. 22 hours??")
    show kelly sc3 sad:
        leftcenterstage
        xzoom -1

    $ setWait(63.516,64.767)
    $ speak(KELLY, "I only have three.")
    $ setWait(64.767,71.941)
    $ speak(KATZ, "All the signatures are different, different ink used every time, it's only been a week and a half and you're 90 percent done.")
    show kelly sc3:
        leftcenterstage
        xzoom -1

    show nicole bape smile:
        leftmidstage

    $ setWait(71.941,73.692)
    $ speak(NICOLE, "I'm kinda awesome like that.")
    $ setWait(73.692,79.74)
    $ speak(KATZ, "I'm.. shockingly surprised, Nicole. Good to see you've really took the initiative for getting these hours.")
    $ setWait(79.74,85.788)
    $ speak(NICOLE, "And aside from just the hours I'm really building a reputation in the community. Anytime someone's in need they know who to call.")
    $ setWait(85.788,90.209)
    $ speak(KATZ, "Quite the turnaround indeed. Alright who else has their sheets to show?")
    $ setWait(90.209,91.043)
    $ speak(HUNTER, "Nah.")
    show katz 2:
        rightcenterstage
        xzoom -1
    $ setWait(91.043,93.504)
    $ speak(KATZ, "What do you mean \"nah\"? Why not?")
    $ setWait(93.504,94.547)
    $ speak(HUNTER, "It's gay.")
    $ setWait(94.547,99.677)
    $ speak(KATZ, "Excuse me? What does helping the community have to do with one's sexuality?")
    $ setWait(99.677,102.972)
    $ speak(HUNTER, "Uh, it has to do with it's gay.")
    show nicole bape:
        leftmidstage

    $ setWait(102.972,111.605)
    $ speak(KATZ, "You think that way now but go above and beyond for this, get 50 hours. You'll get a framed certificate from the National Honors Society.")
    $ setWait(111.605,113.357)
    $ speak(NICOLE, "Why would anyone want that?")
    show katz 2:
        rightcenterstage
        xzoom 1
    $ setWait(113.357,120.573)
    $ speak(KATZ, "It means you really made a difference in life. For years you can hold onto it, show it to your grand kids one day.")
    show kelly sc3 sad:
        leftcenterstage
        xzoom -1
    $ setWait(120.573,121.615)
    $ speak(KELLY, "Who would do that?")
    $ setWait(121.615,127.621)
    $ speak(NICOLE, "Yeah imagine you're 80 and you haven't accomplished anything beyond a community service hour sheet.")
    $ setWait(127.621,130.517)
    $ speak(KATZ, "Alright, alright, who else has a sheet for me?")
    stop ambient fadeout 1
    jump scene_0091
label scene_0091:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0091.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 2
    show lynn 4:
        xzoom -1
        rightmidstage
        pause 0.5
        xzoom 1

    show nicole bape:
        off_left
        linear 2 leftmidstage

    $ setWait(0.036,2.33)
    $ speak(LYNN, "Nicole I'm busy, what is it?")
    show nicole bape smile:
        leftmidstage

    $ setWait(2.33,3.29)
    $ speak(NICOLE, "Oh good so I can leave?")
    $ setWait(3.29,4.958)
    $ speak(LYNN, "No, why were you sent here?")
    show nicole bape:
        leftmidstage

    $ setWait(4.958,8.003)
    $ speak(NICOLE, "One of the security people said I was violating the dress code.")
    $ setWait(8.003,11.756)
    $ speak(LYNN, "Well it looks like there's a gun on your sweatshirt so yes. Take it off.")
    show nicole bape sad:
        leftmidstage
    $ setWait(11.756,13.842)
    $ speak(NICOLE, "I don't really have anything under this.")
    $ setWait(13.842,16.178)
    $ speak(LYNN, "Then turn it inside out and get back to class.")
    $ setWait(16.178,19.347)
    $ speak(NICOLE, "Ew how do I turn a hoodie inside out? It's gonna be weird and itchy.")
    $ setWait(19.347,21.349)
    $ speak(LYNN, "You really don't have anything on under that?")
    show nicole bape:
        leftmidstage
    $ setWait(21.349,22.726)
    $ speak(NICOLE, "Like a sport bra.")
    $ setWait(22.726,24.227)
    $ speak(LYNN, "Well we can't just have you in that.")
    $ setWait(24.227,26.313)
    $ speak(NICOLE, "Are you sure? I think your gym teacher would love it.")
    $ setWait(26.313,28.773)
    $ speak(LYNN, "Please, Nicole. I'm dealing with enough as it is right now.")
    show nicole bape angry:
        leftmidstage
    $ setWait(28.773,32.277)
    $ speak(NICOLE, "What's the big deal over a drawing of a gun on my hoodie?")
    $ setWait(32.277,34.196)
    $ speak(LYNN, "Have you already forgotten Virginia Tech?")
    $ setWait(34.196,37.908)
    $ speak(NICOLE, "Oh so some Asian guy shoots up a school and now we can't wear cool hoodies anymore?")
    $ setWait(37.908,39.784)
    $ speak(LYNN, "It could promote the wrong message.")
    $ setWait(39.784,45.624)
    $ speak(NICOLE, "Who's gonna think I would shoot up a school?\nHe was only a mass shooter cause he's weird and ugly, I'm kinda the opposite of that.")
    $ setWait(45.624,49.169)
    $ speak(LYNN, "Alright fine, wear it for the rest of the day but don't bring it to school again.")
    show nicole bape:
        leftmidstage
    $ setWait(49.169,49.961)
    $ speak(NICOLE, "Whatever.")
    $ setWait(49.961,52.297)
    $ speak(LYNN, "Oh one more thing, I almost forgot.")
    $ setWait(52.297,53.048)
    $ speak(NICOLE, "What?")
    show lynn 4:
        rightmidstage
        linear 2 centerstage

    $ setWait(53.048,57.302)
    $ speak(LYNN, "I've been told of your quick turnaround in civics, congratulations on your hours.")
    $ setWait(57.302,58.637)
    $ speak(NICOLE, "Oh yeah don't mention it.")
    $ setWait(58.637,63.767)
    $ speak(LYNN, "A night and day difference in no time at all really. Where'd you find the motivation for it?")
    $ setWait(63.767,68.146)
    $ speak(NICOLE, "Uh I don't know, the community I guess?")
    $ setWait(68.146,72.108)
    $ speak(LYNN, "The community... You love the people that much now?")
    show nicole bape angry:
        leftmidstage
        pause 0.45
        xzoom -1
        linear 1.7 leftstage

    $ setWait(72.108,73.568)
    $ speak(NICOLE, "Yeah?")
    $ setWait(73.568,75.111)
    $ speak(LYNN, "Look me in the eye and say that.")
    show nicole bape:
        leftstage
        xzoom 1
    $ setWait(75.111,77.322)
    $ speak(NICOLE, "What're you my dom?")
    $ setWait(77.322,79.366)
    $ speak(LYNN, "Is there something you'd like to tell me, Nicole?")
    show nicole bape angry:
        leftstage
    $ setWait(79.366,82.118)
    $ speak(NICOLE, "Could I tell you to fuck off?")
    show lynn 4:
        xzoom -1
        centerstage
        linear 5 off_right

    $ setWait(82.118,84.204)
    $ speak(LYNN, "You're free to go.. I'll be watching.")
    show nicole bape angry:
        leftstage
        xzoom -1
        linear 1.8 off_left
    $ setWait(84.204,86.374)
    $ speak(NICOLE, "Yeah right.")
    stop ambient fadeout 1
    jump scene_0092
label scene_0092:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0092.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    scene cafeteria int 2
    show nicole bape:
        leftcenterstage
        xzoom -1

    show crispin sc3 smile:
        off_left
        xzoom -1
        linear 2 leftmidstage
    $ setWait(0.036,2.997)
    $ speak(CRISPIN, "Oh hey Nicole, what's up what's good?")
    $ setWait(2.997,3.998)
    $ speak(NICOLE, "Yeah.")
    $ setWait(3.998,7.668)
    $ speak(CRISPIN, "Cool so, I just wanted to ask you if you were busy this weekend.")
    show nicole bape angry:
        xzoom -1
        leftcenterstage

    $ setWait(7.668,8.836)
    $ speak(NICOLE, "Fuckin' why?")

    show crispin sc3:
        leftmidstage
        xzoom -1

    $ setWait(8.836,12.924)
    $ speak(CRISPIN, "I gotta do a video for a class project and was kinda wondering if you could be in it.")
    $ setWait(12.924,16.719)
    $ speak(NICOLE, "Why can't you ask the other thirty people who take the class with you?")
    $ setWait(16.719,21.39)
    $ speak(CRISPIN, "Yeah um it's like, I don't know I feel like they're gonna flake on me.")
    $ setWait(21.39,25.561)
    $ speak(NICOLE, "And a girl who doesn't take the class, doesn't even like you, she's gonna come through.")
    $ setWait(25.561,26.979)
    $ speak(CRISPIN, "Y-you don't like me?")
    $ setWait(26.979,27.939)
    $ speak(NICOLE, "I hate you.")
    show crispin sc3 smile:
        leftmidstage
        xzoom -1

    $ setWait(27.939,32.652)
    $ speak(CRISPIN, "Haha dude like, quit like, you're always kidding around and stuff. You're crazy though it's cool.")
    $ setWait(32.652,37.782)
    $ speak(NICOLE, "I'm not laughing. No girl randomly recruited for your class video will ever wanna fuck you.")
    show crispin sc3:
        leftmidstage
        xzoom -1

    $ setWait(37.782,40.159)
    $ speak(CRISPIN, "Whoa whoa, quit jumping around to shit.")
    $ setWait(40.159,44.205)
    $ speak(NICOLE, "What's the endgame then? You're gonna awkwardly go up to a girl just to be friends?")
    $ setWait(44.205,47.667)
    $ speak(CRISPIN, "Well I mean... friends can have a lot of definitions to it.")
    show nicole bape:
        leftcenterstage
        xzoom -1
    $ setWait(47.667,51.295)
    $ speak(NICOLE, "Is there a definition where you blow your brains out with a shotgun while I sit and watch?")
    $ setWait(51.295,53.547)
    $ speak(CRISPIN, "Wh-What the fuck? Why would you do that?")
    show nicole bape smile:
        leftcenterstage
        xzoom -1
    $ setWait(53.547,55.8)
    $ speak(NICOLE, "What else are friends for?")
    $ setWait(55.8,57.802)
    $ speak(CRISPIN, "So are you waiting for somebody?")
    show nicole bape:
        leftcenterstage
        xzoom -1
    $ setWait(57.802,59.512)
    $ speak(NICOLE, "Yeah and she wouldn't wanna fuck you either.")
    $ setWait(59.512,62.765)
    $ speak(CRISPIN, "Bro you're acting wild, how can you even say something like that?")
    show jecka sc5:
        off_right
        linear 2.4 rightcenterstage

    $ setWait(62.765,64.809)
    $ speak(JECKA, "Hey sorry, I got held up in Math.")
    show nicole bape:
        leftcenterstage
        xzoom 1

    $ setWait(64.809,66.269)
    $ speak(NICOLE, "Jecka would you fuck Crispin?")

    show jecka sc5 angry:
        rightcenterstage
    $ setWait(66.269,67.144)
    $ speak(JECKA, "Ew, no!")
    show nicole bape smile:
        xzoom -1
        leftcenterstage

    $ setWait(67.144,68.771)
    $ speak(NICOLE, "See, no one wants to fuck you.")

    show nicole bape:
        leftcenterstage
        xzoom -1

    show crispin sc3 smile:
        leftmidstage
        xzoom -1

    $ setWait(68.771,71.065)
    $ speak(CRISPIN, "You guys are just, man you guys are wild.")
    $ setWait(71.065,72.984)
    $ speak(JECKA, "Fuck off and leave!")
    show crispin sc3 smile:
        xzoom 1
        leftmidstage
        linear 2 off_left

    $ setWait(72.984,75.736)
    $ speak(CRISPIN, "Heh okay I'll see you around, guys.")
    $ setWait(75.736,77.488)
    $ speak(JECKA, "What the fuck are you talking to him for?")
    show nicole bape:
        leftcenterstage
        xzoom 1
    $ setWait(77.488,82.326)
    $ speak(NICOLE, "Dude I don't know I was alone and he came up to me. You know they get brave when we're alone.\nWhat was the hold up?")
    show jecka sc5:
        rightcenterstage

    $ setWait(82.326,83.995)
    $ speak(JECKA, "I was flirting with my teacher.")
    $ setWait(83.995,85.454)
    $ speak(NICOLE, "For business or pleasure?")
    $ setWait(85.454,88.374)
    $ speak(JECKA, "He's fifty, what do you think? I was trying to get an A minus.")
    show nicole bape smile:
        leftcenterstage
    $ setWait(88.374,92.169)
    $ speak(NICOLE, "Cool yeah I might finish with an A for the year in civics at the rate I'm going.")
    $ setWait(92.169,93.045)
    $ speak(JECKA, "He bought it?")
    show nicole bape:
        leftcenterstage
    $ setWait(93.045,95.464)
    $ speak(NICOLE, "He doesn't have to buy anything, they're real signatures.")
    show jecka sc5 sad:
        rightcenterstage

    $ setWait(95.464,97.341)
    $ speak(JECKA, "I'm amazed you haven't been killed yet.")
    show nicole bape angry:
        leftcenterstage
    $ setWait(97.341,100.97)
    $ speak(NICOLE, "Oh my god if you just keep to yourself no neighborhood's all that dangerous.")
    show jecka sc5 angry:
        rightcenterstage

    $ setWait(100.97,103.18)
    $ speak(JECKA, "You're not keeping to yourself, you're selling crack.")
    show nicole bape:
        leftcenterstage
    $ setWait(103.18,106.142)
    $ speak(NICOLE, "Yeah and PG loves me for it so there's no reason to kill me.")
    show jecka sc5:
        rightcenterstage

    $ setWait(106.142,107.31)
    $ speak(JECKA, "Okay we'll see.")
    show nicole bape angry:
        leftcenterstage
    $ setWait(107.31,109.729)
    $ speak(NICOLE, "Dude you're such a hater, you sound like Bitch Lynn right now.")
    $ setWait(109.729,111.272)
    $ speak(JECKA, "What'd Bitch Lynn do this time?")
    $ setWait(111.272,115.86)
    $ speak(NICOLE, "I got called in over my Bape hoodie and then she got all on my ass over doing well in civics.")
    $ setWait(115.86,117.903)
    $ speak(JECKA, "Why wouldn't she be happy about that?")
    $ setWait(117.903,122.867)
    $ speak(NICOLE, "She thinks I'm cheating by not actually doing community service. It's like suspicious or whatever.")
    $ setWait(122.867,125.077)
    $ speak(JECKA, "You're not actually doing community service?")
    $ setWait(125.077,125.828)
    $ speak(NICOLE, "Yeah I am.")
    show jecka sc5 angry:
        rightcenterstage

    $ setWait(125.828,128.748)
    $ speak(JECKA, "You're selling drugs in PG County, how does that help their community?")
    show nicole bape:
        leftcenterstage

    $ setWait(128.748,130.041)
    $ speak(NICOLE, "I have really good prices.")
    $ setWait(130.041,133.711)
    $ speak(JECKA, "Giving pregnant women 2-for-1's on crack rocks doesn't benefit the country.")
    $ setWait(133.711,136.422)
    $ speak(NICOLE, "Oh what so now pregnant women have less rights than the rest of us?")
    $ setWait(136.422,138.549)
    $ speak(JECKA, "No-- okay do whatever the fuck you want.")
    $ setWait(138.549,140.885)
    $ speak(NICOLE, "That's what I planned on. You wanna come with me tonight?")
    $ setWait(140.885,142.887)
    $ speak(JECKA, "I'd rather date my ugly math teacher.")
    $ setWait(142.887,144.305)
    $ speak(NICOLE, "How would you rather do that?")
    $ setWait(144.305,147.6)
    $ speak(JECKA, "Cause if the police show up I won't be the one getting arrested.")

    show nicole bape:
        leftcenterstage
        pause 1.9
        xzoom -1
        linear 2.7 off_left

    $ setWait(147.6,151.145)
    $ speak(NICOLE, "Man I was gonna cut you in and everything, alright then suit yourself.")
    stop ambient fadeout 1
    jump scene_0093
label scene_0093:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0093.mp3")
    play ambient "audio/Ambience/Hood_Ambience.mp3" fadein 1

    scene hood

    show nicole bape smile:
        centerstage

    show car_lincoln:
        xcenter 0.54

    $ setWait(0.084,2.503)
    $ speak(FIEND, "So you in school or?")
    $ setWait(2.503,6.007)
    $ speak(NICOLE, "Yeah that's what the hour sheet's for. After tonight I'll probably be all done.")
    $ setWait(6.007,8.801)
    $ speak(FIEND, "Cool cool yeah I thought you got out the prison or some shit.")
    $ setWait(8.801,11.47)
    $ speak(NICOLE, "Right? But no I'm too white and pretty to go to jail.")
    show nicole bape:
        centerstage
    $ setWait(11.47,14.849)
    $ speak(FIEND, "Ay the fuck, bitch you wild sayin' that shit, you wild you anything.")
    $ setWait(14.849,16.183)
    $ speak(NICOLE, "What do you want me to lie?")
    $ setWait(16.183,17.643)
    $ speak(FIEND, "Yeah yeah I guess.")
    $ setWait(17.643,21.564)
    $ speak(NICOLE, "Uh huh, well I got packs to move so if you could...")
    show car_lincoln:
        xcenter 0.54
        pause 2.5
        linear 0.3 xcenter 0.57
        linear 4 xcenter 3.5

    $ setWait(21.564,26.444)
    $ speak(FIEND, "Nah yeah I'll see you some other time with it.")
    show car_civic:
        xcenter -3.0
        pause 3.1
        linear 4 xcenter 0.54

    $ setWait(26.444,34.201)
    $ speak(NICOLE, "...Damn crack's gotta be awesome if it has this many repeat customers.")
    $ setWait(34.201,36.245)
    $ speak(NICOLE, "Is this a cop?")
    $ setWait(36.245,40.382)
    $ speak(NICOLE, "Hey if you're a cop do you have to tell me that you're a cop?")
    show cut0093 a onlayer screens:
        alpha 1.0
        pause 4.4 alpha 0.0
    $ setWait(40.382,42.793)
    $ speak(NICOLE, "...")
    $ setWait(42.793,46.005)
    $ speak(NICOLE, "White guy buyin' rocks in PG? Yeah you're definitely a cop.")
    $ setWait(46.005,47.173)
    $ speak(KATZ, "I'm not a cop!")
    hide cut0093 a onlayer screens
    $ setWait(47.173,48.591)
    $ speak(NICOLE, "Wait you sound familiar...")
    show nicole bape surprised:
        centerstage
    $ setWait(48.591,50.009)
    $ speak(NICOLE, "is that Mr. Katz??")
    show cut0093 b onlayer screens
    $ setWait(50.009,51.135)
    $ speak(KATZ, "Keep your voice down!")
    $ setWait(51.135,52.97)
    $ speak(NICOLE, "Did Miss Lynn send you to spy on me?")
    $ setWait(52.97,55.389)
    $ speak(KATZ, "No! Just take the money and let me leave with it.")
    hide cut0093 b onlayer screens
    show nicole bape surprised:
        centerstage

    $ setWait(55.389,58.392)
    $ speak(NICOLE, "Holy fuck you weren't missing class cause you're sick...")
    $ setWait(58.392,59.56)
    $ speak(NICOLE, "You're a crackhead!")
    $ setWait(59.56,61.062)
    $ speak(KATZ, "I said keep it down!")
    show nicole bape:
        centerstage

    $ setWait(61.062,65.107)
    $ speak(NICOLE, "I mean if you wanna buy, no problem, but are you allowed to sign my hours sheet?")

    $ setWait(65.107,66.484)
    $ speak(KATZ, "This was your charity??")



    show nicole bape smile:
        centerstage

    $ setWait(66.484,69.904)
    $ speak(NICOLE, "Yeah I sell shit for cheap, I'm the great white hope of PG County.")
    $ setWait(69.904,73.24)
    $ speak(KATZ, "I thought it was a pharmaceutical charity. Medicine Rocks?")
    show nicole bape:
        centerstage

    $ setWait(73.24,75.034)
    $ speak(NICOLE, "Yeah as in crack rocks, duh.")
    show cut0093 b onlayer screens
    $ setWait(75.034,79.08)
    $ speak(KATZ, "That's downright evil! Wait 'till I tell the school board you're cheating on your hours.")
    hide cut0093 b onlayer screens
    show nicole bape angry:
        centerstage

    $ setWait(79.08,82.833)
    $ speak(NICOLE, "Wait 'till I tell the school board you're buying ready rock off one of your students.")

    $ setWait(82.833,86.128)
    $ speak(KATZ, "Fine, we'll both keep our mouths shut. Now gimme the stuff.")
    show nicole bape:
        centerstage

    $ setWait(86.128,87.129)
    $ speak(NICOLE, "Done deal, here ya go.")
    show nicole bape surprised:
        centerstage

    $ setWait(87.129,87.797)
    $ speak(COP, "Freeze!!")

    $ setWait(87.797,88.089)
    $ speak(KATZ, "Huh??")

    show nicole bape surprised:
        centerstage
        xzoom -1

    $ setWait(88.089,88.798)
    $ speak(NICOLE, "Oh shit!")
    show cop:
        off_left
        xzoom -1
        linear 0.65 leftstage

    $ setWait(88.798,91.217)
    $ speak(COP, "A little midnight marketplace here?")
    show nicole bape surprised:
        centerstage
        xzoom 1
    $ setWait(91.217,92.76)
    $ speak(NICOLE, "How'd you let the cops tail you??")

    show nicole bape surprised:
        centerstage
        xzoom -1

    show cop:
        leftstage
        xzoom -1
        linear 2 leftmidstage

    $ setWait(92.76,98.724)
    $ speak(COP, "Actually sweetheart the cops tailed you.\nWe got a tip from a school principal across the Potomac.")
    show car_civic:
        xcenter 0.54
        pause 0.35
        linear 0.25 xcenter 0.56
        linear 0.7 xcenter 3.2

    $ setWait(98.724,99.475)
    $ speak(KATZ, "Shit!")
    show cop:
        leftmidstage
        pause 0.3
        linear 0.6 off_right


    show nicole bape surprised:
        centerstage
        xzoom -1
        pause 0.6
        xzoom 1
        linear 0.3 rightcenterstage


    $ setWait(99.475,100.309)
    $ speak(COP, "We got a runner!")

    show nicole bape yell:
        rightcenterstage
        xzoom 1
    $ setWait(100.309,104.021)
    $ speak(NICOLE, "What the fuck!!")
    show cop:
        off_right
        pause 0.7
        xzoom 1
        linear 1 rightstage

    show nicole bape sad:
        rightcenterstage

    $ setWait(104.021,106.732)
    $ speak(COP, "Ugh now we gotta call in a body bag.")
    $ setWait(106.732,108.692)
    $ speak(NICOLE, "Did you just kill my civics teacher!?")
    $ setWait(108.692,111.07)
    $ speak(COP, "It was calculated risk but it paid off.")
    show nicole bape yell:
        rightcenterstage

    $ setWait(111.07,113.656)
    $ speak(NICOLE, "Dude just shoot me too I can't fucking handle this shit!")
    show cop:
        rightstage
        linear 7 rightcenterstage

    show black onlayer screens:
        alpha 0.0
        pause 1
        linear 4.1 alpha 1.0

    stop ambient fadeout 7

    $ setWait(113.656,122.496)
    $ speak(COP, "Nonsense, you have the right to remain silent. Anything you say can and will be held against you...")
    jump scene_0094
label scene_0094:
    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0094.mp3")
    play ambient "audio/Ambience/Courtroom_Ambience.mp3" fadein 2
    scene jail int

    show nicole jail:
        leftmidstage

    show jecka sc6:
        rightstage
        linear 2 centerstage

    $ setWait(0.042,1.793)
    $ speak(NICOLE, "...")
    $ setWait(1.793,3.795)
    $ speak(NICOLE, "You waited two weeks to visit me?")

    show jecka sc6 angry:
        centerstage
        pause 1.25
        xzoom -1
        linear 2 rightstage

    $ setWait(3.795,5.922)
    $ speak(JECKA, "Okay if you're gonna be a bitch about it I can go now.")

    show nicole jail yell:
        leftmidstage

    $ setWait(5.922,8.008)
    $ speak(NICOLE, "No I'm so bored in here, don't go!")
    show jecka sc6:
        rightstage
        pause 1.3
        xzoom 1
        linear 2 centerstage

    show nicole jail sad:
        leftmidstage

    $ setWait(8.008,10.177)
    $ speak(JECKA, "That's what I thought. So how's jail?")
    $ setWait(10.177,14.765)
    $ speak(NICOLE, "I've been trying to kill myself everyday for the last two weeks but there's like no options.")
    $ setWait(14.765,17.142)
    $ speak(JECKA, "It's not the loony bin, there's no options at all?")
    $ setWait(17.142,25.275)
    $ speak(NICOLE, "Oh my god there's no sleeping pills, no sharp objects, the sheets rip easily, and the guards walk by every hour so you can't even bleed out with the razor blades.")
    $ setWait(25.275,27.319)
    $ speak(JECKA, "Wait how long are you even serving?")
    show nicole jail:
        leftmidstage

    $ setWait(27.319,30.447)
    $ speak(NICOLE, "The public defender was like three years with good behavior.")

    show jecka sc6 angry:
        centerstage

    $ setWait(30.447,34.743)
    $ speak(JECKA, "You're trying to kill yourself over three years? I only came here cause I thought you'd be in for 20.")
    show nicole jail sad:
        leftmidstage

    $ setWait(34.743,41.333)
    $ speak(NICOLE, "Two weeks in here feels like 20. There's only one TV in the whole block and all it plays is UPN reruns.")

    show jecka sc6:
        centerstage

    $ setWait(41.333,42.793)
    $ speak(JECKA, "And that's not even around anymore.")
    $ setWait(42.793,52.719)
    $ speak(NICOLE, "Yeah so I'm going insane, they lock you in here to turn your brain into mush. Fuckin' every night you try going to bed you just hear weird echoey moans in the distance.")
    show jecka sc6 sad:
        centerstage

    $ setWait(52.719,53.804)
    $ speak(JECKA, "Why are they moaning?")
    $ setWait(53.804,58.392)
    $ speak(NICOLE, "I don't know. You can't tell whether they're having sex or withdrawing from heroin.")
    $ setWait(58.392,64.481)
    $ speak(JECKA, "Wow sounds kinda like torture. But I guess that's how the system works to make you not sell crack anymore.")
    show nicole jail angry:
        leftmidstage
    $ setWait(64.481,68.276)
    $ speak(NICOLE, "It's a broken ass system, they just assume we hustle for fun.")
    $ setWait(68.276,73.573)
    $ speak(JECKA, "Well yeah I mean aren't there other things you can do besides selling drugs?")
    $ setWait(73.573,75.45)
    $ speak(NICOLE, "Not for us.")
    $ setWait(75.45,80.247)
    $ speak(NICOLE, "You're born into bullshit, no tools to get out of it, and they still wanna act like it's your fault.")
    $ setWait(80.247,87.879)
    $ speak(NICOLE, "They wanna act like you wanna be in jail, like you didn't know the consequence. No shit I knew but it's either suffer out there or suffer in here.")
    $ setWait(87.879,96.722)
    $ speak(NICOLE, "And when you get out it's even more bullshit. PO, ankle monitor, drug tests, felony record... It's almost like you had less problems on the inside.")
    $ setWait(96.722,99.933)
    $ speak(NICOLE, "The system's educational, for everyone but the prisoner.")
    $ setWait(99.933,108.024)
    $ speak(NICOLE, "This a maze and we're the rats, but most days you'd rather die than get to the finish... Now all I think about is dying.")
    $ setWait(108.024,110.527)
    $ speak(NICOLE, "I guess 50 was right.")
    $ setWait(110.527,112.529)
    $ speak(JECKA, "Right about what?")
    $ setWait(112.529,118.326)
    $ speak(NICOLE, "It's get rich or die trying... I did what I had to.")
    show jecka sc6:
        centerstage

    $ setWait(118.326,120.37)
    $ speak(JECKA, "...You're white.")

    show nicole jail:
        leftmidstage

    $ setWait(120.37,121.121)
    $ speak(NICOLE, "What?")
    show jecka sc6 angry:
        centerstage

    $ setWait(121.121,123.915)
    $ speak(JECKA, "You're white, Nicole. You didn't have to do anything!")
    show nicole jail sad:
        leftmidstage

    $ setWait(123.915,125.083)
    $ speak(NICOLE, "That's what you think.")
    $ setWait(125.083,129.504)
    $ speak(JECKA, "What I know is we live in cul-de-sacs and you don't have to sell crack when you live in a cul-de-sac!")
    $ setWait(129.504,135.01)
    $ speak(NICOLE, "I didn't even totally mean financially like my parents were mean to me and shit, it like makes you make bad decisions!")
    $ setWait(135.01,139.389)
    $ speak(JECKA, "You sold crack to a pregnant woman cause your Mom was mean to you??")
    $ setWait(139.389,140.682)
    $ speak(NICOLE, "Yeah sorta.")
    $ setWait(140.682,145.02)
    $ speak(JECKA, "So all you did was take your little problems and turn them into someone else's bigger problems.")
    $ setWait(145.02,146.188)
    $ speak(NICOLE, "They weren't little to me!")
    $ setWait(146.188,149.191)
    $ speak(JECKA, "You better turn Islamic and pray the judge agrees with that!")
    show nicole jail surprised:
        leftmidstage

    $ setWait(149.191,150.4)
    $ speak(NICOLE, "Can white people be Islam?")

    show jecka sc6 sad:
        centerstage
        pause 0.8
        xzoom -1
        linear 3.6 off_right

    $ setWait(150.4,153.737)
    $ speak(JECKA, "I don't know-- look I gotta go I'll see you next week maybe.")
    show nicole jail yell:
        leftmidstage
        linear 0.2 xalign 0.37

    show black onlayer screens:
        alpha 0.0
        linear 2.4 alpha 1.0

    stop ambient fadeout 5.5

    $ setWait(153.737,158.238)
    $ speak(NICOLE, "Wait no no don't go!!")

    jump end_0095

label end_0095:

    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0

    if "end_0095" not in persistent.endings:
        $ persistent.endings.append("end_0095")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0095.webm")
    return

label scene_0096:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0096.mp3")
    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene classroom int 5
    show megan sc2:
        rightmidstage

    show hunter sc1:
        rightstage

    show emily sc2:
        xzoom -1
        rightcenterstage

    show crispin sc2:
        xzoom -1
        leftcenterstage

    $ setWait(0.045,1.171)
    $ speak(MEGAN, "Crispin?")
    $ setWait(1.171,2.047)
    $ speak(CRISPIN, "Here.")
    $ setWait(2.047,2.964)
    $ speak(MEGAN, "Emily?")
    $ setWait(2.964,4.215)
    $ speak(EMILY, "Uh huh.")
    show megan sc2 angry:
        rightmidstage

    $ setWait(4.215,5.091)
    $ speak(MEGAN, "Emily??")
    show emily sc2 upset
    $ setWait(5.091,7.052)
    $ speak(EMILY, "Dude I'm literally standing in front of you.")
    $ setWait(7.052,8.929)
    $ speak(MEGAN, "Just making sure we do it right.")
    show nicole sc3:
        off_left
        linear 1.5 leftmidstage

    show emily sc2

    $ setWait(8.929,9.888)
    $ speak(NICOLE, "Do what right?")
    $ setWait(9.888,12.849)
    $ speak(MEGAN, "Taking attendance?\nNicole... Tardy.")
    show nicole sc3 angry:
        leftmidstage

    $ setWait(12.849,14.601)
    $ speak(NICOLE, "The fuck you mean \"tardy\"? I'm here.")
    $ setWait(14.601,15.852)
    $ speak(MEGAN, "Meaning you're late?")
    $ setWait(15.852,19.064)
    $ speak(NICOLE, "Since when are you in charge of that? You're a student like the rest of us.")
    show megan sc2
    $ setWait(19.064,25.779)
    $ speak(MEGAN, "As of last week, not anymore. Miss Teagan made me student-teacher while she's off working on a professional stage production.")
    $ setWait(25.779,27.364)
    $ speak(NICOLE, "And what makes you so special?")
    $ setWait(27.364,32.202)
    $ speak(MEGAN, "I was top of the drama class junior year? We can't have a bad actor teach the class.")
    show nicole sc3
    $ setWait(32.202,35.747)
    $ speak(NICOLE, "Well I don't think you're a good actor either, you probably couldn't even lie to the police.")
    $ setWait(35.747,36.748)
    $ speak(EMILY, "Yeah honestly.")
    show megan sc2 angry
    $ setWait(36.748,37.832)
    $ speak(MEGAN, "Don't take her side!")
    show emily sc2 upset
    $ setWait(37.832,39.042)
    $ speak(EMILY, "Why not? She's right.")
    $ setWait(39.042,44.464)
    $ speak(MEGAN, "Cause I'm your student-teacher and I have the power to write you up! Any other questions??")
    $ setWait(44.464,47.634)
    $ speak(NICOLE, "Has a guy ever killed himself while dating you?")
    show emily sc2
    show megan sc2
    $ setWait(47.634,56.101)
    $ speak(MEGAN, "So anyway! Today we'll break up into two separate groups. One'll do a table read exercise, the other will be improvised acting.\nSo who wants to do what?")
    show emily sc2 angry
    $ setWait(56.101,60.146)
    $ speak(EMILY, "I don't wanna do anything. The teacher isn't even here, can't we just hang out?")
    show megan sc2 angry
    $ setWait(60.146,62.983)
    $ speak(MEGAN, "Why would you sign up for drama if you don't even care about acting?")
    $ setWait(62.983,65.777)
    $ speak(EMILY, "It's fuck around class. Like we're gonna be actors one day.")
    $ setWait(65.777,71.491)
    $ speak(NICOLE, "Yeah no offense Megan but you're kinda not pretty enough to be in movies, I don't get why you wanna act.")
    $ setWait(71.491,74.786)
    $ speak(MEGAN, "Acting isn't about looks, it's about talent and creativity!")
    show emily sc2 upset
    $ setWait(74.786,77.455)
    $ speak(EMILY, "When's the last time you saw an ugly girl star in a movie?")
    $ setWait(77.455,78.79)
    $ speak(MEGAN, "Stop calling me ugly!")
    $ setWait(78.79,80.375)
    $ speak(EMILY, "No I'm not calling you ugly.")
    $ setWait(80.375,81.167)
    $ speak(NICOLE, "I am.")
    $ setWait(81.167,82.794)
    $ speak(EMILY, "You're just like...")
    $ setWait(82.794,84.379)
    $ speak(MEGAN, "Like what?")
    $ setWait(84.379,88.091)
    $ speak(EMILY, "...You look like the girl from Harry Potter but not photogenic.")
    show crispin sc2 smile
    $ setWait(88.091,89.426)
    $ speak(CRISPIN, "Oh yeah I see it!")
    show megan sc2 angry:
        rightmidstage
        pause 1.3
        xzoom -1
        linear 1.7 off_right

    $ setWait(89.426,93.513)
    $ speak(MEGAN, "Alright I'm done with this! Get in your groups or I'm writing all of you up!")
    stop ambient fadeout 3
    menu:
        "GROUP IMPROV":
            jump scene_0097
        "TABLE READING":
            jump scene_0098
label scene_0097:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0097.mp3")
    play ambient "audio/Ambience/Courtroom_Ambience.mp3" fadein 1
    scene theatre 2b
    show hunter sc1:
        leftstage
        xzoom -1

    show nicole sc3:
        leftcenterstage
        xzoom -1

    show crispin sc2:
        rightcenterstage

    $ setWait(0.036,2.122)
    $ speak(NICOLE, "So how do we do this?")
    $ setWait(2.122,6.793)
    $ speak(HUNTER, "I give you guys a scenario and you play it out and get feedback afterwards.")
    $ setWait(6.793,7.961)
    $ speak(CRISPIN, "Oh yeah makes sense.")
    $ setWait(7.961,16.261)
    $ speak(HUNTER, "So the scene is you're a newly wed husband and wife in 1949, and the wife wants to know what the war was like.")
    $ setWait(16.261,18.596)
    $ speak(NICOLE, "What if he doesn't know what the war was like?")
    $ setWait(18.596,25.353)
    $ speak(HUNTER, "It was 1949, everybody was just getting out of the war or at least knew someone, right?")
    $ setWait(25.353,26.855)
    $ speak(CRISPIN, "Okay so we go now?")
    $ setWait(26.855,28.565)
    $ speak(HUNTER, "Yeah action.")
    $ setWait(28.565,32.819)
    $ speak(CRISPIN, "Hey you seem kinda upset, is there a thing you wanna talk about?")
    show nicole sc3:
        leftcenterstage
        xzoom 1

    $ setWait(32.819,34.529)
    $ speak(NICOLE, "Nah I'm good.")
    $ setWait(34.529,37.741)
    $ speak(CRISPIN, "Oh well, do you wanna hear about the war?")
    $ setWait(37.741,38.575)
    $ speak(NICOLE, "No.")
    show hunter sc1:
        leftstage
        xzoom -1
        linear 1 leftmidstage

    $ setWait(38.575,44.33)
    $ speak(HUNTER, "Wait wait, Megan said you can never say \"no\" for improv. It just makes it go nowhere.")
    show nicole sc3:
        leftcenterstage
        xzoom -1

    $ setWait(44.33,46.166)
    $ speak(NICOLE, "That was the plan.")
    $ setWait(46.166,48.334)
    $ speak(HUNTER, "Well I guess don't do that?")
    show hunter sc1:
        xzoom -1
        leftmidstage
        linear 1 leftstage

    show crispin sc2 smile

    $ setWait(48.334,52.422)
    $ speak(CRISPIN, "Alright let's try again... Hey wife, something on your mind?")
    show nicole sc3:
        leftcenterstage
        xzoom 1

    $ setWait(52.422,55.592)
    $ speak(NICOLE, "Yeah uh, there's something I've been wanting to say lately.")
    $ setWait(55.592,56.926)
    $ speak(CRISPIN, "Oh what's that?")
    show nicole sc3 smile
    $ setWait(56.926,58.344)
    $ speak(NICOLE, "The N-word.")
    show crispin sc2
    $ setWait(58.344,60.972)
    $ speak(CRISPIN, "Wh-Why would you wanna say that?")
    $ setWait(60.972,65.059)
    $ speak(NICOLE, "It's 1949 isn't it? Don't we usually say the N-word?")
    $ setWait(65.059,66.853)
    $ speak(CRISPIN, "Oh maybe yeah.")
    $ setWait(66.853,74.861)
    $ speak(NICOLE, "The N-word is probably my favorite thing to just scream in public with no repercussions. 1949's a great year, for us anyway.")
    $ setWait(74.861,76.905)
    $ speak(CRISPIN, "Uh huh, I'm glad you're happy.")
    show nicole sc3 smile:
        leftcenterstage
        pause 0.8
        xzoom -1

    $ setWait(76.905,78.74)
    $ speak(NICOLE, "Yeah, oh do you see that?")
    $ setWait(78.74,79.616)
    $ speak(CRISPIN, "See what?")
    $ setWait(79.616,83.995)
    $ speak(NICOLE, "That different colored family pulling up in a Lincoln? You wanna do the honors?")
    $ setWait(83.995,85.205)
    $ speak(CRISPIN, "What are the honors?")
    show nicole sc3 smile:
        leftcenterstage
        xzoom 1
    $ setWait(85.205,87.081)
    $ speak(NICOLE, "Calling them the N-word, duh.")
    $ setWait(87.081,88.208)
    $ speak(CRISPIN, "Why would I do that?")
    $ setWait(88.208,90.71)
    $ speak(NICOLE, "It's 1949, why wouldn't you?")
    $ setWait(90.71,94.756)
    $ speak(CRISPIN, "Oh right um... is there anything else you wanna talk about?")
    $ setWait(94.756,98.218)
    $ speak(NICOLE, "Yeah do you wanna join the KKK? It's normal right now.")
    $ setWait(98.218,99.052)
    $ speak(CRISPIN, "No?")
    show nicole sc3 angry:
        leftcenterstage

    $ setWait(99.052,101.179)
    $ speak(NICOLE, "Dude what the fuck-- Megan!")
    show megan sc2:
        off_right
        linear 2 rightmidstage

    $ setWait(101.179,102.096)
    $ speak(MEGAN, "What's the matter?")
    show nicole sc3
    $ setWait(102.096,104.098)
    $ speak(NICOLE, "Crispin said \"no\" during the improv.")
    show megan sc2 angry:
        rightmidstage

    $ setWait(104.098,106.142)
    $ speak(MEGAN, "What the hell Crispin, we went over this!")
    show crispin sc2:
        xzoom -1
    $ setWait(106.142,106.684)
    $ speak(CRISPIN, "No but--")
    $ setWait(106.684,111.815)
    $ speak(MEGAN, "Another \"no\"! I told you to get that word out of your vocabulary if you're gonna do this exercise.")
    $ setWait(111.815,113.775)
    $ speak(CRISPIN, "Yeah but the situation got kinda--")
    $ setWait(113.775,123.201)
    $ speak(MEGAN, "The situation doesn't matter, it's improv! No matter what you never use that N-word! If you do it again I have the power to fail you for the quarter.")

    show megan sc2 angry:
        rightmidstage
        xzoom -1
        linear 1.7 off_right

    $ setWait(123.201,126.412)
    $ speak(HUNTER, "Alright so uh, resume scene.")
    show nicole sc3 smile:
        leftcenterstage
        xzoom 1

    show crispin sc2:
        xzoom 1

    $ setWait(126.412,131.167)
    $ speak(NICOLE, "But yeah honey, should we sign up for the 1949 KKK initiation?")
    $ setWait(131.167,133.086)
    $ speak(CRISPIN, "N-- ...Okay.")
    $ setWait(133.086,139.05)
    $ speak(NICOLE, "Great to hear. By the way could you tell me about the war? Oh and use the N-word as much as possible when describing it.")
    show hunter sc1:
        leftstage
        xzoom -1
        linear 1 leftmidstage

    $ setWait(139.05,140.301)
    $ speak(HUNTER, "And scene!")
    $ setWait(140.301,141.344)
    $ speak(CRISPIN, "Oh, alright.")
    show nicole sc3 smile:
        xzoom -1

    $ setWait(141.344,142.679)
    $ speak(NICOLE, "So how'd we do?")
    show hunter sc1:
        leftmidstage
        xzoom -1
        linear 3.2 off_right

    $ setWait(142.679,145.765)
    $ speak(HUNTER, "Uh I'm gonna have a talk with Megan.")
    show nicole sc3 angry:
        xzoom 1

    $ setWait(145.765,146.808)
    $ speak(NICOLE, "Shit.")
    stop ambient fadeout 1
    jump scene_0099
label scene_0098:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene theatre 1
    $ setVoiceTrack("audio/Scenes/0098.mp3")
    show nicole sc3:
        rightcenterstage
        xzoom -1

    show emily sc2:
        rightmidstage

    show megan sc2:
        xzoom -1
        leftcenterstage

    $ setWait(0.046,3.8)
    $ speak(MEGAN, "So you just read aloud, but act it out as if you were saying it on stage.")
    $ setWait(3.8,4.884)
    $ speak(EMILY, "Who's playing who?")
    $ setWait(4.884,8.221)
    $ speak(MEGAN, "Emily you'll play the cadet, and Nicole you'll play the captain.")
    show nicole sc3:
        xzoom 1
    $ setWait(8.221,12.684)
    $ speak(NICOLE, "Swell uh, \"What do you think you're doing young lady?\"")
    $ setWait(12.684,15.436)
    $ speak(EMILY, "\"Sorry I'm just nervous.\" Like that?")
    show megan sc2 smile:
        leftcenterstage
        xzoom -1
        pause 2
        xzoom 1
        linear 2.4 off_left

    $ setWait(15.436,19.273)
    $ speak(MEGAN, "Yeah great, so you guys play out the scene I'll be back in a bit.")
    $ setWait(19.273,21.859)
    $ speak(NICOLE, "\"Nervous about what? Missing home?\"")
    $ setWait(21.859,25.113)
    $ speak(EMILY, "\"I am nervous about dying in a war I didn't start.\"")
    $ setWait(25.113,26.906)
    $ speak(NICOLE, "\"You better finish it, cadet.\"")
    $ setWait(26.906,29.992)
    $ speak(EMILY, "\"Why don't we start loving instead of fighting?\" This sucks.")
    $ setWait(29.992,33.496)
    $ speak(NICOLE, "Yeah. \"No fight in you, huh?\" What the fuck is this?")
    show megan sc2 smile:
        off_left
        xzoom -1
        linear 2.1 leftcenterstage

    $ setWait(33.496,35.79)
    $ speak(MEGAN, "I'm back, how you guys doing so far?")
    show emily sc2 upset

    $ setWait(35.79,36.499)
    $ speak(EMILY, "Decent?")

    show nicole sc3:
        xzoom -1

    $ setWait(36.499,38.209)
    $ speak(NICOLE, "Yeah this script's ass, who wrote this?")
    show megan sc2 angry:
        leftcenterstage
        xzoom -1

    $ setWait(38.209,39.752)
    $ speak(MEGAN, "I wrote it, it's not ass!")
    $ setWait(39.752,40.586)
    $ speak(EMILY, "It's pretty ass.")
    $ setWait(40.586,42.714)
    $ speak(NICOLE, "It's J-Lo after her second kid ass.")
    $ setWait(42.714,44.298)
    $ speak(MEGAN, "Like you could write a better script.")
    $ setWait(44.298,46.092)
    $ speak(NICOLE, "Than this? I totally could.")
    $ setWait(46.092,47.427)
    $ speak(MEGAN, "About what?")
    $ setWait(47.427,58.771)
    $ speak(NICOLE, "About... A girl who's super power is all her insides are poisonous.\nSo if a guy molests her his eyes melt out of his head and he dies in a slow grueling pain.")
    show emily sc2 smile
    $ setWait(58.771,61.357)
    $ speak(EMILY, "So then he can't deny it, that's good.")
    $ setWait(61.357,65.486)
    $ speak(MEGAN, "Why wouldn't you just make it so her super power avoids getting molested altogether?")
    show nicole sc3 angry
    $ setWait(65.486,70.032)
    $ speak(NICOLE, "Who the fuck would wanna watch that? Her super power is nothing happens. Wow great movie idea.")
    $ setWait(70.032,72.452)
    $ speak(MEGAN, "Can you just keep reading? It's for a grade y'know.")
    show nicole sc3:
        xzoom 1

    show emily sc2

    $ setWait(72.452,75.496)
    $ speak(EMILY, "Whatever. \"My heart beats to love, not fight\"")
    show emily sc2 angry

    $ setWait(75.496,77.331)
    $ speak(EMILY, "--Who the fuck is this for??")
    $ setWait(77.331,79.876)
    $ speak(NICOLE, "It reads like the anime cartoons Jeffery likes.")
    show emily sc2
    $ setWait(79.876,81.252)
    $ speak(EMILY, "Who's Jeffery again?")
    $ setWait(81.252,84.297)
    $ speak(NICOLE, "He's the weird kid with glasses who draws pictures of girls he has crushes on.")
    $ setWait(84.297,86.174)
    $ speak(EMILY, "Oh he would like shit like this.")
    $ setWait(86.174,87.592)
    $ speak(MEGAN, "Guys I'm right here.")
    show nicole sc3:
        xzoom -1
    $ setWait(87.592,88.259)
    $ speak(NICOLE, "We know.")
    $ setWait(88.259,90.219)
    $ speak(MEGAN, "Can you get back to reading? I gotta grade your acting.")

    show nicole sc3:
        xzoom 1

    $ setWait(90.219,95.224)
    $ speak(NICOLE, "Oh my god. \"Your heart beats to march, cadet. Hut one two three four, hut one two three four.\"")

    show megan sc2

    $ setWait(95.224,96.058)
    $ speak(MEGAN, "Uh, Nicole.")
    show nicole sc3 angry:
        xzoom -1

    $ setWait(96.058,97.059)
    $ speak(NICOLE, "What? I'm reading.")
    $ setWait(97.059,102.482)
    $ speak(MEGAN, "It's like a drill sergeant. You read it like one, two, three, four.")
    $ setWait(102.482,108.321)
    $ speak(NICOLE, "Do I remotely look like I'm even in the same universe of giving a shit as you are?")
    $ setWait(108.321,110.865)
    $ speak(EMILY, "Besides we're the ones acting. Creative liberty.")
    show nicole sc3:
        xzoom 1

    $ setWait(110.865,111.616)
    $ speak(NICOLE, "Exactly.")
    $ setWait(111.616,112.95)
    $ speak(MEGAN, "Whatever, keep going.")
    $ setWait(112.95,116.788)
    $ speak(EMILY, "\"How can you march for someone else's death? I'll march this foot up your ass, ho.\"")
    show megan sc2 angry

    $ setWait(116.788,118.122)
    $ speak(MEGAN, "That's not what I wrote!")
    show nicole sc3 smile:
        xzoom -1
    $ setWait(118.122,119.04)
    $ speak(NICOLE, "Creative liberty.")
    $ setWait(119.04,120.458)
    $ speak(MEGAN, "Acting doesn't work like that.")
    show emily sc2 angry

    $ setWait(120.458,123.002)
    $ speak(EMILY, "You literally said acting's about creativity.")
    $ setWait(123.002,126.38)
    $ speak(NICOLE, "Yeah so is it about looks again? Maybe we should teach the class.")

    show emily sc2

    show megan sc2 angry:
        leftcenterstage
        xzoom 1
        linear 1.6 off_left

    $ setWait(126.38,128.382)
    $ speak(MEGAN, "F for the day!")
    show emily sc2 smile

    $ setWait(128.382,130.218)
    $ speak(EMILY, "Damn this class is easy.")
    stop ambient fadeout 1
    jump scene_0099
label scene_0099:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0099.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 1
    show crispin sc2:
        leftmidstage
        xzoom -1
        linear 2.4 off_right

    show emily sc2:
        xzoom -1
        centerstage
        linear 2 off_right

    show hunter sc1:
        xzoom -1
        rightcenterstage
        linear 1.5 off_right

    show nicole sc3:
        off_left
        linear 1.93 rightcenterstage

    $ setWait(0.084,1.669)
    $ speak(MEGAN, "...")
    show megan sc2 angry:
        xzoom -1
        off_left
        linear 1 leftstage

    $ setWait(1.669,2.378)
    $ speak(MEGAN, "Nicole.")
    show nicole sc3:
        xzoom -1
        rightcenterstage

    $ setWait(2.378,4.255)
    $ speak(NICOLE, "Dude the class is over, what do you want?")
    show megan sc2 angry:
        xzoom -1
        leftstage
        linear 2 leftcenterstage

    $ setWait(4.255,6.799)
    $ speak(MEGAN, "I just needed to have a little talk with you.")
    $ setWait(6.799,7.675)
    $ speak(NICOLE, "About?")
    $ setWait(7.675,12.221)
    $ speak(MEGAN, "Your participation today was a little concerning, gonna be honest.")
    $ setWait(12.221,14.473)
    $ speak(NICOLE, "Okay. Is that it or?")
    $ setWait(14.473,21.939)
    $ speak(MEGAN, "You're not getting it, I am your teacher in this class and you'll treat me as such. This disingenuous attitude isn't gonna fly in my program, got it?")
    show nicole sc3 angry:
        xzoom -1

    $ setWait(21.939,23.482)
    $ speak(NICOLE, "Dude what the fuck ever.")
    $ setWait(23.482,29.405)
    $ speak(MEGAN, "I just told you don't treat me like your classmate. I'm your teacher, is that how you talk to your teachers?")
    $ setWait(29.405,30.281)
    $ speak(NICOLE, "Actually yeah.")
    show megan sc2 angry:
        leftcenterstage
        xzoom -1
        linear 0.23 xalign 0.42
    $ setWait(30.281,31.157)
    $ speak(MEGAN, "Don't lie to me!")
    show nicole sc3 sad:
        rightcenterstage
        xzoom -1
    $ setWait(31.157,32.325)
    $ speak(NICOLE, "Oh my god chill out.")
    $ setWait(32.325,40.625)
    $ speak(MEGAN, "If you don't get your shit together I'm gonna call Miss Teagan and tell her everything. Then she's gonna write you up for in-school suspension. Still think it's all fun and games, Nicole?")
    $ setWait(40.625,44.045)
    $ speak(NICOLE, "Yeah sure. Side note, are you withdrawing from bipolar meds right now?")
    $ setWait(44.045,47.882)
    $ speak(MEGAN, "Don't change the subject, we're talking about you and your issues right now.")
    $ setWait(47.882,49.216)
    $ speak(NICOLE, "Jesus Christ okay.")
    $ setWait(49.216,52.47)
    $ speak(MEGAN, "Think you can just smirk while Emily calls me an ugly Hermione?")
    $ setWait(52.47,53.763)
    $ speak(NICOLE, "I had no part of that.")
    $ setWait(53.763,55.598)
    $ speak(MEGAN, "Go ahead, call me ugly again.")
    $ setWait(55.598,57.016)
    $ speak(NICOLE, "No thanks, can I go?")
    $ setWait(57.016,61.062)
    $ speak(MEGAN, "Aw see now you get it. Now you're treating me like your teacher.")
    $ setWait(61.062,62.021)
    $ speak(NICOLE, "Okay Megan.")
    $ setWait(62.021,63.314)
    $ speak(MEGAN, "It's Miss Megan.")
    show nicole sc3 angry
    $ setWait(63.314,65.858)
    $ speak(NICOLE, "Miss Megan can I get the fuck out of here now?")
    $ setWait(65.858,69.028)
    $ speak(MEGAN, "You're excused, sweetie. But work on that foul language.")
    show nicole sc3 angry:
        rightcenterstage
        xzoom 1
        linear 2 off_right

    $ setWait(69.028,71.447)
    $ speak(NICOLE, "Work on getting a fucking therapist holy shit.")
    stop ambient fadeout 1
    jump scene_0100
label scene_0100:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0100.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    scene cafeteria int 2
    show nicole sc3:
        leftcenterstage
        xzoom 1

    show jecka sc2 angry:
        rightcenterstage
        xzoom 1

    $ setWait(0.044,3.964)
    $ speak(JECKA, "So then she won't shut the fuck up over how special color TVs were.")
    $ setWait(3.964,5.007)
    $ speak(NICOLE, "Who was this again?")
    $ setWait(5.007,8.677)
    $ speak(JECKA, "The English sub today, she was so old and talkative.")
    $ setWait(8.677,10.387)
    $ speak(NICOLE, "At least you can go on your phone, right?")
    $ setWait(10.387,14.725)
    $ speak(JECKA, "That was the worst part, she'd stop her boring story to yell at anyone with their phone out.")
    $ setWait(14.725,17.603)
    $ speak(NICOLE, "A sub that won't let you screw around... What a ripoff.")
    show jecka sc2
    $ setWait(17.603,21.232)
    $ speak(JECKA, "I don't know how someone manages to be more boring than the regular shit.")
    $ setWait(21.232,23.776)
    $ speak(NICOLE, "Weird, yeah I had a sub today too.")
    $ setWait(23.776,24.652)
    $ speak(JECKA, "How'd that go?")
    $ setWait(24.652,28.864)
    $ speak(NICOLE, "The drama teacher nominated a student to teach the class while she's out of school.")
    $ setWait(28.864,29.74)
    $ speak(JECKA, "What the fuck.")
    $ setWait(29.74,31.575)
    $ speak(NICOLE, "I know, why would she pick a student, right?")
    $ setWait(31.575,33.285)
    $ speak(JECKA, "No-- Why are you in drama?")
    $ setWait(33.285,36.705)
    $ speak(NICOLE, "It's a gimme class. Don't worry I have no intention of being an actor.")
    show jecka sc2 angry

    $ setWait(36.705,41.919)
    $ speak(JECKA, "Good, the drama kids are so fucking annoying. They're all ugly yet somehow think they're gonna be in a movie one day.")
    $ setWait(41.919,46.048)
    $ speak(NICOLE, "Yeah that's pretty much the student-teacher, who's a massive bitch by the way.")
    show jecka sc2

    $ setWait(46.048,46.924)
    $ speak(JECKA, "Do I know her?")
    $ setWait(46.924,47.841)
    $ speak(NICOLE, "Do you know Megan?")
    $ setWait(47.841,50.344)
    $ speak(JECKA, "I was in second grade with her, why's she a bitch?")
    $ setWait(50.344,56.976)
    $ speak(NICOLE, "So I'm just doing whatever, not really caring, and then she stops me outside after class and gets super in my face about it.")
    show jecka sc2 worried

    $ setWait(56.976,58.894)
    $ speak(JECKA, "Cause you weren't acting good enough?")
    show nicole sc3 angry

    $ setWait(58.894,64.149)
    $ speak(NICOLE, "I guess, but she's like \"I'm gonna fuckin' write you up, get you suspended\" all this shit and I'm just standing there.")
    show jecka sc2
    $ setWait(64.149,66.318)
    $ speak(JECKA, "Ohhh that makes a lot of sense now.")
    show nicole sc3

    $ setWait(66.318,67.278)
    $ speak(NICOLE, "Sense how?")
    $ setWait(67.278,70.656)
    $ speak(JECKA, "She was a tantrum kid in second grade. Every week was a freakout.")
    $ setWait(70.656,73.033)
    $ speak(NICOLE, "Once a tantrum kid, always a tantrum kid.")
    $ setWait(73.033,76.412)
    $ speak(JECKA, "Yeah control freak for real. So are you gonna drop the class?")
    $ setWait(76.412,79.248)
    $ speak(NICOLE, "Nah I'm good. I'm gonna drop her ass though.")
    $ setWait(79.248,81.125)
    $ speak(JECKA, "Aren't you a little old for revenge?")
    show nicole sc3 angry

    $ setWait(81.125,82.626)
    $ speak(NICOLE, "Oh so now you're taking her side?")

    show jecka sc2 worried

    $ setWait(82.626,85.921)
    $ speak(JECKA, "No, no! I support you I'm just not getting involved.")
    $ setWait(85.921,87.423)
    $ speak(NICOLE, "Cause you have such a future, right?")
    show jecka sc2 angry

    $ setWait(87.423,88.924)
    $ speak(JECKA, "Apparently more than you.")
    show nicole sc3

    $ setWait(88.924,94.138)
    $ speak(NICOLE, "Future or no future, revenge is a dish best served cold... Like pizza.")
    show jecka sc2 worried

    $ setWait(94.138,96.89)
    $ speak(JECKA, "Wha-- ..Do you seriously eat pizza cold?")
    $ setWait(96.89,98.267)
    $ speak(NICOLE, "Yeah what's wrong with that?")
    show jecka sc2 angry

    $ setWait(98.267,100.102)
    $ speak(JECKA, "Now I know you're out of your fucking mind.")
    show nicole sc3 angry

    $ setWait(100.102,101.562)
    $ speak(NICOLE, "Hot pizza's just grease!")
    $ setWait(101.562,104.732)
    $ speak(JECKA, "There's grease in cold pizza, it's just solidified, schizo!")
    show nicole sc3

    $ setWait(104.732,106.567)
    $ speak(NICOLE, "Okay can we talk about this in the courtyard?")
    show jecka sc2

    $ setWait(106.567,107.318)
    $ speak(JECKA, "What for?")
    $ setWait(107.318,114.199)
    $ speak(NICOLE, "I'd prefer to be told I'm crazy outside where it's warm. Not in the mental ward-like cafeteria with freezing cold AC vents.")
    show nicole sc3:
        xzoom -1
        leftcenterstage
        linear 2.3 off_left

    show jecka sc2:
        rightcenterstage
        linear 2.8 off_left

    $ setWait(114.199,116.619)
    $ speak(JECKA, "Just hold your pizza up to one, you'll like it more.")
    stop ambient fadeout 1
    jump scene_0101
label scene_0101:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0101.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school courtyard
    show megan sc2 angry:
        leftstage
        xzoom -1

    show hunter sc1 sad:
        leftmidstage

    $ setWait(0.08,2.041)
    $ speak(MEGAN, "And you got the tickets, right?")
    $ setWait(2.041,3.876)
    $ speak(HUNTER, "Uh tickets for what?")
    $ setWait(3.876,7.296)
    $ speak(MEGAN, "Oh my god you really forgot again. The dinner theatre??")
    $ setWait(7.296,10.716)
    $ speak(HUNTER, "Oh yeah I can like order those tonight still.")
    $ setWait(10.716,12.676)
    $ speak(MEGAN, "Don't bother, I'll do it myself.")
    $ setWait(12.676,14.344)
    $ speak(HUNTER, "Sorry yeah okay.")
    $ setWait(14.344,17.598)
    $ speak(MEGAN, "If you were actually sorry you wouldn't have fucked it up the first time.")
    $ setWait(17.598,20.476)
    $ speak(HUNTER, "Yeah I'll try better next time.")
    show megan sc2 angry:
        xzoom 1
        leftstage
        linear 2 off_left

    show hunter sc1 sad:
        leftmidstage
        pause 0.5
        linear 2.2 off_left

    $ setWait(20.476,23.395)
    $ speak(MEGAN, "Stressed out enough teaching this class.")
    show nicole sc3:
        xzoom -1
        off_right
        linear 2.5 leftcenterstage

    show jecka sc2:
        off_right
        pause 0.4
        linear 2.3 rightcenterstage

    $ setWait(23.395,25.23)
    $ speak(NICOLE, "Does this bitch just yell at all her students?")
    $ setWait(25.23,26.774)
    $ speak(JECKA, "He's her student too?")
    show nicole sc3 surprised:
        xzoom 1
        leftcenterstage

    $ setWait(26.774,28.317)
    $ speak(NICOLE, "What do you mean \"student too\"?")
    $ setWait(28.317,30.027)
    $ speak(JECKA, "They're dating, you didn't know that?")
    show nicole sc3
    $ setWait(30.027,35.199)
    $ speak(NICOLE, "No but it checks out. I thought it was kinda weird he was the only one in class not making fun of her.")
    $ setWait(35.199,39.536)
    $ speak(JECKA, "I know for a fact he wants out of it too. He's flirted with like three of my friends so far.")
    $ setWait(39.536,42.623)
    $ speak(NICOLE, "Not surprising. A bitch like her? I'd cheat on her too.")
    $ setWait(42.623,47.169)
    $ speak(JECKA, "She's in that weird category of just barely pretty enough to be super demanding.")
    $ setWait(47.169,49.546)
    $ speak(NICOLE, "God the sex with her must be so bad.")
    $ setWait(49.546,53.842)
    $ speak(JECKA, "I don't even think he's getting that. She was raised Catholic like super prudish.")
    show nicole sc3 angry
    $ setWait(53.842,55.469)
    $ speak(NICOLE, "Do you just know everything about this bitch?")
    $ setWait(55.469,58.18)
    $ speak(JECKA, "What? I've been around longer, you just hear this shit.")
    show nicole sc3
    $ setWait(58.18,61.6)
    $ speak(NICOLE, "Alright don't worry about it.. Cause I think I have my in.")
    $ setWait(61.6,62.935)
    $ speak(JECKA, "In for what?")
    show nicole sc3 smile

    $ setWait(62.935,68.649)
    $ speak(NICOLE, "Megan's life.\nA boyfriend she isn't fucking is the perfect weakness for me to exploit.")
    show jecka sc2 worried

    $ setWait(68.649,71.11)
    $ speak(JECKA, "This is starting to sound like a RedTube video.")
    show nicole sc3 angry
    $ setWait(71.11,72.361)
    $ speak(NICOLE, "Ew I'm not gonna fuck him!")
    $ setWait(72.361,75.823)
    $ speak(JECKA, "Okay just checking, cause every video on there sounds exactly like that.")
    show nicole sc3
    $ setWait(75.823,76.74)
    $ speak(NICOLE, "Like what?")
    show jecka sc2
    $ setWait(76.74,83.288)
    $ speak(JECKA, "Like.. \"Oh you killed my parents. I'll show you with the most suffocating blowjob ever captured on video.\"")
    show nicole sc3 sad
    $ setWait(83.288,85.04)
    $ speak(NICOLE, "Dude how much RedTube do you watch?")
    $ setWait(85.04,86.041)
    $ speak(JECKA, "Don't worry about it.")
    show nicole sc3

    $ setWait(86.041,91.004)
    $ speak(NICOLE, "Fine but anyway, me and Hunter share a science class next period.")
    $ setWait(91.004,93.09)
    $ speak(JECKA, "That's convenient, what are you gonna do?")
    show nicole sc3 smile

    $ setWait(93.09,97.052)
    $ speak(NICOLE, "Let's just say I'm gonna... order a hot pizza.")
    show jecka sc2 smile

    $ setWait(97.052,99.555)
    $ speak(JECKA, "And wait for it to get cold?")
    $ setWait(99.555,101.723)
    $ speak(NICOLE, "You know me so well.")
    stop ambient fadeout 1
    jump scene_0102
label scene_0102:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0102.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 2
    show burleday 1:
        rightstage

    show hunter sc1:
        rightcenterstage
        xzoom -1

    show jeffery sc2:
        xzoom -1
        leftmidstage

    show nicole sc3:
        leftcenterstage

    $ setWait(0.035,3.747)
    $ speak(BURLEDAY, "And so that's why I wasn't super broken up...")
    $ setWait(3.747,8.502)
    $ speak(BURLEDAY, "...when my wife killed herself. Any questions?\n..Jeffery.")
    $ setWait(8.502,11.13)
    $ speak(JEFFERY, "Yeah what's our science lab gonna be about today?")
    show burleday 1 angry

    $ setWait(11.13,17.177)
    $ speak(BURLEDAY, "I meant questions about my wife killing herself??")
    $ setWait(17.177,19.263)
    $ speak(JEFFERY, "Oh sorry, no.")
    show burleday 1

    $ setWait(19.263,29.898)
    $ speak(BURLEDAY, "So for today's lab we'll be identifying which element is which based on its mass and volume. Get into your groups while I grab the supplies.")
    show burleday 1:
        xzoom -1
        rightstage
        linear 2 off_right

    show hunter sc1:
        xzoom 1
        rightcenterstage

    $ setWait(29.898,31.734)
    $ speak(HUNTER, "Aw my partner's out today.")
    show nicole sc3 sad

    $ setWait(31.734,34.612)
    $ speak(NICOLE, "Damn that sucks, are you gonna be okay?")
    $ setWait(34.612,38.657)
    $ speak(HUNTER, "Uh yeah I guess but it's gonna be bullshit effort doing it alone.")
    $ setWait(38.657,40.659)
    $ speak(NICOLE, "I could partner with you if you want.")
    $ setWait(40.659,42.786)
    $ speak(HUNTER, "Really? I thought you hated this class.")
    show nicole sc3 smile

    $ setWait(42.786,46.832)
    $ speak(NICOLE, "Well we're both in drama so it might help to know each other if we're gonna act.")
    $ setWait(46.832,48.876)
    $ speak(HUNTER, "I thought you hated that class too.")
    $ setWait(48.876,50.044)
    $ speak(NICOLE, "I'm warming up to it.")
    $ setWait(50.044,52.171)
    $ speak(JEFFERY, "But Nicole, I thought we were lab partners--")
    show nicole sc3 yell:
        xzoom -1
        leftcenterstage
    $ setWait(52.171,55.591)
    $ speak(NICOLE, "Shut up! Shut the fuck up! Go away!")

    show nicole sc3 angry

    show jeffery sc2:
        xzoom 1
        leftmidstage
        linear 3 off_left

    $ setWait(55.591,57.593)
    $ speak(JEFFERY, "Oh...")
    show hunter sc1 sad
    $ setWait(57.593,59.261)
    $ speak(HUNTER, "Wasn't that kinda harsh?")
    show nicole sc3 smile:
        leftcenterstage
        xzoom 1

    $ setWait(59.261,65.267)
    $ speak(NICOLE, "Yesterday he was telling me about how he kills dogs in his backyard, I can't work with someone like that.")
    show hunter sc1

    $ setWait(65.267,68.771)
    $ speak(HUNTER, "Huh.. okay I guess that was justified. Sit with me.")
    $ setWait(68.771,70.397)
    $ speak(NICOLE, "Cool.")
    show nicole sc3 flirt

    $ setWait(70.397,73.233)
    $ speak(NICOLE, "You don't mind if I look at porn on my phone, do you?")
    show hunter sc1 blush

    $ setWait(73.233,75.194)
    $ speak(HUNTER, "Uh... n-no.")
    $ setWait(75.194,79.782)
    $ speak(NICOLE, "Awesome yeah it's something I do when I'm bored. That's not TMI, is it?")
    $ setWait(79.782,85.913)
    $ speak(HUNTER, "I-I'm okay with it. But uh, why do you do it at school?")
    show nicole sc3 smile

    $ setWait(85.913,90)
    $ speak(NICOLE, "Kinda adds something to it, I don't know. So what are you doing after school?")
    show hunter sc1 sad
    $ setWait(90,95.339)
    $ speak(HUNTER, "I gotta go to the dentist for a cavity. They always make me gag with all those tools, I hate it.")
    $ setWait(95.339,96.34)
    $ speak(NICOLE, "Can't relate.")
    show hunter sc1
    $ setWait(96.34,97.716)
    $ speak(HUNTER, "You like the dentist??")
    $ setWait(97.716,101.22)
    $ speak(NICOLE, "What? No I meant gagging, I don't have a gag reflex.")
    $ setWait(101.22,103.138)
    $ speak(HUNTER, "Aw you're so lucky.")
    $ setWait(103.138,107.309)
    $ speak(NICOLE, "I don't think luck had anything to do with it, I like testing my limits.")
    show hunter sc1 blush
    $ setWait(107.309,109.978)
    $ speak(HUNTER, "Oh you mean like... uh...")
    show nicole sc3 flirt
    $ setWait(109.978,117.319)
    $ speak(NICOLE, "Yeah like that. But don't worry I know Megan's your girlfriend I won't cross any lines I'm just honest about myself.")
    $ setWait(117.319,119.238)
    $ speak(HUNTER, "H-Honesty's good, I don't mind it.")
    show nicole sc3 smile

    $ setWait(119.238,127.037)
    $ speak(NICOLE, "Sweet I think we'll get along just fine in drama. By the way I realized, you're technically dating your teacher. Ultimate fantasy, right?")
    show hunter sc1

    $ setWait(127.037,129.373)
    $ speak(HUNTER, "Um... I guess so.")
    $ setWait(129.373,133.001)
    $ speak(NICOLE, "She's an actor actor too, do you guys ever roleplay?")
    $ setWait(133.001,135.713)
    $ speak(HUNTER, "No, can't say we do...")
    $ setWait(135.713,139.007)
    $ speak(NICOLE, "I guess she's burned out after acting at school all day, right?")
    show hunter sc1 sad
    $ setWait(139.007,141.301)
    $ speak(HUNTER, "Yeah I guess you could say that.")
    $ setWait(141.301,143.595)
    $ speak(NICOLE, "But me personally, I love roleplaying.")
    show hunter sc1 smile
    $ setWait(143.595,146.181)
    $ speak(HUNTER, "Oh cool, what are some things you play?")
    show nicole sc3 surprised
    $ setWait(146.181,148.726)
    $ speak(NICOLE, "You have a girlfriend and you're asking me about my roleplaying?")
    show hunter sc1 blush
    $ setWait(148.726,150.644)
    $ speak(HUNTER, "Oh no no no I'm sorry! I didn't mean--")
    show nicole sc3 flirt
    $ setWait(150.644,159.611)
    $ speak(NICOLE, "Dude relax I'm fucking with you. Honestly you don't need to worry, I have a sixth sense for relationships and I can tell Megan's a lot of fun.")
    $ setWait(159.611,162.239)
    $ speak(HUNTER, "You can? How fun is she?")
    $ setWait(162.239,171.039)
    $ speak(NICOLE, "Okay don't tell her I told you this, but just based on her personality I can tell she gives amazing head. Am I right?")
    show hunter sc1 sad

    $ setWait(171.039,173.876)
    $ speak(HUNTER, "Uh your sixth sense might need some work.")
    show nicole sc3 sad

    $ setWait(173.876,176.92)
    $ speak(NICOLE, "Oh my god I was wrong? Is she really bad at it?")
    $ setWait(176.92,179.84)
    $ speak(HUNTER, "She doesn't really do any of that.")
    $ setWait(179.84,181.383)
    $ speak(NICOLE, "How long have you been dating?")
    $ setWait(181.383,182.634)
    $ speak(HUNTER, "Few months now.")
    $ setWait(182.634,189.183)
    $ speak(NICOLE, "Wow I'm really sorry you're in a relationship like that. Do you want my number in case you wanna vent or anything?")
    show hunter sc1
    $ setWait(189.183,197.691)
    $ speak(HUNTER, "Yeah okay I'll punch it in. Now that you mention it, the relationship does feel kinda manipulative sometimes.")
    show nicole sc3 smile
    $ setWait(197.691,204.364)
    $ speak(NICOLE, "And that's why I wanna be there for you. Cause trust me, I know all about manipulative relationships.")
    stop ambient fadeout 1
    jump scene_0103
label scene_0103:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0103.mp3")
    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene theatre 1
    show megan sc3:
        centerstage

    show nicole sc4:
        leftmidstage

    show emily sc3:
        leftstage
        xzoom -1

    show hunter sc2:
        rightmidstage

    show crispin sc3:
        rightstage

    $ setWait(0.036,6.793)
    $ speak(MEGAN, "Okay so again this is a romance improv, we're gonna need this to see who's best for our mini-production of Romeo & Juliet.")
    $ setWait(6.793,8.044)
    $ speak(CRISPIN, "Who's going first?")
    show megan sc3:
        xzoom -1

    $ setWait(8.044,11.548)
    $ speak(MEGAN, "Well we need a guy and a girl, Hunter why don't you go first.")
    $ setWait(11.548,12.966)
    $ speak(HUNTER, "Alright sure.")
    show megan sc3:
        xzoom 1
    $ setWait(12.966,16.094)
    $ speak(MEGAN, "Now who's gonna play the other side. Emily?")
    $ setWait(16.094,17.262)
    $ speak(EMILY, "This is for romance?")
    $ setWait(17.262,19.139)
    $ speak(MEGAN, "Yeah, romance improv.")
    show emily sc3 angry
    $ setWait(19.139,21.016)
    $ speak(EMILY, "No, he's ugly.")
    show nicole sc4 smile
    $ setWait(21.016,22.267)
    $ speak(NICOLE, "I'll do it.")
    show emily sc3
    $ setWait(22.267,23.226)
    $ speak(MEGAN, "Seriously?")
    $ setWait(23.226,25.687)
    $ speak(NICOLE, "Yeah I won't get better if I don't practice, right?")
    show megan sc3:
        centerstage
        xzoom 1
        linear 1.7 xalign 0.1
        xzoom -1

    show nicole sc4:
        leftmidstage
        xzoom 1
        pause 0.4
        linear 1.5 leftcenterstage

    show hunter sc2:
        rightmidstage
        pause 0.2
        linear 1.1 rightcenterstage

    $ setWait(25.687,26.98)
    $ speak(MEGAN, "Okay go ahead.")
    $ setWait(26.98,28.857)
    $ speak(HUNTER, "What's the scene again?")
    $ setWait(28.857,33.82)
    $ speak(MEGAN, "You're about to go to prison for ten years and this is your last conversation with your girlfriend.")
    $ setWait(33.82,35.53)
    $ speak(NICOLE, "Scandalous.")
    $ setWait(35.53,39.326)
    $ speak(HUNTER, "This might be the last time we ever talk face to face.")
    show nicole sc4 sad:
        leftcenterstage

    $ setWait(39.326,42.412)
    $ speak(NICOLE, "Are you sure? You'll beat the case, I know you will.")
    $ setWait(42.412,47.918)
    $ speak(HUNTER, "My lawyer said it's not looking good. If I'm lucky I'll get out in five for good behavior.")
    $ setWait(47.918,51.463)
    $ speak(NICOLE, "Well you're just gonna take that? You're free now aren't you?")
    $ setWait(51.463,52.339)
    $ speak(HUNTER, "What do you mean?")
    $ setWait(52.339,55.133)
    $ speak(NICOLE, "Let's run away to Mexico, they won't find you there.")
    $ setWait(55.133,59.888)
    $ speak(HUNTER, "I would but, this ankle monitor isn't doing me any favors.")
    $ setWait(59.888,61.223)
    $ speak(NICOLE, "Just cut it off.")
    $ setWait(61.223,63.266)
    $ speak(HUNTER, "I don't have any scissors.")
    $ setWait(63.266,67.687)
    $ speak(NICOLE, "Yeah okay that makes sense. So you're really just gonna serve the time?")
    $ setWait(67.687,69.064)
    $ speak(HUNTER, "No other options.")
    $ setWait(69.064,72.943)
    $ speak(NICOLE, "But what about me? What am I gonna do with myself without you?")
    $ setWait(72.943,76.238)
    $ speak(HUNTER, "Do you think you can wait for me on the outside?")
    $ setWait(76.238,80.534)
    $ speak(NICOLE, "I don't know, all your friends really wanna have sex with me.")
    $ setWait(80.534,86.623)
    $ speak(HUNTER, "Look I can't control you from the inside, just keep me in the dark about it.")
    $ setWait(86.623,90.377)
    $ speak(NICOLE, "You're giving up that easy? I thought you loved me.")
    $ setWait(90.377,92.003)
    $ speak(HUNTER, "I guess not enough.")
    show nicole sc4 angry
    $ setWait(92.003,100.303)
    $ speak(NICOLE, "You're just telling yourself that to feel less bad about missing me, but actions speak louder than words. Whenever you touch me I know the truth.")
    show hunter sc2 sad
    $ setWait(100.303,102.806)
    $ speak(HUNTER, "But... But what am I supposed to do??")
    show nicole sc4 sad
    $ setWait(102.806,109.271)
    $ speak(NICOLE, "Touch me one more time. Take me to my limit with your last night of freedom and don't ever forget the feeling!")
    show hunter sc2 blush
    $ setWait(109.271,110.73)
    $ speak(HUNTER, "Uh... Uh...")
    $ setWait(110.73,112.023)
    $ speak(MEGAN, "And scene!")
    show hunter sc2

    show nicole sc4:
        xzoom -1
        leftcenterstage

    $ setWait(112.023,113.692)
    $ speak(NICOLE, "Wha- We can't keep going?")
    $ setWait(113.692,116.82)
    $ speak(MEGAN, "That's enough, Nicole. Okay who else wants to try?")
    show nicole sc4:
        leftcenterstage
        xzoom 1
        linear 3 off_right
    $ setWait(116.82,119.155)
    $ speak(NICOLE, "Maybe a little too scandalous.")
    stop ambient fadeout 1
    jump scene_0104
label scene_0104:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0104.mp3")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    scene school int 1
    show crispin sc3:
        xzoom -1
        centerstage
        linear 2 off_right

    show emily sc3:
        rightcenterstage

    show nicole sc4:
        leftcenterstage

    show hunter sc2:
        xzoom -1
        leftmidstage
        linear 2.7 off_right


    $ setWait(0.036,3.247)
    $ speak(NICOLE, "Emily do you know where to buy Whip-Its without getting carded?")
    $ setWait(3.247,6.167)
    $ speak(EMILY, "Uhh no sorry, I don't even do Whip-Its.")
    $ setWait(6.167,9.212)
    $ speak(NICOLE, "Damn, cause you really look like a girl who does Whip-Its.")
    show emily sc3 smile:
        xzoom -1
        rightcenterstage
        linear 2.1 off_right

    $ setWait(9.212,11.13)
    $ speak(EMILY, "Oh my god thank you.")
    $ setWait(11.13,13.299)
    $ speak(NICOLE, "...Little weird she took that as a compliment.")

    show megan sc3:
        xzoom -1
        off_left
        linear 1 leftstage

    show nicole sc4:
        leftcenterstage
        pause 0.65
        xzoom -1

    $ setWait(13.299,15.259)
    $ speak(MEGAN, "Nicole I need another talk with you.")
    $ setWait(15.259,16.511)
    $ speak(NICOLE, "Shit I went overboard.")
    $ setWait(16.511,17.22)
    $ speak(MEGAN, "Over what?")
    $ setWait(17.22,19.514)
    $ speak(NICOLE, "Nothing, so what's the problem this time?")
    show megan sc3 smile:
        leftstage
        xzoom -1
        linear 1.5 leftmidstage

    $ setWait(19.514,26.896)
    $ speak(MEGAN, "Actually there's no problem at all. I just wanted to let you know I really appreciated the effort today.")
    show nicole sc4 surprised
    $ setWait(26.896,27.855)
    $ speak(NICOLE, "Seriously?")
    $ setWait(27.855,33.152)
    $ speak(MEGAN, "Yeah your scene with Hunter today showed a lot of passion and actually kinda moved me.")
    show nicole sc4
    $ setWait(33.152,38.866)
    $ speak(MEGAN, "It's like you were really trying to make him fall in love you. It showed a lot of talent.")
    $ setWait(38.866,41.536)
    $ speak(NICOLE, "Oh well... Okay thanks.")
    show megan sc3
    $ setWait(41.536,45.498)
    $ speak(MEGAN, "And Nicole I just wanted to say I'm really sorry for being so hard on you.")
    $ setWait(45.498,51.421)
    $ speak(MEGAN, "At first I thought you were just another disingenuous white kid taking drama cause it's easy, but you really care.")
    $ setWait(51.421,54.632)
    $ speak(NICOLE, "Yeah I guess, so thanks I'll see ya later, Megan.")
    $ setWait(54.632,55.967)
    $ speak(MEGAN, "Uh Nicole.")
    $ setWait(55.967,56.676)
    $ speak(NICOLE, "Yeah?")
    show megan sc3 angry
    $ setWait(56.676,59.637)
    $ speak(MEGAN, "I told you it's Miss Megan.")
    stop ambient fadeout 1
    jump scene_0105
label scene_0105:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.05):
        zoom 0.55 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.05 zoom 0.62 truecenter
    $ setVoiceTrack("audio/Scenes/0105.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home nicole int
    show nicole pj:
        leftcenterstage
        xzoom -1

    show jecka pj:
        rightcenterstage

    $ setWait(2.05,3.926)
    $ speak(JECKA, "You know WorldStarHipHop?")
    $ setWait(3.926,4.927)
    $ speak(NICOLE, "No what's that?")
    $ setWait(4.927,9.307)
    $ speak(JECKA, "It's this video site with nothing but Waffle House fights and butt implants gone wrong.")
    $ setWait(9.307,10.183)
    $ speak(NICOLE, "Butt implants?")
    $ setWait(10.183,14.395)
    $ speak(JECKA, "Yeah I don't get it either but when they screw it up it just slides around in their leg.")
    show nicole pj angry:
        xzoom 1
    $ setWait(14.395,15.521)
    $ speak(NICOLE, "Ew gross!")
    $ setWait(15.521,16.397)
    $ speak(JECKA, "Do you wanna see it?")
    show nicole pj angry:
        xzoom -1
    $ setWait(16.397,18.608)
    $ speak(NICOLE, "Yeah but later, I'm texting someone right now.")
    show jecka pj angry
    $ setWait(18.608,21.652)
    $ speak(JECKA, "You've been on the phone like all day, who are you talking to?")
    $ setWait(21.652,23.154)
    $ speak(NICOLE, "Little Caesar's Cold 'N Ready.")
    show jecka pj surprised

    $ setWait(23.154,26.074)
    $ speak(JECKA, "Oh I almost forgot, yeah how's it going with Megan's boyfriend?")
    $ setWait(26.074,29.243)
    $ speak(NICOLE, "I'm making some pretty good progress. And so far I got ten--")
    show nicole pj:
        xzoom 1
    $ setWait(29.243,31.037)
    $ speak(NICOLE, "Eleven pictures of his dick so far.")
    show jecka pj sad
    $ setWait(31.037,32.413)
    $ speak(JECKA, "God damn he's desperate.")
    $ setWait(32.413,36.167)
    $ speak(NICOLE, "Yeah but I'm trying to get one with his face in it too so I can prove it's him.")
    $ setWait(36.167,40.421)
    $ speak(JECKA, "Yeah or else that could be anyone's dick. But what if he's just tricking you with a picture of someone else?")
    show nicole pj angry
    $ setWait(40.421,44.384)
    $ speak(NICOLE, "Why would a guy carry around eleven angles of someone else's erection?")
    show jecka pj
    $ setWait(44.384,45.385)
    $ speak(JECKA, "He could be gay.")
    show nicole pj
    $ setWait(45.385,50.765)
    $ speak(NICOLE, "He's definitely not gay. No gay guy would skeet in mom's jewelry box for me.")
    show jecka pj sad

    $ setWait(50.765,56.229)
    $ speak(JECKA, "Uh, why... Would he do that... In his mom's jewelry box?")
    $ setWait(56.229,61.401)
    $ speak(NICOLE, "I told him it would really turn me on and within 90 seconds he sent a picture of it. You wanna see?")
    $ setWait(61.401,63.611)
    $ speak(JECKA, "Ugh... Yes.")
    show sext onlayer screens:
        alpha 0.0
        pause 0.7
        alpha 1.0
    $ setWait(63.611,64.237)
    $ speak(NICOLE, "Look at this.")
    $ setWait(64.237,66.364)
    $ speak(JECKA, "Jesus Christ it's like filled up!")
    $ setWait(66.364,68.074)
    $ speak(NICOLE, "Pearl necklace on a pearl necklace.")
    $ setWait(68.074,69.7)
    $ speak(JECKA, "What's that thing in the bottom corner?")
    $ setWait(69.7,70.576)
    $ speak(NICOLE, "That's the head.")
    hide sext onlayer screens
    show jecka pj angry:
        rightcenterstage
        linear 0.35 rightstage

    $ setWait(70.576,73.413)
    $ speak(JECKA, "Ew uncircumcised!! That's disgusting get it away!")
    $ setWait(73.413,75.957)
    $ speak(NICOLE, "You thought he'd send eleven pics of a photogenic dick?")
    $ setWait(75.957,79.293)
    $ speak(JECKA, "I'm gonna throw up, uncircumcised men should fucking kill themselves!")
    $ setWait(79.293,80.962)
    $ speak(NICOLE, "Maybe that's why he won't include his face.")
    show jecka pj angry:
        rightstage
        linear 1.2 rightcenterstage

    $ setWait(80.962,84.382)
    $ speak(JECKA, "Well you better figure something out quick before he breaks up with her to go for you.")
    show nicole pj surprised
    $ setWait(84.382,89.178)
    $ speak(NICOLE, "Shit you're right, then it wouldn't be cheating anymore, meaning it wouldn't hurt Megan anymore.")
    show jecka pj:
        rightcenterstage

    $ setWait(89.178,95.226)
    $ speak(JECKA, "Meaning you flirted with this guy for literally nothing.\nAs it stands now, you're technically into him.")
    show nicole pj angry

    $ setWait(95.226,97.311)
    $ speak(NICOLE, "I cannot let that happen.")
    stop ambient fadeout 1.2
    jump scene_0106
label scene_0106:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0106.mp3")
    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    scene classroom int 2
    show hunter sc3:
        rightcenterstage

    show nicole sc6:
        leftcenterstage

    $ setWait(0.037,4.583)
    $ speak(HUNTER, "So um do we divide the mass by the volume?")
    $ setWait(4.583,6.377)
    $ speak(NICOLE, "Couldn't tell ya.")
    $ setWait(6.377,10.214)
    $ speak(HUNTER, "Or maybe we multiply the density by the mass...")
    $ setWait(10.214,12.967)
    $ speak(NICOLE, "Dude I'm failing this class anyway, who gives a shit?")
    $ setWait(12.967,15.386)
    $ speak(HUNTER, "Is something bothering you right now?")
    $ setWait(15.386,19.848)
    $ speak(NICOLE, "Not really it's just, caring about science is for white guys who correct your grammar.")
    $ setWait(19.848,25.187)
    $ speak(HUNTER, "Oh right. Actually there's sorta been something I've been thinking about lately.")
    $ setWait(25.187,26.689)
    $ speak(NICOLE, "Oh you don't correct my grammar.")
    show hunter sc3 sad
    $ setWait(26.689,30.234)
    $ speak(HUNTER, "No not that, just... us?")
    show nicole sc6 flirt
    $ setWait(30.234,33.946)
    $ speak(NICOLE, "What about us? I had fun texting last night, did you not like it?")
    show nicole sc6
    $ setWait(33.946,44.999)
    $ speak(HUNTER, "No I liked it too it's just... I think about how I feel talking to you, and compare it with talking to Megan, and I don't think she actually likes me.")
    show nicole sc6 sad

    $ setWait(44.999,46.625)
    $ speak(NICOLE, "What? How so?")
    $ setWait(46.625,52.089)
    $ speak(HUNTER, "She just doesn't humor me the way you do, it doesn't feel like she actually loves me.")
    show nicole sc6
    $ setWait(52.089,55.05)
    $ speak(NICOLE, "Are you sure? I think you could stick it out a little longer.")
    $ setWait(55.05,64.226)
    $ speak(HUNTER, "I could but I don't really want to. It's no fun being with some bossy prude. If she liked me for me she would've done something by now.")
    show nicole sc6 smile
    $ setWait(64.226,70.441)
    $ speak(NICOLE, "Hey now I don't think that's necessarily true. She just needs time and you gotta be there when she's ready.")
    $ setWait(70.441,74.778)
    $ speak(HUNTER, "Even so though, aren't I cheating on her if I keep this up with you?")
    show nicole sc6
    $ setWait(74.778,76.238)
    $ speak(NICOLE, "Keep what up?")
    $ setWait(76.238,78.574)
    $ speak(HUNTER, "Like sending you all those pictures.")
    show nicole sc6 smile
    show burleday 2:
        off_left
        xzoom -1
        linear 2.9 leftmidstage
    $ setWait(78.574,80.534)
    $ speak(NICOLE, "You mean when you came in your Mom's jewelry box?")

    show hunter sc3



    show nicole sc6 surprised:
        leftcenterstage
        pause 0.2
        xzoom -1
        linear 0.08 xalign 0.38
        linear 0.08 xalign 0.36
        linear 0.08 xalign 0.38
        linear 0.08 leftcenterstage

    $ setWait(80.534,82.036)
    $ speak(BURLEDAY, "Did anyone need my help over here?")
    $ setWait(82.036,83.454)
    $ speak(HUNTER, "Yeah actually for the--")
    show nicole sc6:
        leftcenterstage
        xzoom -1

    $ setWait(83.454,85.205)
    $ speak(NICOLE, "No we're fine, just thinking!")
    $ setWait(85.205,86.29)
    $ speak(BURLEDAY, "Okay.")
    show burleday 2:
        leftmidstage
        xzoom 1
        linear 3 off_left

    $ setWait(86.29,89.835)
    $ speak(BURLEDAY, "Jeffery could you draw a better picture of my dead wife?")
    show nicole sc6 smile:
        leftcenterstage
        xzoom 1

    $ setWait(89.835,91.253)
    $ speak(NICOLE, "But yeah the jewelry box?")
    $ setWait(91.253,93.922)
    $ speak(HUNTER, "Yeah, among others.")
    $ setWait(93.922,95.758)
    $ speak(NICOLE, "That was really hot by the way.")
    $ setWait(95.758,100.554)
    $ speak(HUNTER, "You really thought so? I had another one like that but I forgot to send it.")
    show nicole sc6
    $ setWait(100.554,101.847)
    $ speak(NICOLE, "Another jewelry box?")
    $ setWait(101.847,106.31)
    $ speak(HUNTER, "No it was on my brother's Uno collection.")
    show nicole sc6 surprised

    $ setWait(106.31,108.979)
    $ speak(NICOLE, "L-like... Like Uno the restaurant?")
    $ setWait(108.979,111.023)
    $ speak(HUNTER, "No, Uno the card game.")
    show nicole sc6

    $ setWait(111.023,114.526)
    $ speak(NICOLE, "Oh. How can you have a collection of Uno?")
    $ setWait(114.526,120.365)
    $ speak(HUNTER, "Like all the different versions. NFL Uno, Batman Uno, Simpsons Uno.")
    $ setWait(120.365,124.453)
    $ speak(NICOLE, "And you just put 'em all together and blew a fat load on 'em?")
    show hunter sc3 blush

    $ setWait(124.453,130.751)
    $ speak(HUNTER, "Yeah and while I was doing it I was thinking about you and-- oh god listen to me.")
    $ setWait(130.751,134.296)
    $ speak(NICOLE, "What's wrong? We're just having a normal conversation.")
    show hunter sc3 sad
    $ setWait(134.296,138.05)
    $ speak(HUNTER, "Megan has no idea we're doing this, it feels kinda messed up.")
    show nicole sc6 smile

    $ setWait(138.05,149.478)
    $ speak(NICOLE, "Look it's perfectly okay, just think about it like this. Your relationship with her is a long term romance kinda thing like dating and whatever, she really loves you but needs time for the rest of it.")
    $ setWait(149.478,152.648)
    $ speak(HUNTER, "Well yeah, but the time is killing me.")
    show nicole sc6 flirt

    $ setWait(152.648,157.402)
    $ speak(NICOLE, "And if time's the issue, you just need a friend to kill time with.")
    $ setWait(157.402,159.071)
    $ speak(HUNTER, "But what would Megan think?")
    $ setWait(159.071,168.539)
    $ speak(NICOLE, "Megan doesn't need to know. If she won't explore your urges there's nothing wrong with finding someone who will. Besides it's only cheating if you say you love me.")
    show hunter sc3 blush

    $ setWait(168.539,169.748)
    $ speak(HUNTER, "Seriously?")
    $ setWait(169.748,178.048)
    $ speak(NICOLE, "Yeah that's been the rule since forever. As long as we don't kiss and do all that mushy stuff we can hang out however we want.")
    $ setWait(178.048,181.426)
    $ speak(HUNTER, "Man that's pretty cool, I never looked at it like that.")
    $ setWait(181.426,185.055)
    $ speak(NICOLE, "That's what I'm here for... So are you doing anything tonight?")
    show hunter sc3

    $ setWait(185.055,187.766)
    $ speak(HUNTER, "Actually I wanted to invite you to something.")
    $ setWait(187.766,189.268)
    $ speak(NICOLE, "For real? What is it?")
    $ setWait(189.268,193.522)
    $ speak(HUNTER, "Do you wanna go to church with me this Saturday? Megan cancelled on me.")
    show nicole sc6 surprised
    $ setWait(193.522,195.315)
    $ speak(NICOLE, "I-I'm sorry, church?")
    show hunter sc3 smile
    $ setWait(195.315,202.865)
    $ speak(HUNTER, "Yeah it's a parking lot function with food and games, but also little ceremonies in the middle to appreciate the lord.")
    $ setWait(202.865,205.659)
    $ speak(NICOLE, "The lord... Like Jesus?")
    $ setWait(205.659,207.619)
    $ speak(HUNTER, "Yeah the one and only.")
    show nicole sc6
    $ setWait(207.619,211.29)
    $ speak(NICOLE, "So you snap pictures of your penis while frequenting a church?")
    show hunter sc3

    $ setWait(211.29,214.751)
    $ speak(HUNTER, "Yeah I know but that's what confession's for, right?")
    $ setWait(214.751,218.672)
    $ speak(NICOLE, "And you're gonna tell a priest you came in your mom's jewelry box?")
    $ setWait(218.672,224.386)
    $ speak(HUNTER, "Yeah I'll have to this Sunday, huh? Go in blind and just \"forgive me father for I have sinned\".")
    $ setWait(224.386,230.976)
    $ speak(NICOLE, "So you're telling me you blindly say to a guy all the sex shit you did over the week and call him father but not daddy?")
    $ setWait(230.976,234.188)
    $ speak(HUNTER, "Wha- I don't... What do you mean?")
    show nicole sc6 sad
    $ setWait(234.188,235.355)
    $ speak(NICOLE, "Sorry, RedTube.")
    $ setWait(235.355,237.9)
    $ speak(HUNTER, "What's-- ...So you wanna go?")
    show nicole sc6 surprised:
        xzoom -1

    $ setWait(237.9,243.864)
    $ speak(LYNN, "Nicole, please report to the counselor's office. Repeat Nicole, please report to the counselor's office. Thank you.")
    show nicole sc6:
        leftcenterstage
        xzoom 1
        pause 1.8
        xzoom -1
        linear 1.1 off_left

    $ setWait(243.864,247.034)
    $ speak(NICOLE, "Looks like I gotta go, I'll get back to you on that though.")
    show hunter sc3 smile

    $ setWait(247.034,249.203)
    $ speak(HUNTER, "Just lemme know by Friday.")
    stop ambient fadeout 1
    jump scene_0107
label scene_0107:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0107.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 1
    show counselor 2 smile:
        rightmidstage

    show nicole sc6:
        off_left
        linear 1.2 leftmidstage

    $ setWait(0.037,4.291)
    $ speak(NICOLE, "This is the first time being here is less awkward than where I just was.")
    $ setWait(4.291,7.795)
    $ speak(COUNSELOR, "Nicole, hope I'm not interrupting too much with your class.")
    $ setWait(7.795,10.089)
    $ speak(NICOLE, "It was actually the perfect amount of interruption.")
    $ setWait(10.089,13.55)
    $ speak(COUNSELOR, "Regardless I wouldn't want to knock you off of your newfound drive.")
    $ setWait(13.55,14.259)
    $ speak(NICOLE, "Driving where?")
    $ setWait(14.259,18.889)
    $ speak(COUNSELOR, "I meant your effort, your sudden passion for scholastic participation.")

    show nicole sc6 angry:
        leftmidstage

    $ setWait(18.889,22.017)
    $ speak(NICOLE, "Since when-- did you just lie to get me in here?")
    $ setWait(22.017,30.442)
    $ speak(COUNSELOR, "Of course not. You're saying that you haven't gone the extra mile in theatre and science lately? Your teachers in both spoke very highly of you.")
    show nicole sc6 surprised
    $ setWait(30.442,32.194)
    $ speak(NICOLE, "Oh... They have?")
    $ setWait(32.194,43.122)
    $ speak(COUNSELOR, "Yes, they're both very impressed with your sudden initiative when it comes to participating in the classroom. Quite frankly it's pleasantly surprising to hear given your prior reputation.")
    $ setWait(43.122,48.085)
    $ speak(COUNSELOR, "As your counselor it'd be important to know, what's the sudden inspiration?")
    show nicole sc6
    $ setWait(48.085,52.714)
    $ speak(NICOLE, "Oh um, drama and science? Couldn't tell ya. I'm just really smart I guess.")
    $ setWait(52.714,58.512)
    $ speak(COUNSELOR, "Well either way, great to see one of our most beautiful students isn't just a pretty face.")
    show nicole sc6 angry
    $ setWait(58.512,60.848)
    $ speak(NICOLE, "What a great opinion to have of a teenage girl.")
    $ setWait(60.848,65.894)
    $ speak(COUNSELOR, "Not to mention a daring fashion sense. You have a knack for turning heads, don't you?")
    $ setWait(65.894,67.563)
    $ speak(NICOLE, "Whoa now you're really flirting.")
    $ setWait(67.563,75.07)
    $ speak(COUNSELOR, "Nothing flirtatious about admiring a creative mind. You picked out such vibrant shorts, they shape you out very nicely.")
    $ setWait(75.07,77.489)
    $ speak(NICOLE, "Sorry I'll try not to show off next time.")
    $ setWait(77.489,83.537)
    $ speak(COUNSELOR, "Nonsense, you're more than welcome to show off in here. Why don't you give me a twirl?")
    show nicole sc6 sad

    $ setWait(83.537,85.914)
    $ speak(NICOLE, "You're literally 40 why do you wanna see my ass??")
    $ setWait(85.914,92.337)
    $ speak(COUNSELOR, "Now Nicole it's not about that, just to admire you as a whole.\nNow go ahead and give me that twirl.")
    show nicole sc6 angry
    $ setWait(92.337,94.923)
    $ speak(NICOLE, "Dude I'm white there's nothing to see anyway, can I go now!?")
    show counselor 2 smile:
        rightmidstage
        pause 3.2
        linear 2.3 centerstage

    $ setWait(94.923,100.22)
    $ speak(COUNSELOR, "Oh now that sounds like a low self-esteem. If I could volunteer a few more compliments--")
    show nicole sc6 angry:
        leftmidstage
        linear 3 leftstage
        linear 0.27 off_left

    $ setWait(100.22,103.765)
    $ speak(NICOLE, "I'm gonna go while I can still voluntarily leave, bye!")
    stop ambient fadeout 1
    jump scene_0108
label scene_0108:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0108.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school courtyard
    show nicole sc6:
        leftcenterstage

    show jecka sc4:
        off_right
        linear 1.3 rightcenterstage

    $ setWait(0.039,2.166)
    $ speak(JECKA, "I got your text, sorry I was caught up.")
    $ setWait(2.166,3)
    $ speak(NICOLE, "What happened?")
    $ setWait(3,7.171)
    $ speak(JECKA, "I was in French 2 and called the weird kid \"Rugrats fetish\" and got held after.")
    show nicole sc6 surprised
    $ setWait(7.171,8.923)
    $ speak(NICOLE, "Like Rugrats the cartoon?")
    $ setWait(8.923,9.548)
    $ speak(JECKA, "Yeah.")
    show nicole sc6
    $ setWait(9.548,11.05)
    $ speak(NICOLE, "That's a really good diss.")
    show jecka sc4 angry

    $ setWait(11.05,18.682)
    $ speak(JECKA, "I know, everybody laughed and the teacher made both of us stay after for me to apologize to him. But then after that I was forced to say three nice things about him.")
    $ setWait(18.682,20.309)
    $ speak(NICOLE, "While he was there to his face?")
    $ setWait(20.309,21.894)
    $ speak(JECKA, "Yeah, talk about awk as fuck.")
    $ setWait(21.894,25.648)
    $ speak(NICOLE, "That's literally cruel and unusual punishment. What'd you even say?")
    show jecka sc4 sad
    $ setWait(25.648,29.485)
    $ speak(JECKA, "One of 'em was \"you don't smell that bad\" like I had no idea what to say.")
    $ setWait(29.485,34.782)
    $ speak(NICOLE, "Did he get turned on while you did it? Like think of how often a regular girl would say something nice to him.")
    $ setWait(34.782,36.116)
    $ speak(JECKA, "Was trying to block that out.")
    $ setWait(36.116,39.245)
    $ speak(NICOLE, "When he gets home he's going straight for your Facebook summer photos.")
    $ setWait(39.245,42.665)
    $ speak(JECKA, "Shit and I forgot my password too. So what were you freaking out about?")
    $ setWait(42.665,43.874)
    $ speak(NICOLE, "Megan's boyfriend.")
    show jecka sc4
    $ setWait(43.874,45.376)
    $ speak(JECKA, "I thought you said the counselor was horny.")
    $ setWait(45.376,50.005)
    $ speak(NICOLE, "Oh that's like every week I'm already over that, but no her boyfriend is out of his fucking mind.")
    $ setWait(50.005,53.092)
    $ speak(JECKA, "Well yeah he sent eleven dick pics for nothing back, no shit.")
    show nicole sc6 angry

    $ setWait(53.092,56.47)
    $ speak(NICOLE, "No.. he invited me to church this Saturday.")
    $ setWait(56.47,57.763)
    $ speak(JECKA, "Isn't church on Sunday?")
    $ setWait(57.763,61.642)
    $ speak(NICOLE, "He's so involved with the church he goes more than just Sunday.")
    $ setWait(61.642,65.229)
    $ speak(JECKA, "Oh he's one of those those. Is it really that surprising though?")
    $ setWait(65.229,71.235)
    $ speak(NICOLE, "I didn't think a guy who cheats on his girlfriend and photographs his dick would have a strong relationship with Jesus I guess!")
    $ setWait(71.235,76.657)
    $ speak(JECKA, "Oh yeah no I've seen it. \"I would so get off to your pictures if it wasn't for my faith in God.\" Like okay thanks.")
    $ setWait(76.657,78.867)
    $ speak(NICOLE, "How'd you even get that far with a guy so religious?")
    show jecka sc4 angry
    $ setWait(78.867,83.914)
    $ speak(JECKA, "That's when I found out, like what the fuck do I say? I didn't know Jesus was the escrow in titty pics.")
    show nicole sc6
    $ setWait(83.914,86.292)
    $ speak(NICOLE, "Who even is Jesus anymore anyway?")
    show jecka sc4
    $ setWait(86.292,89.336)
    $ speak(JECKA, "Someone pedophiles find to say they're not pedophiles anymore.")
    $ setWait(89.336,91.255)
    $ speak(NICOLE, "You think our counselor will ever find Jesus?")
    $ setWait(91.255,94.341)
    $ speak(JECKA, "Yeah if Jesus is a 15 year old girl wearing Juicy Couture.")
    $ setWait(94.341,99.513)
    $ speak(NICOLE, "High hopes.\nSo I guess I'll just go to a really awkward drama class tomorrow.")
    $ setWait(99.513,100.806)
    $ speak(JECKA, "How are you gonna tell him no?")
    $ setWait(100.806,109.106)
    $ speak(NICOLE, "You just distract him.\n\"Hey so I can't go to church but you know what I do wanna do? You know what I wanna do really fucking badly?\"")
    show jecka sc4 smile
    $ setWait(109.106,110.649)
    $ speak(JECKA, "That was cool, how do you do that?")
    $ setWait(110.649,113.652)
    $ speak(NICOLE, "Dude 90 percent of dirty talk is just rhetorical questions.")
    stop ambient fadeout 1
    jump scene_0109
label scene_0109:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0109.mp3")
    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene theatre 1
    show megan sc4:
        rightstage

    show emily sc4:
        leftstage
        xzoom -1

    show crispin sc4:
        rightcenterstage
        xzoom -1

    show hunter sc1:
        leftcenterstage
        xzoom -1

    show nicole sc6:
        leftmidstage

    $ setWait(0.044,7.468)
    $ speak(MEGAN, "So like I warned last week, here's my casting for the school's Romeo & Juliet production. Let's see for Romeo we have...")
    $ setWait(7.468,9.344)
    $ speak(EMILY, "Wait they made a play about Romeo?")
    show megan sc4 angry
    $ setWait(9.344,11.597)
    $ speak(MEGAN, "Uh yeah Romeo's the lead character.")
    show emily sc4 upset
    $ setWait(11.597,14.767)
    $ speak(EMILY, "Isn't that Master P's kid? Why'd you take the \"little\" out of his name?")
    $ setWait(14.767,19.563)
    $ speak(MEGAN, "No as in Romeo Montague! It's Shakespeare, we studied this all month!")
    $ setWait(19.563,22.191)
    $ speak(CRISPIN, "So it's not Lil' Romeo and Juliet then?")
    $ setWait(22.191,23.108)
    $ speak(NICOLE, "Yeah what the fuck?")
    show emily sc4
    $ setWait(23.108,28.489)
    $ speak(MEGAN, "Enough!\nSo, playing the part of Romeo is Hunter, congratulations.")
    $ setWait(28.489,30.407)
    $ speak(HUNTER, "Oh thanks.")
    $ setWait(30.407,34.078)
    $ speak(MEGAN, "A little more excitement? Can we applaud the castings?")
    show hunter sc1 smile:
        xzoom 1

    $ setWait(34.078,36.58)
    $ speak(HUNTER, "Yeah yay thanks guys.")
    show hunter sc1:
        xzoom -1

    show megan sc4

    $ setWait(36.58,38.999)
    $ speak(MEGAN, "And playing the role of Juliet will be...")
    show emily sc4 sad
    $ setWait(38.999,40.084)
    $ speak(EMILY, "Not me, not me, not me...")
    $ setWait(40.084,40.667)
    $ speak(MEGAN, "Nicole!")
    show emily sc4
    $ setWait(40.667,41.752)
    $ speak(EMILY, "Oh thank god.")
    show nicole sc6 surprised
    $ setWait(41.752,42.795)
    $ speak(NICOLE, "Seriously??")
    show megan sc4 smile
    $ setWait(42.795,50.844)
    $ speak(MEGAN, "Yeah you earned it. I know we got off to a rocky start but your on-stage synergy with Hunter has really blown my mind. I can't think of anyone better for the part.")
    show hunter sc1 smile:
        xzoom 1
    $ setWait(50.844,53.43)
    $ speak(HUNTER, "I'll text you about rehearsal later tonight, Nicole.")
    show nicole sc6 smile
    $ setWait(53.43,54.64)
    $ speak(NICOLE, "Cool yeah sure.")
    $ setWait(54.64,59.228)
    $ speak(MEGAN, "For a pairing like this, communication is everything. Good luck you guys, you're gonna need it.")
    $ setWait(59.228,60.729)
    $ speak(NICOLE, "Oh you too.")
    stop ambient fadeout 1
    jump scene_0110
label scene_0110:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.252):
        zoom 0.55 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 0.62 truecenter
    $ setVoiceTrack("audio/Scenes/0110.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home nicole int
    show nicole sc6 angry:
        centerstage
    $ setWait(0.046,2.715)
    $ speak(NICOLE, "No I don't wanna talk about the fucking script, just send the shit.")
    show gamer_brother:
        off_left
        xzoom -1
        linear 1.5 leftmidstage

    $ setWait(2.715,3.674)
    $ speak(GAMER_BROTHER, "What's going on?")
    show nicole sc6 surprised:
        xzoom -1
    $ setWait(3.674,4.3)
    $ speak(NICOLE, "Nothing!")
    show gamer_brother smile:
        leftmidstage
    $ setWait(4.3,7.97)
    $ speak(GAMER_BROTHER, "Aw dude that does not sound like nothing. Who ya texting?")
    show nicole sc6 angry:
        xzoom -1
    $ setWait(7.97,8.763)
    $ speak(NICOLE, "A guy.")
    $ setWait(8.763,10.64)
    $ speak(GAMER_BROTHER, "Whoa a guy? Is it getting serious?")
    $ setWait(10.64,12.6)
    $ speak(NICOLE, "Ew I'm not having this conversation with you!")
    $ setWait(12.6,14.393)
    $ speak(GAMER_BROTHER, "Is he asking for ass pics or something?")
    $ setWait(14.393,15.228)
    $ speak(NICOLE, "Can you not?")
    $ setWait(15.228,20.191)
    $ speak(GAMER_BROTHER, "I can give you the ass pics trump card if you wanna know it, just so you see it coming if he tries using it.")
    $ setWait(20.191,21.567)
    $ speak(NICOLE, "What trump card?")
    $ setWait(21.567,28.324)
    $ speak(GAMER_BROTHER, "Oh it's real simple. If any girl's holding out on me, I just make it about trust and how I'll kill myself if she doesn't trust me.")
    $ setWait(28.324,30.618)
    $ speak(NICOLE, "Wha-- there's no way that works.")
    $ setWait(30.618,34.122)
    $ speak(GAMER_BROTHER, "No like it works every-- well not every time but like 10 percent of the time.")
    $ setWait(34.122,39.46)
    $ speak(NICOLE, "What girl would respond emotionally enough to a suicidal guy begging to jack off to her?")
    show gamer_brother
    $ setWait(39.46,43.297)
    $ speak(GAMER_BROTHER, "Well you're a sociopath you don't respond emotionally to anything, you wouldn't get it.")
    $ setWait(43.297,44.507)
    $ speak(NICOLE, "Get the fuck outta here.")
    show gamer_brother smile
    $ setWait(44.507,49.637)
    $ speak(GAMER_BROTHER, "Okay suit yourself. But in case you fall for it, the light's really good in the bathroom.")
    $ setWait(49.637,51.18)
    $ speak(NICOLE, "You're my brother.")
    $ setWait(51.18,52.14)
    $ speak(GAMER_BROTHER, "Yeah?")
    $ setWait(52.14,55.351)
    $ speak(NICOLE, "Why would you care about the quality of my ass pics?")
    show gamer_brother:
        leftmidstage
        xzoom -1
        pause 1.45
        xzoom 1
        linear 0.6 off_farleft

    $ setWait(55.351,58.104)
    $ speak(GAMER_BROTHER, "Uh no it's uh, I gotta go!")
    show nicole sc6
    $ setWait(58.104,61.023)
    $ speak(NICOLE, "They had to teach us about ancient Greece in school...")
    show text_stillthere onlayer screens:
        alpha 1.0
        pause 1.45 alpha 0.0

    show nicole sc6 angry

    $ setWait(61.023,65.57)
    $ speak(NICOLE, "\"Are you still there\"--Yeah I'm still here it's been 45 seconds, asshole.")
    hide text_stillthere onlayerscreens

    show nicole sc6

    $ setWait(65.57,70.032)
    $ speak(NICOLE, "Haven't gotten anywhere on this full body pic... But let's try idiot's way.")
    show nicole sc6 behind black:
        xzoom 1
    stop ambient fadeout 9.8
    show black:
        alpha 0.0
        pause 5.2
        linear 3 alpha 1.0
    $ setWait(70.032,80.084)
    $ speak(NICOLE, "Do you not trust me? I just wanna see you all in one picture because it would be really really...")

    jump scene_0111
label scene_0111:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0111.mp3")
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene school ext 4
    show jecka sc5:
        rightmidstage

    show nicole sc7 surprised:
        off_left
        linear 1.6 centerstage

    $ setWait(1.998,2.791)
    $ speak(NICOLE, "I got 'em!")
    show jecka sc5 sad
    $ setWait(2.791,3.458)
    $ speak(JECKA, "Got what?")
    show nicole sc7 angry
    $ setWait(3.458,4.71)
    $ speak(NICOLE, "You know what!")
    show jecka sc5 smile

    $ setWait(4.71,5.585)
    $ speak(JECKA, "Blink tickets?")

    $ setWait(5.585,7.879)
    $ speak(NICOLE, "They're not even together anymore! The pictures??")
    show jecka sc5
    $ setWait(7.879,10.841)
    $ speak(JECKA, "Oh yeah for the revenge you're still plotting, how's that going?")
    show nicole sc7 smile

    $ setWait(10.841,14.469)
    $ speak(NICOLE, "Let's just say I have the key ingredient.")
    show jecka sc5 surprised
    $ setWait(14.469,17.097)
    $ speak(JECKA, "He really sent you a picture with just everything in it?")
    $ setWait(17.097,22.102)
    $ speak(NICOLE, "He sent a lot of pictures with everything in it. After the first one the floodgates just open.")
    show jecka sc5
    $ setWait(22.102,25.021)
    $ speak(JECKA, "Why would he send that many pictures of the same thing over and over?")
    $ setWait(25.021,32.237)
    $ speak(NICOLE, "Oh I had him write different things on himself and send pictures of it. Stuff like \"loser\", \"Nicole's bitch\", \"Megan's a whore\" just cool shit.")
    $ setWait(32.237,36.366)
    $ speak(JECKA, "So that's why you weren't picking up yesterday. Busy with the worst shit imaginable.")
    $ setWait(36.366,41.204)
    $ speak(NICOLE, "I don't know, last night was the closest I got to any sexual gratification in this whole plan.")
    $ setWait(41.204,44.291)
    $ speak(JECKA, "Literally how? It's just some ugly guy writing shit on himself.")
    $ setWait(44.291,49.755)
    $ speak(NICOLE, "No not the visual just the raw control felt really awesome.")
    show jecka sc5 sad

    $ setWait(49.755,51.84)
    $ speak(JECKA, "Nicole that's what rapists say just so you know.")
    show nicole sc7

    $ setWait(51.84,57.053)
    $ speak(NICOLE, "I mean I guess but like, I'm a girl what am I gonna do? Guy'sll fly off the handle for barely anything.")
    show jecka sc5

    $ setWait(57.053,61.767)
    $ speak(JECKA, "Yeah guy'sll not get a Lego set when they're 5 and 30 years later molest kids over it.")
    $ setWait(61.767,64.311)
    $ speak(NICOLE, "Exactly, now on to the next step.")
    $ setWait(64.311,66.354)
    $ speak(JECKA, "Are you gonna post the pictures online somewhere?")
    $ setWait(66.354,71.234)
    $ speak(NICOLE, "No I think I'm gonna hold onto these until the time is right.")
    $ setWait(71.234,73.737)
    $ speak(JECKA, "And what time is that?")
    show nicole sc7 smile
    $ setWait(73.737,78.325)
    $ speak(NICOLE, "Oh you'll know... I think everyone's gonna know...")
    stop ambient fadeout 2
    jump scene_0112
label scene_0112:
    show black onlayer screens with Pause(2.5):
        alpha 0.0
        linear 1.5 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.6 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0112.mp3")
    play ambient "audio/Ambience/Venue_Ambience.mp3" fadein 1.5
    scene theatre backstage
    show nicole juliet:
        leftcenterstage
        xzoom -1

    show megan pa:
        xzoom -1
        off_left
        linear 4.5 off_right

    $ setWait(0.041,4.629)
    $ speak(MEGAN, "We're on in less than five, guys! Phones off, let's get it together.")
    $ setWait(4.629,7.09)
    $ speak(NICOLE, "Megan's number, check.")
    show nicole juliet smile
    $ setWait(7.09,10.677)
    $ speak(NICOLE, "Picture of her boyfriend with his weird dick out, check.")
    show hunter romeo smile:
        off_right
        linear 1.3 rightmidstage
        pause 0.5
        xzoom -1
        linear 1.5 off_right

    show nicole juliet smile:
        pause 0.3
        xzoom 1

    $ setWait(10.677,13.179)
    $ speak(HUNTER, "Hey Nicole, good luck tonight!")
    show nicole juliet flirt:
        leftcenterstage
        xzoom 1
    $ setWait(13.179,15.765)
    $ speak(NICOLE, "Good luck to you too.")
    stop ambient fadeout 6
    menu:
        "SEND PHOTO":
            jump end_0113

label end_0113:

    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    $ quick_menu = False

    if "end_0113" not in persistent.endings:
        $ persistent.endings.append("end_0113")
        $ persistent.new_ending = True

    $ quick_menu = False
    window hide

    scene onlayer master
    show black
    $ renpy.movie_cutscene("cs0113.webm")
    return

label scene_0114:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0114.mp3")
    scene photo classroom
    show lorre 1:
        rightcenterstage

    show kylar sc1:
        rightstage

    show nicole sc3:
        leftstage

    show jecka sc2:
        leftmidstage
        xzoom -1

    $ setWait(0.087,12.266)
    $ speak(LORRE, "For this week's assignment let's really open the floor of creativity. In the medium of newsprint and charcoal pencil we're gonna draw a few characters.")

    $ setWait(12.266,13.976)
    $ speak(KYLAR, "We're gonna draw on newspaper?")

    show lorre 1:
        xzoom -1

    $ setWait(13.976,16.937)
    $ speak(LORRE, "It's like newspaper, without the ink.")
    $ setWait(16.937,20.899)
    $ speak(KYLAR, "What the fuck did my Mom pay a $50 supply fee for if we're drawing on newspaper?")
    $ setWait(20.899,22.943)
    $ speak(JECKA, "Yeah isn't that cheaper than printer paper?")

    show lorre 1:
        xzoom 1

    $ setWait(22.943,29.575)
    $ speak(LORRE, "It's not cheaper it's just specialized.\nArt classes are here to remind you you're special.")
    $ setWait(29.575,32.578)
    $ speak(NICOLE, "So are homeless people special when they eat out of the garbage?")
    $ setWait(32.578,34.455)
    $ speak(LORRE, "Your minds are special.")
    show jecka sc2 worried
    $ setWait(34.455,35.789)
    $ speak(JECKA, "Is he calling us special ed?")
    $ setWait(35.789,37.416)
    $ speak(NICOLE, "I guess we are if we took this class.")
    show jecka sc2
    $ setWait(37.416,45.674)
    $ speak(LORRE, "And with the medium of newsprint and charcoal pencils we'll be drawing characters, any characters you'd like.")
    $ setWait(45.674,55.517)
    $ speak(LORRE, "These characters could tell a story, show how you feel, portray a social cause, anything you feel is worth the time to draw.")
    $ setWait(55.517,57.561)
    $ speak(KYLAR, "Can my characters murder bitches?")
    $ setWait(57.561,64.36)
    $ speak(LORRE, "Be mindful that anything we do in this class must be school appropriate.")
    $ setWait(64.36,67.404)
    $ speak(NICOLE, "Can my characters be the gym teacher trying to molest us?")
    show lorre 1 angry
    $ setWait(67.404,68.447)
    $ speak(LORRE, "Nicole.")
    $ setWait(68.447,70.24)
    $ speak(NICOLE, "What?? It's in school.")
    show lorre 1
    $ setWait(70.24,74.203)
    $ speak(LORRE, "I think you're all smart enough to know what pushes the envelope.")
    $ setWait(74.203,79.041)
    $ speak(LORRE, "It's your first assignment, just play it safe.\nAny other questions?")
    $ setWait(79.041,81.251)
    $ speak(JECKA, "Are we allowed to just draw people hanging out?")
    $ setWait(81.251,92.262)
    $ speak(LORRE, "Of course, though it might not be the strongest test of your creativity. Think why are they hanging out? What purpose brought them all together to hang out?")
    show kylar sc1 smile
    $ setWait(92.262,93.597)
    $ speak(KYLAR, "Heh bitches and shit.")
    $ setWait(93.597,99.103)
    $ speak(LORRE, "If there are no further questions I'll hand you your papers and we can begin!")
    menu:
        "FUCK DRAWING":
            jump scene_0115
        "ACTUALLY DRAW":
            jump scene_0142
label scene_0115:
    $ setVoiceTrack("audio/Scenes/0115.mp3")
    scene photo classroom

    show lorre 1:
        rightcenterstage

    show kylar sc1:
        rightstage

    show nicole sc3 angry:
        leftstage

    show jecka sc2:
        leftmidstage
        xzoom -1

    $ setWait(0.037,1.664)
    $ speak(NICOLE, "Bitch you do that shit.")
    show lorre 1 angry

    $ setWait(1.664,3.374)
    $ speak(LORRE, "Excuse me??")
    $ setWait(3.374,6.585)
    $ speak(NICOLE, "Dude we're seniors, I'm not drawing during one of my sleeping classes.")
    $ setWait(6.585,11.173)
    $ speak(LORRE, "I'm sorry but you're in art, not a sleeping class.")
    show nicole sc3
    $ setWait(11.173,12.633)
    $ speak(NICOLE, "Is this an elective?")
    show lorre 1
    $ setWait(12.633,13.509)
    $ speak(LORRE, "Well yes.")
    $ setWait(13.509,15.135)
    $ speak(NICOLE, "So what are you gonna do about it?")
    $ setWait(15.135,18.055)
    $ speak(LORRE, "Fail you for your lack of participation.")
    $ setWait(18.055,22.017)
    $ speak(NICOLE, "Oh yeah in the elective that doesn't stop me from graduating, that'll really show me.")
    $ setWait(22.017,23.894)
    $ speak(KYLAR, "Yeah actually why the hell are any of us drawing?")
    $ setWait(23.894,25.312)
    $ speak(JECKA, "For the easy GPA.")
    $ setWait(25.312,28.607)
    $ speak(KYLAR, "What fuckin' college would care if you drew some bullshit picture about your feelings?")
    $ setWait(28.607,31.86)
    $ speak(JECKA, "They'd rather see an A in an easy class than a B in a hard class.")
    show nicole sc3 angry
    $ setWait(31.86,36.949)
    $ speak(NICOLE, "I don't wanna be in fuckin' any class. We had to do twelve years of this shit you're gonna volunteer for more of it?")
    $ setWait(36.949,37.616)
    $ speak(JECKA, "Whatever.")
    show lorre 1 angry
    $ setWait(37.616,40.327)
    $ speak(LORRE, "You have a real attitude problem, you know that, Nicole?")
    show nicole sc3
    $ setWait(40.327,45.499)
    $ speak(NICOLE, "You have a teaching a real class problem. Go work at Starbucks with your little apron.")

    show lorre 1 angry:
        rightcenterstage
        pause 0.7
        xzoom -1
        linear 2.5 off_right

    $ setWait(45.499,50.296)
    $ speak(LORRE, "Let's see how the principal deals with your abundance of comebacks.")
    show jecka sc2 worried:
        xzoom 1
    $ setWait(50.296,53.215)
    $ speak(JECKA, "Nicole we're not even a week in and you're getting sent to the principal.")
    show nicole sc3 smile
    $ setWait(53.215,55.009)
    $ speak(NICOLE, "New record, don't be jealous.")
    stop ambient fadeout 1.2
    jump scene_0116
label scene_0116:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0116.mp3")
    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    scene office 2
    show nicole sc3 angry:
        leftcenterstage

    show lynn 4:
        rightmidstage

    $ setWait(0.078,1.746)
    $ speak(LYNN, "You're on your final warning, Nicole.")
    $ setWait(1.746,4.582)
    $ speak(NICOLE, "Final warning?? This is the first time I was sent here!")
    $ setWait(4.582,10.547)
    $ speak(LYNN, "I've decided to roll over your warnings from last year. You made such a habit out of coming here it's hard to forget over the summer.")
    $ setWait(10.547,12.048)
    $ speak(NICOLE, "You don't do that with anyone else!")
    $ setWait(12.048,16.636)
    $ speak(LYNN, "Yes but anyone else doesn't seem to deliberately disrupt the class as much as you do.")
    $ setWait(16.636,19.097)
    $ speak(NICOLE, "What am I supposed to accidentally call my teacher a bitch?")
    $ setWait(19.097,22.892)
    $ speak(LYNN, "You're supposed to follow the class and not insult faculty.")
    $ setWait(22.892,23.768)
    $ speak(NICOLE, "No shit.")
    $ setWait(23.768,26.646)
    $ speak(LYNN, "Then why do you continue to not do that?")
    show nicole sc3
    $ setWait(26.646,27.856)
    $ speak(NICOLE, "Cause that's boring.")
    $ setWait(27.856,30.233)
    $ speak(LYNN, "So your life here is a game to you?")
    show nicole sc3 angry
    $ setWait(30.233,33.361)
    $ speak(NICOLE, "No, Candy Land's a game, this shit's torture.")
    $ setWait(33.361,39.284)
    $ speak(LYNN, "If the current curriculum isn't working for you we could always have you transferred into a different program here.")
    $ setWait(39.284,43.872)
    $ speak(NICOLE, "I swear to god if you put me in spec ed I will bully all of those kids into killing themselves.")
    $ setWait(43.872,45.373)
    $ speak(LYNN, "Nicole don't be ludicrous.")
    $ setWait(45.373,50.17)
    $ speak(NICOLE, "They're special, Miss Lynn. One little push and you'll have to make a really awkward phone call.")
    $ setWait(50.17,57.093)
    $ speak(LYNN, "I wasn't implying special ed, Nicole.\nWe have alternative learning programs for students who feel they can't quite get along.")
    show nicole sc3
    $ setWait(57.093,58.261)
    $ speak(NICOLE, "Really now?")
    $ setWait(58.261,64.809)
    $ speak(LYNN, "I wouldn't look at it as an out. Believe me when I tell you the classes you're in now are a lot more pleasant.")
    show nicole sc3 smile:
        leftcenterstage
        xzoom -1
        linear 3.4 off_left

    $ setWait(64.809,66.269)
    $ speak(NICOLE, "We'll see about that.")
    $ setWait(66.269,68.497)
    $ speak(LYNN, "Again, final warning!")
    stop ambient fadeout 1.3
    jump scene_0117
label scene_0117:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0


    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0117.mp3")
    scene classroom int 2
    show nicole sc3:
        leftmidstage

    show jeffery sc2:
        leftcenterstage

    $ setWait(0.035,9.92)
    $ speak(JEFFERY, "I just don't understand why we can't upload anime to Youtube anymore. A lot of the time there's no other way to watch the original Japanese version with English subtitles.")
    $ setWait(9.92,10.837)
    $ speak(NICOLE, "Uh huh.")
    $ setWait(10.837,22.557)
    $ speak(JEFFERY, "Besides I can't even stomach the American version, they just change so much. It's not a faithful adaptation so Youtube is the only way we can watch the true original version.")
    $ setWait(22.557,26.186)
    $ speak(NICOLE, "Why do you think I know what any of this shit you're talking about is?")
    $ setWait(26.186,33.276)
    $ speak(JEFFERY, "Well it's sorta been a big deal in the online communities. The digital millennium copyright act? Have you heard of it?")
    show nicole sc3 angry
    $ setWait(33.276,34.778)
    $ speak(NICOLE, "Will you shut the fuck up?")

    show jeffery sc2 angry

    $ setWait(34.778,35.779)
    $ speak(JEFFERY, "Wha-- Hey!")
    $ setWait(35.779,38.949)
    $ speak(NICOLE, "You're going off about copyright and shit, you can't even tie your shoes.")
    $ setWait(38.949,42.411)
    $ speak(JEFFERY, "I know how to tie shoes, slip-ons are just quicker is all.")
    $ setWait(42.411,46.039)
    $ speak(NICOLE, "\"Quicker is all\" you sound like a cartoon character arguing age of consent laws.")
    show jeffery sc2
    $ setWait(46.039,51.253)
    $ speak(JEFFERY, "But what's wrong about sounding like a cartoon? Cartoons are my favorite, second to anime.")
    show nicole sc3
    $ setWait(51.253,54.089)
    $ speak(NICOLE, "Weren't you talking about how much you want a girlfriend yesterday?")
    $ setWait(54.089,56.091)
    $ speak(JEFFERY, "Yes and I still want one.")
    $ setWait(56.091,59.97)
    $ speak(NICOLE, "And you plan on this hypothetical girlfriend touching your penis?")
    show jeffery sc2 blush
    $ setWait(59.97,63.849)
    $ speak(JEFFERY, "Well I don't wanna rush things, but one day yes.")
    $ setWait(63.849,71.982)
    $ speak(NICOLE, "Okay lemme help you out. Approaching girls in your velcro shoes with the current events of Youtube anime will not make her wanna fuck you.")
    $ setWait(71.982,77.863)
    $ speak(JEFFERY, "Wh-Who said I was trying to do that with you? Just a talk between friends, I don't think about you in that way.")
    $ setWait(77.863,78.739)
    $ speak(NICOLE, "Really?")
    $ setWait(78.739,79.906)
    $ speak(JEFFERY, "Yeah not at all.")
    show nicole sc3 smile
    $ setWait(79.906,80.782)
    $ speak(NICOLE, "Not even a little?")
    $ setWait(80.782,81.7)
    $ speak(JEFFERY, "N-no.")
    show nicole sc3
    show jeffery sc2
    $ setWait(81.7,83.118)
    $ speak(NICOLE, "Wow, that's a shame.")
    $ setWait(83.118,83.785)
    $ speak(JEFFERY, "Why?")
    show nicole sc3 flirt
    $ setWait(83.785,87.497)
    $ speak(NICOLE, "Cause I wanted to give you a handjob after lunch but if you don't think about me that way--")
    show jeffery sc2 blush

    $ setWait(87.497,92.169)
    $ speak(JEFFERY, "Wait I mean, well I could reconsider my feelings if you felt that way.")
    show nicole sc3 angry

    show jeffery sc2

    $ setWait(92.169,96.173)
    $ speak(NICOLE, "You are so fucking pathetic. I hope you kill yourself while your mom watches.")
    show burleday 2:
        off_right
        linear 2 rightmidstage

    $ setWait(96.173,99.05)
    $ speak(BURLEDAY, "I'm hearing a bit of profanity over here, is everything alright?")
    show nicole sc3 smile

    $ setWait(99.05,103.889)
    $ speak(NICOLE, "Oh I don't know. You're not gonna write me up, are you? I'm on my last warning.")
    $ setWait(103.889,106.683)
    $ speak(BURLEDAY, "That depends, Jeffery what's going on here?")
    show jeffery sc2:
        xzoom -1

    show nicole sc3

    $ setWait(106.683,111.229)
    $ speak(JEFFERY, "N-nothing. Nicole was actually helping me out with some life advice.")
    show burleday 2:
        rightmidstage
        pause 1
        xzoom -1
        linear 2 off_right

    $ setWait(111.229,114.816)
    $ speak(BURLEDAY, "Well alright. Back to work on your lab.")
    show jeffery sc2:
        xzoom 1

    $ setWait(114.816,122.032)
    $ speak(JEFFERY, "Don't worry, Nicole. Usually you just ignore me, but I understand you were trying to be extra mean today so I'd better myself.")
    show nicole sc3 angry
    $ setWait(122.032,127.078)
    $ speak(NICOLE, "No I was extra mean to get written up so I don't have to take these shitty fucking classes anymore.")
    $ setWait(127.078,130.791)
    $ speak(JEFFERY, "Oh well if you're ever feeling like you need an escape...")
    $ setWait(130.791,132.167)
    $ speak(JEFFERY, "The manga club's doing a--")
    show nicole sc3
    $ setWait(132.167,133.16)
    $ speak(NICOLE, "Just stop there.")
    stop ambient fadeout 1
    jump scene_0118
label scene_0118:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0


    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0118.mp3")
    scene cafeteria int
    show nicole sc3:
        leftcenterstage

    show jecka sc2 worried:
        rightcenterstage

    $ setWait(0.036,3.832)
    $ speak(JECKA, "Hold on you told him \"kill yourself while your mom watches\"?")
    $ setWait(3.832,4.582)
    $ speak(NICOLE, "Yeah.")
    $ setWait(4.582,5.625)
    $ speak(JECKA, "That's really good.")
    $ setWait(5.625,6.751)
    $ speak(NICOLE, "I know, right?")
    $ setWait(6.751,8.336)
    $ speak(JECKA, "And that didn't get you written up?")
    $ setWait(8.336,11.84)
    $ speak(NICOLE, "Yeah the teacher wasn't there when I said it so the response was lukewarm.")
    show jecka sc2

    $ setWait(11.84,14.342)
    $ speak(JECKA, "You're really going for these remedial classes, huh?")
    $ setWait(14.342,15.635)
    $ speak(NICOLE, "Is that what they're called?")
    show jecka sc2 worried
    $ setWait(15.635,19.472)
    $ speak(JECKA, "Yeah but it's for major fuck-ups I'm not sure you wanna be there everyday.")
    $ setWait(19.472,20.807)
    $ speak(NICOLE, "What? Stupid kids?")
    $ setWait(20.807,27.48)
    $ speak(JECKA, "No, kids who're gonna go to jail straight after graduation. It's like the worst of the worst, everyday is Saturday school but more eventful.")
    $ setWait(27.48,32.902)
    $ speak(NICOLE, "I know it's gonna be rougher but I'm just tired of these lame ass teachers who won't leave me alone about anything.")

    show jecka sc2

    $ setWait(32.902,35.613)
    $ speak(JECKA, "You think the other teachers are just gonna let you do whatever you want?")
    $ setWait(35.613,43.037)
    $ speak(NICOLE, "If I just wanna sleep in class then by default yes. A collection of the worst kids in school means distractions from me.")
    $ setWait(43.037,46.499)
    $ speak(JECKA, "But you still can't find your way there. Tragic.")
    $ setWait(46.499,48.501)
    $ speak(NICOLE, "Well hold on, what's your textbook there?")
    $ setWait(48.501,50.211)
    $ speak(JECKA, "It's for government, why?")
    $ setWait(50.211,51.629)
    $ speak(NICOLE, "Can I borrow that real quick?")
    $ setWait(51.629,52.505)
    $ speak(JECKA, "Sure?")
    show nicole sc3 smile:
        xzoom -1
        leftcenterstage
        linear 1.2 off_left

    $ setWait(52.505,55.216)
    $ speak(NICOLE, "I'll be right back.")
    show jecka sc2 angry

    $ setWait(55.216,56.551)
    $ speak(JECKA, "What the fuck.")
    show nicole sc3 smile:
        off_left
        xzoom 1
        linear 2.2 leftcenterstage

    $ setWait(56.551,57.552)
    $ speak(NICOLE, "That should do it.")
    $ setWait(57.552,61.306)
    $ speak(JECKA, "Why'd you ask what subject it is if you were just gonna throw it out a window??")
    show nicole sc3
    $ setWait(61.306,63.099)
    $ speak(NICOLE, "Huh.. I don't know.")
    show coach 1 angry:
        off_farleft
        xzoom -1
        linear 1.6 leftmidstage

    $ setWait(63.099,65.435)
    $ speak(COACH, "Alright what the hell's the matter with you!?")
    show nicole sc3:
        leftcenterstage
        xzoom -1

    $ setWait(65.435,68.354)
    $ speak(NICOLE, "Acting out, felt alone-- Do I look like a therapist to you?")
    show coach 1 sad:
        leftmidstage
        xzoom -1
    $ setWait(68.354,76.696)
    $ speak(COACH, "Nicole we've been trying to take a more understanding disciplinary approach lately. Tell me what's wrong, cause you're disappointing us here.")
    show nicole sc3 surprised

    $ setWait(76.696,78.281)
    $ speak(NICOLE, "Wait are you not gonna write me up?")
    $ setWait(78.281,85.788)
    $ speak(COACH, "It's the no child left behind act sorta thing. I don't wanna escalate anything if we can resolve this through a dialogue.")
    show nicole sc3

    $ setWait(85.788,88.833)
    $ speak(COACH, "So why'd you feel the need to break a window?")
    $ setWait(88.833,91.878)
    $ speak(JECKA, "Yeah and did it have to be my textbook? I need that for government.")
    $ setWait(91.878,95.757)
    $ speak(COACH, "Nicole, is there a hostility towards government class?")
    $ setWait(95.757,97.133)
    $ speak(NICOLE, "Are you really not gonna write me up?")
    show coach 1
    $ setWait(97.133,101.846)
    $ speak(COACH, "Nicole answer the question, what's wrong with government?")
    $ setWait(101.846,104.891)
    $ speak(NICOLE, "Uh... Because our government hates women.")
    $ setWait(104.891,106.517)
    $ speak(COACH, "Excuse me?")
    $ setWait(106.517,110.063)
    $ speak(NICOLE, "The government hates women, dude. We can't get abortions or anything.")
    show coach 1 angry
    $ setWait(110.063,116.152)
    $ speak(COACH, "Oh I see, a political extremist huh?? Using violence to spread your message!?")
    $ setWait(116.152,117.32)
    $ speak(NICOLE, "If you wanna call it that.")
    $ setWait(117.32,125.578)
    $ speak(COACH, "The dictionary calls that terrorism, young lady! We've been cracking down on terrorism for the last seven years if you haven't noticed!")
    show nicole sc3 surprised
    $ setWait(125.578,127.58)
    $ speak(NICOLE, "Are you connecting this to 9/11?")
    show nicole sc3

    show coach 1 angry:
        xzoom -1
        leftmidstage
        pause 1.2
        linear 2.4 off_farright

    show nicole sc3:
        leftcenterstage
        xzoom -1
        pause 1.9
        xzoom 1
        pause 0.3
        linear 2 off_right

    $ setWait(127.58,130.959)
    $ speak(COACH, "Just sickening, straight to the principal! Come with me!")
    $ setWait(130.959,132.961)
    $ speak(NICOLE, "Getting warmer.")
    show jecka sc2 surprised
    $ setWait(132.961,135.088)
    $ speak(JECKA, "...Wait am I at lunch alone now??")
    show jeffery sc2:
        xzoom -1
        off_left
        linear 2 leftcenterstage

    $ setWait(135.088,137.757)
    $ speak(JEFFERY, "Join the club, Jecka. I could sit with you if you want.")
    show jecka sc2 angry:
        rightcenterstage
        pause 0.53
        xzoom -1
        linear 1.7 off_right

    $ setWait(137.757,139.425)
    $ speak(JECKA, "No fuck off.")
    stop ambient fadeout 1
    jump scene_0119
label scene_0119:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Office_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0119.mp3")
    scene office 2

    show nicole sc3:
        leftcenterstage

    show lynn 4:
        rightmidstage

    $ setWait(0.047,2.258)
    $ speak(LYNN, "You really don't waste any time, do you?")
    $ setWait(2.258,4.802)
    $ speak(NICOLE, "Guess not, so I'm out of regular school now, right?")
    $ setWait(4.802,9.724)
    $ speak(LYNN, "He accused you of acts of terrorism, Nicole. That's a bigger punishment than remedial classes.")
    show nicole sc3 angry

    $ setWait(9.724,12.602)
    $ speak(NICOLE, "What? How's throwing a book terrorism?")
    $ setWait(12.602,15.73)
    $ speak(LYNN, "You threw a book through a window for a political message.")
    $ setWait(15.73,17.982)
    $ speak(NICOLE, "And did he not explain the message?")
    $ setWait(17.982,21.319)
    $ speak(LYNN, "Nicole I'd rather not get into your diatribe on the communist manifesto.")
    show nicole sc3 surprised

    $ setWait(21.319,22.653)
    $ speak(NICOLE, "Communist??")
    $ setWait(22.653,24.447)
    $ speak(LYNN, "That's what Mr. Colby informed me of.")
    show nicole sc3 angry

    $ setWait(24.447,26.699)
    $ speak(NICOLE, "I don't even know what the fuck communism is!")
    $ setWait(26.699,27.909)
    $ speak(LYNN, "Must you play dumb with me?")
    show nicole sc3

    $ setWait(27.909,31.996)
    $ speak(NICOLE, "No seriously is it like for people who go on the internet too much? I have no clue.")
    $ setWait(31.996,36.083)
    $ speak(LYNN, "Well if not for communism, why did you break the window with a government textbook?")
    $ setWait(36.083,41.047)
    $ speak(NICOLE, "Because the government hates women, that's what I told him. So if anything it was feminism, not communism.")
    $ setWait(41.047,44.133)
    $ speak(LYNN, "This isn't the first time he's referred to feminism as communism.")
    show nicole sc3 surprised

    $ setWait(44.133,49.43)
    $ speak(NICOLE, "See? He's fucking insane, he wants to rape women and force them to keep the baby! Total psycho!")
    $ setWait(49.43,50.431)
    $ speak(LYNN, "Just despicable.")
    show nicole sc3
    $ setWait(50.431,54.393)
    $ speak(NICOLE, "Right there with ya, so are you writing me up or?")
    $ setWait(54.393,61.442)
    $ speak(LYNN, "Women's rights are no reason to write any student up. You're very brave, Nicole. Now I'll be having a word with your gym teacher.")
    show nicole sc3 sad

    $ setWait(61.442,65.655)
    $ speak(NICOLE, "Wait but... I broke a window. Isn't that delinquent behavior?")
    $ setWait(65.655,69.367)
    $ speak(LYNN, "You had your reasons, but this is an intricate conversation we'll need to have later.")
    $ setWait(69.367,73.329)
    $ speak(NICOLE, "But what if I just did it for fun? Like no terrorism or feminism or anything?")
    $ setWait(73.329,75.247)
    $ speak(LYNN, "Well that would be different now wouldn't it?")
    show nicole sc3

    $ setWait(75.247,77.875)
    $ speak(NICOLE, "Okay then I made the feminism shit up, just give me the regular trouble.")
    $ setWait(77.875,80.211)
    $ speak(LYNN, "You're not getting sent to remedial classes.")
    $ setWait(80.211,82.046)
    $ speak(NICOLE, "No seriously, I hate women.")
    $ setWait(82.046,83.255)
    $ speak(LYNN, "Nice try, Nicole.")
    $ setWait(83.255,88.552)
    $ speak(NICOLE, "I'm not messing around, all women are good for is sucking dick and watching Desperate Housewives.")
    $ setWait(88.552,89.762)
    $ speak(LYNN, "Out of my office.")
    stop ambient fadeout 1
    jump scene_0120
label scene_0120:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.04):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.04 zoom 0.64 truecenter

    $ setVoiceTrack("audio/Scenes/0120.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home nicole int
    show mom 1 smile:
        off_right
        linear 2.2 centerstage

    show nicole sc3:
        leftmidstage

    $ setWait(2.04,5.252)
    $ speak(MOM, "Good news, Nicole. Very good day today.")
    $ setWait(5.252,7.379)
    $ speak(NICOLE, "Did the mean lady at Marshall's transfer?")
    $ setWait(7.379,9.506)
    $ speak(MOM, "Even better, I got a new job.")
    $ setWait(9.506,13.093)
    $ speak(NICOLE, "Mom you get eight alimony checks a month, why the fuck did you get a job?")
    show mom 1
    $ setWait(13.093,19.975)
    $ speak(MOM, "You're going to be 18 soon and when that happens the well dries up just a bit. Also it's a reason to get out of the house.")
    $ setWait(19.975,23.103)
    $ speak(NICOLE, "Is daytime drinking at PF Chang's not getting out of the house?")
    show mom 1 upset
    $ setWait(23.103,24.271)
    $ speak(MOM, "Will you be serious?")
    $ setWait(24.271,25.105)
    $ speak(NICOLE, "I am.")
    show mom 1 smile
    $ setWait(25.105,28.942)
    $ speak(MOM, "Well I got a job in catering for that little kosher deli in Falls Church.")
    $ setWait(28.942,29.776)
    $ speak(NICOLE, "Rossler's?")
    $ setWait(29.776,37.242)
    $ speak(MOM, "Yeah Rossler's Deli, I'll be prepping the sandwich trays. It's not the most prestigious but I think there's value in working amongst the common man.")
    $ setWait(37.242,41.413)
    $ speak(NICOLE, "Okay cool, why would you work at a kosher deli? I thought you hated Jewish people.")
    show mom 1 upset
    $ setWait(41.413,44.333)
    $ speak(MOM, "Nicole, I do not hate Jewish people!")
    $ setWait(44.333,50.047)
    $ speak(NICOLE, "You said my third step-dad only got a good settlement cause the courts \"won't let the holocaust go\".")
    show mom 1
    $ setWait(50.047,57.763)
    $ speak(MOM, "We all say brash things when we're upset, let's not read into it. I won't feed into your negativity and let it ruin my moment of progress.")
    show nicole sc3 angry
    $ setWait(57.763,58.931)
    $ speak(NICOLE, "Oh what book is that from--")
    $ setWait(58.931,62.017)
    $ speak(MOM, "Again happy thoughts. So how was school today?")
    show nicole sc3
    $ setWait(62.017,64.895)
    $ speak(NICOLE, "I got in trouble and they transferred me to remedial classes.")
    show mom 1 angry

    $ setWait(64.895,65.479)
    $ speak(MOM, "What!?")
    $ setWait(65.479,66.98)
    $ speak(NICOLE, "I know, took 'em long enough.")
    $ setWait(66.98,69.107)
    $ speak(MOM, "No- what the fuck is the matter with you!?")
    $ setWait(69.107,73.82)
    $ speak(NICOLE, "I need remediation, my grades and behavior are apparently not cutting it.")
    $ setWait(73.82,77.658)
    $ speak(MOM, "Your grades? You go to school everyday, don't you get a C just by showing up??")
    show nicole sc3 angry
    $ setWait(77.658,82.788)
    $ speak(NICOLE, "Mom it's not the 70's anymore where you just show up and get a C! You actually have to do shit now, it sucks!")
    $ setWait(82.788,85.165)
    $ speak(MOM, "Excuses, excuses!")
    $ setWait(85.165,87.125)
    $ speak(NICOLE, "Weren't you supposed to be happy or something?")
    show mom 1 upset
    $ setWait(87.125,92.005)
    $ speak(MOM, "Ugh, I'm gonna go up to my room and read up on how to fold the pastrami.")
    show mom 1 upset:
        centerstage
        linear 3 off_left

    $ setWait(92.005,95.968)
    $ speak(MOM, "You better find a way out of those remedial classes.")
    show nicole sc3 angry:
        xzoom -1
    $ setWait(95.968,98.303)
    $ speak(NICOLE, "You better find a real fuckin' job, bitch.")
    stop ambient fadeout 1
    jump scene_0121
label scene_0121:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(1.745):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 1.745 zoom 1.1 truecenter


    $ setVoiceTrack("audio/Scenes/0121.mp3")
    play ambient "audio/Ambience/Classroom_Ambience_2.mp3"
    scene classroom int 4
    show emily sc3:
        xzoom -1
        rightstage

    show kylar sc2:
        rightmidstage


    show nicole sc4:
        off_left
        linear 2.6 leftcenterstage

    $ setWait(1.745,5.415)
    $ speak(NICOLE, "Jecka was freaking out over nothing, these kids aren't that tough and crazy.")
    show kylar sc2:
        rightmidstage
        linear 0.8 rightcenterstage

    $ setWait(5.415,7.625)
    $ speak(KYLAR, "Hey, you got put in remedial English too?")
    $ setWait(7.625,10.795)
    $ speak(NICOLE, "Wait just English? I thought all my classes would be here.")
    $ setWait(10.795,12.756)
    $ speak(KYLAR, "Nah they only have it for Math and English.")
    show nicole sc4 sad
    $ setWait(12.756,14.466)
    $ speak(NICOLE, "So I still have to go to art class?")
    $ setWait(14.466,16.843)
    $ speak(KYLAR, "If you need extra time here they'll let you skip electives.")
    show nicole sc4
    $ setWait(16.843,18.136)
    $ speak(NICOLE, "Guess I'll have to take it.")
    $ setWait(18.136,20.93)
    $ speak(KYLAR, "So did you get put here for some bullshit reason like the rest of us?")
    $ setWait(20.93,22.766)
    $ speak(NICOLE, "You could say that. Why are you here?")
    show kylar sc2 angry
    $ setWait(22.766,29.147)
    $ speak(KYLAR, "Just some bullshit with Mr. Horvitz, that sheeny shit faced fuckin' fairy. I wish the holocaust happened.")
    show nicole sc4 surprised

    $ setWait(29.147,30.231)
    $ speak(NICOLE, "What was that last part?")
    show kylar sc2
    $ setWait(30.231,33.026)
    $ speak(KYLAR, "I said I wish the holocaust happened?")
    show nicole sc4
    $ setWait(33.026,37.781)
    $ speak(NICOLE, "...I think you need remedial history, pretty sure the holocaust did happen.")
    show kylar sc2 angry
    $ setWait(37.781,42.077)
    $ speak(KYLAR, "Oh. Well I wish it happened more. Then that fuck wouldn't be here.")

    show nicole sc4:
        xzoom -1

    $ setWait(42.077,44.371)
    $ speak(NICOLE, "So this is remedial classes.")
    show ames 1:
        xzoom -1
        off_left
        linear 3.8 leftmidstage

    show kylar sc2

    $ setWait(44.371,48.041)
    $ speak(AMES, "Alright time to start, I wanna see you all in your assigned seats.")
    show emily sc3 angry:
        xzoom 1
        rightstage

    $ setWait(48.041,50.126)
    $ speak(EMILY, "I wanna see you in a wheelchair, bitch!")
    $ setWait(50.126,53.171)
    $ speak(KYLAR, "Yeah fuck you, Ms. Ames!")
    $ setWait(53.171,54.422)
    $ speak(AMES, "...Are we finished?")
    show emily sc3
    show nicole sc4 surprised
    $ setWait(54.422,55.882)
    $ speak(NICOLE, "Whoa she didn't say shit.")
    show nicole sc4
    show ames 1 smile
    $ setWait(55.882,62.18)
    $ speak(AMES, "I see we have a new student, welcome to remedial English.\nMy name is Ms. Ames, what shall we call you?")
    $ setWait(62.18,65.225)
    $ speak(NICOLE, "Uh, Beyonce.")
    show ames 1 smug
    $ setWait(65.225,67.936)
    $ speak(AMES, "Okay I'll just look it up during attendance.")
    $ setWait(67.936,69.396)
    $ speak(EMILY, "Can we listen to our iPods?")
    show ames 1
    $ setWait(69.396,70.48)
    $ speak(AMES, "Listen to what?")
    show emily sc3 upset
    $ setWait(70.48,71.481)
    $ speak(EMILY, "Does it matter?")
    $ setWait(71.481,75.568)
    $ speak(AMES, "If you're listening in class it should serve to benefit the course in some way.")
    $ setWait(75.568,77.153)
    $ speak(KYLAR, "Would Weezy benefit the course?")
    show emily sc3
    $ setWait(77.153,78.696)
    $ speak(EMILY, "Yeah and what about Kanye?")
    show ames 1 smug
    $ setWait(78.696,80.115)
    $ speak(AMES, "Are these rappers?")
    $ setWait(80.115,81.116)
    $ speak(NICOLE, "No they're accountants.")
    $ setWait(81.116,82.534)
    $ speak(EMILY, "C'mon we'll just do one earbud.")
    $ setWait(82.534,90.333)
    $ speak(AMES, "While I'm sure this music is catchy for all of you it serves little in terms of lyrical substance. Not appropriate for English.")
    $ setWait(90.333,91.96)
    $ speak(EMILY, "Then who can we listen to?")
    show ames 1
    $ setWait(91.96,94.129)
    $ speak(AMES, "How do you feel about The Beatles?")
    show nicole sc4 angry
    $ setWait(94.129,96.965)
    $ speak(NICOLE, "You are such a fucking white mom it's not even funny.")
    $ setWait(96.965,97.632)
    $ speak(AMES, "I'm sorry?")
    $ setWait(97.632,100.718)
    $ speak(NICOLE, "Dodge Caravan bitch.")
    $ setWait(100.718,102.762)
    $ speak(EMILY, "Yeah so we can't listen to rap or anything?")
    $ setWait(102.762,109.644)
    $ speak(AMES, "I never said that. You just need to choose something with meaningful lyrical content.\nWhat do you think about 2pac?")
    $ setWait(109.644,110.687)
    $ speak(EMILY, "I think he's dead.")
    show kylar sc2 angry:
        xzoom -1
    $ setWait(110.687,114.023)
    $ speak(KYLAR, "Yeah think he's dead, he could be hiding in Ecuador for all we know.")
    $ setWait(114.023,115.442)
    $ speak(AMES, "His music?")
    show kylar sc2:
        xzoom 1

    show nicole sc4
    $ setWait(115.442,116.651)
    $ speak(NICOLE, "He's whatever.")
    $ setWait(116.651,118.111)
    $ speak(EMILY, "Yeah he's okay I guess.")
    show ames 1 angry

    $ setWait(118.111,130.415)
    $ speak(AMES, "Okay?? Socially conscious music is just okay? The lyrical content of 2pac was such an important submission of modern poetry by the African-American community.")

    $ setWait(130.415,134.419)
    $ speak(NICOLE, "You wouldn't say any of that shit unless the Washington Post did an article on it.")
    $ setWait(134.419,136.963)
    $ speak(EMILY, "Yeah do you have 2pac on cassette or something?")
    show ames 1

    $ setWait(136.963,141.843)
    $ speak(AMES, "Irrelevant to my point but I say all of that as a lead in to your next essay.")
    $ setWait(141.843,144.804)
    $ speak(KYLAR, "Dude why the fuck do we have to write? I just wanna watch fight videos.")
    $ setWait(144.804,156.357)
    $ speak(AMES, "An essay on the state of modern poetry. It needs to be 4 pages, double-spaced, and feature a variety of citations of proper modern poetry.")
    $ setWait(156.357,159.402)
    $ speak(EMILY, "We don't read proper modern poetry.")
    $ setWait(159.402,162.03)
    $ speak(AMES, "And this assignment will force you to do so.")
    $ setWait(162.03,163.198)
    $ speak(KYLAR, "What about our music?")
    show ames 1 smug
    $ setWait(163.198,169.496)
    $ speak(AMES, "Poetic merit seldom exists with these modern rappers. The misogyny alone is sickening.")
    $ setWait(169.496,170.747)
    $ speak(NICOLE, "What misogyny?")
    $ setWait(170.747,173.75)
    $ speak(AMES, "A variety of things I'd rather not repeat.")
    show emily sc3 smile
    $ setWait(173.75,176.836)
    $ speak(EMILY, "Are you bad at pronouncing the slang? I'm white too, it's okay.")
    stop ambient fadeout 1
    jump scene_0122
label scene_0122:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0122.mp3")
    scene cafeteria int 2
    show nicole sc4 angry:
        leftcenterstage

    show kylar sc2:
        rightcenterstage

    $ setWait(0.086,2.046)
    $ speak(NICOLE, "Why is lunch at like 10:30?")
    $ setWait(2.046,6.551)
    $ speak(KYLAR, "It's remedial lunch, they gotta keep us away from the other kids or we'll cause trouble or some bullshit.")
    show counselor 3:
        off_right
        linear 1.6 rightmidstage

    $ setWait(6.551,9.387)
    $ speak(COUNSELOR, "Kylar, was that a negative remark I just heard?")
    $ setWait(9.387,10.513)
    $ speak(NICOLE, "Oh this fuckin' guy.")
    show kylar sc2 angry:
        xzoom -1

    $ setWait(10.513,13.599)
    $ speak(KYLAR, "It wasn't even negative! How's calling something bullshit negative, huh?")
    show nicole sc4
    $ setWait(13.599,21.691)
    $ speak(COUNSELOR, "Do you recall our chat last lunch about the energy in which we charge our language with? Why don't you come with me for a refresher.")
    show counselor 3:
        rightmidstage
        xzoom -1
        linear 1.6 off_right

    show kylar sc2 angry:
        rightcenterstage
        xzoom -1
        pause 0.25
        linear 2 off_right

    $ setWait(21.691,24.068)
    $ speak(KYLAR, "I hate talking, talking's for gay people.")
    $ setWait(24.068,25.027)
    $ speak(NICOLE, "What a theory.")
    show emily sc3:
        off_left
        xzoom -1
        linear 1.7 leftmidstage

    show nicole sc4:
        leftcenterstage
        pause 0.55
        xzoom -1
    $ setWait(25.027,26.487)
    $ speak(EMILY, "Hey can I sit with you?")
    $ setWait(26.487,27.113)
    $ speak(NICOLE, "Why?")
    $ setWait(27.113,29.949)
    $ speak(EMILY, "The kids at the other table keep throwing ketchup packets at me.")
    $ setWait(29.949,31.743)
    $ speak(NICOLE, "You're not covered in ketchup though.")
    $ setWait(31.743,33.619)
    $ speak(EMILY, "They don't know you have to open them first.")
    $ setWait(33.619,36.247)
    $ speak(NICOLE, "Damn we need a remedial bullying class too.")
    $ setWait(36.247,38.374)
    $ speak(EMILY, "So how do you like remedial English?")
    $ setWait(38.374,41.002)
    $ speak(NICOLE, "I guess it's whatever, my Mom was really pissed though.")
    $ setWait(41.002,42.795)
    $ speak(EMILY, "Yeah? What about your Dad?")
    $ setWait(42.795,44.088)
    $ speak(NICOLE, "My Dad killed himself.")
    show emily sc3 upset:
        leftmidstage
        xzoom -1
    $ setWait(44.088,45.673)
    $ speak(EMILY, "Wow dramatic much.")
    show nicole sc4 surprised

    $ setWait(45.673,47.508)
    $ speak(NICOLE, "Oh no- he killed himself last year.")
    $ setWait(47.508,49.594)
    $ speak(EMILY, "Fuuuck, you wanna trade dads?")
    show nicole sc4

    $ setWait(49.594,50.636)
    $ speak(NICOLE, "What's wrong with your dad?")
    show emily sc3 angry
    $ setWait(50.636,57.018)
    $ speak(EMILY, "Literally everything, he's so up his own ass all the time. I'll be happy about anything and he'll go \"what about your grades\" like go away.")
    $ setWait(57.018,58.519)
    $ speak(NICOLE, "He sounds like a weekend dad.")
    $ setWait(58.519,63.649)
    $ speak(EMILY, "He is a weekend dad. Every week I hope he dies so I don't have to see his ass on Saturday.")
    $ setWait(63.649,66.944)
    $ speak(NICOLE, "That's a good dynamic, so do you guys actually do the essays here?")
    show emily sc3
    $ setWait(66.944,69.989)
    $ speak(EMILY, "Yeah in remedial you have to or they transfer you to a hood school.")
    show nicole sc4 angry
    $ setWait(69.989,71.324)
    $ speak(NICOLE, "Dude that's such bullshit.")
    $ setWait(71.324,74.911)
    $ speak(EMILY, "I wouldn't worry, they're not expecting a good paper. It's remedial, right?")
    show nicole sc4
    $ setWait(74.911,79.749)
    $ speak(NICOLE, "I guess but like modern poetry? How do I even write half a page on modern poetry?")
    $ setWait(79.749,82.46)
    $ speak(EMILY, "Every paper here's just zoning out 'till the last minute.")
    show emily sc3 smile
    $ setWait(82.46,84.462)
    $ speak(EMILY, "By the way you wanna pop C's with me?")
    $ setWait(84.462,85.254)
    $ speak(NICOLE, "Triple C's?")
    show emily sc3 angry
    $ setWait(85.254,86.964)
    $ speak(EMILY, "No bitch, quadruple C's.")
    $ setWait(86.964,87.965)
    $ speak(NICOLE, "How many you got?")
    show emily sc3 smile
    $ setWait(87.965,90.593)
    $ speak(EMILY, "Like a ton, I stole a bunch from Rite Aid yesterday.")
    $ setWait(90.593,91.886)
    $ speak(NICOLE, "They weren't behind the counter?")
    $ setWait(91.886,95.223)
    $ speak(EMILY, "Yeah you get far away enough from the beltway they don't care at all.")
    $ setWait(95.223,96.933)
    $ speak(NICOLE, "Now if only I had a car.")
    $ setWait(96.933,98.81)
    $ speak(EMILY, "So you wanna do 'em with me?")
    show nicole sc4 sad
    $ setWait(98.81,101.646)
    $ speak(NICOLE, "...Maybe a little early to get high on cough medicine.")
    show emily sc3 upset

    $ setWait(101.646,103.564)
    $ speak(EMILY, "What like we're too young for it?")
    show nicole sc4 angry

    $ setWait(103.564,105.149)
    $ speak(NICOLE, "Bitch it's 10:30.")
    stop ambient fadeout 1
    jump scene_0123
label scene_0123:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0123.mp3")
    scene school int 1
    show ames 1:
        leftmidstage
        xzoom -1
        linear 4.5 off_right

    show kylar sc2:
        xzoom -1
        leftstage
        linear 6 off_right

    show braxton sc2:
        xzoom -1
        off_left
        linear 6.8 off_right

    show emily sc3 angry:
        xzoom -1
        off_left
        pause 2
        linear 4 leftcenterstage

    show nicole sc4:
        off_left
        pause 2.4
        linear 4.5 leftmidstage

    $ setWait(0.037,1.997)
    $ speak(AMES, "This way, quickly!")
    $ setWait(1.997,6.46)
    $ speak(AMES, "Ugh how do I reach these kids? How do I show them there's more out there?")
    $ setWait(6.46,7.962)
    $ speak(EMILY, "I hate her so much.")
    $ setWait(7.962,10.13)
    $ speak(NICOLE, "They really picked the right teacher for punishment.")
    show emily sc3 upset:
        xzoom 1
        leftcenterstage

    $ setWait(10.13,12.216)
    $ speak(EMILY, "Oh my god I can't even go back there.")
    $ setWait(12.216,13.55)
    $ speak(NICOLE, "What, are you gonna skip?")
    show emily sc3
    $ setWait(13.55,14.301)
    $ speak(EMILY, "Do you wanna?")
    show nicole sc4 sad:
        leftmidstage
        xzoom 1

    $ setWait(14.301,17.805)
    $ speak(NICOLE, "But if we don't do the paper don't they send us to some hood school or whatever?")
    $ setWait(17.805,21.934)
    $ speak(EMILY, "Dude it's just one class, it's not like we won't finish the paper missing one class.")
    show nicole sc4
    $ setWait(21.934,23.519)
    $ speak(NICOLE, "Well where do you wanna go?")
    $ setWait(23.519,28.565)
    $ speak(EMILY, "I don't know, out, around? I got a prescription to pick up, we could go do that.")
    $ setWait(28.565,32.486)
    $ speak(NICOLE, "Do that as in go there? Or do that as in abuse the prescription?")

    show emily sc3 sad

    $ setWait(32.486,35.823)
    $ speak(EMILY, "No you can't do that with Seroquel, it's not a fun high.")
    $ setWait(35.823,38.158)
    $ speak(NICOLE, "Oh, so what's Seroquel for?")
    show emily sc3
    $ setWait(38.158,39.66)
    $ speak(EMILY, "It's like an anti-psychotic.")
    $ setWait(39.66,42.788)
    $ speak(NICOLE, "It's like an anti-psychotic or it's an anti-psychotic?")
    $ setWait(42.788,47.626)
    $ speak(EMILY, "I don't know it just makes you sleepy. My Mom forced me to get it after I slashed her tires.")
    $ setWait(47.626,49.044)
    $ speak(NICOLE, "Cool...")
    $ setWait(49.044,51.13)
    $ speak(EMILY, "Yeah, so you wanna go with me?")
    $ setWait(51.13,52.589)
    $ speak(NICOLE, "Why can't you just go yourself?")
    show emily sc3 angry
    $ setWait(52.589,56.093)
    $ speak(EMILY, "I'm not gonna skip alone. That's like a step above reading at lunch alone.")
    show nicole sc4 angry
    $ setWait(56.093,58.262)
    $ speak(NICOLE, "Just ask some other psycho remedial kid.")
    show emily sc3 upset
    $ setWait(58.262,61.015)
    $ speak(EMILY, "No they're all shitty, I wanna go with someone cool.")
    show nicole sc4
    $ setWait(61.015,62.016)
    $ speak(NICOLE, "Are you hitting on me?")
    show emily sc3 sad
    $ setWait(62.016,63.851)
    $ speak(EMILY, "Wha- No! I got a boyfriend.")
    $ setWait(63.851,65.686)
    $ speak(NICOLE, "But do you actually love him?")
    $ setWait(65.686,68.147)
    $ speak(EMILY, "Yeah... No...")
    show emily sc3
    $ setWait(68.147,69.815)
    $ speak(EMILY, "I love that my parents hate him!")
    $ setWait(69.815,70.566)
    $ speak(NICOLE, "Close enough.")
    show emily sc3 sad
    $ setWait(70.566,72.693)
    $ speak(EMILY, "But seriously c'mon let's go.")
    menu:
        "DO SOMETHING EVIL\nWITH THE ESSAY":
            jump scene_0124
        "SKIP SCHOOL WITH\nVIOLENT ALT GIRL":
            jump scene_0132
label scene_0124:
    $ setVoiceTrack("audio/Scenes/0124.mp3")
    scene school int 1

    show nicole sc4 sad:
        leftmidstage

    show emily sc3:
        leftcenterstage

    $ setWait(0.036,3.289)
    $ speak(NICOLE, "I kinda wanna but I just can't right now.")
    show emily sc3 sad
    $ setWait(3.289,6.793)
    $ speak(EMILY, "I told you the papers don't need to be good, they just need to be done.")
    show nicole sc4

    $ setWait(6.793,8.878)
    $ speak(NICOLE, "Yeah but I want it to be good to me.")
    show emily sc3 upset

    $ setWait(8.878,10.797)
    $ speak(EMILY, "What so you care about school now?")
    $ setWait(10.797,13.883)
    $ speak(NICOLE, "Never said that. Good to me but bad for the teacher.")
    show emily sc3 smile

    $ setWait(13.883,15.218)
    $ speak(EMILY, "Oh so you're plotting.")
    show nicole sc4 smile

    $ setWait(15.218,21.516)
    $ speak(NICOLE, "I'm plotting heavy. I wanna write something that gets me the grade but destroys her reputation.")
    show emily sc3
    $ setWait(21.516,25.269)
    $ speak(EMILY, "This sounds like way too much effort. How would you even do that?")
    $ setWait(25.269,32.777)
    $ speak(NICOLE, "Everybody has biases. And when push comes to shove those biases turn into major personality flaws.")
    $ setWait(32.777,34.737)
    $ speak(EMILY, "Are you trying to get Ms. Ames fired?")
    $ setWait(34.737,43.204)
    $ speak(NICOLE, "Maybe, and if I can't get her fired I'm perfectly happy with showing her she's just another democrat in a gated community.")
    $ setWait(43.204,47.375)
    $ speak(EMILY, "Yeah she's really afraid of rap music too.\nBut then again she likes 2pac.")
    show nicole sc4
    $ setWait(47.375,52.213)
    $ speak(NICOLE, "Does she like 2pac? Or does she feel obligated to mention 2pac?")
    show emily sc3 sad
    $ setWait(52.213,55.675)
    $ speak(EMILY, "Oh shit, yeah she always says that as a response to something.")
    $ setWait(55.675,59.47)
    $ speak(NICOLE, "Yeah so I'm gonna go back to class, I need to do some research.")
    show emily sc3
    $ setWait(59.47,62.473)
    $ speak(EMILY, "Okay well I'm gonna skip anyway. Do you wanna hang out though?")
    show nicole sc4 smile

    $ setWait(62.473,65.393)
    $ speak(NICOLE, "Y'know yeah, come over after school.")
    $ setWait(65.393,68.646)
    $ speak(EMILY, "Seriously? Your Mom's not gonna bitch about it or anything?")
    show nicole sc4 angry

    $ setWait(68.646,70.648)
    $ speak(NICOLE, "I mean she will but fuck her.")
    show emily sc3 smile:
        leftcenterstage
        linear 3 off_left
    $ setWait(70.648,72.817)
    $ speak(EMILY, "Yeah I get it, I'll see you tonight.")
    stop ambient fadeout 1
    jump scene_0125
label scene_0125:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Classroom_Ambience_2.mp3" fadein 1

    $ setVoiceTrack("audio/Scenes/0125.mp3")
    scene classroom int 4
    show kylar sc2:
        rightcenterstage

    show braxton sc2:
        rightstage

    show nicole sc4:
        xzoom -1
        rightmidstage

    $ setWait(0.036,2.038)
    $ speak(KYLAR, "You had to make this shit about poetry.")
    show ames 1:
        xzoom -1
        off_left
        linear 1.5 leftmidstage

    $ setWait(2.038,3.54)
    $ speak(AMES, "Are we having trouble over here?")
    $ setWait(3.54,7.627)
    $ speak(KYLAR, "These poetry books suck ass, can I just say the state of modern poetry sucks ass?")
    $ setWait(7.627,9.296)
    $ speak(AMES, "Remember, four pages.")
    $ setWait(9.296,13.675)
    $ speak(KYLAR, "So can I just copy and paste \"modern poetry sucks ass\" until it fills four pages?")
    show nicole sc4 angry


    $ setWait(13.675,16.094)
    $ speak(NICOLE, "Are these books you gave us really all we're allowed to use?")
    $ setWait(16.094,22.142)
    $ speak(AMES, "Unless you're able to find some contemporary works on your own. And that's other than the rap on your iPods.")
    $ setWait(22.142,23.81)
    $ speak(KYLAR, "But what if it's meaningful rap?")
    show ames 1 smug
    $ setWait(23.81,32.903)
    $ speak(AMES, "And what's the likelihood of that? You find a stanza about drug use and misogyny? There will be no papers on the meaning of hos in this classroom.")
    show nicole sc4
    $ setWait(32.903,34.237)
    $ speak(NICOLE, "Not a big fan, huh?")
    $ setWait(34.237,40.702)
    $ speak(AMES, "I won't lecture you on intellectually stimulating music but I think it's necessary to not voluntarily degrade yourself.")
    $ setWait(40.702,46.166)
    $ speak(NICOLE, "Uh huh so... What if the angle is on how rap is bad?")
    show ames 1
    $ setWait(46.166,47.292)
    $ speak(AMES, "I'm listening.")
    show nicole sc4 smile

    $ setWait(47.292,52.172)
    $ speak(NICOLE, "I could do a paper on this culture of rap and how it's so awful now.")
    $ setWait(52.172,54.382)
    $ speak(AMES, "That would be a new one.")
    show ames 1 smile
    $ setWait(54.382,60.805)
    $ speak(AMES, "You can try that, just make sure to give it real effort even if it might disagree with your some of your stances.")
    $ setWait(60.805,65.352)
    $ speak(NICOLE, "I'll try my best. Who knows, studying some other opinion might change my mind.")
    show ames 1 smile:
        xzoom 1
        leftmidstage
        linear 1 leftstage

    show nicole sc4

    $ setWait(65.352,67.729)
    $ speak(AMES, "Finally reaching these kids.")
    show ames 1:
        pause 0.6
        xzoom -1
    $ setWait(67.729,69.856)
    $ speak(KYLAR, "Reaching what? Is this like a movie for you?")
    $ setWait(69.856,73.652)
    $ speak(NICOLE, "Yeah we're not black or Mexican or anything you don't need to feel good about helping us.")
    show ames 1 angry:
        xzoom 1
        leftstage
        linear 1 off_left

    $ setWait(73.652,74.611)
    $ speak(AMES, "Back to work.")
    stop ambient fadeout 1
    jump scene_0126
label scene_0126:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.252):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 0.66 truecenter

    $ setVoiceTrack("audio/Scenes/0126.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home nicole int
    show nicole sc4:
        leftcenterstage

    show mom deli smile:
        off_right
        linear 3.3 rightcenterstage

    $ setWait(0.04,3.377)
    $ speak(MOM, "Ugh today was hard but still rewarding.")
    $ setWait(3.377,4.127)
    $ speak(NICOLE, "What was?")
    $ setWait(4.127,6.38)
    $ speak(MOM, "My day working at the deli?")
    $ setWait(6.38,9.049)
    $ speak(NICOLE, "Oh. I wasn't asking but alright.")
    show mom deli:
        rightcenterstage

    $ setWait(9.049,10.759)
    $ speak(MOM, "You don't wanna hear what happened?")
    $ setWait(10.759,11.676)
    $ speak(NICOLE, "I think I'm good.")
    show mom deli upset

    $ setWait(11.676,15.263)
    $ speak(MOM, "Nicole, just because I'm your mother doesn't mean you can take me for granted.")
    $ setWait(15.263,17.057)
    $ speak(NICOLE, "Who said I was taking you for granted?")
    $ setWait(17.057,19.893)
    $ speak(MOM, "Then talk with me like you would with anyone else.")
    $ setWait(19.893,24.523)
    $ speak(NICOLE, "This is how I talk with anyone else. Somebody says boring shit and I let 'em know I'm not interested.")
    $ setWait(24.523,28.276)
    $ speak(MOM, "Y'know it's not surprising why you only have one friend at school.")
    show nicole sc4 angry
    $ setWait(28.276,29.653)
    $ speak(NICOLE, "I have more than one friend.")
    $ setWait(29.653,31.113)
    $ speak(MOM, "Oh yeah? Who?")
    $ setWait(31.113,31.822)
    $ speak(NICOLE, "Emily.")
    $ setWait(31.822,33.281)
    $ speak(MOM, "Who the fuck is Emily?")
    show nicole sc4

    $ setWait(33.281,37.744)
    $ speak(NICOLE, "Girl that goes to my school. She's pretty cool and way more fucked up on drugs than I am.")
    show mom deli

    $ setWait(37.744,41.164)
    $ speak(MOM, "Really now... And you're not making this up, right?")
    show nicole sc4 angry

    $ setWait(41.164,47.337)
    $ speak(NICOLE, "Mom I'm not gonna make up a person to look less lonely. Am I some guy on AOL with a model girlfriend?")
    $ setWait(47.337,49.923)
    $ speak(MOM, "Alright, okay, what's her last name then?")
    $ setWait(49.923,50.757)
    $ speak(NICOLE, "I don't know.")
    $ setWait(50.757,51.842)
    $ speak(MOM, "I knew it.")
    $ setWait(51.842,54.845)
    $ speak(NICOLE, "Mom I'm not a cop who just asks for people's full names.")
    $ setWait(54.845,57.431)
    $ speak(MOM, "Well if she's real why don't you invite her over?")
    $ setWait(57.431,58.348)
    $ speak(NICOLE, "You wanna meet her?")
    $ setWait(58.348,59.474)
    $ speak(MOM, "I'd love to.")
    show nicole sc4 smile

    $ setWait(59.474,61.601)
    $ speak(NICOLE, "Cool, cause she's coming over in five minutes.")
    show mom deli angry

    $ setWait(61.601,62.227)
    $ speak(MOM, "What??")
    show nicole sc4

    $ setWait(62.227,63.353)
    $ speak(NICOLE, "You said you wanna meet her.")
    $ setWait(63.353,65.856)
    $ speak(MOM, "How could you invite someone over? This place is a mess!")
    $ setWait(65.856,68.275)
    $ speak(NICOLE, "Well she's a mess too, it's a perfect match.")
    show mom deli upset:
        rightcenterstage
        linear 2.65 leftstage
        xzoom -1

    $ setWait(68.275,72.612)
    $ speak(MOM, "Oh my god every little comment will just come back to haunt me. Tell her she can't come!")
    show nicole sc4:
        leftcenterstage
        linear 2.2 off_right

    $ setWait(72.612,73.28)
    $ speak(NICOLE, "Too late.")
    $ setWait(73.28,75.991)
    $ speak(MOM, "And I'm still in my work apron.")
    show nicole sc4:
        off_right
        linear .6 rightmidstage

    show emily sc3:
        off_right
        linear .65 rightstage

    $ setWait(75.991,76.741)
    $ speak(EMILY, "Hey.")
    show nicole sc4:
        rightmidstage
        pause 1
        xzoom -1
        linear 1.35 leftcenterstage

    show emily sc3:
        rightstage
        pause 1.23
        linear 1.1 rightcenterstage

    $ setWait(76.741,78.493)
    $ speak(NICOLE, "Yeah hey, let's head to my room.")
    show mom deli:
        leftstage
        xzoom -1
        linear 1 leftmidstage

    $ setWait(78.493,80.454)
    $ speak(MOM, "Nicole, you're not gonna introduce us?")

    show nicole sc4 angry:
        leftcenterstage
        xzoom -1

    $ setWait(80.454,82.497)
    $ speak(NICOLE, "Mom do not fucking do this right now.")
    show mom deli upset

    $ setWait(82.497,84.541)
    $ speak(MOM, "What? I can't even know her name?")
    $ setWait(84.541,85.333)
    $ speak(EMILY, "Emily?")
    show mom deli smile
    $ setWait(85.333,88.003)
    $ speak(MOM, "Hello Emily it's nice to meet you.")
    $ setWait(88.003,89.296)
    $ speak(NICOLE, "You are such a fucking bitch.")
    show mom deli upset
    $ setWait(89.296,95.343)
    $ speak(MOM, "Nicole! Don't call me a bitch in front of your friends! I'm sure Emily doesn't call her mother a bitch.")
    $ setWait(95.343,96.803)
    $ speak(EMILY, "You can believe that.")
    $ setWait(96.803,97.679)
    $ speak(MOM, "Excuse me?")
    $ setWait(97.679,99.473)
    $ speak(NICOLE, "Okay mom so we gotta go to my room now!")
    show mom deli
    $ setWait(99.473,104.769)
    $ speak(MOM, "Well hold on, I'd like to know some more about your friend. Emily what do your parents do?")
    $ setWait(104.769,107.522)
    $ speak(EMILY, "Uh my mom is like a nurse or something?")
    $ setWait(107.522,109.107)
    $ speak(MOM, "A nurse practitioner?")
    $ setWait(109.107,110.65)
    $ speak(EMILY, "Yeah I think so.")
    show mom deli smile

    $ setWait(110.65,112.694)
    $ speak(MOM, "Ooh, and how bout your father?")
    $ setWait(112.694,117.866)
    $ speak(EMILY, "He's a boardroom person for a non-profit. It's called United Police Fund?")
    $ setWait(117.866,121.995)
    $ speak(MOM, "Oh I see them collecting donations at the mall sometimes.")
    show emily sc3 upset
    $ setWait(121.995,123.497)
    $ speak(EMILY, "That's really interesting.")
    show nicole sc4:
        xzoom 1
        leftcenterstage

    show emily sc3

    $ setWait(123.497,124.831)
    $ speak(NICOLE, "Yeah okay so let's go.")
    $ setWait(124.831,130.42)
    $ speak(MOM, "Before you leave I just wanted to say it's very nice to meet a friend of Nicole's with such an impressive background.")
    show nicole sc4 angry:
        xzoom -1
    $ setWait(130.42,132.005)
    $ speak(NICOLE, "You didn't even ask about her!")
    show mom deli:
        leftmidstage
        xzoom 1
        linear 3 off_left

    $ setWait(132.005,135.383)
    $ speak(MOM, "I'd love to but I need to take care of some things, I'll see you later.")
    show nicole sc4 angry:
        xzoom 1
    $ setWait(135.383,136.801)
    $ speak(NICOLE, "You never told me you were rich.")
    show emily sc3 sad
    $ setWait(136.801,138.011)
    $ speak(EMILY, "Is that rich for real?")
    $ setWait(138.011,140.805)
    $ speak(NICOLE, "God now I look like an even trashier bitch.")
    show emily sc3
    $ setWait(140.805,142.641)
    $ speak(EMILY, "So are we going to your room?")
    show nicole sc4

    $ setWait(142.641,145.185)
    $ speak(NICOLE, "I kinda just want you to go home now.")
    stop ambient fadeout 1
    jump scene_0127
label scene_0127:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Cafeteria_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0127.mp3")
    scene cafeteria int 2
    show kelly sc3:
        xzoom -1
        leftcenterstage

    show jecka sc4:
        rightcenterstage

    $ setWait(0.079,1.872)
    $ speak(KELLY, "Are you gonna see Nick & Norah?")
    $ setWait(1.872,2.915)
    $ speak(JECKA, "Wait- see who?")
    $ setWait(2.915,6.919)
    $ speak(KELLY, "It's the new like romance movie with the guy from Superbad.")
    show jecka sc4 sad
    $ setWait(6.919,9.213)
    $ speak(JECKA, "They put McLovin in a romance movie?")
    $ setWait(9.213,10.131)
    $ speak(KELLY, "No the other one.")
    show jecka sc4 angry
    $ setWait(10.131,12.299)
    $ speak(JECKA, "Who would watch a romance with that fat piece of shit?")
    show kelly sc3 angry
    $ setWait(12.299,14.218)
    $ speak(KELLY, "No the other other one.")
    show jecka sc4 surprised
    $ setWait(14.218,16.929)
    $ speak(JECKA, "Oh wait! Yeah no I saw the preview for that.")
    show jecka sc4
    show kelly sc3

    $ setWait(16.929,18.889)
    $ speak(KELLY, "Yeah... So are you gonna see it?")
    $ setWait(18.889,21.475)
    $ speak(JECKA, "No, why would they make a romance starring ugly people?")
    $ setWait(21.475,23.436)
    $ speak(KELLY, "It's like different and free spirited.")

    show nicole sc5:
        off_left
        linear 1.3 leftmidstage

    $ setWait(23.436,24.603)
    $ speak(NICOLE, "Are we talking about me?")
    show kelly sc3 angry:
        xzoom 1

    show jecka sc4 surprised

    $ setWait(24.603,26.439)
    $ speak(KELLY, "No, Nick & Norah!")
    $ setWait(26.439,27.565)
    $ speak(JECKA, "What are you doing here??")
    show nicole sc5

    $ setWait(27.565,30.234)
    $ speak(NICOLE, "Nothing right now, you got any good shit on you?")
    show kelly sc3

    show jecka sc4
    $ setWait(30.234,32.987)
    $ speak(KELLY, "Jecka said you're in remedial classes?")
    $ setWait(32.987,34.155)
    $ speak(NICOLE, "Yeah what of it?")
    show kelly sc3 sad

    $ setWait(34.155,38.284)
    $ speak(KELLY, "Don't you have a different lunch from the rest of us? Are you skipping remedial?")
    show nicole sc5 angry

    $ setWait(38.284,40.619)
    $ speak(NICOLE, "Snitch and I'll drown you in your dad's swimming pool.")
    show kelly sc3 angry:
        pause 0.9
        xzoom -1

    $ setWait(40.619,43.038)
    $ speak(KELLY, "What the hell? C'mon Jecka let's go.")
    $ setWait(43.038,43.914)
    $ speak(JECKA, "You can go.")
    $ setWait(43.914,45.624)
    $ speak(KELLY, "No I meant go with me?")
    show jecka sc4 angry

    $ setWait(45.624,47.543)
    $ speak(JECKA, "Why the fuck would I go with you? Bye.")
    show kelly sc3 sad

    $ setWait(47.543,49.003)
    $ speak(KELLY, "I thought we were friends!")
    show jecka sc4

    $ setWait(49.003,51.881)
    $ speak(JECKA, "I only sit with you so I don't sit at lunch alone like the weird kids.")
    $ setWait(51.881,53.34)
    $ speak(NICOLE, "Damn, shit hurts.")
    show kelly sc3 angry:
        leftcenterstage
        xzoom 1
        linear 3 off_farleft

    $ setWait(53.34,55.926)
    $ speak(KELLY, "Fuck you guys... Whores...")
    show nicole sc5:
        leftmidstage
        linear 1 leftcenterstage

    $ setWait(55.926,58.095)
    $ speak(NICOLE, "Dude how have you handled a week of Kelly?")
    $ setWait(58.095,60.055)
    $ speak(JECKA, "No she's pretty entertaining.")
    $ setWait(60.055,66.353)
    $ speak(NICOLE, "Entertaining like Britney Spears in 1999 or like Britney Spears now?")
    $ setWait(66.353,71.484)
    $ speak(JECKA, "Oh Britney Spears now for sure. All of her stories start with her and a guy who graduated three years ago.")
    $ setWait(71.484,72.359)
    $ speak(NICOLE, "How do they end?")
    show jecka sc4 smile
    $ setWait(72.359,76.155)
    $ speak(JECKA, "Last weekend she told me she went down on a guy during High School Musical 3.")
    $ setWait(76.155,78.073)
    $ speak(NICOLE, "Is that the one in theaters right now?")
    $ setWait(78.073,78.657)
    $ speak(JECKA, "Yeah.")
    show nicole sc5
    $ setWait(78.657,80.993)
    $ speak(NICOLE, "That movie's for children, why would she do it there?")
    show jecka sc4
    $ setWait(80.993,84.246)
    $ speak(JECKA, "I don't know but there was a baby crying two rows down while she did it.")
    $ setWait(84.246,85.164)
    $ speak(NICOLE, "Was it Kelly's?")
    $ setWait(85.164,86.957)
    $ speak(JECKA, "Not yet, so why're you here?")
    $ setWait(86.957,89.001)
    $ speak(NICOLE, "I need a little help with a paper.")
    show jecka sc4 angry

    $ setWait(89.001,92.88)
    $ speak(JECKA, "Since when, the fuck, do you care about turning in a good paper?")
    $ setWait(92.88,100.221)
    $ speak(NICOLE, "Since I got an idea to fuck over a teacher with it. Ms. Ames wants us to do a paper on modern poetry and hates rap music.")
    show jecka sc4

    $ setWait(100.221,103.516)
    $ speak(JECKA, "So... you think she's racist? I don't follow.")
    $ setWait(103.516,108.896)
    $ speak(NICOLE, "I know she's racist and I wanna write something where she shows her whole ass over it.")
    show jecka sc4 angry

    $ setWait(108.896,114.527)
    $ speak(JECKA, "Nicole if you write about rap music being good you're just gonna get an F which won't prove shit cause all your other papers get F's.")
    $ setWait(114.527,122.326)
    $ speak(NICOLE, "No no no no, I'm gonna write a paper that agrees with her. And if she agrees with it back it's gonna get her fired.")
    show jecka sc4

    $ setWait(122.326,125.746)
    $ speak(JECKA, "Yeah but you're gonna write the racist paper she agrees with.")
    $ setWait(125.746,127.164)
    $ speak(NICOLE, "I'm a kid, what do I know?")
    $ setWait(127.164,131.418)
    $ speak(JECKA, "Then how could I possibly help you with this? Do you wanna ask my Dad about Katrina refugees?")
    $ setWait(131.418,136.757)
    $ speak(NICOLE, "Well no so you read books and shit, is there like a really racist book I could just plagiarize?")
    show jecka sc4 sad
    $ setWait(136.757,140.678)
    $ speak(JECKA, "Uh.. I have the English version of Mein Kampf if you wanna borrow it.")
    $ setWait(140.678,143.013)
    $ speak(NICOLE, "Why do you have the Hitler book in your backpack?")
    show jecka sc4

    $ setWait(143.013,145.307)
    $ speak(JECKA, "They assign parts of it for AP History.")
    $ setWait(145.307,149.103)
    $ speak(NICOLE, "Bitch you pop pills and fuck on the first date, why are you in AP History?")
    show jecka sc4 angry
    $ setWait(149.103,151.689)
    $ speak(JECKA, "Cause maybe I wanna fuck on the third date one day??")
    $ setWait(151.689,152.982)
    $ speak(NICOLE, "Literally for who?")
    $ setWait(152.982,157.111)
    $ speak(JECKA, "Ryan Sheckler obviously, and he's not gonna marry some dumb blonde ho, I know that.")
    show nicole sc5 smile
    $ setWait(157.111,159.78)
    $ speak(NICOLE, "But a smart blonde ho, that's where the alimony is.")
    show jecka sc4 smile
    $ setWait(159.78,165.077)
    $ speak(JECKA, "By the time I graduate I'll know three different languages so I'll be set to impress when I see him at the X-Games.")
    show nicole sc5
    $ setWait(165.077,167.83)
    $ speak(NICOLE, "You only take French, giving head isn't a third language.")
    show jecka sc4 angry

    $ setWait(167.83,169.999)
    $ speak(JECKA, "It is if you're good at it. Take the book.")
    stop ambient fadeout 1.35
    jump scene_0128
label scene_0128:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show diner ext with Pause(2.172):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.172 zoom 0.65 truecenter
    $ setVoiceTrack("audio/Scenes/0128.mp3")
    play ambient "audio/Ambience/Diner_Ambience.mp3"
    scene diner int
    show nicole sc6:
        centerstage

    $ setWait(2.172,7.636)
    $ speak(NICOLE, "Reading Mein Kampf alone at the diner, let's see guys turn this into a conversation starter.")
    $ setWait(7.636,17.646)
    $ speak(NICOLE, "\"Hence today I believe that I am acting in accordance with the will of the almighty creator: by defending myself against the Jew.\"")
    $ setWait(17.646,25.32)
    $ speak(NICOLE, "Okay let's cross out \"Jew\" and replace that with \"rappers\"... What else?")
    $ setWait(25.32,30.951)
    $ speak(NICOLE, "\"The ignorance of the broad masses about the inner nature of the J--\"")
    $ setWait(30.951,40.377)
    $ speak(NICOLE, "Hip-Hop artists... if you could even call them that.")
    show nicole sc6 smile

    $ setWait(40.377,42.587)
    $ speak(NICOLE, "This paper's gonna be so fuckin' easy.")

    show ari sc3:
        off_right
        linear 1.2 rightmidstage

    show nicole sc6

    $ setWait(42.587,45.34)
    $ speak(ARI, "Nicole? I didn't know you were in AP History.")
    $ setWait(45.34,47.926)
    $ speak(NICOLE, "Huh? No I'm not in AP History.")
    show ari sc3 angry:
        rightmidstage

    $ setWait(47.926,51.096)
    $ speak(ARI, "...Then why are you reading Mein Kampf?")
    $ setWait(51.096,52.722)
    $ speak(NICOLE, "I'm racist now.")
    show ari sc3:
        rightmidstage
        linear 3.2 off_left

    $ setWait(52.722,54.808)
    $ speak(ARI, "Oh alright.")
    show nicole sc6:
        xzoom -1
    $ setWait(54.808,57.936)
    $ speak(NICOLE, "Man Ari's cool about anything.")
    show crispin sc3 smile:
        xzoom -1
        off_left
        linear 1.6 leftmidstage

    $ setWait(57.936,59.354)
    $ speak(CRISPIN, "Oh hey hey what's up?")
    show nicole sc6 angry
    $ setWait(59.354,60.438)
    $ speak(NICOLE, "What the fuck do you want?")
    show crispin sc3

    $ setWait(60.438,67.821)
    $ speak(CRISPIN, "What? No nothing, just saw you reading and was like \"wow she looks real smart like that\". Is this like a usual thing for you?")
    show nicole sc6

    $ setWait(67.821,70.115)
    $ speak(NICOLE, "Reading in public? Sure.")
    $ setWait(70.115,72.784)
    $ speak(CRISPIN, "Yeah yeah so what'cha reading there?")
    $ setWait(72.784,73.743)
    $ speak(NICOLE, "Mein Kampf.")
    show crispin sc3 smile

    $ setWait(73.743,77.288)
    $ speak(CRISPIN, "Oh yeah I've heard of that, it's supposed to be really interesting right?")
    $ setWait(77.288,81.001)
    $ speak(NICOLE, "Uh huh, what do you think about it like specifically?")
    $ setWait(81.001,85.046)
    $ speak(CRISPIN, "I think it has uh, like really good themes and a story.")
    $ setWait(85.046,87.132)
    $ speak(NICOLE, "Big fan of the message in Mein Kampf?")
    $ setWait(87.132,89.342)
    $ speak(CRISPIN, "Yeah you could say that, what's your favorite part?")
    $ setWait(89.342,90.76)
    $ speak(NICOLE, "What's yours?")
    show crispin sc3
    $ setWait(90.76,93.304)
    $ speak(CRISPIN, "Oh uh, like the middle.")
    $ setWait(93.304,95.265)
    $ speak(NICOLE, "Did you read it in English or German?")
    $ setWait(95.265,97.434)
    $ speak(CRISPIN, "Was it in German first or something?")
    $ setWait(97.434,100.812)
    $ speak(NICOLE, "Yeah it's the only German book America cares about.")
    show crispin sc3 smile

    $ setWait(100.812,104.274)
    $ speak(CRISPIN, "Oh that just means it's super good then, I should recommend it to a friend, right?")
    $ setWait(104.274,106.192)
    $ speak(NICOLE, "Right.")
    $ setWait(106.192,107.819)
    $ speak(CRISPIN, "S-so can I sit with you?")
    show nicole sc6 angry

    $ setWait(107.819,109.821)
    $ speak(NICOLE, "Mein Kampf is the Nazi book.")
    $ setWait(109.821,112.866)
    $ speak(CRISPIN, "Oh cool I didn't know that, so can I sit with you?")
    stop ambient fadeout 1
    jump scene_0129
label scene_0129:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Classroom_Ambience_2.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0129.mp3")
    scene classroom int 4
    show emily sc4 angry:
        rightstage

    show kylar sc3:
        rightcenterstage

    show nicole sc2:
        rightmidstage
        xzoom -1

    $ setWait(0.044,2.129)
    $ speak(EMILY, "Why do they block MySpace on the wifi?")
    show kylar sc3:
        xzoom -1
    $ setWait(2.129,3.839)
    $ speak(KYLAR, "Cause you're not supposed to be on it, duh.")

    show nicole sc2 angry

    $ setWait(3.839,6.342)
    $ speak(NICOLE, "How the fuck is there a narc in remedial class?")
    $ setWait(6.342,10.137)
    $ speak(EMILY, "Yeah all I wanna do is see what this bitch is saying about her infected snake bites.")
    show nicole sc2

    $ setWait(10.137,12.848)
    $ speak(NICOLE, "To be emo and unclean, tragic.")
    show ames 2:
        off_left
        xzoom -1
        linear 1.3 leftmidstage

    show nicole sc2:
        xzoom -1

    show kylar sc3:
        xzoom 1

    $ setWait(12.848,17.561)
    $ speak(AMES, "Alright settle down, your papers were all interesting to say the least.")
    show kylar sc3 smile
    $ setWait(17.561,19.313)
    $ speak(KYLAR, "Yeah cause they're good as shit right?")
    $ setWait(19.313,21.023)
    $ speak(AMES, "Kylar. F!")
    show kylar sc3
    $ setWait(21.023,23.15)
    $ speak(KYLAR, "F!? I turned it in and everything!")
    $ setWait(23.15,28.656)
    $ speak(AMES, "Three paragraphs about how \"gay\" poetry is doesn't make for a comprehensive think piece.")
    $ setWait(28.656,30.116)
    $ speak(KYLAR, "I'll give you this stink piece, motherfucker.")
    show emily sc4 upset
    $ setWait(30.116,32.409)
    $ speak(EMILY, "How do you fail a paper in remedial English?")
    show kylar sc3 angry
    $ setWait(32.409,34.161)
    $ speak(KYLAR, "I didn't know we weren't allowed to tell the truth!")
    show emily sc4 smile
    $ setWait(34.161,36.038)
    $ speak(EMILY, "You're dumber than the bitches on Next.")
    show nicole sc2 smile
    show kylar sc3
    $ setWait(36.038,39.375)
    $ speak(NICOLE, "Yeah and MTV reality show hos are really fuckin' dumb.")
    $ setWait(39.375,41.252)
    $ speak(AMES, "Emily. D!")
    show emily sc4
    show nicole sc2
    $ setWait(41.252,43.421)
    $ speak(EMILY, "Are you even supposed to call our grades out like this?")
    $ setWait(43.421,45.464)
    $ speak(AMES, "Just so the class knows the bar they're setting.")
    show kylar sc3 smile:
        xzoom -1
    $ setWait(45.464,47.842)
    $ speak(KYLAR, "D in remedial? You're gonna end up on Next.")
    show kylar sc3:
        pause 0.5
        xzoom 1
    $ setWait(47.842,49.301)
    $ speak(AMES, "And Nicole...")
    show nicole sc2 sad
    $ setWait(49.301,50.803)
    $ speak(NICOLE, "Uh huh?")
    show ames 2 smile
    $ setWait(50.803,51.804)
    $ speak(AMES, "A!")
    show nicole sc2 surprised
    show emily sc4 sad
    $ setWait(51.804,52.513)
    $ speak(NICOLE, "A??")
    $ setWait(52.513,55.975)
    $ speak(EMILY, "A as in \"ay where the loud at\" or like the letter?")
    show nicole sc2
    $ setWait(55.975,61.814)
    $ speak(AMES, "Almost A plus if anything, I was happily surprised with the gripping prose you provided on rap music.")
    show emily sc4
    $ setWait(61.814,62.731)
    $ speak(EMILY, "So like the letter.")
    $ setWait(62.731,64.817)
    $ speak(NICOLE, "Really you thought it was that good?")
    $ setWait(64.817,75.453)
    $ speak(AMES, "It was excellent, the best paper I've ever received teaching these classes. The persuasive wording, direness of tone, as if you were a poetic politician wise beyond your years.")
    show nicole sc2 sad
    $ setWait(75.453,76.912)
    $ speak(NICOLE, "As if, right?")
    $ setWait(76.912,79.206)
    $ speak(EMILY, "Literally got an A, what're you white?")
    show nicole sc2:
        xzoom 1
    $ setWait(79.206,80.541)
    $ speak(NICOLE, "I've earned the title.")
    show nicole sc2:
        pause 0.5
        xzoom -1

    $ setWait(80.541,88.55)
    $ speak(AMES, "It's actually perfect timing because next week your principal is bringing a few members of the school board to demonstrate why this program is still worth funding.")
    $ setWait(88.55,93.929)
    $ speak(AMES, "With this paper I think it'll be obvious remedial programs can still reach troubled students.")
    $ setWait(93.929,95.764)
    $ speak(KYLAR, "What you're gonna like read the paper aloud?")
    $ setWait(95.764,101.312)
    $ speak(AMES, "Of course, an amateur written work like this deserves an audience. If it's okay with you, Nicole.")
    show nicole sc2 smile
    $ setWait(101.312,105.9)
    $ speak(NICOLE, "Um, yeah definitely. I think that is an amazing idea.")
    $ setWait(105.9,108.652)
    $ speak(AMES, "Great, and I trust you'll all be here this Friday.")
    show emily sc4 upset
    $ setWait(108.652,109.487)
    $ speak(EMILY, "Let's hope.")
    show ames 2 smug:
        xzoom -1
        leftmidstage
        pause 3
        linear 2 leftcenterstage

    $ setWait(109.487,114.158)
    $ speak(AMES, "Anyway for today's lesson. Slang. The death of the English language.")
    stop ambient fadeout 2
    jump scene_0130
label scene_0130:
    show black onlayer screens with Pause(1.8):
        alpha 0.0
        linear 1.2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show title_oneweeklater onlayer screens
    show school front with Pause(2.252):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.627 zoom 1.1 truecenter



    $ setVoiceTrack("audio/Scenes/0130.mp3")
    hide title_oneweeklater onlayer screens
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3"
    scene cafeteria int

    show nicole sc7 angry:
        leftcenterstage

    show emily sc5 upset:
        rightcenterstage

    $ setWait(0.079,3.082)
    $ speak(EMILY, "Why would they pick the cafeteria for this? It's freezing.")
    $ setWait(3.082,6.085)
    $ speak(NICOLE, "Yeah how many people could possibly be on the school board?")
    $ setWait(6.085,8.212)
    $ speak(EMILY, "What's the school board do anyway?")
    $ setWait(8.212,12.425)
    $ speak(NICOLE, "Stupid shit like making the lunch healthy and covering up sex scandals.")
    $ setWait(12.425,17.43)
    $ speak(EMILY, "At least with a scandal someone  enjoys themselves. When they fuck the chicken nuggets up everyone suffers.")
    $ setWait(17.43,20.35)
    $ speak(NICOLE, "I wish we were in California where the schools have food courts.")
    $ setWait(20.35,22.852)
    $ speak(EMILY, "Yeah then it'd be too far for your Mom to wander in.")
    show nicole sc7
    $ setWait(22.852,24.145)
    $ speak(NICOLE, "Yeah...")
    show nicole sc7 surprised

    $ setWait(24.145,24.979)
    $ speak(NICOLE, "Wait what?")
    show emily sc5
    $ setWait(24.979,28.524)
    $ speak(EMILY, "I saw your Mom in the hall 20 minutes ago. Is she picking you up early?")
    $ setWait(28.524,31.861)
    $ speak(NICOLE, "No? Wait what the fuck did you actually see my mom here??")
    $ setWait(31.861,34.864)
    $ speak(EMILY, "I'm pretty sure it was your Mom, she was with a bunch of people too.")
    show nicole sc7 sad
    $ setWait(34.864,39.077)
    $ speak(NICOLE, "What is wrong with her?? Why?? Are you sure you're not just hallucinating off those meds?")
    $ setWait(39.077,42.08)
    $ speak(EMILY, "No Seroquel doesn't make you hallucinate...")
    show emily sc5 sad
    $ setWait(42.08,43.122)
    $ speak(EMILY, "During the day.")
    $ setWait(43.122,44.207)
    $ speak(NICOLE, "I'm gonna kill myself.")
    show emily sc5

    $ setWait(44.207,45.166)
    $ speak(MOM, "Nicole!")

    show nicole sc7 angry:
        xzoom -1

    $ setWait(45.166,47.627)
    $ speak(NICOLE, "No-- Mom get the fuck out of here right now!")

    show mom deli:
        off_left
        xzoom -1
        linear 1.4 leftmidstage

    $ setWait(47.627,51.297)
    $ speak(MOM, "What? I can't see my daughter when we get called out to her school?")
    $ setWait(51.297,52.423)
    $ speak(NICOLE, "Called by who??")
    show mom deli smile
    $ setWait(52.423,63.142)
    $ speak(MOM, "Your principal called us at Rossler's Kosher Deli to cater your little remedial presentation. I was so proud to hear a paper you did would be the main event, I've been excited to hear this all week.")
    $ setWait(63.142,65.561)
    $ speak(NICOLE, "You knew about this for a week and didn't tell me?")
    $ setWait(65.561,67.271)
    $ speak(MOM, "I thought it'd be a fun surprise.")
    show emily sc5 upset

    $ setWait(67.271,68.272)
    $ speak(EMILY, "Why would they cater this?")
    show mom deli
    $ setWait(68.272,73.695)
    $ speak(NICOLE, "So instead of telling me so I could blackmail you to call in sick you just wanna swoop in and socially ruin me!")
    show emily sc5

    $ setWait(73.695,77.74)
    $ speak(MOM, "Oh you're so dramatic. I'm sure Emily wouldn't mind if her mother was here.")
    show emily sc5 angry

    $ setWait(77.74,79.617)
    $ speak(EMILY, "I would actually choke her.")
    show emily sc5

    $ setWait(79.617,82.078)
    $ speak(LYNN, "Right this way, here's our star students.")
    $ setWait(82.078,84.664)
    $ speak(ROSSLER, "Ay yo we need ya with the sandwich trays!")
    show mom deli:
        leftmidstage
        xzoom -1
        pause 1.8
        xzoom 1
        linear 1.7 off_left

    $ setWait(84.664,87.875)
    $ speak(MOM, "Looks like my boss needs me to set up. Good luck, sweetie.")
    show ames 3:
        off_left
        xzoom -1
        linear 2.7 rightcenterstage
        xzoom 1

    show nicole sc7:
        xzoom -1
        leftcenterstage
        pause 1.4
        linear 1.3 rightmidstage

    show emily sc5:
        rightcenterstage
        pause 1.9
        linear 1.2 rightstage

    $ setWait(87.875,91.629)
    $ speak(AMES, "School board members if you could just line around over there for our presentation.")
    show lynn 1:
        off_left
        xzoom -1
        linear 2.2 leftcenterstage
        xzoom 1

    $ setWait(91.629,97.468)
    $ speak(LYNN, "Yes, before we get to the catering we wanted to present just one of the works produced by this remedial program.")
    $ setWait(97.468,107.812)
    $ speak(AMES, "Right and as I've come to understand the remedial classes are up for renewal at the end of this school year. A lot of talk has gone around asking \"what's the point of helping these troublemaker students?\"")
    show lynn:
        xzoom 1
        pause 5.1
        xzoom -1
    $ setWait(107.812,115.319)
    $ speak(LYNN, "And after hearing this paper, we think you'll see the progress that can still be made here. Nicole, would you like to read your paper to the board?")
    show nicole sc7 surprised
    $ setWait(115.319,116.779)
    $ speak(NICOLE, "That is okay.")
    show ames 3:
        xzoom -1

    show lynn 1:
        xzoom 1
    $ setWait(116.779,118.823)
    $ speak(AMES, "Well I'd love to read it for you.")
    show nicole sc7 smile
    $ setWait(118.823,119.866)
    $ speak(NICOLE, "Go ahead.")

    show nicole sc7

    show ames 3 behind black:
        xzoom 1

    $ setWait(119.866,132.42)
    $ speak(AMES, "Right, so this is Nicole's paper I'll be reading for all of you. When Nicole first came to us she had a 1.1 GPA, several truancy violations, and even more in-school suspensions.")
    $ setWait(132.42,136.424)
    $ speak(LYNN, "I'm all too familiar.")
    $ setWait(136.424,138.384)
    $ speak(NICOLE, "Look at all these sexless marriages.")
    $ setWait(138.384,141.512)
    $ speak(AMES, "At first she didn't want anything to do with language arts...")
    $ setWait(141.512,151.647)
    $ speak(AMES, "...but after we exposed her to the right literature again and again, she was inspired to write this incredibly biting piece on contemporary music and poetry.")
    $ setWait(151.647,154.275)
    $ speak(ROSSLER, "This better not take forever, I got temple at three o'clock.")
    $ setWait(154.275,162.7)
    $ speak(AMES, "Ahem... \"As a teen I've come to be disappointed with the ignorance of the broad masses about the inner nature of rappers.\"")
    $ setWait(162.7,171.834)
    $ speak(AMES, "\"The lack of instinct and narrow-mindedness of our upper classes make the people an easy victim for Hip-hop's campaign of lies.\"")
    $ setWait(171.834,184.222)
    $ speak(AMES, "\"Little Wayne's domination in the state seems so assured that now not only can he call himself a rapper, but he ruthlessly admits his ultimate national and political designs.\"")
    show lynn 1:
        xzoom -1
    $ setWait(184.222,184.931)
    $ speak(LYNN, "Huh...")
    $ setWait(184.931,194.273)
    $ speak(AMES, "\"A section of his genre owns itself to be a foreign people, yet even here they lie. For a while the Zionists try to make the rest of the world believe that\"--")
    $ setWait(194.273,195.149)
    $ speak(ROSSLER, "What is this again?")
    show nicole sc7 sad
    $ setWait(195.149,195.691)
    $ speak(NICOLE, "Uh oh.")
    $ setWait(195.691,196.984)
    $ speak(AMES, "Catering, please don't interrupt.")
    show lynn 1 behind black:
        xzoom -1
        pause 4.7
        linear 5 off_left

    show nicole sc7 sad behind black:
        xzoom -1
        rightmidstage
        pause 4
        linear 4.5 off_right

    show emily sc5 behind black:
        rightstage
        pause 8.1
        linear 3 off_right

    stop ambient fadeout 15

    show black onlayer screens:
        alpha 0.0
        pause 9
        linear 4.4 alpha 1.0

    $ setWait(196.984,211.332)
    $ speak(AMES, "\"the Zionists try to make the rest of the world believe that the national consciousness of the rapper finds its satisfaction in the creation of MTV. The rappers again slyly dupe the dumb...\"")

    jump end_0131

label end_0131:

    show black onlayer screens:
        alpha 0.0

    scene black



    if "end_0131" not in persistent.endings:
        $ persistent.endings.append("end_0131")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0131.webm")

    return

label scene_0132:
    $ setVoiceTrack("audio/Scenes/0132.mp3")
    scene school int 1
    show nicole sc4 sad:
        leftmidstage

    show emily sc3:
        leftcenterstage


    $ setWait(0.043,2.588)
    $ speak(NICOLE, "God I really don't wanna go back either.")
    $ setWait(2.588,3.422)
    $ speak(EMILY, "See?")
    $ setWait(3.422,4.756)
    $ speak(NICOLE, "But I don't know...")
    show emily sc3 upset
    $ setWait(4.756,6.8)
    $ speak(EMILY, "You already know what you're getting if you go back there.")
    show nicole sc4 angry

    $ setWait(6.8,9.219)
    $ speak(NICOLE, "Some white bitch with wholesome bumper stickers.")
    show emily sc3 angry

    $ setWait(9.219,12.556)
    $ speak(EMILY, "And a sun damaged poster telling you your outfit doesn't matter.")
    $ setWait(12.556,15.058)
    $ speak(NICOLE, "Plus her whole stupid \"I don't own a TV\" attitude.")
    $ setWait(15.058,19.146)
    $ speak(EMILY, "Yeah so fuck that bitch. Fuck that petition-writing, Prius-driving bitch.")
    show nicole sc4

    $ setWait(19.146,22.441)
    $ speak(NICOLE, "Okay but if we don't go back to class where should we hang out then?")
    show emily sc3

    $ setWait(22.441,25.068)
    $ speak(EMILY, "I don't know, I have a car so pretty much anywhere we want.")
    $ setWait(25.068,26.528)
    $ speak(NICOLE, "What car you drive?")
    show emily sc3 smile
    $ setWait(26.528,29.031)
    $ speak(EMILY, "'98 Saturn.")
    $ setWait(29.031,31.408)
    $ speak(NICOLE, "You said that like a Saturn's badass or something.")
    show emily sc3 upset

    $ setWait(31.408,32.618)
    $ speak(EMILY, "It's the 2-door?")
    show nicole sc4 surprised
    $ setWait(32.618,33.744)
    $ speak(NICOLE, "Ohhh shit.")
    show nicole sc4
    $ setWait(33.744,37.998)
    $ speak(EMILY, "Yeah, but all the AC vents are chipped cause we kept using 'em as bottle openers.")
    show nicole sc4 smile
    show emily sc3 smile

    $ setWait(37.998,41.251)
    $ speak(NICOLE, "That's hot, you're like Avril Lavigne if she never got famous.")
    $ setWait(41.251,42.753)
    $ speak(EMILY, "I know, right?")
    $ setWait(42.753,43.837)
    $ speak(NICOLE, "Alright let's go.")
    $ setWait(43.837,46.048)
    $ speak(EMILY, "Cool, but first we gotta stop by my locker.")
    $ setWait(46.048,47.382)
    $ speak(NICOLE, "Yeah sure, what for?")
    show emily sc3:
        leftcenterstage
        xzoom -1
        linear 3.2 off_right

    show nicole sc4:
        leftmidstage
        pause 0.65
        linear 3.1 off_right

    $ setWait(47.382,49.676)
    $ speak(EMILY, "I need adderall to stop at stop signs.")
    stop ambient fadeout 1
    jump scene_0133
label scene_0133:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1

    $ setVoiceTrack("audio/Scenes/0133.mp3")
    scene school int 2

    show crispin sc4:
        xzoom -1
        rightstage

    show emily sc3 upset:
        xzoom -1
        off_left
        linear 1.4 leftcenterstage

    show nicole sc4:
        off_left
        pause 0.6
        linear 1 leftmidstage


    $ setWait(0.083,1.834)
    $ speak(EMILY, "Why does he have to be right in front of my locker?")

    show crispin sc4 smile:
        rightstage
        xzoom 1
        linear 1 rightcenterstage

    $ setWait(1.834,3.962)
    $ speak(CRISPIN, "Yo yo hey you guys hanging around too?")
    show nicole sc4 angry
    $ setWait(3.962,4.671)
    $ speak(NICOLE, "God dammit.")
    show emily sc3 angry
    $ setWait(4.671,8.424)
    $ speak(EMILY, "Is there a reason you're specifically here? Or are you just some annoying free spirit?")
    $ setWait(8.424,13.263)
    $ speak(CRISPIN, "Well if skipping to skip is free-spirited doesn't that make you guys free-spirited too? It's not a bad thing.")
    $ setWait(13.263,15.557)
    $ speak(EMILY, "When girls are free-spirited it's actually cute.")
    $ setWait(15.557,18.268)
    $ speak(NICOLE, "Yeah when men do it it's like fuck off go die in a war.")
    $ setWait(18.268,22.188)
    $ speak(EMILY, "Exactly so if you don't have any business here go to Iraq and leave us alone.")
    $ setWait(22.188,24.607)
    $ speak(CRISPIN, "Actually I kinda might have some business here.")
    $ setWait(24.607,26.025)
    $ speak(EMILY, "Business like what?")
    $ setWait(26.025,29.237)
    $ speak(CRISPIN, "Business like... I heard you buy bud.")
    $ setWait(29.237,30.154)
    $ speak(NICOLE, "Jesus Christ.")
    show emily sc3 upset
    $ setWait(30.154,31.281)
    $ speak(EMILY, "Doesn't everybody?")
    $ setWait(31.281,33.616)
    $ speak(CRISPIN, "Yeah but not everybody buys good shit.")
    $ setWait(33.616,35.368)
    $ speak(EMILY, "Okay what do you got, how much?")
    $ setWait(35.368,37.161)
    $ speak(CRISPIN, "A quarter for $180.")
    show emily sc3 angry
    show crispin sc4
    $ setWait(37.161,38.121)
    $ speak(EMILY, "$180??")
    show nicole sc4
    $ setWait(38.121,39.414)
    $ speak(NICOLE, "Is it laced with gold?")
    $ setWait(39.414,43.835)
    $ speak(CRISPIN, "I know there's cheaper stuff out there but this shit here.. This shit here is $180.")
    $ setWait(43.835,46.671)
    $ speak(EMILY, "You better turn 180 and walk away, gringo.")
    $ setWait(46.671,47.505)
    $ speak(NICOLE, "Gringo?")
    show emily sc3 smile:
        xzoom 1
    $ setWait(47.505,50.133)
    $ speak(EMILY, "My boyfriend's in MS-13, I have the pass.")
    $ setWait(50.133,52.385)
    $ speak(CRISPIN, "Okay so what? $175?")

    show emily sc3:
        xzoom -1

    $ setWait(52.385,54.304)
    $ speak(EMILY, "How bout $120 and a buzz?")
    $ setWait(54.304,56.347)
    $ speak(CRISPIN, "I'm open to trades, what you got?")
    show cut0133 onlayer screens
    $ setWait(56.347,57.974)
    $ speak(EMILY, "You're into X, right?")
    $ setWait(57.974,62.061)
    $ speak(CRISPIN, "I could be, but why's your X shiny and red? I-Is that cough medicine?")
    $ setWait(62.061,64.689)
    $ speak(NICOLE, "Dude no way, it's only like that cause she got it for Mardi Gras.")
    $ setWait(64.689,66.441)
    $ speak(EMILY, "Yeah blends in with the necklace.")
    hide cut0133 onlayer screens
    $ setWait(66.441,67.692)
    $ speak(CRISPIN, "Is red a Mardi Gras color?")
    show emily sc3 angry
    $ setWait(67.692,69.11)
    $ speak(EMILY, "Do you wanna get fucked up or not!?")
    $ setWait(69.11,70.32)
    $ speak(CRISPIN, "How do I know if they're good??")
    show emily sc3 smile
    $ setWait(70.32,73.323)
    $ speak(EMILY, "Take one- no actually take all of them cause they're kinda weak.")
    show black onlayer screens:
        alpha 0.0
        pause .6
        linear 0.6 alpha 1.0

    stop ambient fadeout 2
    $ setWait(73.323,78.911)
    $ speak(CRISPIN, "Okay...")
    play ambient "audio/Ambience/Hallway_Ambience.mp3" fadein 1.6
    show black onlayer screens:
        alpha 1.0
        linear 1.4 alpha 0.0

    show emily sc3 upset:
        rightmidstage
        xzoom 1

    show nicole sc4 surprised:
        leftmidstage

    hide crispin
    $ setWait(78.911,81.205)
    $ speak(NICOLE, "Damn that wasn't even 20 minutes.")
    show emily sc3 smile:
        rightmidstage
        xzoom 1
        pause 1.8
        xzoom -1
        linear 1.3 rightstage

    $ setWait(81.205,84.167)
    $ speak(EMILY, "Now I can finally open my locker, steal his shit by the way.")
    show nicole sc4 smile:
        leftmidstage
        linear 0.4 leftcenterstage

    $ setWait(84.167,86.628)
    $ speak(NICOLE, "Yeah I got it, that was really good.")
    show emily sc3 smile:
        xzoom 1
        rightstage
        linear 1 rightcenterstage

    $ setWait(86.628,89.422)
    $ speak(EMILY, "You were really good, the Mardi Gras save was awesome.")
    $ setWait(89.422,93.134)
    $ speak(NICOLE, "I was surprised you didn't fuck it up, when I try that with Jecka it takes her a second.")
    show emily sc3 sad
    $ setWait(93.134,94.51)
    $ speak(EMILY, "And then they'd know something's up.")
    $ setWait(94.51,97.263)
    $ speak(NICOLE, "Yeah exactly. We're really good at fucking with people.")
    show emily sc3 smile

    $ setWait(97.263,99.932)
    $ speak(EMILY, "I know, just wait 'till we get to the mall.")
    show nicole sc4 angry
    $ setWait(99.932,101.726)
    $ speak(NICOLE, "God this isn't even that much weed.")
    show emily sc3
    $ setWait(101.726,102.727)
    $ speak(EMILY, "You wanna roll some?")
    $ setWait(102.727,106.105)
    $ speak(NICOLE, "No marijuana's a baby drug, you can't even die smoking it.")
    show nicole sc4:
        xzoom -1
        leftcenterstage
        linear 3 off_left

    show emily sc3 upset:
        rightcenterstage
        pause 0.6
        linear 3 off_left

    $ setWait(106.105,108.191)
    $ speak(EMILY, "Okay we'll just sell it.")
    stop ambient fadeout 1
    jump scene_0134
label scene_0134:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 1

    $ setVoiceTrack("audio/Scenes/0134.mp3")
    scene mall int 2

    show emily sc3 smile:
        off_left
        xzoom -1
        linear 2.5 rightcenterstage
        xzoom 1

    show nicole sc4 smile:
        off_left
        pause 0.4
        linear 2.3 leftcenterstage


    $ setWait(0.077,3.122)
    $ speak(EMILY, "This might be the first time they ever actually restocked this mall.")
    $ setWait(3.122,6.083)
    $ speak(NICOLE, "Yeah did you see the \"Homicidal Slut\" shirt with a gun on it?")
    $ setWait(6.083,10.796)
    $ speak(EMILY, "The one in Spencers? Yeah that was awesome.\nWhat about those panties with Kurt Cobain's suicide note on them?")
    show nicole sc4
    $ setWait(10.796,13.09)
    $ speak(NICOLE, "Those were so hot- fuck we need money!")
    show emily sc3
    $ setWait(13.09,14.634)
    $ speak(EMILY, "We gotta sell this weed.")
    show jeffery sc3:
        xzoom -1
        off_left
        linear 1.2 leftmidstage

    show nicole sc4:
        pause 0.5
        xzoom -1

    $ setWait(14.634,18.054)
    $ speak(JEFFERY, "Emily and Nicole? I didn't know you guys were friends.")
    show nicole sc4:
        xzoom 1

    $ setWait(18.054,19.347)
    $ speak(NICOLE, "Why is Jeffery here?")
    show emily sc3 upset
    $ setWait(19.347,20.431)
    $ speak(EMILY, "You know his name?")
    $ setWait(20.431,21.223)
    $ speak(NICOLE, "You don't?")
    $ setWait(21.223,23.184)
    $ speak(EMILY, "No I just call him nerd shirt.")
    show nicole sc4:
        xzoom -1

    show emily sc3

    $ setWait(23.184,24.602)
    $ speak(NICOLE, "Jeffery why aren't you at school?")
    $ setWait(24.602,26.812)
    $ speak(JEFFERY, "It's 3:30, school's been over.")
    $ setWait(26.812,28.898)
    $ speak(EMILY, "Wow, time is like automatic in here.")
    $ setWait(28.898,33.069)
    $ speak(NICOLE, "Well Jeffery since you're out and about and everything... you tryna get faded?")
    $ setWait(33.069,35.821)
    $ speak(JEFFERY, "Faded? Are you gonna throw bleach on me again?")
    show emily sc3 smile
    $ setWait(35.821,40.952)
    $ speak(EMILY, "No no what she means is like.. are lookin' to blaze right now?")
    $ setWait(40.952,42.411)
    $ speak(JEFFERY, "Blaze...")
    show jeffery sc3 smile
    $ setWait(42.411,44.538)
    $ speak(JEFFERY, "Like Blaziken the Pokemon?")
    show emily sc3
    $ setWait(44.538,45.122)
    $ speak(EMILY, "What?")
    show nicole sc4 angry
    $ setWait(45.122,48.042)
    $ speak(NICOLE, "Pikachu's a Pokemon, what the fuck is Blaziken?")
    show jeffery sc3
    $ setWait(48.042,50.544)
    $ speak(JEFFERY, "Blaziken's a newer Pokemon.")
    show nicole sc4 surprised
    $ setWait(50.544,53.089)
    $ speak(NICOLE, "Y-you're up to date on all the Pokemon?")
    $ setWait(53.089,57.885)
    $ speak(JEFFERY, "Isn't everybody? They're only up to 493 now.")
    $ setWait(57.885,59.22)
    $ speak(EMILY, "How much head do you get an hour?")
    $ setWait(59.22,61.722)
    $ speak(JEFFERY, "Can the two of you just speak English??")
    show nicole sc4 angry
    $ setWait(61.722,65.267)
    $ speak(NICOLE, "Jeffery you wanna get really high off some OG kush?")
    show jeffery sc3 blush
    show nicole sc4
    $ setWait(65.267,67.228)
    $ speak(JEFFERY, "Wait- I know what that means...")
    show jeffery sc3 angry
    $ setWait(67.228,68.896)
    $ speak(JEFFERY, "Are you guys trying to sell me drugs!?")
    show nicole sc4 angry
    show emily sc3 angry

    $ setWait(68.896,70.022)
    $ speak(NICOLE, "Dude shut the fuck up!")
    $ setWait(70.022,71.649)
    $ speak(EMILY, "Don't make us stab you with an eyeliner pencil!")
    $ setWait(71.649,75.903)
    $ speak(JEFFERY, "Nice try but I think my time and money are spent better elsewhere.")
    $ setWait(75.903,76.57)
    $ speak(EMILY, "I don't.")
    show jeffery sc3 angry:
        leftmidstage
        linear 5 off_right

    show nicole sc4 angry:
        pause 2.2
        xzoom 1

    show emily sc3 angry:
        pause 3
        xzoom -1

    $ setWait(76.57,82.159)
    $ speak(JEFFERY, "Let's just hope the both of you learn how to pay attention in health class. I'll see ya never.")
    $ setWait(82.159,86.998)
    $ speak(EMILY, "I hate him so much.\nHow can you talk shit when you can't even tie your shoes?")
    show nicole sc4
    $ setWait(86.998,89.875)
    $ speak(NICOLE, "Yeah.. Did that seem out of character for him?")
    show emily sc3:
        xzoom 1
    $ setWait(89.875,91.252)
    $ speak(EMILY, "You seen him with a blunt before?")
    $ setWait(91.252,98.342)
    $ speak(NICOLE, "No not that, he's never been that dismissive with a girl before. I've literally told him to kill himself and he'll still try to be friends.")
    $ setWait(98.342,100.845)
    $ speak(EMILY, "Oh me too. He just likes female attention.")
    show nicole sc4 surprised
    $ setWait(100.845,103.681)
    $ speak(NICOLE, "But if he's turning ours down, that means...")
    scene mall int

    hide emily sc3
    hide nicole sc4

    show karen sc3 smile:
        rightmidstage

    show jeffery sc3 smile:
        off_left
        xzoom -1
        linear 2 rightcenterstage

    $ setWait(103.681,105.891)
    $ speak(JEFFERY, "Sorry I'm late, got a little caught up.")
    $ setWait(105.891,108.185)
    $ speak(KAREN, "It's okay. What do you wanna do next?")
    scene mall int 2
    hide jeffery sc3
    hide karen sc3

    show emily sc3 sad:
        rightcenterstage
        xzoom -1

    show nicole sc4 surprised:
        xzoom 1
        leftcenterstage

    $ setWait(108.185,108.978)
    $ speak(EMILY, "Oh my god.")
    $ setWait(108.978,113.19)
    $ speak(NICOLE, "He actually found a human female willing to listen to him.")
    show emily sc3 angry
    $ setWait(113.19,114.608)
    $ speak(EMILY, "I'm not happy for him.")
    show nicole sc4 angry
    $ setWait(114.608,117.111)
    $ speak(NICOLE, "After the way he just talked to us, me neither.")
    $ setWait(117.111,118.821)
    $ speak(EMILY, "Are we gonna do something about it?")
    show nicole sc4 angry:
        leftcenterstage
        linear 2 off_right
    $ setWait(118.821,120.489)
    $ speak(NICOLE, "I think you already know.")
    scene mall int
    hide nicole sc4
    hide emily sc3

    show jeffery sc3:
        xzoom -1
        rightcenterstage

    show karen sc3:
        rightmidstage

    $ setWait(120.489,125.453)
    $ speak(JEFFERY, "Yeah, by the way did I mention the Youtube anime copyright controversy?")
    $ setWait(125.453,128.039)
    $ speak(KAREN, "You did actually, it's okay though.")
    $ setWait(128.039,132.626)
    $ speak(JEFFERY, "Oh sorry, it's just a big deal, a lot of people have been talking about it.")
    $ setWait(132.626,136.881)
    $ speak(KAREN, "I don't mind. Do you wanna hang out after school again tomorrow?")
    $ setWait(136.881,143.429)
    $ speak(JEFFERY, "Tomorrow? I guess so, that'd be good. In like a.. date sort of way?")
    show karen sc3 smile
    $ setWait(143.429,147.6)
    $ speak(KAREN, "Yeah, I'd like that. We have a lot in common and you're really nice.")
    show jeffery sc3 smile
    $ setWait(147.6,148.934)
    $ speak(JEFFERY, "Wow a girlfriend.")
    show karen sc3
    $ setWait(148.934,149.727)
    $ speak(KAREN, "What was that?")
    show jeffery sc3 blush

    $ setWait(149.727,152.229)
    $ speak(JEFFERY, "Oh nothing! Nothing at all, um...")
    show nicole sc4 angry:
        off_left
        linear 2 leftcenterstage

    show emily sc3 angry:
        xzoom -1
        off_farleft
        linear 2 leftmidstage

    show jeffery sc3:
        pause 0.6
        xzoom 1

    $ setWait(152.229,153.439)
    $ speak(NICOLE, "Oh look at this!")
    $ setWait(153.439,155.858)
    $ speak(EMILY, "Is this your next jumpoff, Jeffery!?")
    $ setWait(155.858,158.235)
    $ speak(JEFFERY, "Um... Okay??")
    show karen sc3 sad
    $ setWait(158.235,159.403)
    $ speak(KAREN, "What's going on?")
    $ setWait(159.403,162.656)
    $ speak(NICOLE, "Oh he didn't tell you? Then again he didn't tell us either.")
    $ setWait(162.656,165.284)
    $ speak(EMILY, "Yeah Jeffery loves telling girls they're the only one.")
    $ setWait(165.284,167.912)
    $ speak(NICOLE, "Then he blocks your numbers after you're left with herpes!")
    $ setWait(167.912,170.331)
    $ speak(EMILY, "Fuck the herpes, you got me pregnant, Jeffery!")
    show jeffery sc3 blush
    $ setWait(170.331,171.332)
    $ speak(JEFFERY, "Wha- Wha- Wha-")
    $ setWait(171.332,174.627)
    $ speak(KAREN, "I-is this true?? You told me you're a virgin, Jeffery.")
    $ setWait(174.627,176.337)
    $ speak(NICOLE, "Oh so we just never existed to you?")
    show jeffery sc3 blush:
        xzoom -1

    $ setWait(176.337,180.132)
    $ speak(JEFFERY, "They're making all this up, I don't understand! I am a virgin!")
    $ setWait(180.132,184.22)
    $ speak(EMILY, "Would a virgin say there's 493 Pokemon before going down on me?")
    $ setWait(184.22,189.642)
    $ speak(KAREN, "493? You told me that exact Pokemon number yesterday! Were you cheating on me??")
    $ setWait(189.642,191.393)
    $ speak(JEFFERY, "No! I don't even know them!")
    $ setWait(191.393,194.73)
    $ speak(NICOLE, "Not only will he cheat on you, he's also really Christian.")
    $ setWait(194.73,197.316)
    $ speak(EMILY, "Yeah he'll tell you he's pro-life while finishing.")
    $ setWait(197.316,198.109)
    $ speak(KAREN, "Oh no!")
    $ setWait(198.109,200.027)
    $ speak(JEFFERY, "You're not believing them, are you?")
    show karen sc3 sad:
        xzoom -1
        rightmidstage
        linear 1.7 rightstage
    $ setWait(200.027,201.987)
    $ speak(KAREN, "I.. I need a minute!")
    $ setWait(201.987,203.656)
    $ speak(NICOLE, "I need you to pay for my treatment!")
    $ setWait(203.656,205.866)
    $ speak(EMILY, "And you better pay for this baby, Jeffery!")
    show karen sc3 sad:
        xzoom -1
        rightstage
        linear 0.36 off_right

    $ setWait(205.866,207.076)
    $ speak(KAREN, "I gotta go!")
    show jeffery sc3 blush:
        rightcenterstage
        xzoom -1
        pause 1.1
        linear 0.85 off_right

    $ setWait(207.076,210.621)
    $ speak(JEFFERY, "What the-- Karen no! Come back!")
    show nicole sc4 smile:
        xzoom -1
    $ setWait(210.621,213.374)
    $ speak(NICOLE, "I feel... better.")
    show emily sc3
    $ setWait(213.374,216.001)
    $ speak(EMILY, "Yeah I don't even feel like selling this quad anymore.")
    show nicole sc4
    $ setWait(216.001,219.088)
    $ speak(NICOLE, "We can just go back and steal all that stuff. Drop me off after though.")
    show emily sc3:
        xzoom 1
        leftmidstage
        linear 1.5 off_left

    show nicole sc4:
        leftcenterstage
        pause 0.35
        linear 1.5 off_left

    $ setWait(219.088,220.339)
    $ speak(EMILY, "Yeah okay.")
    stop ambient fadeout 1
    jump scene_0135
label scene_0135:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.298):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.298 zoom 0.7 truecenter

    $ setVoiceTrack("audio/Scenes/0135.mp3")
    scene home nicole int
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    show nicole sc4 smile:
        off_right
        xzoom -1
        linear 1.6 rightmidstage
        xzoom 1

    show emily sc3:
        off_right
        pause 0.68
        linear 1 rightstage

    $ setWait(2.298,4.383)
    $ speak(NICOLE, "But yeah that was productive.")
    $ setWait(4.383,6.218)
    $ speak(EMILY, "Why do Skittles taste better when they're stolen?")
    show nicole sc4:
        rightmidstage

    $ setWait(6.218,7.261)
    $ speak(NICOLE, "Dopamine rush.")
    $ setWait(7.261,8.971)
    $ speak(EMILY, "I thought Seroquel stopped that.")

    show mom 2 upset:
        xzoom -1
        off_left
        linear 1 leftmidstage

    $ setWait(8.971,11.057)
    $ speak(MOM, "Nicole, where have you been all night??")
    show nicole sc4:
        xzoom -1
    $ setWait(11.057,12.475)
    $ speak(NICOLE, "I don't know, are you a cop now?")
    $ setWait(12.475,13.434)
    $ speak(MOM, "And who's this??")
    $ setWait(13.434,14.226)
    $ speak(EMILY, "Should I go?")
    show nicole sc4:
        xzoom 1
        pause 1.1
        xzoom -1
    $ setWait(14.226,16.687)
    $ speak(NICOLE, "Nah you can hang out. We were at the mall, Mom!")
    $ setWait(16.687,20.232)
    $ speak(MOM, "So I'm supposed to believe you were just at the mall all night?")
    show nicole sc4 angry
    $ setWait(20.232,23.819)
    $ speak(NICOLE, "The fuck you mean \"all night\"? We were there for like what? Two, Three hours?")
    $ setWait(23.819,25.696)
    $ speak(EMILY, "Yeah two and a half, like the sitcom.")
    $ setWait(25.696,27.573)
    $ speak(MOM, "It's 1 in the morning!")
    show emily sc3 sad

    $ setWait(27.573,29.492)
    $ speak(EMILY, "Damn we hung out with that guy that long?")
    $ setWait(29.492,30.576)
    $ speak(MOM, "What guy??")
    show emily sc3

    $ setWait(30.576,31.243)
    $ speak(EMILY, "Nobody.")
    $ setWait(31.243,32.411)
    $ speak(MOM, "What guy, Nicole!?")
    $ setWait(32.411,34.455)
    $ speak(NICOLE, "Mom don't even worry about it you're gonna freak out.")
    show mom 2 angry
    $ setWait(34.455,35.206)
    $ speak(MOM, "Tell me!")
    $ setWait(35.206,35.998)
    $ speak(NICOLE, "Oh my god.")
    show mom 2 angry:
        xzoom -1
        leftmidstage
        linear 2.5 leftcenterstage

    $ setWait(35.998,38.542)
    $ speak(MOM, "Tell me or your friend has to go home!")
    show emily sc3 smile
    $ setWait(38.542,39.293)
    $ speak(EMILY, "Ultimatum.")
    show emily sc3

    show nicole sc4 angry:
        rightmidstage
        xzoom -1
        linear 1 rightcenterstage

    $ setWait(39.293,40.461)
    $ speak(NICOLE, "You really wanna know!?")
    $ setWait(40.461,42.338)
    $ speak(MOM, "Yes, what guy was this!?")
    show nicole sc4 yell:
        rightcenterstage
        xzoom -1
    $ setWait(42.338,45.633)
    $ speak(NICOLE, "The crackhead in front of the mall we sold weed to!")
    show nicole sc4 angry
    $ setWait(45.633,48.719)
    $ speak(MOM, "Where did you even get-- Ugh you're so stupid!!")
    $ setWait(48.719,50.721)
    $ speak(NICOLE, "Oh so I guess you hate homeless people too?")
    $ setWait(50.721,55.81)
    $ speak(MOM, "No! Dealing drugs in public, dealing drugs in general-- Just how can you be so idiotic!")
    $ setWait(55.81,57.561)
    $ speak(EMILY, "Uh it was actually kinda smart.")
    $ setWait(57.561,58.771)
    $ speak(MOM, "Excuse me??")
    show emily sc3 angry:
        rightstage
        linear 2 rightmidstage

    $ setWait(58.771,61.899)
    $ speak(EMILY, "Bitch you better fix your fucking tone with me before I slash your tires!")
    $ setWait(61.899,62.608)
    $ speak(MOM, "Really?")
    $ setWait(62.608,68.197)
    $ speak(EMILY, "We sold to a crackhead cause what would a crackhead want with weed? Cops would never expect that shit, it's genius!")
    $ setWait(68.197,70.616)
    $ speak(NICOLE, "Yeah so why don't you shut the fuck up, Mom!")
    $ setWait(70.616,75.121)
    $ speak(MOM, "How bout I call the police!? Your plan's just so bulletproof you shouldn't worry!")
    show nicole sc4 sad

    $ setWait(75.121,75.788)
    $ speak(NICOLE, "Oh shit.")
    $ setWait(75.788,80.584)
    $ speak(EMILY, "Go the fuck ahead, bitch! They'll side with us anyway cause we're cute and you're old and used up!")
    show mom 2 upset
    $ setWait(80.584,83.546)
    $ speak(MOM, "Ugh- Nicole I don't want you hanging around with her anymore--")
    $ setWait(83.546,86.215)
    $ speak(EMILY, "She can hang out with whoever the fuck she wants, whore!")
    show mom 2 sad
    $ setWait(86.215,91.512)
    $ speak(EMILY, "So why don't you go to your room, pour your little wine, put on Grey's Anatomy, and shut the fuck up!")
    show mom 2 sad:
        leftcenterstage
        xzoom -1
        pause 1.05
        xzoom 1
        linear 0.8 off_left

    $ setWait(91.512,95.307)
    $ speak(MOM, "I... I can't believe you!")
    show emily sc3 upset
    $ setWait(95.307,98.352)
    $ speak(EMILY, "God that felt good, wish I could say that to my Mom.")
    show nicole sc4 sad:
        xzoom 1
    $ setWait(98.352,99.603)
    $ speak(NICOLE, "Why don't you?")
    show emily sc3
    $ setWait(99.603,101.48)
    $ speak(EMILY, "She'd probably cut me out of the will.")
    show nicole sc4 surprised
    $ setWait(101.48,104.191)
    $ speak(NICOLE, "Yeah that's uh... huh.")
    show emily sc3 smile
    show nicole sc4
    $ setWait(104.191,110.239)
    $ speak(EMILY, "But hanging out with you, this was easily like the best day of my life. Shutting your Mom down was just the cherry on top.")
    show nicole sc4 smile
    $ setWait(110.239,112.408)
    $ speak(NICOLE, "Yeah you're cool, let's do it again sometime.")
    $ setWait(112.408,113.784)
    $ speak(EMILY, "Oh can I spend the night here?")
    show nicole sc4
    $ setWait(113.784,116.37)
    $ speak(NICOLE, "I guess, my Mom's too busy crying to say no now.")
    $ setWait(116.37,117.955)
    $ speak(EMILY, "Awesome, where's your bathroom?")
    $ setWait(117.955,119.206)
    $ speak(NICOLE, "There's one downstairs.")
    $ setWait(119.206,121.375)
    $ speak(EMILY, "Cool, I'm just gonna flush my Seroquel.")
    $ setWait(121.375,122.168)
    $ speak(NICOLE, "All of it?")
    show emily sc3
    $ setWait(122.168,124.42)
    $ speak(EMILY, "Yeah I'm just done with it period.")
    $ setWait(124.42,126.463)
    $ speak(NICOLE, "Oh... Why?")
    show emily sc3 smile
    $ setWait(126.463,133.679)
    $ speak(EMILY, "Just all the stuff we did today, how I ripped your Mom to shreds, that's the real me.\nThat is the real unfiltered me.")
    show emily sc3 angry
    $ setWait(133.679,138.1)
    $ speak(EMILY, "So fuck this med shit. I don't want my Mom controlling me anymore, and yours shouldn't either.")
    show nicole sc4 smile
    $ setWait(138.1,139.518)
    $ speak(NICOLE, "Yeah I get you, that's cool.")
    show emily sc3
    $ setWait(139.518,144.899)
    $ speak(EMILY, "Besides I wanna take a percocet to fall asleep and percs do not mix with Seroquel.")
    stop ambient fadeout 1
    jump scene_0136
label scene_0136:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0136.mp3")
    play ambient "audio/Ambience/Classroom_Ambience_2.mp3" fadein 1
    scene classroom int 4

    show emily sc4:
        rightcenterstage

    show nicole sc2:
        rightmidstage
        xzoom -1

    show kylar sc3:
        rightstage

    $ setWait(0.043,2.003)
    $ speak(KYLAR, "How do I do this paper, dude?")
    show emily sc4 upset
    $ setWait(2.003,4.297)
    $ speak(EMILY, "There's gotta be a way to get out of doing most of this.")
    show ames 2 smug:
        xzoom -1
        off_left
        linear 2.3 leftcenterstage
    $ setWait(4.297,7.634)
    $ speak(AMES, "How many times have I petitioned for Pom juice in the lounge vending machine?")
    show emily sc4 smile
    $ setWait(7.634,8.468)
    $ speak(EMILY, "Ms. Ames.")
    show ames 2
    $ setWait(8.468,9.219)
    $ speak(AMES, "What is it?")
    $ setWait(9.219,13.306)
    $ speak(EMILY, "Me and Nicole we wondering if we could pair together for our essay?")
    show nicole sc2 surprised
    $ setWait(13.306,13.932)
    $ speak(NICOLE, "We were?")
    $ setWait(13.932,15.016)
    $ speak(AMES, "Pair together?")
    show nicole sc2
    $ setWait(15.016,19.396)
    $ speak(EMILY, "Yeah like we make it an oral presentation for class, we'll make flashcards and everything.")
    $ setWait(19.396,22.899)
    $ speak(AMES, "An oral presentation on the state of modern poetry?")
    $ setWait(22.899,25.944)
    $ speak(EMILY, "Isn't poetry all about the spoken word?")
    $ setWait(25.944,32.45)
    $ speak(AMES, "Hmm... I'll allow it. But just know I'll have a higher level of scrutiny since it's two of you together.")
    $ setWait(32.45,34.077)
    $ speak(EMILY, "No that's fine, thanks.")
    $ setWait(34.077,36.705)
    $ speak(NICOLE, "Since when are teachers okay with switching the whole assignment?")
    show emily sc4:
        xzoom -1

    $ setWait(36.705,38.373)
    $ speak(EMILY, "It's remedial, they just wanna see it done.")
    show emily sc4:
        pause 0.4
        xzoom 1
    $ setWait(38.373,40.875)
    $ speak(AMES, "Something you two would like to share with the rest of the class?")
    $ setWait(40.875,41.501)
    $ speak(NICOLE, "Like what?")
    show emily sc4 sad:
        xzoom 1
    $ setWait(41.501,43.878)
    $ speak(EMILY, "Actually could we be excused to the restroom?")
    show ames 2 angry
    $ setWait(43.878,45.547)
    $ speak(AMES, "Since when do you ask?")
    $ setWait(45.547,51.553)
    $ speak(EMILY, "Well I just had an anxiety flashback to when... Hillary Clinton lost to Obama last summer.")
    show ames 2 sad

    $ setWait(51.553,52.929)
    $ speak(AMES, "Oh, oh no.")
    show nicole sc2 sad
    $ setWait(52.929,56.599)
    $ speak(NICOLE, "Yeah we don't care what color he was, it's still misogynistic.")
    $ setWait(56.599,59.185)
    $ speak(AMES, "Understandable, take all the time you need.")
    stop ambient fadeout 1
    jump scene_0137
label scene_0137:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Bathroom_Lockerroom_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0137.mp3")
    scene bathroom
    show nicole sc2:
        off_right
        xzoom -1
        linear 2.1 leftmidstage
        xzoom 1

    show emily sc4:
        off_right
        pause 0.4
        linear 1.75 centerstage

    $ setWait(0.086,2.171)
    $ speak(NICOLE, "Well that was spontaneous.")
    show emily sc4 angry

    $ setWait(2.171,3.422)
    $ speak(EMILY, "What?")
    show nicole sc2 surprised

    $ setWait(3.422,5.424)
    $ speak(NICOLE, "How you switched the assignment?")
    $ setWait(5.424,7.426)
    $ speak(EMILY, "No not that, \"spontaneous\"?")
    show nicole sc2
    $ setWait(7.426,9.136)
    $ speak(NICOLE, "Oh yeah it means like--")
    show emily sc4 angry:
        centerstage
        linear 0.25 leftcenterstage

    $ setWait(9.136,10.429)
    $ speak(EMILY, "Are you tryna talk down to me?")
    show nicole sc2 sad
    $ setWait(10.429,14.975)
    $ speak(NICOLE, "What? No it's just a word. They had it in the...")
    $ setWait(14.975,19.814)
    $ speak(NICOLE, "Cat in the Hat live action movie... The one with Dakota Fanning?")
    show emily sc4 smile
    $ setWait(19.814,21.982)
    $ speak(EMILY, "Oh no you're right, I love you.")
    $ setWait(21.982,23.317)
    $ speak(NICOLE, "Yeah love you too.")
    $ setWait(23.317,27.404)
    $ speak(EMILY, "But if you were talking down to me I'd smack the shit out of you. I'd make you bleed.")
    $ setWait(27.404,28.197)
    $ speak(NICOLE, "Good to know.")
    $ setWait(28.197,34.829)
    $ speak(EMILY, "But anyway I wanted switch to a presentation cause I've had a pretty big idea for that class but no one to do it with.")
    show nicole sc2
    $ setWait(34.829,36.163)
    $ speak(NICOLE, "Until now obviously.")
    $ setWait(36.163,39.208)
    $ speak(EMILY, "Exactly, you're down for anything even if it crosses the line.")
    show nicole sc2 smile
    $ setWait(39.208,40.251)
    $ speak(NICOLE, "Bitch what line?")
    $ setWait(40.251,46.006)
    $ speak(EMILY, "Exactly. Ms. Ames is this perfect little bitch in her perfect little world and I wanna ruin that for her.")
    $ setWait(46.006,48.425)
    $ speak(NICOLE, "Oh yeah totally. What do you wanna do?")
    $ setWait(48.425,55.516)
    $ speak(EMILY, "So I've had this planned for a while actually but um... Sorry it's really wild. Lemme think how to word this.")
    $ setWait(55.516,58.227)
    $ speak(NICOLE, "No take your time, it doesn't smell that bad in here for once.")
    show emily sc4
    $ setWait(58.227,63.065)
    $ speak(EMILY, "Right? Yeah uh... Fuck I need a cigarette to think.")
    show ari sc6:
        off_right
        linear 1.2 rightmidstage

    show nicole sc2

    $ setWait(63.065,64.567)
    $ speak(ARI, "There's always somebody in here.")
    show emily sc4:
        xzoom -1
        leftcenterstage
        linear 0.5 centerstage

    $ setWait(64.567,66.235)
    $ speak(EMILY, "Oh Ari do you have a cigarette?")
    $ setWait(66.235,67.111)
    $ speak(ARI, "I don't smoke.")
    show emily sc4 angry
    $ setWait(67.111,68.154)
    $ speak(EMILY, "Of course!")
    show ari sc6 angry
    $ setWait(68.154,69.363)
    $ speak(ARI, "What's your problem?")
    $ setWait(69.363,70.739)
    $ speak(EMILY, "Do I look like I wanna be asked?")
    $ setWait(70.739,71.949)
    $ speak(ARI, "Calm down.")

    show emily sc4 angry:
        xzoom 1

    $ setWait(71.949,73.117)
    $ speak(EMILY, "You hear this bitch, Nicole?")
    show nicole sc2 angry

    $ setWait(73.117,74.702)
    $ speak(NICOLE, "Yeah she can't tell you what to do.")
    show emily sc4 angry:
        pause 0.34
        xzoom -1

    $ setWait(74.702,78.372)
    $ speak(ARI, "Okay what the fuck is this?? Can you stoners act normal for once?")
    $ setWait(78.372,80.749)
    $ speak(NICOLE, "\"Stoner\"?? What is it 1990?")
    $ setWait(80.749,82.71)
    $ speak(EMILY, "Show us your purity ring, Jonas Sister.")
    $ setWait(82.71,85.296)
    $ speak(ARI, "Show me the guy in his 30's you're banging this weekend.")
    show nicole sc2 surprised
    $ setWait(85.296,86.255)
    $ speak(NICOLE, "Yooo.")
    show emily sc4 smile
    show nicole sc2
    $ setWait(86.255,87.756)
    $ speak(EMILY, "Heh you're really cute, Ari.")
    $ setWait(87.756,88.424)
    $ speak(ARI, "Shut up.")
    $ setWait(88.424,95.848)
    $ speak(EMILY, "No seriously, your eyeliner's always sharp, your lip gloss matches your hair, you're actually really pretty.")
    show ari sc6 shy
    $ setWait(95.848,96.807)
    $ speak(ARI, "Thanks?")
    $ setWait(96.807,98.601)
    $ speak(EMILY, "That's why I wanna look you in the face when I")
    show emily sc4 angry:
        centerstage
        xzoom -1
        linear 0.15 rightcenterstage

    $ setWait(98.601,99.351)
    $ speak(EMILY, "STAB YOU.")
    show ari sc6 sad:
        xzoom -1
        rightmidstage
        linear 0.5 off_right

    $ setWait(99.351,102.188)
    $ speak(ARI, "Okay I'm outta here!")
    show emily sc4:
        rightcenterstage
        xzoom 1
        linear 1.3 leftcenterstage

    $ setWait(102.188,103.564)
    $ speak(EMILY, "I knew that bitch was soft.")
    $ setWait(103.564,106.65)
    $ speak(NICOLE, "Yeah she's weird. What was the idea by the way?")
    show emily sc4 upset
    $ setWait(106.65,109.236)
    $ speak(EMILY, "Ugh I still need that cigarette.")
    $ setWait(109.236,112.448)
    $ speak(NICOLE, "Jecka has a ton, she's not in remedial though.")
    $ setWait(112.448,114.033)
    $ speak(EMILY, "You wanna ditch and go to regular lunch?")
    show nicole sc2:
        leftmidstage
        linear 2.4 off_right

    show emily sc4:
        leftcenterstage
        pause 1
        xzoom -1
        linear 2.1 off_right

    $ setWait(114.033,116.243)
    $ speak(NICOLE, "Not like we do anything in class anyway.")
    stop ambient fadeout 1
    jump scene_0138
label scene_0138:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0138.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3"
    scene cafeteria int 2

    show jecka sc6:
        rightcenterstage

    show nicole sc2:
        off_left
        linear 1.7 leftcenterstage

    show emily sc4:
        off_farleft
        xzoom -1
        linear 1.7 leftmidstage

    $ setWait(0.043,1.836)
    $ speak(NICOLE, "Always the same table.")
    show jecka sc6 surprised

    $ setWait(1.836,3.421)
    $ speak(JECKA, "What're you guys doing here?")
    $ setWait(3.421,4.339)
    $ speak(NICOLE, "Hanging out.")
    $ setWait(4.339,5.965)
    $ speak(EMILY, "Do you have any cigarettes?")
    $ setWait(5.965,8.134)
    $ speak(JECKA, "A-are you guys skipping remedial?")
    show nicole sc2 surprised
    $ setWait(8.134,9.552)
    $ speak(NICOLE, "Are you at lunch alone?")
    show jecka sc6 sad
    $ setWait(9.552,13.556)
    $ speak(JECKA, "No, Kelly just went to get water. You guys are gonna go to school jail if they catch you.")
    show emily sc4 angry
    $ setWait(13.556,17.06)
    $ speak(EMILY, "Well they won't catch us, right? Cause you're gonna keep your mouth shut, right?")
    $ setWait(17.06,17.769)
    $ speak(JECKA, "Nicole?")
    show nicole sc2 smile:
        xzoom -1

    $ setWait(17.769,19.27)
    $ speak(NICOLE, "Nah nah Emily, she's cool.")
    show emily sc4 smile

    $ setWait(19.27,22.273)
    $ speak(EMILY, "Oh oh cool. So yeah can I borrow a cigarette?")
    show nicole sc2:
        xzoom 1

    $ setWait(22.273,24.233)
    $ speak(JECKA, "Uh if I have one in my locker.")
    $ setWait(24.233,26.778)
    $ speak(EMILY, "And yours is by the science rooms, right?")
    show jecka sc6
    $ setWait(26.778,27.445)
    $ speak(JECKA, "Yeah.")
    show emily sc4 smile:
        leftmidstage
        xzoom -1
        linear 1.72 rightstage
        xzoom 1
    $ setWait(27.445,29.197)
    $ speak(EMILY, "Sweet, don't get up I got it.")
    show jecka sc6 surprised:
        xzoom -1

    $ setWait(29.197,31.616)
    $ speak(JECKA, "Wait! You don't even know the combination.")
    show emily sc4 smile:
        rightstage
        xzoom 1
        pause 0.4
        xzoom -1
        linear 0.8 off_right

    $ setWait(31.616,33.618)
    $ speak(EMILY, "Don't worry I'll get in there.")
    show nicole sc2 smile
    $ setWait(33.618,34.535)
    $ speak(NICOLE, "Isn't she great?")
    show jecka sc6 angry:
        xzoom 1

    $ setWait(34.535,36.954)
    $ speak(JECKA, "Nicole, what are you doing with that girl?")
    $ setWait(36.954,39.332)
    $ speak(NICOLE, "Just yesterday? Triple C's and a line of perc.")
    $ setWait(39.332,41.334)
    $ speak(JECKA, "No, why are you hanging out with her?")
    show nicole sc2 angry
    $ setWait(41.334,44.837)
    $ speak(NICOLE, "Oh dude don't be a bitch over this. I'm allowed to make new friends, okay?")
    $ setWait(44.837,48.383)
    $ speak(JECKA, "No I'm not jealous, she is fucking insane, Nicole.")
    $ setWait(48.383,49.467)
    $ speak(NICOLE, "Insane how?")
    $ setWait(49.467,53.429)
    $ speak(JECKA, "Psych ward visits, choked a girl in class, set her ex-boyfriend's car on fire?")
    show nicole sc2
    $ setWait(53.429,58.351)
    $ speak(NICOLE, "Yeah but that makes her fun. Besides you're a hypocrite cause you buy scripts off her all the time.")
    $ setWait(58.351,65.566)
    $ speak(JECKA, "Buying her adderall isn't the same as hanging out with her. That bitch is gonna get weirdly attached to you and snap as soon as you get tired of her.")
    $ setWait(65.566,68.444)
    $ speak(NICOLE, "Well I'm not tired of her now so I guess we're gonna have to wait and see.")
    show kelly sc3 sad:
        xzoom -1
        off_left
        linear 1.5 leftmidstage

    show nicole sc2:
        pause 0.6
        xzoom -1


    $ setWait(68.444,70.279)
    $ speak(KELLY, "Were you guys just talking to Emily?")
    show jecka sc6
    $ setWait(70.279,71.114)
    $ speak(JECKA, "Sort of.")
    show kelly sc3 angry
    $ setWait(71.114,75.284)
    $ speak(KELLY, "I hate her. She literally choked me in gym and didn't even get expelled.")
    show jecka sc6 angry
    $ setWait(75.284,75.868)
    $ speak(JECKA, "See?")
    $ setWait(75.868,78.037)
    $ speak(NICOLE, "Hold on but why'd she choke you?")
    $ setWait(78.037,80.373)
    $ speak(KELLY, "Cause I said she wasn't as pretty as Fergie.")
    $ setWait(80.373,81.916)
    $ speak(JECKA, "Still sound okay to you?")

    show nicole sc2 sad:
        xzoom 1

    $ setWait(81.916,83.126)
    $ speak(NICOLE, "A girl can be confident.")
    $ setWait(83.126,86.546)
    $ speak(KELLY, "Confident? I was passed out on the floor for like two minutes!")
    show nicole sc2:
        xzoom -1
    $ setWait(86.546,89.048)
    $ speak(NICOLE, "Bitch that sounds like a you problem.")
    stop ambient fadeout 1
    jump scene_0139
label scene_0139:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0139.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3" fadein 1
    scene bedroom nicole
    show nicole pj:
        leftcenterstage

    show emily pj:
        rightcenterstage

    $ setWait(0.037,2.248)
    $ speak(EMILY, "By the way where's your Mom been?")
    $ setWait(2.248,6.46)
    $ speak(NICOLE, "Uh.. she hasn't been here since you yelled at her. I think she's afraid of you.")
    show emily pj angry

    $ setWait(6.46,7.586)
    $ speak(EMILY, "She better be.")
    $ setWait(7.586,8.296)
    $ speak(NICOLE, "Oh yeah?")
    $ setWait(8.296,14.635)
    $ speak(EMILY, "For real, I don't like how she talks to you, Nicole. You're actually like really cool and smart and you should be treated as such.")
    show nicole pj sad
    $ setWait(14.635,17.013)
    $ speak(NICOLE, "Wow that's uh...")
    show emily pj
    $ setWait(17.013,18.222)
    $ speak(EMILY, "What's wrong?")
    $ setWait(18.222,25.271)
    $ speak(NICOLE, "Guys tell me that all the time and I just say \"I know\". But now that a girl's saying it- I forgot how to take an actual compliment.")
    $ setWait(25.271,27.44)
    $ speak(EMILY, "We're friends, don't worry about it.")
    $ setWait(27.44,28.941)
    $ speak(NICOLE, "Are you trying to have sex with me?")
    $ setWait(28.941,29.734)
    $ speak(EMILY, "Not really.")
    show nicole pj surprised
    $ setWait(29.734,31.819)
    $ speak(NICOLE, "Yeah I have no idea how to process this.")
    $ setWait(31.819,33.362)
    $ speak(EMILY, "Does your Mom ever compliment you?")
    show nicole pj
    $ setWait(33.362,34.155)
    $ speak(NICOLE, "No.")
    show emily pj angry
    $ setWait(34.155,39.368)
    $ speak(EMILY, "Cause she can't appreciate what she has.. and seriously, like seriously Nicole...")
    $ setWait(39.368,46.667)
    $ speak(EMILY, "If I ever see her talk like that to you again I will rip her beating heart out and hand it to you on a silver platter.")
    $ setWait(46.667,49.128)
    $ speak(NICOLE, "...And you don't wanna have sex with me?")
    show emily pj
    $ setWait(49.128,50.296)
    $ speak(EMILY, "No.")
    show nicole pj sad
    $ setWait(50.296,51.213)
    $ speak(NICOLE, "Are you sure?")
    show nicole pj

    show emily pj sad
    $ setWait(51.213,55.051)
    $ speak(EMILY, "No c'mon if you saw someone talking down to me what would you do?")
    $ setWait(55.051,58.22)
    $ speak(NICOLE, "Oh uh... Damn killing my Mom's a tough act to follow.")
    show emily pj
    $ setWait(58.22,61.265)
    $ speak(EMILY, "Okay like, if you saw my boyfriend cheating what would you do?")
    $ setWait(61.265,62.183)
    $ speak(NICOLE, "Kill that bitch.")
    show emily pj sad
    $ setWait(62.183,65.227)
    $ speak(EMILY, "Oh my god pleeeaase, he's such an asshole now.")
    $ setWait(65.227,68.147)
    $ speak(NICOLE, "Things are rocky with your gang member boyfriend? No way.")
    $ setWait(68.147,71.734)
    $ speak(EMILY, "Yeah he fucked all his shit up on heroin, the sex isn't even good anymore.")
    $ setWait(71.734,74.278)
    $ speak(NICOLE, "Yeah competing with heroin? May as well kill yourself.")
    show emily pj smile
    $ setWait(74.278,76.989)
    $ speak(EMILY, "Oh that reminds me, the idea for the oral presentation.")
    show nicole pj sad
    $ setWait(76.989,78.991)
    $ speak(NICOLE, "Oh god that's tomorrow isn't it?")
    $ setWait(78.991,81.369)
    $ speak(EMILY, "No no don't worry I got all the supplies ready.")
    show nicole pj
    $ setWait(81.369,82.953)
    $ speak(NICOLE, "It's just flashcards, right?")
    show emily pj
    $ setWait(82.953,86.999)
    $ speak(EMILY, "Not exactly. So you know how we wanna like screw up Ms. Ames?")
    $ setWait(86.999,87.917)
    $ speak(NICOLE, "Yeah for sure.")
    $ setWait(87.917,92.588)
    $ speak(EMILY, "And we don't even really like have a plan after high school, right? Like honestly what are we gonna do?")
    $ setWait(92.588,93.506)
    $ speak(NICOLE, "No you're right.")
    show emily pj smile
    $ setWait(93.506,100.429)
    $ speak(EMILY, "So I thought it'd be really badass if we show her the real state of modern poetry. Real suffering not some bumper sticker bullshit.")
    show nicole pj smile
    $ setWait(100.429,102.348)
    $ speak(NICOLE, "Dude I'm down for it, what do we do?")
    $ setWait(102.348,107.77)
    $ speak(EMILY, "Okay... We go to the front of class, say a few words, and then we'll swallow this pill mixture I made--")
    show nicole pj
    $ setWait(107.77,109.313)
    $ speak(NICOLE, "Mixture of what?")
    $ setWait(109.313,118.406)
    $ speak(EMILY, "So I started saving all my Seroquel instead of flushing it, and then I mixed it with stuff my boyfriend gave me, and then I bought percocet off Kylar--")
    show nicole pj surprised
    $ setWait(118.406,120.116)
    $ speak(NICOLE, "Hold up...")
    $ setWait(120.116,123.369)
    $ speak(NICOLE, "You're gonna OD in front of the class?")
    $ setWait(123.369,131.752)
    $ speak(EMILY, "We're gonna OD. Cause death is fucking poetry, and when Ms. Ames sees that she's gonna shut her ass up about poetry for the rest of her life.")
    show nicole pj sad
    $ setWait(131.752,134.547)
    $ speak(NICOLE, "Uh... Are you sure about that?")
    show emily pj angry
    $ setWait(134.547,136.048)
    $ speak(EMILY, "Are you backing out?")
    $ setWait(136.048,137.466)
    $ speak(NICOLE, "Well it's just a little--")
    $ setWait(137.466,140.553)
    $ speak(EMILY, "This is a two-person gang here, Nicole. Don't make me jump your ass out.")
    $ setWait(140.553,141.303)
    $ speak(NICOLE, "No no I'm cool!")
    show emily pj yell:
        xzoom -1
    $ setWait(141.303,142.221)
    $ speak(EMILY, "Shut the fuck up!!")
    show nicole pj angry
    $ setWait(142.221,143.18)
    $ speak(NICOLE, "I said I'm cool with it!")
    show emily pj angry:
        xzoom 1
    $ setWait(143.18,146.016)
    $ speak(EMILY, "No not you! I was hearing voices again.")
    show nicole pj sad
    $ setWait(146.016,147.101)
    $ speak(NICOLE, "Voices where?")
    $ setWait(147.101,149.979)
    $ speak(EMILY, "Like in my head, they always tell me I'm wrong about something.")
    $ setWait(149.979,154.442)
    $ speak(NICOLE, "The psychiatrists might disagree but have you considered listening to the voices in your head?")
    $ setWait(154.442,156.652)
    $ speak(EMILY, "Whatever, look are you down or what?")
    show nicole pj surprised
    $ setWait(156.652,158.112)
    $ speak(NICOLE, "Totally. Anything you want.")
    show emily pj smile behind black
    $ setWait(158.112,165.202)
    $ speak(EMILY, "Awesome, you're awesome. I love you Nicole, like I really fucking love you. If you told me to kill someone I'd do it, I wouldn't tell the cops shit.")
    show nicole pj sad
    $ setWait(165.202,169.331)
    $ speak(NICOLE, "What if I told you to not kill someone? Like yourself?")
    $ setWait(169.331,176.046)
    $ speak(EMILY, "Nicole I know you're worried but we're gonna do it together, it's gonna be okay. We got a big day tomorrow, let's get some sleep.")

    show nicole pj sad behind black:
        xzoom -1
        leftcenterstage
        linear 1.7 off_left


    show black:
        alpha 0.0
        pause 1.1
        alpha 1.0

    $ setWait(176.046,182.052)
    $ speak(NICOLE, "We sure do.")
    $ setWait(182.052,183.679)
    $ speak(EMILY, "...You're not gonna kiss me goodnight?")
    $ setWait(183.679,185.473)
    $ speak(NICOLE, "Oh my god, mwah.")
    $ setWait(185.473,187.475)
    $ speak(EMILY, "Thanks, I love you.")
    $ setWait(187.475,189.602)
    $ speak(NICOLE, "Yeah.")
    $ setWait(189.602,190.978)
    $ speak(EMILY, "Are you gonna say it back?")
    $ setWait(190.978,192.813)
    $ speak(NICOLE, "Okay now I do wanna kill myself.")
    stop ambient fadeout 1
    jump scene_0140
label scene_0140:
    show black onlayer screens with Pause(1.8):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.2 alpha 0.0

    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(2.379):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.379 zoom 1.06 truecenter



    $ setVoiceTrack("audio/Scenes/0140.mp3")
    play ambient "audio/Ambience/Classroom_Ambience_2.mp3"
    scene classroom int 4
    show ames 1:
        rightmidstage

    show kylar sc4:
        xzoom -1
        leftmidstage

    $ setWait(2.379,7.259)
    $ speak(KYLAR, "\"And that is why modern poetry is written.\" Done!")
    $ setWait(7.259,8.635)
    $ speak(AMES, "You certainly are.")
    show kylar sc4:
        xzoom -1
        leftmidstage
        linear 2 rightstage
        xzoom 1

    $ setWait(8.635,9.511)
    $ speak(KYLAR, "Is that a threat?")
    show emily sc4:
        xzoom -1
        off_left
        linear 1.8 leftmidstage

    show nicole sc7:
        off_farleft
        linear 1.7 leftstage

    $ setWait(9.511,11.972)
    $ speak(EMILY, "Hey Ms. Ames, sorry we're late.")
    $ setWait(11.972,13.056)
    $ speak(NICOLE, "Not actually though.")
    show ames 1 smug
    $ setWait(13.056,15.809)
    $ speak(AMES, "Late again, what's the excuse this time?")
    show emily sc4 sad
    $ setWait(15.809,20.105)
    $ speak(EMILY, "I tried ironing my shirt with a hair straightener and it caught on fire.")
    $ setWait(20.105,20.772)
    $ speak(NICOLE, "Witness.")
    show ames 1

    $ setWait(20.772,24.234)
    $ speak(AMES, "Putting out a tiny fire wouldn't make you ten minutes late, would it?")
    $ setWait(24.234,28.989)
    $ speak(EMILY, "Well no it was a really cute shirt so I cried for like nine minutes.")
    $ setWait(28.989,30.449)
    $ speak(AMES, "I find that hard to believe.")
    $ setWait(30.449,32.659)
    $ speak(EMILY, "No it was actually such a good shirt.")
    $ setWait(32.659,37.289)
    $ speak(NICOLE, "Yeah it had a Jack The Ripper crime scene photo and said \"all work is sex work\" under it.")
    show ames 1 angry
    $ setWait(37.289,41.793)
    $ speak(AMES, "I meant the crying-- front of the class! This oral presentation better be good.")
    show ames 1
    show emily sc4 smile:
        xzoom -1
        leftmidstage
        linear 0.8 leftcenterstage
    $ setWait(41.793,42.669)
    $ speak(EMILY, "It will be.")
    show nicole sc7 sad:
        leftstage
        linear 1.3 leftmidstage

    $ setWait(42.669,43.921)
    $ speak(NICOLE, "Uh, yeah...")
    $ setWait(43.921,46.173)
    $ speak(AMES, "Well go ahead, when you're ready.")
    $ setWait(46.173,48.634)
    $ speak(NICOLE, "N-no warm-up or anything?")
    $ setWait(48.634,53.055)
    $ speak(AMES, "I don't see why you'd need one. Does public speaking make you nervous, Nicole?")
    $ setWait(53.055,56.266)
    $ speak(NICOLE, "No there's.. just a few things higher on that list.")
    show emily sc4:
        xzoom 1
    $ setWait(56.266,57.476)
    $ speak(EMILY, "Okay let's just start.")
    show nicole sc7
    $ setWait(57.476,58.936)
    $ speak(AMES, "Go on.")
    show emily sc4:
        xzoom -1

    $ setWait(58.936,64.274)
    $ speak(EMILY, "So me and Nicole have been looking at modern poetry and made one main conclusion.")
    show nicole sc7 sad
    $ setWait(64.274,65.984)
    $ speak(NICOLE, "Yeah, a real big one.")
    show emily sc4 angry
    show nicole sc7
    $ setWait(65.984,71.156)
    $ speak(EMILY, "When you really get down to it, any living poet is a whole ass poser.")
    $ setWait(71.156,72.157)
    $ speak(AMES, "And why's that?")
    $ setWait(72.157,77.913)
    $ speak(EMILY, "Poetry's about the spoken word, about storytelling, right? But movies have stories too.")
    $ setWait(77.913,79.331)
    $ speak(NICOLE, "Yeah last I checked.")
    $ setWait(79.331,85.337)
    $ speak(EMILY, "And movies suck when you see the ending coming a mile away. Why should it be different with anything else?")
    $ setWait(85.337,88.632)
    $ speak(NICOLE, "Yeah and poetry sucks too because...")
    $ setWait(88.632,96.974)
    $ speak(EMILY, "Because a writers life is reflected in their work, and if their life is boring and stupid how can we expect their work to be any better?")
    show emily sc4 yell
    $ setWait(96.974,98.183)
    $ speak(EMILY, "We can't!")
    show emily sc4 angry
    $ setWait(98.183,100.519)
    $ speak(AMES, "The poetry's link to the poet, good.")
    $ setWait(100.519,110.153)
    $ speak(EMILY, "Most people's lives are boring, lot's of waiting around, lot's of doing nothing, but when does it suddenly get interesting? When do people care about you more than any other point in your life?")
    $ setWait(110.153,111.989)
    $ speak(NICOLE, "When you die?")
    $ setWait(111.989,118.37)
    $ speak(EMILY, "Exactly! Especially when it's unexpected, and especially when it's voluntary.")
    show nicole sc7 sad
    $ setWait(118.37,119.913)
    $ speak(NICOLE, "Like suicide.")
    show nicole sc7
    $ setWait(119.913,126.461)
    $ speak(EMILY, "And so I noticed a link, basically all the best writers kill themselves.\nHunter S. Thompson, Ernest Hummerway.")
    $ setWait(126.461,127.129)
    $ speak(AMES, "Hemingway.")
    $ setWait(127.129,127.671)
    $ speak(NICOLE, "Whatever.")
    $ setWait(127.671,132.092)
    $ speak(EMILY, "It's pretty obvious to me modern poetry sucks now, it's ruined!")
    $ setWait(132.092,133.301)
    $ speak(AMES, "Ruined by what?")
    $ setWait(133.301,137.889)
    $ speak(EMILY, "Therapy, self-help books, psych meds. It's like you're not allowed to be sad anymore.")
    $ setWait(137.889,140.475)
    $ speak(NICOLE, "Yeah what about the pursuit of unhappiness?")
    $ setWait(140.475,147.107)
    $ speak(EMILY, "Happy people aren't interesting, they don't tell good stories. They'll tell you about their cousin's science fair project or some other shit you don't care about!")
    show ames 1 angry
    $ setWait(147.107,147.983)
    $ speak(AMES, "Language!")
    show ames 1

    $ setWait(147.983,157.743)
    $ speak(EMILY, "So get rid of the good poets, get rid of the people who keep you guessing, you're left with no good modern poetry.")
    $ setWait(157.743,161.538)
    $ speak(AMES, "So all poets and storytellers need to be suicidal?")
    $ setWait(161.538,166.043)
    $ speak(EMILY, "It's not about what they need to be, it's what they are. Their life is their work.")
    $ setWait(166.043,167.586)
    $ speak(AMES, "Then what's the thesis?")
    show emily sc4 upset

    $ setWait(167.586,168.378)
    $ speak(EMILY, "The what?")
    $ setWait(168.378,171.298)
    $ speak(AMES, "The central message of your essay?")
    show emily sc4 angry

    $ setWait(171.298,179.097)
    $ speak(EMILY, "All great writers have suicidal thoughts, cause you can't have a good story knowing there's gonna be a happy ending.")
    $ setWait(179.097,181.516)
    $ speak(AMES, "That's very nice, girls. C+.")
    show nicole sc7 surprised
    $ setWait(181.516,182.434)
    $ speak(NICOLE, "That's it?")
    $ setWait(182.434,186.229)
    $ speak(AMES, "Decent length but a little inaccurate and rather melodramatic.")
    show emily sc4 upset
    $ setWait(186.229,188.482)
    $ speak(EMILY, "Oh then how many poems have you published?")
    show ames 1 smug
    $ setWait(188.482,189.524)
    $ speak(AMES, "Excuse me?")
    show emily sc4 angry
    $ setWait(189.524,192.611)
    $ speak(EMILY, "You graded us low cause we implied you're a shitty writer. Just say it.")
    $ setWait(192.611,193.82)
    $ speak(AMES, "That's enough, Emily.")
    $ setWait(193.82,197.074)
    $ speak(EMILY, "Sorry your world's too cozy for anyone to care about what you make.")

    $ setWait(197.074,199.534)
    $ speak(AMES, "This is entirely baseless, have a seat.")
    $ setWait(199.534,201.203)
    $ speak(EMILY, "You're soft bitch, face it.")
    show kylar sc4 smile
    show nicole sc7 angry
    $ setWait(201.203,202.37)
    $ speak(NICOLE, "Yeah honestly.")
    show ames 1 angry
    $ setWait(202.37,206.083)
    $ speak(AMES, "Truly deep thoughts come at a much older age than 17.")
    $ setWait(206.083,209.127)
    $ speak(EMILY, "Whatever, you'd probably call Bob Dylan deep.")
    $ setWait(209.127,215.258)
    $ speak(AMES, "What's really deep is voting, volunteering in your community, have you ever thought of anyone other than yourself??")
    $ setWait(215.258,216.51)
    $ speak(NICOLE, "You did not say that.")
    $ setWait(216.51,222.015)
    $ speak(EMILY, "Lip service, ho. You're the type of bitch to fuck one black dude then call yourself lightskinned.")
    $ setWait(222.015,225.102)
    $ speak(AMES, "Okay out of bounds! I think you need to be written up!")
    $ setWait(225.102,228.146)
    $ speak(EMILY, "Go ahead, write me up, no one's gonna wanna read it!")
    $ setWait(228.146,231.9)
    $ speak(AMES, "You're teenagers, you think you're any deeper than any other adult in the world!?")
    $ setWait(231.9,234.111)
    $ speak(EMILY, "Deeper than you, bitch, we're about that shit!")
    show ames 1 smug
    $ setWait(234.111,235.362)
    $ speak(AMES, "And how's that?")
    show emily sc4 angry:
        pause 1.4
        xzoom 1
    $ setWait(235.362,238.615)
    $ speak(EMILY, "Watch us! You ready, Nicole?")
    stop ambient fadeout 1.6
    jump end_0141

label end_0141:

    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    scene black

    if "end_0141" not in persistent.endings:
        $ persistent.endings.append("end_0141")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0141.webm")

    return

label scene_0142:
    $ setVoiceTrack("audio/Scenes/0142.mp3")
    scene photo classroom
    show lorre 1:
        rightcenterstage

    show kylar sc1:
        rightstage

    show nicole sc3 angry:
        leftstage

    show jecka sc2:
        leftmidstage
        xzoom -1

    $ setWait(0.035,1.62)
    $ speak(NICOLE, "This is gonna suck ass.")
    $ setWait(1.62,2.58)
    $ speak(JECKA, "Yeah.")
    $ setWait(2.58,5.04)
    $ speak(LORRE, "I'm sensing some negativity over here, girls.")
    show nicole sc3
    $ setWait(5.04,7.668)
    $ speak(NICOLE, "It's negative to think your class is a waste of time?")
    $ setWait(7.668,9.461)
    $ speak(JECKA, "That's not negative, it's just accurate.")
    $ setWait(9.461,12.089)
    $ speak(NICOLE, "Yeah like you're gonna fail us if we're bad at drawing.")
    show lorre 1 angry
    $ setWait(12.089,14.633)
    $ speak(LORRE, "I'll fail you if you're bad at giving effort.")
    show jecka sc2 angry
    $ setWait(14.633,17.72)
    $ speak(JECKA, "So there's no tangible achievement in this class. That's fucking stupid.")
    $ setWait(17.72,18.929)
    $ speak(LORRE, "Watch the language.")
    show jecka sc2
    $ setWait(18.929,19.972)
    $ speak(NICOLE, "Watch The Office.")
    show lorre 1

    $ setWait(19.972,21.765)
    $ speak(LORRE, "The Office? The TV show?")
    $ setWait(21.765,23.767)
    $ speak(NICOLE, "Yeah it's for people who aren't funny, you'll love it.")
    $ setWait(23.767,26.353)
    $ speak(KYLAR, "Hey I like the office.")
    $ setWait(26.353,29.648)
    $ speak(JECKA, "So yeah why do we have to draw and paint? It's our last year of high school.")
    $ setWait(29.648,32.443)
    $ speak(LORRE, "You're never too old for creativity.")
    show nicole sc3 angry
    $ setWait(32.443,35.237)
    $ speak(NICOLE, "We don't know what we're doing, we're just fingerpainting with brushes.")
    $ setWait(35.237,41.744)
    $ speak(LORRE, "Well if you put the effort in maybe you'll learn what you're doing. Or maybe I'll have to fail you for the year.")
    show jecka sc2 angry
    $ setWait(41.744,46.749)
    $ speak(JECKA, "No I'll do it, it's just dumb as shit.\nNext terrorist attack better be an art school.")
    show jecka sc2
    $ setWait(46.749,50.419)
    $ speak(LORRE, "...Yes, and Nicole? Can I trust you'll participate?")
    $ setWait(50.419,52.129)
    $ speak(NICOLE, "Can I trust the housing market?")
    $ setWait(52.129,54.715)
    $ speak(LORRE, "Your friend's doing it, why not join her?")
    show nicole sc3 angry
    $ setWait(54.715,58.093)
    $ speak(NICOLE, "Cause she wants to go to college and shit, I just wanna hang out and get fucked up.")
    $ setWait(58.093,59.053)
    $ speak(JECKA, "Respectable.")
    $ setWait(59.053,61.222)
    $ speak(LORRE, "So you won't be participating?")
    show nicole sc3
    $ setWait(61.222,62.014)
    $ speak(NICOLE, "Nope.")
    $ setWait(62.014,66.143)
    $ speak(LORRE, "Then maybe you could serve as my teaching assistant for the year.")
    $ setWait(66.143,67.686)
    $ speak(NICOLE, "And what's that entail?")
    $ setWait(67.686,71.899)
    $ speak(LORRE, "Cleaning brushes, organizing supplies, and posting to our MySpace pages.")
    show nicole sc3 angry
    $ setWait(71.899,73.692)
    $ speak(NICOLE, "Why would you put any of this on MySpace?")
    $ setWait(73.692,82.993)
    $ speak(LORRE, "Online networking is the future. What if one of you kids went viral and spun a career out of it?\nHave you heard of Owl Town?")
    show jecka sc2 angry
    $ setWait(82.993,84.536)
    $ speak(JECKA, "You mean Owl City?")
    $ setWait(84.536,92.419)
    $ speak(LORRE, "Either way, in the arts we embrace the future, and MySpace is that future. Welcome aboard, Nicole.")
    show jecka sc2
    $ setWait(92.419,93.504)
    show nicole sc3 sad
    $ speak(NICOLE, "Oh my god.")
    $ setWait(93.504,95.089)
    $ speak(LORRE, "Is that excitement I hear?")
    show nicole sc3 angry
    $ setWait(95.089,97.132)
    $ speak(NICOLE, "Fine I'll do your little baby drawing, okay?")
    show lorre 1:
        rightcenterstage
        linear 1.85 leftcenterstage

    $ setWait(97.132,99.26)
    $ speak(LORRE, "To the best of your ability?")
    show nicole sc3
    $ setWait(99.26,101.553)
    $ speak(NICOLE, "Oh yeah... You'll see.")
    stop ambient fadeout 1
    jump scene_0143
label scene_0143:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1
    $ setVoiceTrack("audio/Scenes/0143.mp3")
    scene classroom int 2

    show ari sc6:
        leftstage
        xzoom -1

    show nicole sc3:
        leftmidstage
        xzoom -1

    show jeffery sc2:
        centerstage


    $ setWait(0.035,2.871)
    $ speak(ARI, "Your hand's covered in that weird charcoal stuff.")
    $ setWait(2.871,5.457)
    $ speak(NICOLE, "Yeah I washed my hands for like two minutes, it doesn't come off.")
    show ari sc6 sad
    $ setWait(5.457,10.045)
    $ speak(ARI, "Damn art sucks, I'm so glad I'm not in it. Do you like drawing or whatever?")
    show nicole sc3 angry
    show ari sc6
    $ setWait(10.045,16.176)
    $ speak(NICOLE, "No I was just randomly placed in it. The kids who actually wanted to be there are so annoying too.")

    show jeffery sc2 smile

    $ setWait(16.176,19.262)
    $ speak(JEFFERY, "I like taking art class. Mr. Lorre's the best!")
    $ setWait(19.262,19.888)
    $ speak(NICOLE, "See?")
    show ari sc6 sad
    $ setWait(19.888,20.847)
    $ speak(ARI, "No I see.")
    show jeffery sc2
    $ setWait(20.847,22.057)
    $ speak(JEFFERY, "See what?")

    show ari sc6:
        leftstage
        xzoom -1

    $ setWait(22.057,24.601)
    $ speak(ARI, "I gotta work on my lab I'll see ya later, Nicole.")
    show ari sc6:
        leftstage
        xzoom -1
        pause 1.8
        xzoom 1
        linear 1 off_left

    $ setWait(24.601,27.02)
    $ speak(JEFFERY, "What about me?")
    show nicole sc3 angry:
        xzoom 1

    $ setWait(27.02,31.483)
    $ speak(NICOLE, "God I drew for an hour, and then in two days I'll have to draw for another hour.")
    $ setWait(31.483,32.943)
    $ speak(JEFFERY, "What's so bad about drawing?")
    $ setWait(32.943,34.194)
    $ speak(NICOLE, "Jeffery just do the lab.")
    $ setWait(34.194,37.948)
    $ speak(JEFFERY, "Well no what's wrong with it? Or do you not like Mr. Lorre?")
    $ setWait(37.948,39.324)
    $ speak(NICOLE, "Uh both?")
    $ setWait(39.324,43.954)
    $ speak(JEFFERY, "Aw I wish more people understood him, he's been through a lot this year in his home life.")
    show nicole sc3
    $ setWait(43.954,46.873)
    $ speak(NICOLE, "How would you know? He's a teacher, they don't tell us anything.")
    $ setWait(46.873,54.798)
    $ speak(JEFFERY, "I have lunch in his classroom cause no one sits with me in the cafeteria. We talk about a bunch of stuff like his house foreclosing, and his wife cheating on him, and--")
    show nicole sc3 surprised
    $ setWait(54.798,57.259)
    $ speak(NICOLE, "Wait cheated on him?? With who?")
    $ setWait(57.259,62.18)
    $ speak(JEFFERY, "It was um... I think this might've been private I don't know if I should tell you.")
    show nicole sc3 angry
    $ setWait(62.18,62.973)
    $ speak(NICOLE, "No come on.")
    $ setWait(62.973,64.266)
    $ speak(JEFFERY, "I-I can't.")
    show nicole sc3 flirt
    $ setWait(64.266,67.561)
    $ speak(NICOLE, "Come on, Jeffery. Don't you wanna make me happy?")
    show jeffery sc2 blush
    $ setWait(67.561,69.146)
    $ speak(JEFFERY, "Uh... Yeah.")
    $ setWait(69.146,71.314)
    $ speak(NICOLE, "So you go ahead and tell me, okay?")
    $ setWait(71.314,72.858)
    $ speak(JEFFERY, "It was the UPS man!")
    show nicole sc3 smile
    $ setWait(72.858,74.276)
    $ speak(NICOLE, "Holy shit.")
    $ setWait(74.276,74.818)
    $ speak(JEFFERY, "What?")
    $ setWait(74.818,79.99)
    $ speak(NICOLE, "From teacher to mailman? He's so bad of a husband that she's fucking down.")
    $ setWait(79.99,82.117)
    $ speak(JEFFERY, "You're not gonna tell anyone, are you?")
    show nicole sc3 sad
    $ setWait(82.117,84.828)
    $ speak(NICOLE, "Jeffery, don't you trust me?")
    $ setWait(84.828,87.038)
    $ speak(JEFFERY, "Uh okay I trust you.")
    show nicole sc3 flirt
    $ setWait(87.038,88.703)
    $ speak(NICOLE, "Thank you.")
    jump scene_0144
label scene_0144:
    $ setVoiceTrack("audio/Scenes/0144.mp3")
    play ambient "audio/Ambience/Cafeteria_Ambience.mp3"
    scene cafeteria int

    show jecka sc2 surprised:
        rightcenterstage

    show nicole sc3 smile:
        leftcenterstage

    $ setWait(0.038,1.414)
    $ speak(JECKA, "She's fucking down?")
    $ setWait(1.414,2.957)
    $ speak(NICOLE, "Yeah he's pathetic, right?")
    show jecka sc2
    $ setWait(2.957,6.919)
    $ speak(JECKA, "What if she's just really ugly? When you're ugly all you can do is fuck down.")
    show nicole sc3
    $ setWait(6.919,10.423)
    $ speak(NICOLE, "Yeah but she still cheated, it takes a lot for an ugly woman to cheat.")
    $ setWait(10.423,14.135)
    $ speak(JECKA, "Oh totally. Mr. Lorre had to have been into some terrible shit.")
    $ setWait(14.135,15.47)
    $ speak(NICOLE, "But what though?")
    show kylar sc1 smile:
        off_left
        xzoom -1
        linear 1.1 leftmidstage

    show nicole sc3:
        pause 0.6
        xzoom -1

    $ setWait(15.47,16.721)
    $ speak(KYLAR, "Sup, bitches?")
    show jecka sc2 angry
    $ setWait(16.721,17.639)
    $ speak(JECKA, "Who invited you?")
    $ setWait(17.639,20.558)
    $ speak(KYLAR, "Me motherfucker, you guys wanna go to the fair with me this weekend?")
    show nicole sc3 surprised
    $ setWait(20.558,21.559)
    $ speak(NICOLE, "The fair?")
    $ setWait(21.559,22.935)
    $ speak(KYLAR, "Yeah with like games and shit.")
    show nicole sc3 angry
    $ setWait(22.935,25.938)
    $ speak(NICOLE, "Is it 1920? Why would I go to the fair?")
    $ setWait(25.938,28.232)
    $ speak(JECKA, "Yeah we have internet and xanax, fuck the fair.")
    show kylar sc1
    $ setWait(28.232,30.985)
    $ speak(KYLAR, "What's so bad about old stuff? 1920's a cool year.")
    $ setWait(30.985,32.945)
    $ speak(NICOLE, "You would like a year where rape was legal.")
    show jecka sc2 worried
    $ setWait(32.945,35.114)
    $ speak(JECKA, "Rape was not legal in 1920.")
    show nicole sc3:
        xzoom 1
    $ setWait(35.114,36.366)
    $ speak(NICOLE, "In practice it was.")
    show kylar sc1 angry
    show nicole sc3:
        pause 0.5
        xzoom -1

    show jecka sc2
    $ setWait(36.366,41.329)
    $ speak(KYLAR, "God shut up! There's cool shit to do there, they don't even card you, honestly it's your loss.")
    show crispin sc2:
        off_right
        linear 1.4 rightmidstage

    show jecka sc2:
        pause 0.55
        xzoom -1
    $ setWait(41.329,43.247)
    $ speak(CRISPIN, "Hey whoa what's going on? Chill with the yelling.")
    $ setWait(43.247,46.125)
    $ speak(KYLAR, "Leave me alone bro, don't be a bitch. Don't make me fight you.")
    $ setWait(46.125,48.127)
    $ speak(CRISPIN, "Dude what? Don't be lame right now.")
    show jecka sc2 angry
    $ setWait(48.127,49.629)
    $ speak(JECKA, "Why are you still here?")
    $ setWait(49.629,50.254)
    $ speak(CRISPIN, "Me?")

    show jecka sc2 angry

    $ setWait(50.254,51.673)
    $ speak(JECKA, "No, both of you.")
    $ setWait(51.673,54.175)
    $ speak(CRISPIN, "I was just tryna like- he was kinda going at you.")
    show nicole sc3 angry:
        xzoom 1
    $ setWait(54.175,56.719)
    $ speak(NICOLE, "We're not gonna fuck either of you.")
    show kylar sc1:
        xzoom 1
        leftmidstage
        linear 2 off_left

    show crispin sc2:
        rightmidstage
        pause 1
        xzoom -1
        linear 2.3 off_right

    $ setWait(56.719,57.512)
    $ speak(KYLAR, "Aw whatever then.")
    $ setWait(57.512,59.597)
    $ speak(CRISPIN, "Yeah n- um...")
    show jecka sc2:
        xzoom 1

    $ setWait(59.597,61.349)
    $ speak(JECKA, "They literally do that every week.")
    show nicole sc3

    $ setWait(61.349,64.936)
    $ speak(NICOLE, "Speaking of every week, are you still watching Real Housewives Atlanta?")
    $ setWait(64.936,66.854)
    $ speak(JECKA, "Nah I got tired of it.")
    $ setWait(66.854,67.814)
    $ speak(NICOLE, "Is it bad now?")
    $ setWait(67.814,75.071)
    $ speak(JECKA, "No just every commercial on Bravo's like \"Guess which celebrity's gay! We got him this time!\" it's annoying. For the gay channel it's kinda homophobic.")
    $ setWait(75.071,79.075)
    $ speak(NICOLE, "Yeah I only watch at midnight when they're selling Girls Gone Wild and Enzyte.")
    $ setWait(79.075,80.368)
    $ speak(JECKA, "Do you think they pay well?")
    $ setWait(80.368,81.369)
    $ speak(NICOLE, "Who? Bravo?")
    show lorre 1 smile:
        off_right
        linear 3 rightmidstage
    $ setWait(81.369,82.787)
    $ speak(JECKA, "No, Girls Gone Wild.")
    $ setWait(82.787,85.039)
    $ speak(LORRE, "There's my artists, hello girls.")
    show jecka sc2 surprised:
        xzoom -1

    $ setWait(85.039,85.748)
    $ speak(JECKA, "Oh god.")
    $ setWait(85.748,88.543)
    $ speak(NICOLE, "Let's keep the conversations to inside the classroom.")
    show jecka sc2
    show lorre 1
    $ setWait(88.543,99.22)
    $ speak(LORRE, "Oh I won't be long, I just wanted to compliment your effort today, Nicole. At first apprehensive but then sinking your teeth into the assignment more than anyone. Good showing.")
    $ setWait(99.22,100.888)
    $ speak(NICOLE, "Thanks, Mr. Lorre...")
    $ setWait(100.888,107.228)
    $ speak(LORRE, "I look forward to the final product. Beautiful girls make beautiful pictures, right girls?")
    $ setWait(107.228,108.479)
    $ speak(JECKA, "When it's a mirror photo.")
    show lorre 1 smile:
        rightmidstage
        linear 3.2 off_left

    show jecka sc2:
        pause 0.85
        xzoom 1

    $ setWait(108.479,111.315)
    $ speak(LORRE, "I'll see you on Thursday, Nicole.")
    show nicole sc3 angry
    $ setWait(111.315,113.443)
    $ speak(NICOLE, "What a fucking weirdo, what's his problem?")
    show jecka sc2 worried
    $ setWait(113.443,115.653)
    $ speak(JECKA, "I think he's a tiny bit into you.")
    $ setWait(115.653,117.697)
    $ speak(NICOLE, "Cool another child predator.")
    show jecka sc2

    $ setWait(117.697,119.991)
    $ speak(JECKA, "You've literally said that about every guy teacher here.")
    $ setWait(119.991,124.12)
    $ speak(NICOLE, "Well it's literally true. You still have a dad so they don't go for you as much.")
    $ setWait(124.12,124.871)
    $ speak(JECKA, "Really?")
    show nicole sc3
    $ setWait(124.871,130.877)
    $ speak(NICOLE, "Yeah \"sexual father figure\" is like top five male fantasies. Right after murder.")
    show jecka sc2 surprised
    $ setWait(130.877,134.714)
    $ speak(JECKA, "Oh and if they hook up with you there's no angry dad to kick their ass over it.")
    $ setWait(134.714,138.342)
    $ speak(NICOLE, "Exactly. So you could be prettier, but I'm way more desirable.")
    show jecka sc2
    $ setWait(138.342,142.93)
    $ speak(JECKA, "I've had my fair share of guy teachers flirt with me I just don't jump to all of them wanting sex.")
    $ setWait(142.93,145.6)
    $ speak(NICOLE, "Well no not all of them, just like 90%%.")
    $ setWait(145.6,146.642)
    show jecka sc2
    $ speak(JECKA, "That high?")
    $ setWait(146.642,151.939)
    $ speak(NICOLE, "Yeah I'm pretty sure like 90%% of men have the urge to sexually murder teenage girls.")
    $ setWait(151.939,157.028)
    $ speak(NICOLE, "Anyone who opposes that is probably like.. some ugly white guy who gets mad at video games.")
    show jecka sc2 worried

    $ setWait(157.028,158.246)
    $ speak(JECKA, "Is that a thing?")
    stop ambient fadeout 1.2

    jump scene_0145
label scene_0145:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show home nicole ext night with Pause(2.33):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.33 zoom 0.7 truecenter

    $ setVoiceTrack("audio/Scenes/0145.mp3")
    play ambient "audio/Ambience/House_Night_Ambience.mp3"
    scene home nicole int
    show nicole sc3:
        xzoom -1
        off_right
        linear 1.6 rightmidstage

    $ setWait(2.33,4.332)
    $ speak(NICOLE, "I wonder if Jamie Lynn had that baby yet.")
    show mom 2:
        off_left
        xzoom -1
        linear 2.6 leftcenterstage

    $ setWait(4.332,8.878)
    $ speak(MOM, "Excuse me, Nicole? First week of school and your friends are already pregnant?")
    show nicole sc3 angry
    $ setWait(8.878,11.089)
    $ speak(NICOLE, "No Mom-- Jamie Lynn Spears??")
    show mom 2 upset

    $ setWait(11.089,15.718)
    $ speak(MOM, "I don't care who her parents are, I don't want you hanging around girls who make bad decisions.")
    $ setWait(15.718,16.636)
    $ speak(NICOLE, "Little late for that.")
    show mom 2:
        xzoom -1
        leftcenterstage
        linear 2.5 rightcenterstage

    $ setWait(16.636,19.848)
    $ speak(MOM, "This is a new year and I want you to start it off right.")
    show nicole sc3 angry:
        xzoom -1
        rightmidstage
        linear 1.55 leftcenterstage
        xzoom 1
    $ setWait(19.848,21.391)
    $ speak(NICOLE, "As if I did last year wrong?")
    show mom 2 upset:
        xzoom 1
        rightcenterstage

    $ setWait(21.391,24.644)
    $ speak(MOM, "Oh let me count the ways, far too many for a number.")
    $ setWait(24.644,27.021)
    $ speak(NICOLE, "Yeah right, name one incident.")
    $ setWait(27.021,29.148)
    $ speak(MOM, "The time you dated your gym teacher?")
    show nicole sc3:
        leftcenterstage
        xzoom 1

    $ setWait(29.148,30.692)
    $ speak(NICOLE, "I needed money, that doesn't count.")
    $ setWait(30.692,33.778)
    $ speak(MOM, "Then how about when you caused a boy to get locked in the psych ward?")
    show nicole sc3 angry
    $ setWait(33.778,35.947)
    $ speak(NICOLE, "It's not my fault I'm beautiful, Mom.")
    $ setWait(35.947,41.16)
    $ speak(MOM, "I didn't know it was common for beautiful girls to ask for a gallon of their partner's blood.")
    show nicole sc3
    $ setWait(41.16,43.58)
    $ speak(NICOLE, "If they're beautiful and hot? Absolutely.")
    $ setWait(43.58,47.876)
    $ speak(MOM, "Okay then explain the time you set a POW-MIA flag on fire in the cafeteria.")
    $ setWait(47.876,50.169)
    $ speak(NICOLE, "It was funny? Honestly answer that for all of them.")
    show mom 2 angry
    $ setWait(50.169,54.549)
    $ speak(MOM, "It's excuse after excuse, you're driving me crazy with your bullshit, Nicole!")
    show nicole sc3 sad
    $ setWait(54.549,56.718)
    $ speak(NICOLE, "I just got the fuck home, can we do this later!?")
    $ setWait(56.718,60.805)
    $ speak(MOM, "Another excuse! Get your shit together and we won't have this problem!")
    show nicole sc3 angry

    $ setWait(60.805,62.39)
    $ speak(NICOLE, "What shit?? I'm fine!")
    $ setWait(62.39,68.187)
    $ speak(MOM, "Stop lying, quit shoplifting, don't talk back to your teachers, and fix your fucking drug problem!")
    show nicole sc3 sad
    $ setWait(68.187,70.94)
    $ speak(NICOLE, "What drug problem?? What are you talking about!?")
    $ setWait(70.94,73.61)
    $ speak(MOM, "Stay out of my medicine cabinet, Nicole.")
    $ setWait(73.61,76.112)
    $ speak(NICOLE, "Mom you are so fucking paranoid right now!")
    $ setWait(76.112,79.365)
    $ speak(MOM, "Am I? You wouldn't mind if I looked in your backpack, would you!?")
    show nicole sc3 angry
    $ setWait(79.365,81.91)
    $ speak(NICOLE, "I would mind! But you wouldn't find shit anyway!")
    $ setWait(81.91,83.828)
    $ speak(MOM, "Cause you did it all at school, right?")
    $ setWait(83.828,85.58)
    $ speak(NICOLE, "What is this? The Salem Ho Trials??")
    show mom 2 upset
    $ setWait(85.58,87.749)
    $ speak(MOM, "You have two options, Nicole.")
    show mom 2 angry
    $ setWait(87.749,95.048)
    $ speak(MOM, "Live by the rules of society, or live on the god damn street!\nRight now your school work is the only thing keeping you here.")
    $ setWait(95.048,96.382)
    $ speak(NICOLE, "You wouldn't kick me out!")
    show mom 2 upset
    $ setWait(96.382,98.676)
    $ speak(MOM, "I can do whatever I want!")
    $ setWait(98.676,100.178)
    $ speak(NICOLE, "Except find a good husband, right?")
    show mom 2 angry
    $ setWait(100.178,101.679)
    $ speak(MOM, "Shut your fucking mouth!")
    $ setWait(101.679,103.598)
    $ speak(NICOLE, "The MILF window's closing, Mom!")
    $ setWait(103.598,106.059)
    $ speak(MOM, "Ugh I wanna hit you so bad right now!")
    show mom 2 angry:
        rightcenterstage
        linear 1.6 off_left

    $ setWait(106.059,108.436)
    $ speak(MOM, "Where's my Valium??")
    show nicole sc3:
        leftcenterstage
        linear 2 centerstage

    $ setWait(108.436,109.896)
    $ speak(NICOLE, "Top shelf on the left.")
    stop ambient fadeout 1
    jump scene_0146
label scene_0146:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Classroom_Ambience.mp3" fadein 1.5


    $ setVoiceTrack("audio/Scenes/0146.mp3")
    scene photo classroom

    show jecka sc3:
        xzoom -1
        leftstage

    show nicole sc4:
        leftmidstage

    show kylar sc2:
        rightmidstage


    $ setWait(0.035,3.08)
    $ speak(JECKA, "Why do guys say \"we\" when they talk about football teams?")
    $ setWait(3.08,4.373)
    $ speak(NICOLE, "Hold on.")
    $ setWait(4.373,6.083)
    $ speak(JECKA, "What are you drawing? Can I see?")
    $ setWait(6.083,7.834)
    $ speak(NICOLE, "No no, not yet. Surprise.")
    $ setWait(7.834,11.922)
    $ speak(JECKA, "I don't know what you're drawing for this class but it better be really good if you care this much.")
    show nicole sc4:
        xzoom -1
    $ setWait(11.922,13.382)
    $ speak(NICOLE, "We're graded on effort.")
    show nicole sc4:
        xzoom 1

    $ setWait(13.382,16.426)
    $ speak(JECKA, "I wonder if art studios hire based on effort.")
    show kylar sc2 smile
    $ setWait(16.426,17.969)
    $ speak(KYLAR, "Aw just finished my drawing!")
    $ setWait(17.969,19.054)
    $ speak(JECKA, "What'd you draw?")
    $ setWait(19.054,22.057)
    $ speak(KYLAR, "Bitches getting killed. Women dying is cool.")
    $ setWait(22.057,23.934)
    $ speak(JECKA, "You should move when you graduate.")
    show lorre 1:
        off_right
        linear 4.5 centerstage

    show kylar sc2

    $ setWait(23.934,33.068)
    $ speak(LORRE, "Unfortunately the deadline for your character drawings has come. I will now walk around to provide feedback and collect your artwork.")
    $ setWait(33.068,33.86)
    $ speak(LORRE, "Jecka?")
    show drawing_jecka onlayer screens
    $ setWait(33.86,34.986)
    $ speak(JECKA, "Oh here.")
    $ setWait(34.986,36.697)
    $ speak(LORRE, "Care to explain the piece to me?")
    show jecka sc3 smile

    $ setWait(36.697,38.824)
    $ speak(JECKA, "It's me and Ryan Sheckler at the Warped Tour.")
    $ setWait(38.824,39.95)
    $ speak(KYLAR, "Ryan Sheckler?")
    hide drawing_jecka onlayer screens
    show jecka sc3 angry
    $ setWait(39.95,41.493)
    $ speak(JECKA, "Yeah bitch, he's sexy.")
    $ setWait(41.493,45.539)
    $ speak(KYLAR, "That's an unlockable character in Tony Hawk, he's not even real.")
    $ setWait(45.539,47.165)
    $ speak(NICOLE, "You are really fuckin' stupid.")
    show lorre 1 angry
    $ setWait(47.165,48.834)
    $ speak(LORRE, "Watch the language, Nicole.")
    show nicole sc4 surprised
    show lorre 1
    $ setWait(48.834,52.212)
    $ speak(NICOLE, "Fuck sorry-- I mean shit sorry-- I mean.. whatever.")
    show nicole sc4

    $ setWait(52.212,54.589)
    $ speak(LORRE, "Now I'm very interested to see yours.")
    $ setWait(54.589,55.465)
    $ speak(NICOLE, "Are you sure?")
    $ setWait(55.465,58.343)
    $ speak(LORRE, "You worked hard on it, let's share it with the class.")
    show nicole sc4 smile
    show drawing_nicole onlayer screens:
        alpha 0.0
        pause 1.3 alpha 1.0
    $ setWait(58.343,60.554)
    $ speak(NICOLE, "If you say so.")

    $ setWait(60.554,63.306)
    $ speak(LORRE, "This is... What is this??")
    $ setWait(63.306,68.145)
    $ speak(NICOLE, "Oh it's a picture of you killing yourself while your wife blows the UPS man.")
    show lorre 1 angry
    show jecka sc3 smile
    show kylar sc2 smile

    hide drawing_nicole onlayer screens
    $ setWait(68.145,71.481)
    $ speak(LORRE, "What-- How-- Where'd you get this information!?")
    show nicole sc4 surprised
    $ setWait(71.481,74.901)
    $ speak(NICOLE, "Oh my god I'm so sorry, was it FedEx?")
    $ setWait(74.901,77.028)
    $ speak(LORRE, "This isn't funny, Nicole!")
    $ setWait(77.028,78.613)
    $ speak(JECKA, "I think it's pretty funny.")
    $ setWait(78.613,86.705)
    $ speak(LORRE, "Insubordination, inappropriate imagery, and sexual harassment of faculty! I'll let Principal Lynn handle you!")
    show nicole sc4 angry

    $ setWait(86.705,89.082)
    $ speak(NICOLE, "I'm sorry, sexual harassment??")
    $ setWait(89.082,91.042)
    $ speak(LORRE, "That's precisely what this is.")
    $ setWait(91.042,95.131)
    $ speak(NICOLE, "There's nothing sexy about you, it's just regular harassment.")
    stop ambient fadeout 1
    jump scene_0147
label scene_0147:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0147.mp3")
    play ambient "audio/Ambience/House_Ambience.mp3" fadein 1

    scene home nicole int
    show nicole sc4 angry:
        xzoom -1
        off_right
        linear 2.58 rightcenterstage

    $ setWait(0.039,2.583)
    $ speak(NICOLE, "This bitch better have some Valium left.")
    $ setWait(2.583,3.71)
    $ speak(MOM, "Expelled!?")

    show nicole sc4:
        rightcenterstage
        xzoom -1

    $ setWait(3.71,4.46)
    $ speak(NICOLE, "Guess not.")
    show mom 1 angry:
        xzoom -1
        off_left
        linear 1.4 leftmidstage

    $ setWait(4.46,7.505)
    $ speak(MOM, "I told you you were on thin ice, and what'd you go and do!?")
    show nicole sc4 angry

    $ setWait(7.505,9.674)
    $ speak(NICOLE, "What the fuck are you talking about!?")
    $ setWait(9.674,14.304)
    $ speak(MOM, "You really think they'd refer you to the board for expulsion without giving me a phone call??")
    $ setWait(14.304,17.557)
    $ speak(NICOLE, "The fuck you mean expelled? I got suspended, thank you!")
    $ setWait(17.557,19.559)
    $ speak(MOM, "Suspended indefinitely!")
    show nicole sc4 sad
    $ setWait(19.559,23.396)
    $ speak(NICOLE, "Yeah indefinitely! Meaning not definite, like not for sure.")
    $ setWait(23.396,27.734)
    $ speak(MOM, "Meaning until they know what to do with you! That's how much trouble you're in!")
    show nicole sc4 angry

    $ setWait(27.734,31.696)
    $ speak(NICOLE, "Fucking what ever, it's not a big deal, Mom! They always threaten this.")
    $ setWait(31.696,33.197)
    $ speak(MOM, "And what if they follow through??")
    $ setWait(33.197,35.7)
    $ speak(NICOLE, "I don't know, it's not even your problem just fuck off!")
    show mom 1 upset
    $ setWait(35.7,37.785)
    $ speak(MOM, "So I'd take it you're not my problem either?")
    $ setWait(37.785,38.911)
    $ speak(NICOLE, "Definitely not.")
    show mom 1

    $ setWait(38.911,41.789)
    $ speak(MOM, "Fine, as of tonight you no longer live here.")
    show nicole sc4 surprised
    $ setWait(41.789,42.373)
    $ speak(NICOLE, "What?")
    show mom 1 upset
    $ setWait(42.373,45.293)
    $ speak(MOM, "You heard me. Pack your shit, get out of my house.")
    show nicole sc4 angry
    $ setWait(45.293,47.67)
    $ speak(NICOLE, "Go drink some wine, you're such a bitch when you're sober.")
    show mom 1 angry

    $ setWait(47.67,49.422)
    $ speak(MOM, "Get the fuck out of my house!")
    show nicole sc4 sad
    $ setWait(49.422,51.382)
    $ speak(NICOLE, "Are you serious right now? C'mon.")
    show mom 1 upset

    $ setWait(51.382,52.759)
    $ speak(MOM, "Should I call the police?")
    show nicole sc4 angry
    $ setWait(52.759,55.053)
    $ speak(NICOLE, "Y'know what, do it!")
    show mom 1 upset:
        xzoom 1
        leftmidstage
        linear 1.3 off_left

    $ setWait(55.053,57.889)
    $ speak(MOM, "...")
    show nicole sc4 surprised:
        xzoom 1
        rightcenterstage
        linear 1 off_right

    $ setWait(57.889,59.974)
    $ speak(NICOLE, "God dammit.")
    stop ambient fadeout 1
    jump scene_0148
label scene_0148:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Neighborhood_Ambience_Night.mp3" fadein 1
    scene onlayer master
    show black
    show house jecka night with Pause(2.342):
        zoom 1 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.342 zoom 1.08 truecenter

    $ setVoiceTrack("audio/Scenes/0148.mp3")
    scene porch_jecka
    show nicole sc4 angry:
        leftstage
        xzoom -1


    $ setWait(2.342,5.512)
    $ speak(NICOLE, "Hurry up, I texted like five minutes ago.")
    show jecka pj angry:
        xzoom -1
        off_left
        linear 0.9 leftstage

    show nicole sc4:
        leftstage
        xzoom -1
        pause 0.5
        linear 0.28 leftmidstage

    $ setWait(5.512,7.138)
    $ speak(JECKA, "Okay what the hell is going on?")
    $ setWait(7.138,9.39)
    $ speak(NICOLE, "Do you still have that futon in your basement?")
    show jecka pj
    $ setWait(9.39,12.143)
    $ speak(JECKA, "Yeah, it's covered in dried Mr. Pibb but yeah.")
    show nicole sc4 sad
    $ setWait(12.143,14.229)
    $ speak(NICOLE, "I guess that's fine, can I sleep here?")
    show jecka pj surprised

    $ setWait(14.229,14.896)
    $ speak(JECKA, "Tonight??")
    show nicole sc4 angry

    $ setWait(14.896,16.189)
    $ speak(NICOLE, "No bitch, tomorrow.")
    show jecka pj sad

    $ setWait(16.189,20.11)
    $ speak(JECKA, "Are you really getting expelled over that drawing? That's bullshit, just tell your Mom that.")
    $ setWait(20.11,24.072)
    $ speak(NICOLE, "I'm done telling my Mom anything. She can rot in a tanning bed for all I care.")
    show jecka pj
    $ setWait(24.072,26.908)
    $ speak(JECKA, "Well you're gonna rot in the street if you don't work it out with her.")
    show nicole sc4 sad
    $ setWait(26.908,28.785)
    $ speak(NICOLE, "Dude you have a house, just let me stay with you.")
    show jecka pj sad
    $ setWait(28.785,34.916)
    $ speak(JECKA, "If it was my house you could stay all you want but it's my parents' house. Mom'll get pissed, Dad'll probably hit on you, it'll be weird.")
    show nicole sc4 smile
    $ setWait(34.916,37.585)
    $ speak(NICOLE, "Okay so you and your dad against her, that's perfect lemme stay.")
    show nicole sc4
    $ setWait(37.585,41.965)
    $ speak(JECKA, "No, Nicole. Like I wish I could help but, I don't know.")
    show nicole sc4 sad
    $ setWait(41.965,45.009)
    $ speak(NICOLE, "Well can you at least gimme all the fruit roll-ups in your kitchen?")
    show jecka pj angry:
        leftstage
        xzoom -1
        pause 0.6
        xzoom 1
        linear 1.3 off_left

    $ setWait(45.009,47.679)
    $ speak(JECKA, "Ugh I'll be right back.")
    show nicole sc4:
        leftmidstage
        xzoom 1
        linear 2 centerstage

    $ setWait(47.679,50.849)
    $ speak(NICOLE, "Wonder which mall has the softest benches...")
    stop ambient fadeout 1.5
    jump scene_0149
label scene_0149:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.2 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0

    play ambient "audio/Ambience/Mall_Ambience.mp3" fadein 2
    $ setVoiceTrack("audio/Scenes/0149.mp3")
    scene mall int
    show emily sc3:
        xzoom -1
        rightmidstage

    show nicole sc4 angry:
        off_left
        linear 3.4 leftcenterstage


    $ setWait(0.047,3.968)
    $ speak(NICOLE, "Those were the worst benches ever, it's like they don't want homeless customers.")
    show emily sc3:
        xzoom 1
        rightmidstage
        linear 1 rightcenterstage

    $ setWait(3.968,5.803)
    $ speak(EMILY, "Damn Nicole you're here early.")
    show nicole sc4
    $ setWait(5.803,7.763)
    $ speak(NICOLE, "Yeah you too, what for?")
    $ setWait(7.763,9.473)
    $ speak(EMILY, "Just buying something.")
    $ setWait(9.473,10.474)
    $ speak(NICOLE, "...Buying what?")
    show emily sc3 upset
    $ setWait(10.474,11.433)
    $ speak(EMILY, "Are you a cop?")
    show nicole sc4 angry
    $ setWait(11.433,13.018)
    $ speak(NICOLE, "Bitch do I look like a cop?")
    show emily sc3
    $ setWait(13.018,16.188)
    $ speak(EMILY, "Yeah just waiting for Kylar, he's supposed to sell me his oxy.")
    show nicole sc4
    $ setWait(16.188,17.481)
    $ speak(NICOLE, "He's got a lot, right?")
    $ setWait(17.481,21.235)
    $ speak(EMILY, "Totally these dumbass white guys break their legs and turn into pharmacies.")
    $ setWait(21.235,23.779)
    $ speak(NICOLE, "I'd buy more from him but then I'd have to give him my phone number.")
    $ setWait(23.779,25.906)
    $ speak(EMILY, "No you don't. MySpace, make a ghost account.")
    show nicole sc4 surprised
    $ setWait(25.906,27.032)
    $ speak(NICOLE, "A ghost account?")
    show nicole sc4

    $ setWait(27.032,32.454)
    $ speak(EMILY, "Or they call it a burner, or a puppet, basically an account separate from you where you do illegal shit.")
    $ setWait(32.454,34.373)
    $ speak(NICOLE, "Oh I think I already have one of those.")
    $ setWait(34.373,35.457)
    $ speak(EMILY, "What do you use it for?")
    $ setWait(35.457,37.292)
    $ speak(NICOLE, "Stalking people who blocked me.")
    $ setWait(37.292,43.966)
    $ speak(EMILY, "Kind of a waste.\nYou add the right people you can buy anything on there. Drugs, guns, ass, whatever.")
    $ setWait(43.966,48.053)
    $ speak(NICOLE, "Drugs, guns, and ass... And the cops aren't tracking that?")
    show emily sc3 angry
    $ setWait(48.053,51.306)
    $ speak(EMILY, "No, they're old ass cops, they can't figure that shit out.")
    $ setWait(51.306,57.146)
    $ speak(NICOLE, "Cool, yeah this is good to hear cause my Mom kicked me out yesterday. I should buy something to forget about this shit.")
    show emily sc3
    $ setWait(57.146,58.897)
    $ speak(EMILY, "Are you couch surfing or straight up homeless?")
    $ setWait(58.897,61.608)
    $ speak(NICOLE, "Homeless straight up, I slept on a bench last night.")
    show emily sc3 upset
    $ setWait(61.608,63.861)
    $ speak(EMILY, "Damn... well go make some money on MySpace.")
    $ setWait(63.861,66.196)
    $ speak(NICOLE, "But I don't have any drugs or guns to sell.")
    $ setWait(66.196,67.281)
    $ speak(EMILY, "You know what I meant.")
    show nicole sc4 sad
    $ setWait(67.281,70.576)
    $ speak(NICOLE, "Ugh I don't know if I'm ready to be a MySpace escort.")
    $ setWait(70.576,72.036)
    $ speak(EMILY, "Have you never thought about it before?")
    $ setWait(72.036,76.04)
    $ speak(NICOLE, "No I think about it every week I just never thought I'd have this crossroad in high school.")
    show emily sc3
    $ setWait(76.04,78.417)
    $ speak(EMILY, "Shit happens, dude. I wouldn't think any less of you.")
    $ setWait(78.417,81.628)
    $ speak(NICOLE, "Yeah but would I think less of myself?")
    show nicole sc4
    show kylar sc3:
        off_right
        linear 1 rightstage

    show emily sc3:
        pause 0.5
        xzoom -1
    $ setWait(81.628,83.172)
    $ speak(KYLAR, "Yo what's up? I got the shit.")
    show emily sc3 angry:
        rightcenterstage
        xzoom -1
        linear 0.7 rightmidstage

    $ setWait(83.172,84.548)
    $ speak(EMILY, "Where the fuck were you?")
    $ setWait(84.548,87.968)
    $ speak(KYLAR, "Places? I got shit to do I'm not some drug addict like you.")
    $ setWait(87.968,90.179)
    $ speak(EMILY, "They're not for me, they're for my boyfriend.")
    $ setWait(90.179,92.723)
    $ speak(KYLAR, "You have a boyfriend? I don't even wanna sell this to you anymore.")
    $ setWait(92.723,95.476)
    $ speak(EMILY, "Are you kidding me? I got a hundred for the bottle right here.")
    $ setWait(95.476,96.226)
    $ speak(KYLAR, "110.")
    $ setWait(96.226,98.562)
    $ speak(EMILY, "You said a hundred on MySpace, asshole.")
    $ setWait(98.562,100.272)
    $ speak(KYLAR, "Yeah but you didn't say you had a boyfriend.")
    $ setWait(100.272,102.191)
    $ speak(EMILY, "Fuck me, okay 110, here.")
    show kylar sc3 smile

    $ setWait(102.191,104.068)
    $ speak(KYLAR, "Thanks, and lemme know when you're single.")
    show emily sc3:
        xzoom 1
        rightmidstage
        linear 4.5 off_left

    $ setWait(104.068,105.36)
    $ speak(EMILY, "Lemme know when you're not.")
    show kylar sc3

    $ setWait(105.36,105.903)
    $ speak(KYLAR, "What?")
    $ setWait(105.903,106.987)
    $ speak(EMILY, "Have fun, Nicole.")

    show nicole sc4:
        xzoom -1

    $ setWait(106.987,108.072)
    $ speak(NICOLE, "I'll try.")
    show kylar sc3:
        rightstage
        linear 2.5 rightcenterstage

    $ setWait(108.072,110.324)
    $ speak(KYLAR, "Gotta get home before Mind Of Mencia comes on.")
    show nicole sc4:
        xzoom 1

    $ setWait(110.324,112.409)
    $ speak(NICOLE, "Kylar can I have a pill? I don't have a boyfriend.")
    $ setWait(112.409,114.953)
    $ speak(KYLAR, "Panhandling pills? What're you homeless?")
    show nicole sc4 surprised

    $ setWait(114.953,116.497)
    $ speak(NICOLE, "Uh.. No.")
    show nicole sc4
    show kylar sc3 smile
    $ setWait(116.497,121.168)
    $ speak(KYLAR, "Oh good yeah you can have one cause I fucking hate the homeless.")
    $ setWait(121.168,121.835)
    $ speak(NICOLE, "Okay.")
    $ setWait(121.835,128.258)
    $ speak(KYLAR, "Seriously, like a lot of politicians just say that but I actually want homeless people exterminated off the planet.")
    $ setWait(128.258,129.802)
    $ speak(NICOLE, "Yeah that's an opinion.")
    $ setWait(129.802,135.933)
    $ speak(KYLAR, "Like the only way they could contribute to our society is by jumping in a meat grinder so we have something to feed farm animals--")
    show nicole sc4 yell
    $ setWait(135.933,137.059)
    $ speak(NICOLE, "Gimme the fucking pill!")
    show nicole sc4 angry
    show kylar sc3
    $ setWait(137.059,138.685)
    $ speak(KYLAR, "Whoa fine, are you like an addict?")
    show nicole sc4

    $ setWait(138.685,139.645)
    $ speak(NICOLE, "You could say that.")
    show kylar sc3 smile
    $ setWait(139.645,143.357)
    $ speak(KYLAR, "Sweet yeah, drug addict girls are hot cause they're really easy to control.")
    show nicole sc4 angry
    $ setWait(143.357,144.525)
    $ speak(NICOLE, "Jesus Christ!")
    show kylar sc3
    $ setWait(144.525,145.317)
    $ speak(KYLAR, "What??")
    show nicole sc4 surprised
    $ setWait(145.317,146.777)
    $ speak(NICOLE, "Oh uh...")
    show nicole sc4
    $ setWait(146.777,148.737)
    $ speak(NICOLE, "I think Mind Of Mencia's starting soon!")
    show kylar sc3 sad:
        rightcenterstage
        pause 1
        linear 1.6 off_left

    $ setWait(148.737,151.615)
    $ speak(KYLAR, "Aw you're right, I gotta go!")
    show nicole sc4:
        xzoom -1

    $ setWait(151.615,154.284)
    $ speak(NICOLE, "Okay I gotta figure something out.")
    stop ambient fadeout 3
    menu:
        "WORK AT\nDYING DVD STORE":
            jump scene_0150
        "START YOUR OWN\nCAR WASH":
            jump scene_0153
label scene_0150:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0150.mp3")
    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene breakroom
    show nicole fye:
        leftcenterstage

    show kelly fye:
        rightcenterstage

    $ setWait(0.035,2.621)
    $ speak(KELLY, "Okay so welcome to FYE.")
    $ setWait(2.621,3.83)
    $ speak(NICOLE, "I thought it was \"Fie\"?")
    $ setWait(3.83,8.877)
    $ speak(KELLY, "Uh no, FYE, it's an abbreviation. I'm Kelly, I'll be your manager.")
    $ setWait(8.877,10.587)
    $ speak(NICOLE, "Yeah we go to school together.")
    show kelly fye sad
    $ setWait(10.587,13.173)
    $ speak(KELLY, "Do we? I don't think we've properly met.")
    show nicole fye angry
    $ setWait(13.173,14.215)
    $ speak(NICOLE, "Are you fucking with me?")
    show kelly fye
    $ setWait(14.215,24.517)
    $ speak(KELLY, "Okay, Nicole, that language is okay amongst co-workers but not in front of the customers.\nSo first training question, what does FYE stand for?")
    show nicole fye
    $ setWait(24.517,26.645)
    $ speak(NICOLE, "...For Your Excitement?")
    $ setWait(26.645,27.854)
    $ speak(KELLY, "Try again.")
    $ setWait(27.854,30.44)
    $ speak(NICOLE, "For Your Ejaculation?")
    $ setWait(30.44,32.567)
    $ speak(KELLY, "No, that's our adult video branch.")
    $ setWait(32.567,35.278)
    $ speak(NICOLE, "For Your Entertainment?")
    $ setWait(35.278,41.159)
    $ speak(KELLY, "Good! But not only are the products for the customer's entertainment, it's also the store experience.")
    $ setWait(41.159,43.161)
    $ speak(NICOLE, "Are you saying we gotta flirt with the customers?")
    $ setWait(43.161,45.288)
    $ speak(KELLY, "If you wanna sell that rewards program.")
    $ setWait(45.288,46.539)
    $ speak(NICOLE, "Is that optional?")
    $ setWait(46.539,48.541)
    $ speak(KELLY, "Sell it once a month or else you're fired.")
    $ setWait(48.541,52.003)
    $ speak(NICOLE, "Oh and after hours am I allowed to sleep in the break room?")
    $ setWait(52.003,54.798)
    $ speak(KELLY, "I mean I don't care but the regional manager might.")
    $ setWait(54.798,58.593)
    $ speak(NICOLE, "I can close every night. Even the days I'm not working I'll just show up to close.")
    $ setWait(58.593,62.013)
    $ speak(KELLY, "Dang really? Yeah do whatever you want then, go getter.")
    $ setWait(62.013,63.098)
    $ speak(NICOLE, "And do you drug test?")
    $ setWait(63.098,65.725)
    $ speak(KELLY, "No. It's an FYE, not a hospital.")
    show nicole fye smile

    $ setWait(65.725,67.018)
    $ speak(NICOLE, "This is gonna be sick.")
    show kelly fye:
        rightcenterstage
        pause 1
        xzoom -1
        linear 2.1 off_right

    show nicole fye smile:
        leftcenterstage
        pause 1.3
        linear 2.6 off_right

    $ setWait(67.018,70.647)
    $ speak(KELLY, "Glad to hear! Let's go out on the floor so I can show you how it's done.")
    stop ambient fadeout 1
    jump scene_0151
label scene_0151:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0151.mp3")

    play ambient "audio/Ambience/Fye_NoMusic_Ambience.mp3" fadein 1

    scene fye

    show nicole fye:
        leftmidstage

    show kelly fye:
        leftcenterstage



    $ setWait(0.035,5.541)
    $ speak(KELLY, "Okay we're just opening so some customers are gonna show soon. Remember the four steps to the register?")
    $ setWait(5.541,8.919)
    $ speak(NICOLE, "Greet, compliment, help, entertain?")
    $ setWait(8.919,10.254)
    $ speak(KELLY, "Oh my god, good memory.")
    show crispin sc4:
        off_right
        linear 4 rightmidstage


    $ setWait(10.254,12.548)
    $ speak(NICOLE, "I try, cause I have to now.")

    show kelly fye:
        leftcenterstage
        pause 1.4
        xzoom -1
        linear 0.8 rightcenterstage


    $ setWait(12.548,16.635)
    $ speak(KELLY, "Oh customer, watch this- Hey welcome to FYE, I'm Kelly!")
    show crispin sc4 smile
    $ setWait(16.635,17.678)
    $ speak(CRISPIN, "Oh yeah hey.")
    $ setWait(17.678,19.305)
    $ speak(KELLY, "Nice shirt by the way.")
    $ setWait(19.305,22.933)
    $ speak(CRISPIN, "Thanks uh, yeah most people were kinda down on this Guns & Roses.")
    $ setWait(22.933,26.562)
    $ speak(KELLY, "Really? I thought it was even better than the first movie.")
    show crispin sc4
    $ setWait(26.562,27.229)
    $ speak(CRISPIN, "Movie?")
    $ setWait(27.229,29.231)
    $ speak(KELLY, "So you looking for anything in particular?")
    $ setWait(29.231,31.775)
    $ speak(CRISPIN, "Uh some DVD box sets for a road trip.")
    show kelly fye:
        xzoom 1
        rightcenterstage
        linear 11.5 off_farleft

    show crispin sc4:
        rightmidstage
        pause 0.6
        linear 12 off_left

    $ setWait(31.775,37.156)
    $ speak(KELLY, "Oh yeah collections are right over here. But you gotta pick the right one or you're in for a miserable drive.")
    $ setWait(37.156,38.032)
    $ speak(CRISPIN, "Yeah really?")
    $ setWait(38.032,41.619)
    $ speak(KELLY, "My ex-boyfriend picked the most boring movies, that's why I'm single now.")
    $ setWait(41.619,44.914)
    $ speak(CRISPIN, "Aw man sorry to hear, what a mistake.")
    hide crispin sc4
    hide kelly fye
    show nicole fye:
        xzoom -1

    $ setWait(44.914,49.585)
    $ speak(NICOLE, "And the difference between this and whoring myself out on MySpace is...")
    show jeffery sc3:
        off_right
        linear 2 rightmidstage

    $ setWait(49.585,52.838)
    $ speak(JEFFERY, "I wonder if this place has anime... Nicole?")
    show nicole fye:
        xzoom 1
        leftmidstage
        linear 1.6 leftcenterstage

    $ setWait(52.838,54.882)
    $ speak(NICOLE, "Hi, welcome to FYE.")
    $ setWait(54.882,56.425)
    $ speak(JEFFERY, "I didn't know you worked here.")
    $ setWait(56.425,61.18)
    $ speak(NICOLE, "Well now you do. By the way nice um... Damn.")
    $ setWait(61.18,62.097)
    $ speak(JEFFERY, "Nice what?")
    show nicole fye sad
    $ setWait(62.097,64.391)
    $ speak(NICOLE, "Compliment uh- You...")
    show nicole fye
    $ setWait(64.391,67.561)
    $ speak(NICOLE, "Don't look like a regular rapist.")
    $ setWait(67.561,68.646)
    $ speak(JEFFERY, "Thanks?")
    $ setWait(68.646,70.105)
    $ speak(NICOLE, "So are you looking for anything?")
    $ setWait(70.105,75.069)
    $ speak(JEFFERY, "Well actually I wandered in here under the assumption there would be anime DVDs.")
    $ setWait(75.069,76.904)
    $ speak(NICOLE, "Cool.")
    $ setWait(76.904,79.239)
    $ speak(JEFFERY, "Um... Do you have any?")
    $ setWait(79.239,82.201)
    $ speak(NICOLE, "No we don't carry anime, so sorry you're gonna have to leave.")
    $ setWait(82.201,83.494)
    $ speak(JEFFERY, "Leave? But why?")
    $ setWait(83.494,86.413)
    $ speak(NICOLE, "You're just gross? You look like you breast fed 'till you were 8.")
    show jeffery sc3 angry
    $ setWait(86.413,89.5)
    $ speak(JEFFERY, "Wha!? You're just saying that cause of my breast milk fetish!")
    show nicole fye surprised
    $ setWait(89.5,91.251)
    $ speak(NICOLE, "Oh now you really have to leave.")
    show jeffery sc3 blush
    show nicole fye
    $ setWait(91.251,92.461)
    $ speak(JEFFERY, "B-but... But!")
    show kelly fye:
        xzoom -1
        off_left
        linear 1.8 rightcenterstage

    $ setWait(92.461,95.297)
    $ speak(KELLY, "Nicole! Welcome to FYE, I'm Kelly.")
    $ setWait(95.297,96.006)
    $ speak(JEFFERY, "Hello.")
    $ setWait(96.006,98.717)
    $ speak(KELLY, "I like your shirt, dude, really funny.")
    show jeffery sc3 smile
    $ setWait(98.717,101.637)
    $ speak(JEFFERY, "Oh thanks, my Mom got it for me at Target.")
    $ setWait(101.637,102.596)
    $ speak(NICOLE, "That's really hot.")
    $ setWait(102.596,104.264)
    $ speak(KELLY, "What brings you here today?")
    show jeffery sc3
    $ setWait(104.264,105.474)
    $ speak(JEFFERY, "Anime?")
    show kelly fye:
        pause 2.9
        xzoom 1

    $ setWait(105.474,110.396)
    $ speak(KELLY, "So we only have a few anime DVDs but you can look at them on that back shelf.")
    show jeffery sc3 smile:
        rightmidstage
        linear 3.5 off_left

    $ setWait(110.396,113.273)
    $ speak(JEFFERY, "Oh okay, I could browse for a moment.")
    $ setWait(113.273,115.275)
    $ speak(KELLY, "And I'll be with you in just a sec.")
    show kelly fye angry
    $ setWait(115.275,117.736)
    $ speak(KELLY, "Nicole could I have a word with you in the break room?")
    stop ambient fadeout 1
    jump scene_0152
label scene_0152:

    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0152.mp3")

    play ambient "audio/Ambience/Breakroom_Ambience.mp3" fadein 1
    scene breakroom
    show nicole fye angry:
        leftcenterstage

    show kelly fye angry:
        rightcenterstage

    $ setWait(0.047,2.675)
    $ speak(NICOLE, "Okay I get a redo, that was a psycho customer!")
    $ setWait(2.675,8.055)
    $ speak(KELLY, "Sure he was a little off but you can't just insult the customers like that! You saw how I handled him.")
    $ setWait(8.055,12.018)
    $ speak(NICOLE, "Yeah but you didn't see the other weird shit about his breast milk fetish.")
    $ setWait(12.018,14.228)
    $ speak(KELLY, "Nicole, we're in the business of sales.")
    $ setWait(14.228,18.149)
    $ speak(KELLY, "If the customer says he has a breast milk fetish you tell that bitch to drink up.")
    show nicole fye sad
    $ setWait(18.149,19.567)
    $ speak(NICOLE, "That's insane.")
    show kelly fye
    $ setWait(19.567,21.152)
    $ speak(KELLY, "That's customer service.")
    $ setWait(21.152,29.035)
    $ speak(KELLY, "He won't remember what he bought, but he will remember telling the pretty girl working at FYE about breast milk and her being totally cool with it.")
    $ setWait(29.035,30.786)
    $ speak(NICOLE, "I don't get it, is this Hooters?")
    $ setWait(30.786,35.75)
    $ speak(KELLY, "Basically. But instead of wings we sell DVDs, and instead of a boobjob you get a lip ring.")
    show nicole fye angry
    $ setWait(35.75,40.922)
    $ speak(NICOLE, "Why the hell did I get a job? This is just as degrading as selling my body on MySpace.")
    $ setWait(40.922,41.714)
    $ speak(KELLY, "You can do that?")
    show nicole fye smile
    $ setWait(41.714,45.218)
    $ speak(NICOLE, "Hell yeah, Emily told me. It's on the internet so the cops don't track it.")
    show kelly fye sad
    $ setWait(45.218,49.263)
    $ speak(KELLY, "I've been having sex for free this whole time, you're telling me I could've got paid for it??")
    $ setWait(49.263,51.849)
    $ speak(NICOLE, "Yeah, you wanna try it with me? Fuck this place, let's quit.")
    show kelly fye

    $ setWait(51.849,53.184)
    $ speak(KELLY, "I'm the manager, remember?")
    show nicole fye
    $ setWait(53.184,54.977)
    $ speak(NICOLE, "So you get a lanyard, big deal.")
    $ setWait(54.977,59.649)
    $ speak(KELLY, "This lanyard means I make $9.25 an hour, plus discounts plus benefits.")
    $ setWait(59.649,64.57)
    $ speak(NICOLE, "Yeah you're kinda set for life here...\nHow long do we have to work before they give us the lip ring?")
    $ setWait(64.57,67.24)
    $ speak(KELLY, "We don't give you one, you just get it yourself.")
    $ setWait(67.24,69.325)
    $ speak(NICOLE, "Oh, well I quit then.")
    $ setWait(69.325,71.202)
    $ speak(KELLY, "Okay, it was nice working with you.")

    show nicole fye smile:
        leftcenterstage
        xzoom -1
        linear 2.5 off_left

    $ setWait(71.202,72.37)
    $ speak(NICOLE, "Yeah good luck.")
    stop ambient fadeout 1
    jump scene_0156
label scene_0153:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    $ setVoiceTrack("audio/Scenes/0153.mp3")
    play ambient "audio/Ambience/HardwareStore_Ambience.mp3" fadein 1
    scene hardwarestore
    show nicole sc4:
        off_left
        linear 4 leftcenterstage

    $ setWait(0.036,4.165)
    $ speak(NICOLE, "In a hardware store alone... Now I know how it feels to be racist.")
    show megan sc3 smile:
        off_right
        linear 2 rightcenterstage

    $ setWait(4.165,5.208)
    $ speak(MEGAN, "Oh hey, Nicole.")
    show nicole sc4 surprised
    $ setWait(5.208,7.794)
    $ speak(NICOLE, "Uhh... Oh wait, it's not awkward.")
    show megan sc3
    $ setWait(7.794,9.671)
    $ speak(MEGAN, "What's awkward?")
    show nicole sc4
    $ setWait(9.671,13.091)
    $ speak(NICOLE, "Usually when I see someone from school in public I try to avoid them...")
    show nicole sc4 smile

    $ setWait(13.091,15.76)
    $ speak(NICOLE, "But I just realized.. I'm not in school anymore!")
    $ setWait(15.76,16.97)
    $ speak(MEGAN, "Did you drop out?")
    $ setWait(16.97,18.346)
    $ speak(NICOLE, "No I'm getting expelled.")
    $ setWait(18.346,19.389)
    $ speak(MEGAN, "For what?")
    show nicole sc4
    $ setWait(19.389,20.89)
    $ speak(NICOLE, "Some bullshit, don't worry about it.")
    show megan sc3 smile
    $ setWait(20.89,24.227)
    $ speak(MEGAN, "Okay yeah, well at school stuff's been going good for me--")
    show megan sc3
    $ setWait(24.227,27.355)
    $ speak(NICOLE, "Do you know where the sponges are? I'm trying to start a car wash.")
    $ setWait(27.355,31.985)
    $ speak(MEGAN, "Near the chemical supplies, but I'm still class president, could you not interrupt me?")
    $ setWait(31.985,34.779)
    $ speak(NICOLE, "I'm not in class anymore, you're not my president.")
    show megan sc3 angry
    $ setWait(34.779,37.449)
    $ speak(MEGAN, "Well I'm still a person so you should respect me.")
    $ setWait(37.449,42.662)
    $ speak(NICOLE, "Dude I'm out of high school, you're just a memory now. There's zero consequences for anything I say to you.")
    $ setWait(42.662,43.163)
    $ speak(MEGAN, "Are you even--")
    show nicole sc4 smile
    $ setWait(43.163,44.164)
    $ speak(NICOLE, "You're a whore.")
    $ setWait(44.164,47.125)
    $ speak(MEGAN, "Excuse me? I have boyfriend and a purity ring!")
    $ setWait(47.125,48.752)
    $ speak(NICOLE, "For real? How do I get one?")
    $ setWait(48.752,49.753)
    $ speak(MEGAN, "Little late for you.")
    show nicole sc4
    $ setWait(49.753,53.381)
    $ speak(NICOLE, "No, it's never too late to have your boyfriend fuck every girl but you.")
    $ setWait(53.381,57.427)
    $ speak(MEGAN, "Ugh I don't need to take this! I'm on the honor roll, something you'll never do.")
    show nicole sc4 angry
    $ setWait(57.427,61.473)
    $ speak(NICOLE, "Bitch why don't you shut the fuck up before I slit your throat and watch the honor roll out?")
    $ setWait(61.473,62.724)
    $ speak(MEGAN, "Are you threatening me??")
    show nicole sc4
    $ setWait(62.724,64.893)
    $ speak(NICOLE, "No I'm hitting on you, flash me a titty, bitch.")
    show megan sc3 angry:
        rightcenterstage
        xzoom -1
        linear 1.3 off_right
    $ setWait(64.893,67.52)
    $ speak(MEGAN, "Cokehead slut!")
    show nicole sc4 smile:
        leftcenterstage
        linear 4.6 rightmidstage

    $ setWait(67.52,71.399)
    $ speak(NICOLE, "And there is no one she can report me to. Awesome.")
    stop ambient fadeout 1
    jump scene_0154
label scene_0154:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    $ setVoiceTrack("audio/Scenes/0154.mp3")
    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1

    scene parkinglot

    show nicole carwash smile:
        centerstage
        xzoom -1

    show car_corolla:
        parallel:
            xcenter -3
            pause 1
            linear 4.2 xcenter 0.51
        parallel:
            alpha 0.0
            pause 2 alpha 1.0

    $ setWait(0.006,4.927)
    $ speak(NICOLE, "Hand washed for only 8 bucks, great deal!")


    $ setWait(4.927,5.928)
    $ speak(COROLLA, "Hey what's up?")

    show nicole carwash smile behind car_corolla:
        xzoom 1

    $ setWait(5.928,8.139)
    $ speak(NICOLE, "Uh nothing much, you interested?")
    $ setWait(8.139,9.265)
    $ speak(COROLLA, "What are you selling?")
    $ setWait(9.265,10.975)
    $ speak(NICOLE, "Car washes, 8 bucks.")
    $ setWait(10.975,12.852)
    $ speak(COROLLA, "With one of those peanut sponges?")
    $ setWait(12.852,16.856)
    $ speak(NICOLE, "Yeah the big yellow one, hand washed. Get a car wash to support the homeless.")
    show nicole carwash surprised behind car_corolla

    show car_corolla:
        xcenter 0.51
        pause 1.82
        linear 0.65 xcenter 0.54
        linear 0.8 xcenter 3.6

    $ setWait(16.856,20.777)
    $ speak(COROLLA, "With that sponge? Fuck the homeless.")
    show nicole carwash angry
    $ setWait(20.777,23.321)
    $ speak(NICOLE, "You drive a Corolla, what're you worried about?")
    show nicole carwash behind car_mustang

    show car_mustang:
        xcenter -3.3
        linear 4.2 xcenter 0.53

    $ setWait(23.321,27.2)
    $ speak(NICOLE, "...Maybe I should flirt more.")
    $ setWait(27.2,28.618)
    $ speak(MUSTANG, "You washing cars?")
    show nicole carwash angry behind car_mustang

    $ setWait(28.618,30.161)
    $ speak(NICOLE, "What does it look-- I mean...")

    show nicole carwash flirt behind car_mustang

    $ setWait(30.161,35.291)
    $ speak(NICOLE, "Yeah, and I'd really like to wash a car like yours. I bet it's fast.")
    $ setWait(35.291,38.294)
    $ speak(MUSTANG, "Yeah 300 horsepower, not to brag.")
    $ setWait(38.294,41.714)
    $ speak(NICOLE, "Of course not, it is what it is, right?")
    $ setWait(41.714,45.301)
    $ speak(MUSTANG, "Yeah it's the GT so leather seats and everything.")
    $ setWait(45.301,50.681)
    $ speak(NICOLE, "Leather is so sexy, you wanna take me for a ride after I get this cleaned?")
    $ setWait(50.681,51.682)
    $ speak(MUSTANG, "A ride where?")
    $ setWait(51.682,54.185)
    $ speak(NICOLE, "I don't know, your place maybe?")
    show car_mustang:
        xcenter 0.53
        pause 1.55
        linear 0.5 xcenter 0.57
        linear 0.68 xcenter 3.76
    $ setWait(54.185,58.231)
    $ speak(MUSTANG, "I don't think my husband would like that.")
    show nicole carwash angry
    $ setWait(58.231,61.526)
    $ speak(NICOLE, "Since when the fuck do gay people drive Mustangs??")
    show nicole carwash sad:
        centerstage
        xzoom -1
        linear 4 off_left

    $ setWait(61.526,63.403)
    $ speak(NICOLE, "I gotta find a new spot.")
    stop ambient fadeout 1

    jump scene_0155
label scene_0155:

    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0
    play ambient "audio/Ambience/School_Ext_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show school front with Pause(2.249):
        zoom 1.0 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.249 zoom 1.1 truecenter

    $ setVoiceTrack("audio/Scenes/0155.mp3")
    scene school ext 2
    show nicole carwash behind car_camry:
        centerstage
        xzoom -1

    show car_camry:
        xcenter -3.3
        pause 2
        linear 0.8 xcenter 3.5

    $ setWait(2.249,4.626)
    $ speak(NICOLE, "Teachers are charitable, right?")
    show nicole carwash surprised behind car_camry:
        xzoom 1

    $ setWait(4.626,9.881)
    $ speak(NICOLE, "Damn he went 60 in a 10!")
    show nicole carwash

    show coach 1 smile:
        off_right
        linear 2.6 rightmidstage

    $ setWait(9.881,12.801)
    $ speak(COACH, "Oh hey sweetie, what you doing here on a Saturday?")
    $ setWait(12.801,14.052)
    $ speak(NICOLE, "I'm doing a car wash.")
    show coach 1

    $ setWait(14.052,17.681)
    $ speak(COACH, "Are you sure you're allowed to do that at school without staff supervision?")
    $ setWait(17.681,21.018)
    $ speak(NICOLE, "I'm a student here, it's whatever. Are you sure you're allowed to go that fast?")
    show coach 1 smile
    $ setWait(21.018,25.355)
    $ speak(COACH, "Ah there's no kids around today, and even if I hit one it's just a write-off.")

    show nicole carwash angry

    $ setWait(25.355,26.732)
    $ speak(NICOLE, "How is that a write-off?")
    $ setWait(26.732,28.775)
    $ speak(COACH, "Cause you write 'em off the student list.")
    show nicole carwash
    $ setWait(28.775,30.277)
    $ speak(NICOLE, "Wow- So you want a car wash?")
    $ setWait(30.277,33.405)
    $ speak(COACH, "I might have some time, how much?")
    $ setWait(33.405,34.322)
    $ speak(NICOLE, "8 bucks.")
    $ setWait(34.322,36.366)
    $ speak(COACH, "Get that shirt wet and I'll give ya 10.")
    show nicole carwash angry
    $ setWait(36.366,37.993)
    $ speak(NICOLE, "I'm in high school, Mr. Colby.")
    show coach 1

    $ setWait(37.993,40.037)
    $ speak(COACH, "You're right, you're right, 15 then.")
    show nicole carwash
    $ setWait(40.037,40.954)
    $ speak(NICOLE, "Not what I meant.")
    show megan sc4:
        xzoom -1
        off_left
        linear 2 leftmidstage

    $ setWait(40.954,42.08)
    $ speak(MEGAN, "15 what?")
    show nicole carwash:
        xzoom 1

    $ setWait(42.08,43.498)
    $ speak(NICOLE, "Years in prison at this rate.")
    show megan sc4 angry
    $ setWait(43.498,45.042)
    $ speak(MEGAN, "Nicole what do you think you're doing here?")
    $ setWait(45.042,47.044)
    $ speak(COACH, "She's a student, she can be here.")
    show nicole carwash:
        xzoom 1
    $ setWait(47.044,48.045)
    $ speak(NICOLE, "Yeah I know, right?")
    $ setWait(48.045,49.963)
    $ speak(MEGAN, "She got expelled, Mr. Colby!")
    show coach 1 worried
    $ setWait(49.963,51.506)
    $ speak(COACH, "What?? Is this true?")
    show nicole carwash angry

    $ setWait(51.506,56.261)
    $ speak(NICOLE, "I didn't get expelled, I'm suspended indefinitely while they consider expulsion.")
    $ setWait(56.261,58.346)
    $ speak(COACH, "Honey you can't be here, you gotta go!")
    $ setWait(58.346,60.015)
    $ speak(NICOLE, "Why- Or else what?")
    $ setWait(60.015,62.851)
    $ speak(COACH, "Or I gotta report ya for an unsanctioned car wash.")
    $ setWait(62.851,67.147)
    $ speak(NICOLE, "Well.. I'll report you for trying to buy a wet T-shirt car wash!")
    $ setWait(67.147,69.775)
    $ speak(COACH, "Uh-- Well maybe we could just forget about all this.")
    show megan sc4 laugh
    $ setWait(69.775,71.693)
    $ speak(MEGAN, "All what? I didn't see anything.")
    show nicole carwash angry:
        xzoom -1
    $ setWait(71.693,73.945)
    $ speak(NICOLE, "You were literally walking up as he said it.")
    $ setWait(73.945,80.035)
    $ speak(MEGAN, "No actually as I recall you were offering him a topless car wash, right Mr. Colby?")
    show coach 1 smile
    $ setWait(80.035,82.079)
    $ speak(COACH, "Oh uh um- yeah!")
    show nicole carwash sad:
        xzoom 1
    $ setWait(82.079,83.914)
    $ speak(NICOLE, "Are you actually fucking kidding me??")
    show megan sc4 laugh:
        leftmidstage
        xzoom -1
    $ setWait(83.914,85.874)
    $ speak(MEGAN, "Who's the whore now, Nicole?")
    show nicole carwash angry:
        centerstage
        linear 3 off_right

    $ setWait(85.874,87.793)
    $ speak(NICOLE, "You Jesus bitches are fucked up.")
    stop ambient fadeout 1
    jump scene_0156
label scene_0156:

    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1

    $ setVoiceTrack("audio/Scenes/0156.mp3")
    scene coffeeext
    show nicole sc4 angry:
        leftcenterstage

    $ setWait(0.086,4.09)
    $ speak(NICOLE, "God MySpace sucks on the phone. How do I make a new account...")
    show emily sc4 smile:
        xzoom -1
        off_left
        linear 1.6 leftmidstage
    $ setWait(4.09,5.466)
    $ speak(EMILY, "Oh shit what's up?")
    show nicole sc4:
        xzoom -1
    $ setWait(5.466,9.136)
    $ speak(NICOLE, "Hey what's good? I didn't know you drank coffee, do you need to be somewhere?")
    show emily sc4

    $ setWait(9.136,12.056)
    $ speak(EMILY, "I don't need to be anywhere, it just tastes good. Are you still homeless?")
    $ setWait(12.056,15.059)
    $ speak(NICOLE, "Basically. I'm trying to use the Starbucks wifi right now.")
    $ setWait(15.059,16.435)
    $ speak(EMILY, "Did you try what I told you about?")
    $ setWait(16.435,20.064)
    $ speak(NICOLE, "No I'm making the account for it now though. What should my name be?")
    $ setWait(20.064,22.733)
    $ speak(EMILY, "I mean, something that just lets people know you're down honestly.")
    $ setWait(22.733,26.821)
    $ speak(NICOLE, "Gotcha... How about DirtyLittleRental?")
    show emily sc4 upset
    $ setWait(26.821,28.03)
    $ speak(EMILY, "Little slutty.")
    $ setWait(28.03,31.784)
    $ speak(NICOLE, "Alright what about... PiercedPrincess?")
    show emily sc4 smile
    $ setWait(31.784,35.955)
    $ speak(EMILY, "Hmmm I like the innuendo, super cute, but really emo.")
    show nicole sc4 angry
    $ setWait(35.955,38.165)
    $ speak(NICOLE, "I got shit to be emo about, don't I?")
    show emily sc4
    $ setWait(38.165,42.086)
    $ speak(EMILY, "Yeah true. But that's probably already taken, so put X's in the name.")
    show nicole sc4

    $ setWait(42.086,47.883)
    $ speak(NICOLE, "Okay xXPiercedPrincessXx, it's available.")

    show emily sc4 smile

    $ setWait(47.883,53.556)
    $ speak(EMILY, "There ya go. Damn you went from like.. hesitant to making awesome screen names. What happened over the week?")
    $ setWait(53.556,56.684)
    $ speak(NICOLE, "Like I just came to grips with the fact that...")
    show emily sc4
    $ setWait(56.684,61.355)
    $ speak(NICOLE, "...when you're pretty, retail and escorting make you feel equally disgusting.")

    $ setWait(61.355,64.233)
    $ speak(EMILY, "Yeah either way you deal with hideous people against your will.")
    $ setWait(64.233,67.111)
    $ speak(NICOLE, "So who do I add? How do I even know they're around here?")
    $ setWait(67.111,72.074)
    $ speak(EMILY, "There's one guy who's pretty much connected with everybody in the area. You add one then the others start hitting you up.")
    $ setWait(72.074,73.284)
    $ speak(NICOLE, "What's his name?")
    $ setWait(73.284,77.163)
    $ speak(EMILY, "Uh.. CreampieCasanova420?")
    $ setWait(77.163,79.29)
    $ speak(NICOLE, "Yeah I see him here, added.")
    show emily sc4 smile
    $ setWait(79.29,82.209)
    $ speak(EMILY, "So when he accepts just PM him and he'll shout you out.")
    show nicole sc4 sad
    $ setWait(82.209,85.046)
    $ speak(NICOLE, "Cool, but how does it work? I don't have a car.")
    show emily sc4
    $ setWait(85.046,90.76)
    $ speak(EMILY, "When you're selling favors they usually come to you. And if you let 'em pay you in drugs you get way more for your time.")
    $ setWait(90.76,92.136)
    $ speak(NICOLE, "Have you done this before?")
    $ setWait(92.136,95.848)
    $ speak(EMILY, "I'm on there but I never sold favors, my friends in Laurel have though.")
    show nicole sc4
    $ setWait(95.848,100.561)
    $ speak(NICOLE, "Damn there's some white trash in Laurel too. Would they get paid in drugs?")
    $ setWait(100.561,102.897)
    $ speak(EMILY, "Yeah but only cause they had people to sell to.")
    show emily sc4:
        xzoom -1
        leftmidstage
        linear 5 off_right

    $ setWait(102.897,106.108)
    $ speak(EMILY, "Anyway I gotta go, good luck with the wifi.")
    show nicole sc4 sad:
        xzoom 1

    $ setWait(106.108,108.486)
    $ speak(NICOLE, "God this is sketchy.")
    show nicole sc4:
        xzoom 1
        leftcenterstage
        linear 4.6 off_right

    $ setWait(108.486,111.614)
    $ speak(NICOLE, "I guess if one of them kills me it'll make my Mom mad.")
    stop ambient fadeout 1

    jump scene_0157
label scene_0157:
    show black onlayer screens with Pause(1):
        alpha 0.0
        linear 1 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 0.7 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show title_oneweeklater onlayer screens
    show diner ext with Pause(2.879):
        zoom 0.6 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.879 zoom 0.7 truecenter
    $ setVoiceTrack("audio/Scenes/0157.mp3")

    play ambient "audio/Ambience/Diner_Ambience.mp3"
    scene diner int
    hide title_oneweeklater onlayer screens

    show nicole sc4:
        leftcenterstage

    show jecka sc5 sad:
        rightcenterstage

    $ setWait(2.879,7.676)
    $ speak(JECKA, "Y'know for two weeks of being homeless you don't really look that homeless.")
    show nicole sc4 angry

    $ setWait(7.676,10.47)
    $ speak(NICOLE, "What do you think everybody homeless wears a barrel with suspenders?")
    show jecka sc5
    $ setWait(10.47,18.353)
    $ speak(JECKA, "No but you're still so like clean and put together. The homeless dudes on the bus are covered in dried spit and Burlington Coat Factory.")
    show nicole sc4

    $ setWait(18.353,21.857)
    $ speak(NICOLE, "A lot of the guys let me crash, use their shower, everything.")
    show jecka sc5 sad
    $ setWait(21.857,23.859)
    $ speak(JECKA, "Guys that you're meeting on...")
    $ setWait(23.859,26.528)
    $ speak(NICOLE, "On MySpace, yeah.")
    show jecka sc5
    $ setWait(26.528,31.783)
    $ speak(JECKA, "I never thought I'd ask this not as an insult but; how's being a whore going?")
    show nicole sc4 angry
    $ setWait(31.783,32.701)
    $ speak(NICOLE, "Escort?")
    show jecka sc5 sad

    $ setWait(32.701,36.872)
    $ speak(JECKA, "Or that. Whatever means money for sex.")
    show nicole sc4

    $ setWait(36.872,40.709)
    $ speak(NICOLE, "On MySpace we don't call it sex, we call it favors.")
    $ setWait(40.709,44.963)
    $ speak(JECKA, "So what are the guys like? Are they really weird?")
    $ setWait(44.963,50.385)
    $ speak(NICOLE, "Well they're buying favors so obviously but the actual doing it isn't even the worst part. It's after.")
    $ setWait(50.385,51.762)
    $ speak(JECKA, "What is it awkward?")
    $ setWait(51.762,60.896)
    $ speak(NICOLE, "Uh so after they finish, depending on the guy, you get this wide range of emotions from wanting to save you to wanting to kill you.")
    $ setWait(60.896,62.105)
    $ speak(JECKA, "What's in the middle?")
    show nicole sc4 angry
    $ setWait(62.105,64.274)
    $ speak(NICOLE, "Wanting you to get out before their wife comes home.")
    show jecka sc5 surprised

    $ setWait(64.274,67.027)
    $ speak(JECKA, "They're married? What if they get you pregnant, Nicole??")
    show nicole sc4

    $ setWait(67.027,72.407)
    $ speak(NICOLE, "There's upper favors and lower favors, I don't do lower favors. Those are for ugly girls.")
    show jecka sc5 sad
    $ setWait(72.407,76.036)
    $ speak(JECKA, "Shit.. what do they pay if you're not giving it all up?")
    $ setWait(76.036,81.875)
    $ speak(NICOLE, "There's not really a number cause I usually trade for drugs, guys into this are like pharmacies.")
    $ setWait(81.875,84.795)
    $ speak(JECKA, "That better be some awesome shit if you're not getting paid.")
    $ setWait(84.795,88.632)
    $ speak(NICOLE, "Oh it is. I probably did a thousand dollars in free pills this week.")
    show jecka sc5 angry
    $ setWait(88.632,91.343)
    $ speak(JECKA, "They're not free if you're doing favors for 'em.")
    $ setWait(91.343,92.594)
    $ speak(NICOLE, "Let's not get that deep.")
    show jecka sc5 sad
    $ setWait(92.594,94.596)
    $ speak(JECKA, "But you're only doing this cause you're homeless.")
    show nicole sc4 surprised

    $ setWait(94.596,95.639)
    $ speak(NICOLE, "For real?")
    show nicole sc4

    $ setWait(95.639,102.854)
    $ speak(JECKA, "What I'm saying is, being a regular ho for actual cash would be better than were you are right now.\nThen you could get your own place maybe.")
    show nicole sc4 angry

    $ setWait(102.854,108.36)
    $ speak(NICOLE, "No shit. I ask for drugs because I can't do this sober.")
    $ setWait(108.36,116.076)
    $ speak(NICOLE, "I can't beg sober, I can't starve sober, and I definitely can't fuck a stranger sober.")
    $ setWait(116.076,119.371)
    $ speak(JECKA, "Yeah but why not go to a womens shelter or something?")
    $ setWait(119.371,124.876)
    $ speak(NICOLE, "You can't have drugs in a womens shelter which is the last place you wanna be sober in.")
    $ setWait(124.876,130.59)
    $ speak(JECKA, "I guess it's just a month ago I couldn't imagine you doing this, I could never do this. It's so gross.")
    $ setWait(130.59,143.478)
    $ speak(NICOLE, "Well a month ago I wasn't homeless, but when your Mom kicks you out and your friend won't let you stay with her, that kinda forces you to do shit you wouldn't normally do.")
    $ setWait(143.478,145.272)
    $ speak(JECKA, "Are you trying to guilt me right now?")
    show nicole sc4
    $ setWait(145.272,147.44)
    $ speak(NICOLE, "I don't need to try.")
    show jecka sc5 angry

    $ setWait(147.44,149.901)
    $ speak(JECKA, "I gave you fruit roll-ups, what do you want from me?")
    stop ambient fadeout 2.1
    jump scene_0158
label scene_0158:
    show black onlayer screens with Pause(2.5):
        alpha 0.0
        linear 1.5 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.0

    play ambient "audio/Ambience/Exterior_Ambience.mp3" fadein 1
    scene onlayer master
    show black
    show library ext with Pause(2.2172):
        zoom 0.96 truecenter
        alpha 0.0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 2.127 zoom 1 truecenter

    $ setVoiceTrack("audio/Scenes/0158.mp3")
    play ambient "audio/Ambience/Library_Ambience.mp3"
    scene library

    show nicole sc4:
        leftstage
        xzoom -1

    $ setWait(2.172,6.092)
    $ speak(NICOLE, "This is so much easier than phone MySpace... Let's see.")
    show crt_myspace onlayer screens
    $ setWait(6.092,9.638)
    $ speak(NICOLE, "\"I can only pay in cash if that's okay\"")
    show nicole sc4 sad
    hide crt_myspace onlayer screens
    $ setWait(9.638,12.724)
    $ speak(NICOLE, "Shit, I guess I have enough on me to get me through it.")
    show crt_myspace onlayer screens
    $ setWait(12.724,21.775)
    $ speak(NICOLE, "\"Also please keep this to yourself, I have a high profile career and don't want this getting around.\"")
    show nicole sc4 surprised
    hide crt_myspace onlayer screens
    $ setWait(21.775,28.406)
    $ speak(NICOLE, "High profile means rich, and rich means blackmail money.")
    show nicole sc4 angry
    $ setWait(28.406,31.618)
    $ speak(NICOLE, "But I can't hold up a camera phone in his face for the proof...")
    show karen sc3:
        off_right
        linear 4 leftcenterstage

    $ setWait(31.618,35.33)
    $ speak(KAREN, "Nicole you're not allowed to use MySpace on the library computers.")
    show nicole sc4:
        xzoom 1
    $ setWait(35.33,38.959)
    $ speak(NICOLE, "Karen, right? Do you know how to set up a timed photo on the Sidekick?")
    show karen sc3 angry

    $ setWait(38.959,44.172)
    $ speak(KAREN, "The phone-- Don't change the subject. I'm the librarian assistant you're gonna get me in trouble.")
    show nicole sc4 angry
    $ setWait(44.172,45.841)
    $ speak(NICOLE, "Why can't we use MySpace??")
    show karen sc3
    $ setWait(45.841,47.676)
    $ speak(KAREN, "It's not an educational website.")
    $ setWait(47.676,51.68)
    $ speak(NICOLE, "I learned how to break into a car on MySpace, how is that not educational?")
    show karen sc3 sad
    $ setWait(51.68,54.307)
    $ speak(KAREN, "Rules are rules, Nicole, you need to log off now.")
    show nicole sc4 sad
    $ setWait(54.307,58.353)
    $ speak(NICOLE, "Log off? I gotta reply to this. Dude can you just act like a hot bitch for once?")
    $ setWait(58.353,60.105)
    $ speak(KAREN, "But I'm not a hot bitch.")
    show nicole sc4
    $ setWait(60.105,64.526)
    $ speak(NICOLE, "No uh.. your um, your glasses are cute.")
    $ setWait(64.526,66.027)
    $ speak(KAREN, "Just cute though...")
    show nicole sc4 smile
    $ setWait(66.027,69.406)
    $ speak(NICOLE, "Did I say cute? -I meant hot. Like sex for free hot.")
    $ setWait(69.406,73.618)
    $ speak(KAREN, "I don't know, I feel kinda nerdy wearing them but contacts hurt my eyes.")
    show nicole sc4 sad
    $ setWait(73.618,76.913)
    $ speak(NICOLE, "Nerdy? No they're like really distinctive in a hot way.")
    show nicole sc4 smile
    $ setWait(76.913,80.208)
    $ speak(NICOLE, "You could like be in Playboy with a quadratic formula tramp stamp.")
    $ setWait(80.208,83.169)
    $ speak(KAREN, "Tramp stamp? Like the back tattoo?")
    $ setWait(83.169,85.797)
    $ speak(NICOLE, "Yeah, dudes could study it while hittin' you doggy and shit.")
    show karen sc3
    $ setWait(85.797,87.09)
    $ speak(KAREN, "I'm allergic to dogs.")
    show nicole sc4 angry

    $ setWait(87.09,91.553)
    $ speak(NICOLE, "Christ whatever-- Karen do you see what I'm saying? You're a hot bitch, act like one.")
    show karen sc3 sad
    $ setWait(91.553,95.015)
    $ speak(KAREN, "What are hot bitches supposed to act like?")
    $ setWait(95.015,101.813)
    $ speak(NICOLE, "Hot bitches aren't worried about losing their depressing unpaid internship at the local library.")
    show karen sc3
    $ setWait(101.813,106.484)
    $ speak(KAREN, "Well I guess you could use the computer for five more minutes but then you really gotta log off.")
    show nicole sc4
    $ setWait(106.484,109.321)
    $ speak(NICOLE, "Close enough, so how do I do a timed photo?")
    $ setWait(109.321,116.62)
    $ speak(KAREN, "Uh okay so you go to the camera section, do new capture, then go over to flash and exposure settings...")
    stop ambient fadeout 2
    jump scene_0159
label scene_0159:
    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1 alpha 0.1

    play ambient "audio/Ambience/Hood_Ambience.mp3" fadein 1

    $ setVoiceTrack("audio/Scenes/0159.mp3")
    scene darkalley

    $ setWait(0.083,1.584)
    $ speak(NICOLE, "...")
    show nicole sc4:
        xzoom -1
        off_left
        linear 1 leftstage
    $ setWait(1.584,4.671)
    $ speak(NICOLE, "Okay that camera angle should be good.")
    show nicole sc4:
        xzoom 1
        leftstage
        linear 1.3 leftmidstage

    $ setWait(4.671,7.757)
    $ speak(NICOLE, "Where is this guy? And I wonder how rich he's gonna be.")
    $ setWait(7.757,11.26)
    $ speak(NICOLE, "He could be like a basketball player, or Steve Jobs...")
    $ setWait(11.26,14.472)
    $ speak(NICOLE, "...or the guy who invented adderall.")
    show nicole sc4 surprised:
        leftmidstage

    $ setWait(14.472,25.274)
    $ speak(NICOLE, "Oh I think that's him, it's so dark he probably can't even recognize me.")
    show nicole sc4 flirt

    $ setWait(25.274,28.111)
    $ speak(NICOLE, "Heyy you weren't looking for favors, were you?")
    show lorre 2:
        off_right
        linear 1.5 rightmidstage

    show flash:
        xzoom -1
        yzoom 1.3
        alpha 0.0
        pause 2.6
        linear 0.06 alpha 1.0
        pause 0.06
        linear 0.12 alpha 0.0

    show black onlayer screens:
        alpha 0.1
        pause 2.63
        linear 0.05 alpha 0.0

    $ setWait(28.111,31.072)
    $ speak(LORRE, "Guilty as charged, PiercedPrincess.")
    show nicole sc4 surprised
    $ setWait(31.072,33.866)
    $ speak(NICOLE, "What the fuck- you're not rich, you're Mr. Lorre!")
    show lorre 2 surprised:
        rightmidstage
        linear 0.08 xalign 0.89
        linear 0.08 xalign 0.87
        linear 0.08 xalign 0.89
        linear 0.1 rightmidstage

    $ setWait(33.866,34.701)
    $ speak(LORRE, "Oh god!")
    $ setWait(34.701,37.37)
    $ speak(NICOLE, "You work at a school and you're on that part of MySpace??")
    show lorre 2 freakout:
        rightmidstage

    $ setWait(37.37,39.58)
    $ speak(LORRE, "Ugh Nicole please don't- oh no!")
    show nicole sc4 angry
    $ setWait(39.58,43.126)
    $ speak(NICOLE, "That's why your wife left you, you kept payin' for ass on the internet!")
    show nicole sc4 angry:
        xzoom -1
    $ setWait(43.126,44.21)
    $ speak(NICOLE, "Emily come out here!")
    show emily sc5 upset:
        xzoom -1
        off_left
        linear 1 leftstage

    $ setWait(44.21,46.671)
    $ speak(EMILY, "Damn, I was hoping you were the guy from Transformers!")
    $ setWait(46.671,47.839)
    $ speak(LORRE, "What was this??")
    show nicole sc4 angry:
        xzoom 1

    show emily sc5 angry

    $ setWait(47.839,51.3)
    $ speak(EMILY, "We thought you were gonna be a celebrity so Nicole had me hide with her camera phone.")
    $ setWait(51.3,54.429)
    $ speak(LORRE, "Oh two witnesses-- why not just use the self-timer!")
    show nicole sc4
    $ setWait(54.429,55.388)
    $ speak(NICOLE, "I couldn't figure it out.")
    $ setWait(55.388,56.681)
    $ speak(EMILY, "How long have you been doing this?")
    $ setWait(56.681,59.475)
    $ speak(LORRE, "Girls, please, I'm just very anxious!")
    show nicole sc4 surprised

    $ setWait(59.475,63.02)
    $ speak(NICOLE, "I popped three xans and I'm still freaking out, how do you think I feel??")
    show lorre 2 freakout:
        rightmidstage
        linear 2.2 centerstage

    $ setWait(63.02,66.649)
    $ speak(LORRE, "Now uh come on, let's work something out here.")
    $ setWait(66.649,67.442)
    $ speak(EMILY, "Like what?")
    show nicole sc4 angry

    $ setWait(67.442,70.695)
    $ speak(NICOLE, "No fuck that, this dude got me expelled, he ruined my life!")
    $ setWait(70.695,74.824)
    $ speak(LORRE, "I'm sorry Nicole just please don't tell anyone about this!")
    $ setWait(74.824,76.159)
    $ speak(NICOLE, "You better pay up then!")
    $ setWait(76.159,78.119)
    $ speak(EMILY, "Starting at a thousand each.")
    $ setWait(78.119,82.206)
    $ speak(LORRE, "But ugh.. on a teacher's salary, and my house payment...")
    $ setWait(82.206,84.876)
    $ speak(NICOLE, "Your house was foreclosed, what do you gotta worry about?")
    show emily sc5 upset
    $ setWait(84.876,85.96)
    $ speak(EMILY, "Bitch take a loan out.")
    $ setWait(85.96,87.837)
    $ speak(NICOLE, "Yeah ask your wife for that UPS money.")
    show lorre 2 freakout:
        centerstage
        linear 3.3 xalign 0.84
    $ setWait(87.837,91.132)
    $ speak(LORRE, "Alright fine! Fine!")
    $ setWait(91.132,96.345)
    $ speak(LORRE, "I'll go to the ATM if you promise to just not tell anyone.")
    show emily sc5 smile
    $ setWait(96.345,97.263)
    $ speak(EMILY, "Oh for sure.")
    show nicole sc4
    $ setWait(97.263,101.017)
    $ speak(NICOLE, "Yeah trust me, we won't tell a soul.")
    stop ambient fadeout 2.3
    jump end_0160

label end_0160:

    show black onlayer screens with Pause(2):
        alpha 0.0
        linear 1.4 alpha 1.0

    show black onlayer screens:
        alpha 1.0
        linear 1.5 alpha 0.0

    if "end_0160" not in persistent.endings:
        $ persistent.endings.append("end_0160")
        $ persistent.new_ending = True

    $ quick_menu = False

    $ csbox = True

    $ renpy.movie_cutscene("cs0160.webm")

    return

label scene_0999:

    scene onlayer master
    show black
    $ quick_menu = False
    $ csbox = True

    $ renpy.movie_cutscene("cs0999.webm")

    return
