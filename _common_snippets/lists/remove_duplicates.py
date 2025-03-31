# Can be ran after checking for duplicates -> check_for duplicates.py

sample_list = [ 1, 1, 2, 3, 4, 5, 5]

def remove_duplicates(sample_list):
    sample_list_new = []
    for item in sample_list:
        if item not in sample_list_new:
            sample_list_new.append(item)
    return sample_list_new

print(remove_duplicates(sample_list))