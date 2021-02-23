# If you dont know how to do this, you can read the comments in here or the description in github.
# If you need help in pypresence, you can visit the docs: https://qwertyquerty.github.io/pypresence/html/index.html
# This is only an example for a presence with pypresence. I am not the developer of pypresence!
# Pypresence on GitHub: https://github.com/qwertyquerty/pypresence
# Before you can use this, you must install pypresence (pip install pypresence / python -m pip install -U pypresence)

from pypresence import Presence
import time

rpc = Presence(739245643377148026)  # The ID of your Application you use
rpc.connect()  # Here the RP connects.

# Here the RP gets updated. You can delete things, you don't want to have in your RP.
while True:
    try:
        rpc.update(
            # You can customize all settings here.
            # Also, you can remove some of them.
            large_image="cool_image",  # The Image-Key you get, when you upload an Image on the developer page
            large_text="Hello world! A cool Image!",  # This will be displayed, if you hover over the large image.
            small_image="cool_small_image",  # Here you can put an Image-Key too.
            small_text="Small but cool image!",  # This will be displayed, if you hover over the small image.
            start=1507665886,  # Here you can put in a start-timestamp of your game.
            end=1507665886,  # Here you can put in an end-timestamp of your game.
            state="Playing Solo",  # This will be shown under the details. If you have a party,
            # this will look like this: Playing Solo (1 of 5)
            details="Hello World!",  # This are some details of your game.
            # join="abcdefghijklmnop", # You can create invite on discord with this to join your game. (DONT WORK WITH BUTTONS!)
            # party_id="abcdefghijklmnop", # ID of the party if you are in a party in the game.
            # party_size= [1, 5], # (Users, Max users) The users in the party and the max users
            # --------------------------------------------------------------------------------
            # Here are the buttons you can use.
            # If you want, you can let the two buttons there or you can remove one or both.
            # Warning: You can use max. two buttons in the RP!
            # --------------------------------------------------------------------------------
            buttons=[
                {
                    "label": "Button 1",
                    "url": "https://example.com"
                },
                {
                    "label": "Button 2!",
                    "url": "https://example.com"
                }
            ]
        )

        print('The RP is displayed!')

    except Exception as e:
        print(f"The RP cannot be displayed! Error: {e}")

    # You can change your RP after some time.
    # --> WARNING: DONT REMOVE THE time.sleep()!
    time.sleep(15)
