#!/usr/bin/env pythonc

# Device-dependent imports:
from PIL import Image, ImageDraw, ImageFont
import os
import re
import socket
import subprocess
import sys
import time
import warnings


def get_hostname():
	return socket.gethostname().lower()

pi_parent_dir = os.path.dirname(__file__)

def is_raspberry_pi():
	try:
		with open('/proc/device-tree/model', 'r') as file:
			model = file.read()
			return 'Raspberry Pi' in model
	except FileNotFoundError:
		return False

is_pi = is_raspberry_pi()

if is_pi:
	sys.path.append(os.path.join(pi_parent_dir, "lib"))
  	# Suppress warnings about GPIO:
	with warnings.catch_warnings(action="ignore"):
		from waveshare_epd import epd2in13_V4

# Set up fonts:
if is_pi:
    picdir = os.path.join(pi_parent_dir, "pic")
    font24 = ImageFont.truetype(os.path.join(picdir,"Font.ttc"),24)
    font14 = ImageFont.truetype(os.path.join(picdir,"Font.ttc"),14)
else:
    font24 = ImageFont.truetype("Font.ttc", 24)
    font14 = ImageFont.truetype("Font.ttc", 14)


def main():
	if is_pi:
		epd = epd2in13_V4.EPD()
		epd.init()
		epd.Clear(0xFF)

if __name__ == "__main__":
	main()


