SHINY_GOLD = "shiny gold"
if __name__ == "__main__":
    def bag_color_count_with_at_least_one(bags: dict, bag_type: str):
        if bag_type == SHINY_GOLD:
            return 0

        rules = bags[bag_type]

        if len(rules) == 0:
            return 0

        current_sum = 0
        for rule in rules:
            current_bag_type = rule["bag_type"]
            current_sum += bag_color_count_with_at_least_one(bags, current_bag_type) + (
                1 if current_bag_type == SHINY_GOLD else 0)

        return current_sum


    def number_of_bags_inside_bag(bags: dict, bag_type: str):
        rules = bags[bag_type]

        if len(rules) == 0:
            return 0

        current_sum = 0
        for rule in rules:
            current_bag_type = rule["bag_type"]
            quantity = rule["quantity"]
            current_sum += quantity + quantity * number_of_bags_inside_bag(bags, current_bag_type)

        return current_sum


    with open("input.txt") as file:
        lines = file.readlines()

        bags = {}
        for line in lines:
            bag_type, right = line.strip().split("bags contain")
            implications = right.strip().split(",")

            rules = []
            for implication in implications:
                if implication.__contains__("no other bags"):
                    continue

                quantity, color_attribute, color_name, *rest = implication.strip().split(" ")
                rule = {
                    "quantity": int(quantity),
                    "bag_type": f"{color_attribute.strip()} {color_name.strip()}"
                }
                rules.append(rule)

            bags[bag_type.strip()] = rules

        counts = [bag_color_count_with_at_least_one(bags, _bag_type) for _bag_type in bags]
        print("Task 1", sum([count > 0 for count in counts]))
        print("Task 2", number_of_bags_inside_bag(bags, SHINY_GOLD))
