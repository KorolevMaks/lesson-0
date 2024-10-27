first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)
second_result = [(x, b) for x in first_strings for b in second_strings if len(x) == len(b)]
print(second_result)
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print(third_result)
