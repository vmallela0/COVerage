from googlesearch import *

def searcher(county, category):
    query = county + " covid-19 " + category + " news"
    urls = []
    for url in search(
        query,
        tld="com",
        num=5,
        stop=5,
        pause=2
    ):
        urls.append(url)
    return urls

cat_list = ["policies", "education", "biology", "economy", "statistics"]
search_export = {}
for i in cat_list:
    search_export[i] = []

def export_search(county, cats, search_dict):
    for i in cats:
        search_dict[i].append(searcher(county, i))
    return search_dict

# print(export_search("Santa Clara County, CA", cat_list, search_export)['policies'])
# print(export_search("Santa Clara County, CA", cat_list, search_export)['education'])
# print(export_search("Santa Clara County, CA", cat_list, search_export)['biology'])
# print(export_search("Santa Clara County, CA", cat_list, search_export)['economy'])
# print(export_search("Santa Clara County, CA", cat_list, search_export)['statistics'])
