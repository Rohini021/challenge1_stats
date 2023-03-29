import json
from collections import Counter

def add_entry_to_stats(stats: dict, entry: dict) -> dict:
    try:
        print("\nAdd entry to stats")

        # Get keys from entry to loop over, so that any new element which is not yet in stats will be added.
        keys_from_entry = list(entry.keys())

        # amount, count and num_items are common regardless of any other elements
        if len(stats) == 0:
            stats = dict()
            stats["amount"] = entry["amount"]
            stats["count"] = 1
            stats["num_items"] = entry["num_items"]
        else:
            stats["amount"] = stats["amount"] +entry["amount"]
            stats["count"] = stats["count"] + 1
            stats["num_items"] = stats["num_items"] +entry["num_items"]

        # already modified amount and num_items, so remove those from keys array
        keys_from_entry.remove("amount")
        keys_from_entry.remove("num_items")

        # loop over keys of 'entry' to add in stats
        for key in keys_from_entry:

            # if key is new (not yet in stats), then create new dict for that element and add to stats
            if key not in stats:
                data = dict()
                data["amount"] = entry["amount"]
                data["count"] = 1
                data["num_items"] = entry["num_items"]
                new_element = {entry[key]:data}
                stats[key] = new_element

            # if key is already present then modify count, amount and num_items 
            else:
                stats[key][entry[key]]["count"] += 1
                stats[key][entry[key]]["amount"] = stats[key][entry[key]]["amount"] + entry["amount"]
                stats[key][entry[key]]["num_items"] = stats[key][entry[key]]["num_items"] + entry["num_items"]
        return stats
    except Exception as ex:
        print("Exception occured: ", str(ex))

def merge_stats(*args: dict) -> dict:
    try:
        print("\nmerge stats")
        stats_to_merge = args
        final_merged_dict = dict()
        for stat in stats_to_merge:
            merge_nested_objects(final_merged_dict,stat)
        return final_merged_dict
    except Exception as ex:
        print("Exception: ", str(ex))

def merge_nested_objects(final_merged_dict,stat):
    for stat_key, stat_value in stat.items():
        if isinstance(stat_value, dict):
            merge_nested_objects(final_merged_dict.setdefault(stat_key, dict()), stat_value)
        elif isinstance(stat_value, int):
            final_merged_dict[stat_key] = final_merged_dict.get(stat_key, 0) + stat_value
