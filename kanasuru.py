#!/usr/bin/env python3.12
#
#  kanasuru.py
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
import sys
import time
import subprocess as subproc
import kana

def main() -> int:
	"""
	Main function
	"""
	print("Welcome to KanaSuru (かなする)!")
	print(f"VERSION: { kana.common.VERSION }")
	kana.common.load_settings()
	if ("--help" in sys.argv) or ("-h" in sys.argv):
		print(kana.common.HELP)
		return 0
	if "--inside-venv" in sys.argv:
		print(f"RESPAWNING IN VENV!\n{'=' * 52}")
		subproc.check_call([f"{kana.common.VENV_NAME}/bin/python3"] + [each for each in sys.argv if each != "--inside-venv"])
		return 0
	print("LOADING...")
	load_time: float = kana.main.init()
	print(f"""
{"=" * 52}
STATS
{"=" * 52}
KANA:      {len(kana.main.KANA["KANA"])}
KANJI:     {len(kana.main.KANA["KANJI"])}
META:
    GRAPHICS:   {len(kana.main.KANA["META"]["GRAPHICS"])}
    DICTIONARY: {len(kana.main.KANA["META"]["DICT"])}
LOAD TIME: {load_time:.2f} seconds
""")
	import_status: bool = kana.main.test_for_deps()
	if (not import_status) and ("--setup-venv" not in sys.argv):
		print("ERROR: NECESSARY DEPS NOT AVAILABLE PLEASE INSTALL THE NECESSARY DEPS OR PASS THE --setup-venv FLAG!")
		return 1
	elif (not import_status) and ("--setup-venv" in sys.argv):
		print("SETTING UP VENV AS REQUESTED!")
		setup_venv()
	elif (import_status) and ("--setup-venv" in sys.argv):
		print("NO NEED TO SETUP VENV!")
	else:
		print("ALL REQUIRED DEPENDENCIES AVAILABLE!")
	return 0


def setup_venv():
	"""Setup venv"""
	subproc.check_call(["python3", "-m", "venv", kana.common.VENV_NAME])
	with open("requirements.txt", "r") as file:
		packages = [contents.split("-")[1] for contents in file.read().split('\n') if contents not in ("", None)]
	for each in enumerate(packages):
		if each[1] == "cairo":
			packages[each[0]] = "pycairo"
	subproc.check_call(f". {kana.common.VENV_NAME}/bin/activate; pip install {' '.join(packages)}", shell=True)


if __name__ == "__main__":
    sys.exit(main())
