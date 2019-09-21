import count

# --------------------------------
# get_nth_triple()
# --------------------------------
assert count.get_nth_triple(123456789, 0) == 789
assert count.get_nth_triple(123456789, 1) == 456
assert count.get_nth_triple(123456789, 2) == 123
assert count.get_nth_triple(7312, 1) == 7
assert count.get_nth_triple(12, 0) == 12
assert count.get_nth_triple(132004, 0) == 4
assert count.get_nth_triple(1, 0) == 1
assert count.get_nth_triple(12, 2) == -1
assert count.get_nth_triple(84952, 2) == -1

# --------------------------------
# say_number()
# --------------------------------
assert round(count.say_number(123), 2) == 2.15
assert round(count.say_number(342), 2) == 2.15
assert round(count.say_number(104), 2) == 1.4
assert round(count.say_number(9), 2) == 0.40
assert round(count.say_number(7), 2) == 0.60
assert round(count.say_number(21), 2) == 1.15
assert round(count.say_number(12), 2) == 0.60
assert round(count.say_number(13), 2) == 0.75

# --------------------------------
# get_triples()
# --------------------------------
assert count.get_triples(1111) == [111, 1]
assert count.get_triples(1001) == [1, 1]
assert count.get_triples(1000) == [0, 1]
assert count.get_triples(123456789) == [789, 456, 123]
assert count.get_triples(1) == [1]
assert count.get_triples(12) == [12]
assert count.get_triples(10) == [10]
assert count.get_triples(204) == [204]
assert count.get_triples(123000321) == [321, 0, 123]
assert count.get_triples(999888777666555) == [555, 666, 777, 888, 999]

print('All tests passed.')