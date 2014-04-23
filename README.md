pydrone
=======

Python port of scriptcraft's JS drone class

This uses the API provided by [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice) to replicate some of the functionality that is provided by
[ScriptCraft](http://scriptcraftjs.org/)

Thanks to @panicnot for the example.py code and the introduction to RaspberryJuice and ScriptCraft.

Usage
-----

Install the RaspberryJuice plugin into your minecraft server, download it from <http://zhuowei.github.com/RaspberryJuice/raspberryjuice-1.2.jar>

Start the server then join it as normal.

Set your python include path to where the RaspberryJuice is installed.

    export PYTHONPATH=$PYTHONPATH:/Users/someuser/Downloads/mcpi/api/python

Once you have a minecraft server running just execute the example script:

    python src/example.py

You should see the output in the minecraft world.

API
---

Currently implemented methods:

*    fwd
*    back
*    left
*    right
*    chkpt
