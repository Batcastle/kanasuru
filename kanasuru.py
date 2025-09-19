#!/usr/bin/env python3
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
import kana
import time


def main() -> int:
    kana.main.init()
    print(f"""
{"=" * 52}
STATS
{"=" * 52}
KANA:  {len(kana.main.KANA["KANA"])}
KANJI: {len(kana.main.KANA["KANJI"])}
META:
    GRAPHICS:   {len(kana.main.KANA["META"]["GRAPHICS"])}
    DICTIONARY: {len(kana.main.KANA["META"]["DICT"])}
""")
    time.sleep(500)
    return 0


if __name__ == "__main__":
    sys.exit(main())
