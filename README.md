# discord-richpresence-example
An example how you can have your own Rich presence with python with pypresence.

First, you must have pypresence installed. (with `pip3 install pypresence` / `python3 -m pip install -U pypresence`.
If you have problems with pypresence, you can find the docs of pypresence here: https://qwertyquerty.github.io/pypresence/html/index.html
or the GitHub page: https://github.com/qwertyquerty/pypresence

## Make an Application and get the data for the RP:

To make an Application for your RP, you must visit https://discord.com/developers/applications.
Then, you go to the button "New Application" right in the corner. If you done this, you have your Application!
There you can find the topic "Rich Presence" and there "Visualizer". There you can see some data you can use.
When you need the large_image and the small_image, you must go to "Art Assets", and there you can Upload Images.
Alle Uploaded Images there have a name. This name you can use in the program.
So, if you name the uploaded Image "wumpus", you can write large_image="wumpus" or small_image="wumpus".
You can also use the picture of your application. This picture has the same name like the application but in lowercase! (Application name: "App", then the Image name is "app".)
