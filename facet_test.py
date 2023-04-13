from classes.Facet import Facet
import json

file_path = "./data/"
with open(file_path + "search_value.json", encoding='utf-8') as f:
    data = json.load(f)

facet = Facet(data)

# facet.print_original_datasets()
#facet.print_facet()
#facet.keyphrase_extract()
facet.facet_query("중개")