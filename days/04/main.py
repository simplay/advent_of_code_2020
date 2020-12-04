import re

hair_color_pattern = re.compile(r"#[0-9a-f]{6}")
eye_color_pattern = re.compile(r"amb|blu|brn|gry|grn|hzl|oth")
pid_pattern = re.compile(r"[0-9]{9}")
unit_tests = {
    "cm": lambda height: 150.0 <= height <= 193.0,
    "in": lambda height: 59.0 <= height <= 76.0
}

passport_field_validations = {
    "byr": lambda value: len(value) == 4 and 1920 <= int(value) <= 2002,
    "iyr": lambda value: len(value) == 4 and 2010 <= int(value) <= 2020,
    "eyr": lambda value: len(value) == 4 and 2020 <= int(value) <= 2030,
    "hgt": lambda value: len(value) >= 4
                         and re.search(r"cm|in", value) is not None
                         and unit_tests[value[-2:]](float(value[:-2])),
    "hcl": lambda value: hair_color_pattern.fullmatch(value) is not None,
    "ecl": lambda value: eye_color_pattern.fullmatch(value) is not None,
    "pid": lambda value: pid_pattern.fullmatch(value) is not None
}
required_passport_fields = set(passport_field_validations.keys())


def extract_passport(line):
    normalized_line = line.replace("\n", ' ').strip()
    return dict([item.split(":") for item in normalized_line.split(" ")])


def contains_required_keys(passport):
    included_keys = set(passport.keys())
    return len(required_passport_fields.intersection(included_keys)) == 7


def validate(passport):
    return all(
        [passport_field_validations[key](value) for key, value in passport.items() if key in required_passport_fields])


if __name__ == "__main__":
    blank_line_regex = r"(?:\r?\n){2,}"

    with open("input.txt") as file:
        content = file.read()
        lines = re.split(blank_line_regex, content)
        passports = [extract_passport(line) for line in lines]

        passports_with_required_fields = [passport for passport in passports if contains_required_keys(passport)]
        print("Number of passport with required fields is: ", len(passports_with_required_fields))

        valid_passports = [passport for passport in passports_with_required_fields if validate(passport)]
        print("Number of valid passports: ", len(valid_passports))
