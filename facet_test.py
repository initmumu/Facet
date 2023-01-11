from classes.Facet import Facet
import json

file_path = "./data/"
with open(file_path + "search_value.json", encoding='utf-8') as f:
    data = json.load(f)

facet = Facet(data)

facet.apply_facet_filter(
    {
        "title": ["벤처기업", "zip"]
    }
)

#facet.print_original_datasets()
facet.print_filtered_datasets()
#facet.print_facet()