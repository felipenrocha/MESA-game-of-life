from random import randint, randrange


def generate_rule():
    born_rule = generate_rule_number()
    survive_rule = generate_rule_number()

    return concat_rule(born_rule, survive_rule)



def concat_rule(born_rule, survive_rule):
    rule = 'B'
    for letter in born_rule:
        rule += letter
    rule += '/S'
    for letter in survive_rule:
        rule +=letter
    return rule


def generate_rule_number():
    # returned rule string


    # length of born and survive rules
    number_rules = randint(1,9)

    # string that has numbers of born rule
    rule = ''

    numbers_pushed = []
    while len(numbers_pushed) != number_rules:
        number = randint(1,9)
        if number not in numbers_pushed:
            rule += str(number)
            numbers_pushed.append(number)
        


    return rule
