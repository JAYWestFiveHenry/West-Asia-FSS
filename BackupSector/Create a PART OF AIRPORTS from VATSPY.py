### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS AFTERWARDS ###
### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS AFTERWARDS ###
### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS AFTERWARDS ###
### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS AFTERWARDS ###
### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS AFTERWARDS ###
### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS AFTERWARDS ###

airports_to_convert = """
VRDA|Maafaru Intl|5.818572|73.469708||VRMF|0
VREI|Ungoofaaru Ifuru|5.7083330|73.0250000||VRMF|0
VRGD|Madivaru|5.4577780|73.3702780||VRMF|0
VRMD|Dharavandhoo|5.156225|73.130275|DRV|VRMF|0
VRMG|Gan Intl|-0.68306|73.15||VRMF|0
VRMH|Hanimaadhoo Intl|6.746111|73.168333|HAQ|VRMF|0
VRMK|Kadhdhoo|1.858333|73.519722|KDO|VRMF|0
VRMM|Male Velana Intl|4.19165|73.529144||VRMF|0
VRMO|Kooddoo|0.733333|73.434167|GKK|VRMF|0
VRMR|Fuvahmulah|-0.309444|73.432778|FVM|VRMF|0
VRMT|Kaadedhdhoo|0.488333|72.996111|KDM|VRMF|0
VRMU|Dhaalu|2.666119|72.886303||VRMF|0
VRMV|Maamigili Villa Intl|3.471611|72.8345|VAM|VRMF|0
VRNT|Thimarafushi|2.210794|73.153033||VRMF|0
"""
lines = airports_to_convert.split("\n")
lines = [x for x in lines if x != '']

airports_dictionary = {}
for line in lines:
    line_parts = line.split("|")
    
    dict_contents = {}
    dict_contents["callsign"] = line_parts[1]
    dict_contents["coord"] =  [float(line_parts[2]),float(line_parts[3])]
    
    airports_dictionary[line_parts[0]] = dict_contents


final_dictionary = {
    "airports" : airports_dictionary
}

# Directly from dictionary
import json
with open('BackupSector/airports.json', 'w') as outfile:
    ### DO NOT FORGET TO ADD THE TOPDOWN KEY FOR RELEVANT AIRPORTS ###
    json.dump(final_dictionary, outfile)

print(final_dictionary)