#!/usr/bin/env python3
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
import cairo

#internal imports
import kana.common as common


KANA = {"KANA": {}, "KANJI": {}, "META": {"GRAPHICS": [], "DICT": []}}


def init():
	print("Welcome to KanaSuru (かなする)!")
	print(f"VERSION: { common.VERSION }")
	print("LOADING...")
	with open("animCJK/graphicsJaKana.txt", "r") as file:
		line_count: int = 0
		for data in file.read().split('\n'):
			line_count += 1
			if data.isspace() or data in (None, ""):
				continue
			try:
				KANA["META"]["GRAPHICS"].append(json.loads(data))
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
				KANA["META"]["GRAPHICS"].append(json.loads(data))
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
				KANA["META"]["DICT"].append(json.loads(data))
			except json.decoder.JSONDecodeError:
				print(f"Data is: {data}")
				print(f"Line Count: {line_count}")
				exit()
	print("KANA...")
	for each in os.listdir("animCJK/svgsJaKana"):
		with open(f"animCJK/svgsJaKana/{each}", "r") as file:
			KANA["KANA"][each.split(".")[0]] = file.read()
	print("KANJI...")
	for each in os.listdir("animCJK/svgsJa"):
		with open(f"animCJK/svgsJa/{each}", "r") as file:
			KANA["KANJI"][each.split(".")[0]] = file.read()
