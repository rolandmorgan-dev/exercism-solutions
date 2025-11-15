"""Functions to manage and organize queues at Chaitana's roller coaster."""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    # Adding the person to the right list, according to the type of the ticket
    return (normal_queue.append(person_name) or normal_queue, 
            express_queue.append(person_name) or express_queue)[ticket_type == 1]

def find_my_friend(queue, friend_name):
    # Returns the position of the person's name in the queue
    return queue.index(friend_name) if friend_name in queue else None

def add_me_with_my_friends(queue, index, person_name):
    # Queue returned with the late arrival's name
    return queue.insert(index, person_name) or queue

def remove_the_mean_person(queue, person_name):
    # List returned without the person's name
    return queue.remove(person_name) or queue

def how_many_namefellows(queue, person_name):
    # Namefellows counted and occurrences returned in a number
    return queue.count(person_name)

def remove_the_last_person(queue):
    # Last person removed from the list, name returned from the function
    return queue.pop()

def sorted_names(queue):
    # Queue sorted into alphabetical order and returned
    return sorted(queue)