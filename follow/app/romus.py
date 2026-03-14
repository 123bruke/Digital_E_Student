import json

def load_selected_criteria():

    with open("data/rubric_criteria.json") as f:
        rubric = json.load(f)

    with open("data/assignment_config.json") as f:
        config = json.load(f)

    selected_ids = config["criteria_ids"]

    selected = []

    for category in rubric["assignment_review_criteria"]["categories"]:

        for c in category["criteria"]:

            if c["id"] in selected_ids:
                selected.append(c)

    return selected