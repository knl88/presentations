import os

import sys
import emoji


is_emoji_crazy = os.getenv("NIVA_ENV", 'False').lower() in ('true', '1', 't', 'True')
favourite_emoji_path = os.getenv("FAVOURITE_PATH", '')

if os.path.isfile(favourite_emoji_path):

    with open(favourite_emoji_path, "r") as f:
        for l in f.readlines():
            print(l)
            print(emoji.emojize(l))

elif is_emoji_crazy:

    for v in emoji.EMOJI_DATA.values():
        print(f"{emoji.emojize(v['en'])} {v['en']}")

else:

    for arg in sys.argv[1:]:
        if arg=="docker":
            print("Hello Docker") 
            print(emoji.emojize(":grinning_face_with_big_eyes:"))
            print(emoji.emojize(":whale:"))
        elif emoji.is_emoji(emoji.emojize(arg)):
            print(emoji.emojize(arg))
        else:
            print("Options are:")
            for v in emoji.EMOJI_DATA.values():
                print(v['en'])
            print(f"Try the above {emoji.emojize(':backhand_index_pointing_up:')}")