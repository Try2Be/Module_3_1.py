calls = 0   # 1
def count_calls():  #2
    global calls
    calls += 1

def string_info(string):    #3
    strng = str(string)
    result = (len(strng), strng.upper(), strng.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)