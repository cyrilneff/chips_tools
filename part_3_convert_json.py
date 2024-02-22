import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file

input_json_file = "data/clneff_cc1.json"
with open(input_json_file, "r") as reader:
    level_json_data = json.load(reader) #Reads the JSON file created for the levels

#Convert JSON data to CCLevelPack

def make_level_pack_from_json(json_data):
    level_pack = cc_classes.CCLevelPack() #Sets up the function/where it pulls code from to create level
    levels = json_data["ccLevels"]
    for ccLevels in levels:
        newLevel = cc_classes.CCLevel() #New Level
        newLevel.level_number = ccLevels["level_number"] #Start of new level attributes
        newLevel.time = ccLevels["time"]
        newLevel.num_chips = ccLevels["num_chips"]
        newLevel.upper_layer = ccLevels["upper_layer"]
        newLevel.lower_layer = ccLevels["lower_layer"]

        optional_fields_list = ccLevels["optional_fields"]
        for field in optional_fields_list: #References items in "optional_fields" data list
            #Title
            if "title" in field:
                title_field = cc_classes.CCMapTitleField(field["title"])
                newLevel.add_field(title_field)

            #Password
            if "password" in field:
                password_field = cc_classes.CCEncodedPasswordField(field["password"])
                newLevel.add_field(password_field)

            #Hint
            if "hint" in field:
                hint_field = cc_classes.CCMapHintField(field["hint"])
                newLevel.add_field(hint_field)

            #Monster(s)
            if "monster" in field:
                coordinate_field = []
                for x,y in field["monster"]:
                    monster_coordinate = cc_classes.CCCoordinate(x, y)
                    coordinate_field.append(monster_coordinate)
                monster_field = cc_classes.CCMonsterMovementField(coordinate_field)
                newLevel.add_field(monster_field)

        level_pack.add_level(newLevel)
    return level_pack

#Save converted data to DAT file

dat_level = "clneff_cc1.dat" #Creates name/variable reference for the file to print as
cc_dat_utils.write_cc_level_pack_to_dat(make_level_pack_from_json(level_json_data), dat_level)
print(cc_dat_utils.make_cc_level_pack_from_dat(dat_level))