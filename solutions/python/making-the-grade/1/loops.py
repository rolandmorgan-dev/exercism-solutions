"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    # Returning student_scores numbers, rounded in a list
    return [round(num) for num in student_scores]

def count_failed_students(student_scores):
    # Return the occurrences of numbers below 41
    return len([num for num in student_scores if num<41])

def above_threshold(student_scores, threshold):
    # Returns the numbers from the list, that equals or above the threshold
    return [num for num in student_scores if num >= threshold]

def letter_grades(highest):
    # Returning a list of grades, depending on highest number 
    return [i for i in range(41,highest,(highest-40)//4)]

def student_ranking(student_scores, student_names):
    # Creating a rank list, returning the ranking list
    ranking=[]
    for index, name in enumerate(student_names):
        ranking.append(f"{index+1}. {name}: {student_scores[index]}")
    return ranking

def perfect_score(student_info):
    # The first list element with the perfect score returned, otherwise an empty list returned
    return next((student_info[index] for index,(name,score) in enumerate(student_info) if score==100), [])
