from datetime import datetime

def calculate_four_pillars_luck_pillars_ten_gods(birth_date):
    # Define Heavenly Stems and Earthly Branches
    heavenly_stems = [
        {"name": "Yang Wood", "value": 1, "character": "甲", "spelling": "jia"},
        {"name": "Yin Wood", "value": 2, "character": "乙", "spelling": "yi"},
        {"name": "Yang Fire", "value": 3, "character": "丙", "spelling": "bing"},
        {"name": "Yin Fire", "value": 4, "character": "丁", "spelling": "ding"},
        {"name": "Yang Earth", "value": 5, "character": "戊", "spelling": "wu"},
        {"name": "Yin Earth", "value": 6, "character": "己", "spelling": "ji"},
        {"name": "Yang Metal", "value": 7, "character": "庚", "spelling": "geng"},
        {"name": "Yin Metal", "value": 8, "character": "辛", "spelling": "xin"},
        {"name": "Yang Water", "value": 9, "character": "壬", "spelling": "ren"},
        {"name": "Yin Water", "value": 10, "character": "癸", "spelling": "gui"},
    ]

    earthly_branches = [
        {"name": "Rat", "value": 1, "character": "子", "spelling": "zi", "hidden_stems": ["癸"], "element": "Water水"},
        {"name": "Ox", "value": 2, "character": "丑", "spelling": "chou", "hidden_stems": ["己", "癸"], "element": "Earth土"},
        {"name": "Tiger", "value": 3, "character": "寅", "spelling": "yin", "hidden_stems": ["甲", "丙", "戊"], "element": "Wood木"},
        {"name": "Rabbit", "value": 4, "character": "卯", "spelling": "mao", "hidden_stems": ["乙"], "element": "Wood木"},
        {"name": "Dragon", "value": 5, "character": "辰", "spelling": "chen", "hidden_stems": ["戊", "乙", "癸"], "element": "Earth土"},
        {"name": "Snake", "value": 6, "character": "巳", "spelling": "si", "hidden_stems": ["丙", "戊", "庚"], "element": "Fire火"},
        {"name": "Horse", "value": 7, "character": "午", "spelling": "wu", "hidden_stems": ["丁", "己"], "element": "Fire火"},
        {"name": "Goat", "value": 8, "character": "未", "spelling": "wei", "hidden_stems": ["己", "丁", "乙"], "element": "Earth土"},
        {"name": "Monkey", "value": 9, "character": "申", "spelling": "shen", "hidden_stems": ["庚", "壬", "戊"], "element": "Metal金"},
        {"name": "Rooster", "value": 10, "character": "酉", "spelling": "you", "hidden_stems": ["辛"], "element": "Metal金"},
        {"name": "Dog", "value": 11, "character": "戌", "spelling": "xu", "hidden_stems": ["戊", "辛", "丁"], "element": "Earth土"},
        {"name": "Pig", "value": 12, "character": "亥", "spelling": "hai", "hidden_stems": ["壬", "甲"], "element": "Water水"},
    ]

    ten_gods = {
    "Yang Wood": {
        "Yang Wood": "Friend", "Yin Wood": "Rob Wealth", "Yang Fire": "Output", "Yin Fire": "Hurt Officer",
        "Yang Earth": "Direct Wealth", "Yin Earth": "Indirect Wealth", "Yang Metal": "Direct Officer",
        "Yin Metal": "Seven Killings", "Yang Water": "Direct Resource", "Yin Water": "Indirect Resource"
    },
    "Yin Wood": {
        "Yang Wood": "Rob Wealth", "Yin Wood": "Friend", "Yang Fire": "Hurt Officer", "Yin Fire": "Output",
        "Yang Earth": "Indirect Wealth", "Yin Earth": "Direct Wealth", "Yang Metal": "Seven Killings",
        "Yin Metal": "Direct Officer", "Yang Water": "Indirect Resource", "Yin Water": "Direct Resource"
    },
    "Yang Fire": {
        "Yang Wood": "Direct Resource", "Yin Wood": "Indirect Resource", "Yang Fire": "Friend", "Yin Fire": "Rob Wealth",
        "Yang Earth": "Output", "Yin Earth": "Hurt Officer", "Yang Metal": "Direct Wealth",
        "Yin Metal": "Indirect Wealth", "Yang Water": "Direct Officer", "Yin Water": "Seven Killings"
    },
    "Yin Fire": {
        "Yang Wood": "Indirect Resource", "Yin Wood": "Direct Resource", "Yang Fire": "Rob Wealth", "Yin Fire": "Friend",
        "Yang Earth": "Hurt Officer", "Yin Earth": "Output", "Yang Metal": "Indirect Wealth",
        "Yin Metal": "Direct Wealth", "Yang Water": "Seven Killings", "Yin Water": "Direct Officer"
    },
    "Yang Earth": {
        "Yang Wood": "Seven Killings", "Yin Wood": "Direct Officer", "Yang Fire": "Direct Resource",
        "Yin Fire": "Indirect Resource", "Yang Earth": "Friend", "Yin Earth": "Rob Wealth",
        "Yang Metal": "Output", "Yin Metal": "Hurt Officer", "Yang Water": "Direct Wealth", "Yin Water": "Indirect Wealth"
    },
    "Yin Earth": {
        "Yang Wood": "Direct Officer", "Yin Wood": "Seven Killings", "Yang Fire": "Indirect Resource",
        "Yin Fire": "Direct Resource", "Yang Earth": "Rob Wealth", "Yin Earth": "Friend",
        "Yang Metal": "Hurt Officer", "Yin Metal": "Output", "Yang Water": "Indirect Wealth", "Yin Water": "Direct Wealth"
    },
    "Yang Metal": {
        "Yang Wood": "Indirect Wealth", "Yin Wood": "Direct Wealth", "Yang Fire": "Seven Killings",
        "Yin Fire": "Direct Officer", "Yang Earth": "Direct Resource", "Yin Earth": "Indirect Resource",
        "Yang Metal": "Friend", "Yin Metal": "Rob Wealth", "Yang Water": "Output", "Yin Water": "Hurt Officer"
    },
    "Yin Metal": {
        "Yang Wood": "Direct Wealth", "Yin Wood": "Indirect Wealth", "Yang Fire": "Direct Officer",
        "Yin Fire": "Seven Killings", "Yang Earth": "Indirect Resource", "Yin Earth": "Direct Resource",
        "Yang Metal": "Rob Wealth", "Yin Metal": "Friend", "Yang Water": "Hurt Officer", "Yin Water": "Output"
    },
    "Yang Water": {
        "Yang Wood": "Output", "Yin Wood": "Hurt Officer", "Yang Fire": "Indirect Wealth",
        "Yin Fire": "Direct Wealth", "Yang Earth": "Seven Killings", "Yin Earth": "Direct Officer",
        "Yang Metal": "Direct Resource", "Yin Metal": "Indirect Resource", "Yang Water": "Friend", "Yin Water": "Rob Wealth"
    },
    "Yin Water": {
        "Yang Wood": "Hurt Officer", "Yin Wood": "Output", "Yang Fire": "Direct Wealth",
        "Yin Fire": "Indirect Wealth", "Yang Earth": "Direct Officer", "Yin Earth": "Seven Killings",
        "Yang Metal": "Indirect Resource", "Yin Metal": "Direct Resource", "Yang Water": "Rob Wealth", "Yin Water": "Friend"
    },
}


    def get_heavenly_stem_and_earthly_branch(year):
        heavenly_stem = heavenly_stems[(year - 4) % 10]
        earthly_branch = earthly_branches[(year - 4) % 12]
        return heavenly_stem, earthly_branch

    # Four Pillars Calculation
    birth_year = birth_date.year
    year_heavenly_stem, year_earthly_branch = get_heavenly_stem_and_earthly_branch(birth_year)

    month_index = (birth_date.month - 1) % 12
    month_earthly_branch = earthly_branches[month_index]
    month_heavenly_stem = heavenly_stems[(year_heavenly_stem["value"] + month_index) % 10]

    day_heavenly_stem = heavenly_stems[(birth_date.toordinal() % 10)]
    day_earthly_branch = earthly_branches[(birth_date.toordinal() % 12)]

    hour = birth_date.hour
    hour_heavenly_stem = heavenly_stems[(day_heavenly_stem["value"] * 2 + hour // 2) % 10]
    hour_earthly_branch = earthly_branches[hour // 2 % 12]

    # Calculate 10 Gods
    day_master = day_heavenly_stem["name"]
    four_pillars = {
        "year_pillar": {"heavenly_stem": year_heavenly_stem, "earthly_branch": year_earthly_branch},
        "month_pillar": {"heavenly_stem": month_heavenly_stem, "earthly_branch": month_earthly_branch},
        "day_pillar": {"heavenly_stem": day_heavenly_stem, "earthly_branch": day_earthly_branch},
        "hour_pillar": {"heavenly_stem": hour_heavenly_stem, "earthly_branch": hour_earthly_branch},
    }
    for pillar in four_pillars.values():
        pillar["ten_god"] = ten_gods.get(day_master, {}).get(pillar["heavenly_stem"]["name"], "Unknown")

    # Luck Pillars Calculation
    first_luck_pillar_age = 6
    month_heavenly_stem_index = heavenly_stems.index(month_heavenly_stem)
    month_earthly_branch_index = earthly_branches.index(month_earthly_branch)

    luck_pillars = []
    for i in range(9):
        heavenly_stem = heavenly_stems[(month_heavenly_stem_index + i) % 10]
        earthly_branch = earthly_branches[(month_earthly_branch_index + i) % 12]
        age = first_luck_pillar_age + i * 10

        luck_pillars.append({
            "age": age,
            "heavenly_stem": heavenly_stem["character"],
            "earthly_branch": earthly_branch["character"],
            "element": earthly_branch["element"],
            "hidden_stems": earthly_branch["hidden_stems"],
        })

    return {"four_pillars": four_pillars, "luck_pillars": luck_pillars}


# Example Usage
birth_date = datetime(1976, 4, 19, 11, 23)  # Year, Month, Day, Hour, Minute
result = calculate_four_pillars_luck_pillars_ten_gods(birth_date)

# Print Result
import pprint
pprint.pprint(result)
