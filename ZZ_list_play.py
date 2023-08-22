import random

# set up a list

my_list = []

for item in range(0, 100):

    random_num = random.randint(1, 100)

    my_list.append(random_num)

print(my_list)

my_list.sort()

my_list_len = len(my_list)

print()
print(my_list)
print("The list has {} items".format(my_list_len))
print()


def factors(my_list, the_number, the_factor=3):
    if the_number % the_factor == 0:
        print(the_factor)
        my_list.append(the_factor)
        factors(the_number, the_factor)
    elif the_factor <= the_number:
        factors(the_number, the_factor+2)