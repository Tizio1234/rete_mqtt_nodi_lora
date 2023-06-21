from serial import Serial
from os import environ

raspberry = Serial(environ.get("raspberry"), 115200)