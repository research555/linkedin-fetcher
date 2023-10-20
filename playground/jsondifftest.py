from jsondiff import diff
import json




def calculate_difference(a, b):
    return diff(a, b)













import pprint

pp = pprint.PrettyPrinter(indent=1)


with open(r'C:\Users\immi\PyCharmProjects\Startups\kale-linkedin-api\playground\prof_a.json' , 'r', encoding='utf-8') as f:
    a = json.load(f)


with open(r'C:\Users\immi\PyCharmProjects\Startups\kale-linkedin-api\playground\prof_b.json' , 'r', encoding='utf-8') as f:
    b = json.load(f)



difference = calculate_difference(a, b)

pp.pprint(difference)











