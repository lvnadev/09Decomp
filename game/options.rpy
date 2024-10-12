














define config.name = _("Class of '09 | The Re-Up")




define gui.show_name = True




define config.version = "1.0"





define gui.about = _p("""
""")






define build.name = "C09RU"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False



























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None



















define config.window = "auto"

define config.log = "gamelog.txt"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0
default preferences.skip_unseen = True




default preferences.afm_after_click = True
default preferences.afm_enable = True
default preferences.afm_time = 0
















define config.save_directory = "TheReUp-1594772489"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)






    config.keymap['pause_game'] = [ ]




    build.documentation('*.html')
    build.documentation('*.txt')






define build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArCFy6vl7fEbCFbvHEmf58OLg9Gtzpc4z5l2lZ1/vnE9WQ0LqZnLFyAex72TVReyEuZbYxjBOj+Na0a9gQ3NEFqHk5uGAAF1Iuhiq3wYRAI2qQLQiw7SH4jKxUtxU8vAERC8glRS3hgxtvpyafrJAKpu/EbocezXUaULhiYb1dtI/0kRuS6+4MFI6cGp8aI3iq93opJO3CKkGUcFvBCoW68qMBusbNVp6Uf4/Eq3L2+PY3UrKeB8L2ix8y44TvpRpjIfPHxcbuOg9uWq6wleJOzntnNDkIi7fOaBqcfZDAEWJUFmaHq8SJJbQS/M3dOfjIolzHK0UP0KXHDpCFytliwIDAQAB"
