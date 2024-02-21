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
    for ccLevels in json_data:
        newLevel = cc_classes.CCLevel() #New Level
        newLevel.level_number = ccLevels["level_number"] #Start of new level attributes
        newLevel.time = ccLevels["time"]
        newLevel.num_chips = ccLevels["num_chips"]
        newLevel.upper_layer = ccLevels["upper_layer"]
        newLevel.lower_layer = ccLevels["lower_layer"]

        optional_fields_list = []
        for field in ccLevels["optional_fields"]: #References items in "optional_fields" data list
            #Title
            title_field = cc_classes.CCMapTitleField(field["title"])
            optional_fields_list.append(title_field)

            #Password
            password_field = cc_classes.CCEncodedPasswordField(field["password"])
            optional_fields_list.append(password_field)

            #Hint
            hint_field = cc_classes.CCMapHintField(field["hint"])
            optional_fields_list.append(hint_field)

            #Monster(s)
            coordinate_field = []
            for coordinate in field["monster"]:
                monster_coordinate = cc_classes.CCCoordinate(coordinate["0"], coordinate["1"])
                coordinate_field.append(monster_coordinate)
            monster_field = cc_classes.CCMonsterMovementField(coordinate_field)
            optional_fields_list.append(monster_field)
        newLevel.optional_fields_list = optional_fields_list
        level_pack.add_level(newLevel)
    return level_pack

#Save converted data to DAT file

dat_level = "clneff_cc1.dat" #Creates name/variable reference for the file to print as
cc_dat_utils.write_cc_level_pack_to_dat(level_json_data, dat_level)
print(cc_dat_utils.make_cc_level_pack_from_dat(dat_level))