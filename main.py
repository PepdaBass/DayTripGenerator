import random

# Selects random index number from a list of travel options.
def random_selection(trip_list_option):
    random_index = random.randrange(0, len(trip_list_option))
    trip_item = trip_list_option.pop(random_index)
    return trip_item

# Creates the initial travel itinerary.
def create_initial_trip():
    initial_trip = []
    random_dest = random_selection(destinations)
    random_rest = random_selection(restaurants)
    random_transport = random_selection(modes_of_transportation)
    random_entertain = random_selection(entertainments)
    initial_trip.append(random_dest)
    initial_trip.append(random_rest)
    initial_trip.append(random_transport)
    initial_trip.append(random_entertain)
    return initial_trip

# Displays the itinerary in an easier to read format.
def display_list():
    print('Travel Itinerary:')
    for item in first_plan:
        print(item)

# If the user wishes to randomly change one item, they may declare which one. If the list drops to
# one item, the user is stuck with the final randomly selected item.
def random_reselect():
    reselection = input('To change an item, please enter: Destination, Restaurant, Transport, or Entertainment. ')
    give_me_another = True
    while give_me_another is True:
        if reselection == 'Destination':
            if len(destinations) == 1:
                print('No more destination options available.')
                break
            else:                                      # The selection is taken out of the list and reinserted in the correct 
                first_plan.pop(0)                      # index.
                random_dest = random_selection(destinations)
                first_plan.insert(0, random_dest)
                give_me_another = False
        elif reselection == 'Restaurant':
            if len(restaurants) == 1:
                print('No more dining options available.')
                break
            else:
                first_plan.pop(1)
                random_rest = random_selection(restaurants)
                first_plan.insert(1, random_rest)
                give_me_another = False
        elif reselection == 'Transport':
            if len(modes_of_transportation) == 1:
                print('No more transporation options available.')
                break
            else:
                first_plan.pop(2)
                random_transport = random_selection(modes_of_transportation)
                first_plan.insert(2, random_transport)
                give_me_another = False
        elif reselection == 'Entertainment':
            if len(entertainments) == 1:
                print('No more entertainment options available.')
                break
            else:
                first_plan.pop(3)
                random_entertain = random_selection(entertainments)
                first_plan.insert(3, random_entertain)
                give_me_another = False
        elif reselection != 'Destination' or 'Restaurant' or 'Transport' or 'Entertainment':
            reselection = input('Invalid selection. Try again: ')

# This asks if the user is satisfied with the most current itinerary.
def satisfaction():
    satisfied = False
    while satisfied is False:
        yes_or_no = input('Are you satisfied with this plan? ')
        if yes_or_no == 'yes' or yes_or_no == 'Yes':
            satisfied = True
            break
        elif yes_or_no == 'no' or yes_or_no == 'No':
            change_item = random_reselect()
            display_list()
        elif yes_or_no != 'no' or yes_or_no != 'No' or yes_or_no != 'yes' or yes_or_no != 'Yes':
            print('Invalid selection, try again.')
            continue
    
            
# Options for random itinerary assignment.
destinations = ['New York', 'Las Vegas', 'Detroit', 'Seattle', 'Chicago']
restaurants = ['Olive Garden', 'Applebees', 'Mellow Mushroom', 'Outback Steakhouse', 'Art of Pizza']
modes_of_transportation = ['car', 'rollerblades', 'bicycle', 'motorcycle', 'bus']
entertainments = ['the cinema', 'a concert', 'hackysack', 'Fight Club', 'paintball']

# Begins the process of choosing a randomly selected itinerary and its components, displays the itinerary for the user,
# checks the user's satisfaction, and offers options to randomly change items.
first_plan = create_initial_trip()
display_list()
satisfaction()

# Automatic message after user is satisfied with the itinerary.
print(f'''
Congratulations! You are going to beautiful {first_plan[0]}, eating at the famous {first_plan[1]}, 
getting about by {first_plan[2]}, and enjoying {first_plan[3]}!
''')


