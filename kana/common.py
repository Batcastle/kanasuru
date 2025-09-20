#!/usr/bin/env python3.12
#
#  common.py
#  
#  Copyright 2025 Thomas Castleman <batcastle@draugeros.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import json
import os


VERSION: str = "0.0.1-DEV"
HELP: str = """
-h, --help           Print this help message and exit
    --inside-venv    Run inside existing venv
    --setup-venv     Setup venv and exit
-v, --version        Print version and exit
"""
# DEFAULT SETTINGS
VENV_NAME: str = "venv"
SETTINGS: dict = {}


def load_settings() -> dict:
	"""
	Load settings
	"""
	global SETTINGS, VENV_NAME
	if os.path.exists("settings.json"):
		with open("settings.json", "r") as file:
			SETTINGS = json.load(file)
	if "VENV_NAME" in SETTINGS:
		VENV_NAME = SETTINGS["VENV"]
	else:
		SETTINGS["VENV"] = VENV_NAME
	if not os.path.exists("settings.json"):
		save_settings()
	

def save_settings():
	"""
	Save settings to disk
	"""
	with open("settings.json", "w+") as file:
		json.dump(SETTINGS, file, indent=2)
