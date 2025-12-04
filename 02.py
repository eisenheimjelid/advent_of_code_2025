"""🎄 Solution for Day 2 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 02.py
"""

import re

inp = """96952600-96977512,6599102-6745632,32748217-32835067,561562-594935,3434310838-3434398545,150-257,864469-909426,677627997-677711085,85-120,2-19,3081-5416,34-77,35837999-36004545,598895-706186,491462157-491543875,5568703-5723454,6262530705-6262670240,8849400-8930122,385535-477512,730193-852501,577-1317,69628781-69809331,2271285646-2271342060,282-487,1716-2824,967913879-967997665,22-33,5722-11418,162057-325173,6666660033-6666677850,67640049-67720478,355185-381658,101543-146174,24562-55394,59942-93946,967864-1031782"""
part1_asserts = [
    (inp, 28146997880),
]
part2_asserts = [
    (inp, 40028128307),
]


def part1(inp: str) -> str | int | None:
    result = 0
    ranges = [list(map(int, pair.split("-"))) for pair in inp.split(",")]
    for block in ranges:
        start, end = block
        for num in range(start, end + 1):
            if len(str(num)) % 2 == 0:
                first_half = str(num)[: len(str(num)) // 2]
                second_half = str(num)[len(str(num)) // 2 :]
                if first_half == second_half:
                    result += num
    return result


def part2(inp: str) -> str | int | None:
    result = 0
    ranges = [list(map(int, pair.split("-"))) for pair in inp.split(",")]
    for block in ranges:
        start, end = block
        for num in range(start, end + 1):
            skip = False
            if len(str(num)) % 2 == 0:
                first_half = str(num)[: len(str(num)) // 2]
                second_half = str(num)[len(str(num)) // 2 :]
                if first_half == second_half:
                    result += num
                    skip = True
            if not skip:
                regex_pattern = r"(pattern)".replace("pattern", str(num)[:1] + str(num)[:1] + "+")
                match = re.search(regex_pattern, str(num))
                matches = re.findall(regex_pattern, str(num))
                if match:
                    if match.group(1) == str(num):
                        result += num
                        skip = True
            if not skip and len(str(num)) > 3:
                regex_pattern = r"(pattern)".replace("pattern", str(num)[:2])
                matches = re.findall(regex_pattern, str(num))
                if "".join(matches) == str(num):
                    result += num
                    skip = True
            if not skip and len(str(num)) > 4:
                regex_pattern = r"(pattern)".replace("pattern", str(num)[:3])
                matches = re.findall(regex_pattern, str(num))
                if "".join(matches) == str(num):
                    result += num
                    skip = True
    return result
