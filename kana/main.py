#!/usr/bin/env python3.12
#
#  main.py
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
# External imports
import os
import json
import time

#internal imports
import kana.common as common


KANA: dict = {"KANA": {}, "KANJI": {}, "META": {"GRAPHICS": {}, "DICT": {}}}


def init() -> float:
	"""
	Initalize KanaSuru
	   - Load necessary assets
	"""
	start: float = time.time()
	with open("animCJK/graphicsJaKana.txt", "r") as file:
		line_count: int = 0
		for data in file.read().split('\n'):
			line_count += 1
			if data.isspace() or data in (None, ""):
				continue
			try:
				data = json.loads(data)
				KANA["META"]["GRAPHICS"][ord(data["character"])] = data
			except json.decoder.JSONDecodeError:
				print(f"Data is: {data}")
				print(f"Line Count: {line_count}")
				exit()
	with open("animCJK/graphicsJa.txt", "r") as file:
		line_count: int = 0
		for data in file.read().split('\n'):
			line_count += 1
			if data.isspace() or data in (None, ""):
				continue
			try:
				data = json.loads(data)
				KANA["META"]["GRAPHICS"][ord(data["character"])] = data
			except json.decoder.JSONDecodeError:
				print(f"Data is: {data}")
				print(f"Line Count: {line_count}")
				exit()
	with open("animCJK/dictionaryJa.txt", "r") as file:
		line_count: int = 0
		for data in file.read().split('\n'):
			line_count += 1
			if data.isspace() or data in (None, ""):
				continue
			try:
				data = json.loads(data)
				KANA["META"]["DICT"][ord(data["character"])] = data
			except json.decoder.JSONDecodeError:
				print(f"Data is: {data}")
				print(f"Line Count: {line_count}")
				exit()
	for each in os.listdir("animCJK/svgsJaKana"):
		with open(f"animCJK/svgsJaKana/{each}", "r") as file:
			KANA["KANA"][each.split(".")[0]] = file.read()
	for each in os.listdir("animCJK/svgsJa"):
		with open(f"animCJK/svgsJa/{each}", "r") as file:
			KANA["KANJI"][each.split(".")[0]] = file.read()
	end: float = time.time()
	return end - start


def test_for_deps():
	"""Attempt to import necessary deps"""
	try:
		import cairo
		import kivy
	except ImportError:
		return False
	return True
