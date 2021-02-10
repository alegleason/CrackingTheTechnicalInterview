def CalculateTaxes(income, tax_brackets_table):  # 8,000
    if len(tax_brackets_table) == 0:
        raise Exception('Please check table')
    if income <= 0:
        return 0
    total_tax = 0
    # O(b) time complexity where b is the number of elements we have on the bracket table
    for tax_entree in tax_brackets_table:
        # We are on the last line
        if not tax_entree[0]:
            total_tax += income * tax_entree[1]
            return total_tax

        # Check if we can subtract
        new_income = income - tax_entree[0]  # -7,000
        if new_income >= 0:
            # Perform the tax calculation
            income = new_income  # 3,000
            total_tax += tax_entree[1] * tax_entree[0]
            # total_tax += tax_entree[1] * min(tax_entree[0], income)
        else:
            total_tax += tax_entree[1] * income  # 3,000 * .1
            break
    return total_tax


# CalculateTaxes(8000, [[5000, 0], [10000, .1], [20000, .2], [10000, .3], [None, .4]])

def tupleizer():
    # Helper function to detect prime numbers
    def isPrime(n):
        # 1 is not prime by definition, neither nums < 0
        if num < 2: return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # Read contents of file
    f = open("integers.txt", "r")
    # Check for empty file - No imports :(
    # if os.stat("integers.txt").st_size == 0:
    #    return
    temp_list = []
    # Iterate through the values
    for num in f:
        # Remove new line char line
        num = num.strip('\n')
        # Avoid non-numeric types
        if num.isnumeric():
            # Append its numeric form
            num = int(num)
            temp_list.append(num)
    # Convert to tuple
    int_tuple = tuple(temp_list)
    # Analyze tuple to get some data
    even_nums, prime_nums = 0, 0
    for num in int_tuple:
        # Check if number is even
        if num % 2 == 0:
            even_nums += 1
        # Check if number is prime
        if isPrime(num):
            prime_nums += 1
    # Print report
    print('The difference between the largest and smallest value: ', abs(min(int_tuple) - max(int_tuple)))
    print('The number of items in the tuple: ', len(int_tuple))
    print('The number of even integers in the tuple: ', even_nums)
    print('The sum of the values in the tuple: ', sum(int_tuple))
    print('The average of the values: ', round(sum(int_tuple) / len(int_tuple), 2))
    print('The number of prime numbers in the tuple: ', prime_nums)
    print('The number of items if the tuple is converted to a set: ', len(set(int_tuple)))


def altnet():
    # Read contents of file
    f = open("file.txt", "r")
    message_flag = False
    topic_dict = dict()
    for row in f:
        # Locate the beginning of the file
        if '8<' in row and not message_flag:
            message_flag = True
            continue
        # Skip the part before the message
        elif not message_flag:
            continue
        # Skip the part after the message
        elif '8<' in row and message_flag:
            break
        # Keep only the interesting part
        temp_str = row.split()
        if len(temp_str) > 0:
            temp_str = temp_str[0]
            # Copy an unmodified string
            copy_str = temp_str
            temp_str = temp_str.split('.')
            # Check we are dealing with a valid row
            if temp_str[0] == 'alt':
                if len(temp_str) > 1:
                    topic = temp_str[1]
                    if topic not in topic_dict:
                        topic_dict[topic] = []
                    # Retrieve the subtopic
                    # print("Starting at idx ", 5+len(topic), " on string ", copy_str)
                    copy_str = copy_str[5 + len(topic):]
                    if len(copy_str) > 0:
                        topic_dict[topic].append(copy_str)
                    else:
                        topic_dict[topic].append('root')
    # Analyze the dictionary

    # Print the report
    print("The total number of topics is ", len(topic_dict))
    print("The total number of newsgroups is ", 1)


def calculator():
    # Declare valid operations
    valid_ops = {'+', '-', '*', '/', '^', '%'}
    # While 'q' has not been entered
    while True:
        op = input('Enter operation: ')
        if op == 'q':
            return
        elif op not in valid_ops:
            print('Invalid operator, please try again')
            continue
        # Capture first and second number
        first_num = input('Enter first number: ')
        first_num = float(first_num) if first_num != "" else 0
        second_num = input('Enter second number: ')
        second_num = float(second_num) if second_num != "" else 0
        # Perform the actual operations
        if op == '+':
            print(round(first_num + second_num, 2))
        elif op == '-':
            print(round(first_num - second_num, 2))
        elif op == '*':
            print(round(first_num * second_num, 2))
        elif op == '/':
            if not second_num:
                print('There is no integer division by 0')
                continue
            print(round(first_num / second_num, 1))
        elif op == '^':
            print(round(pow(first_num, second_num), 1))
        else:
            print(first_num % second_num)


def MeetMyTeam():
    # Read contents of file
    f = open("team.txt", "r")
    names = []
    activities = []
    members_not_interested = 0
    for idx, row in enumerate(f):
        row = row.strip('\n')
        curr_row = idx % 4
        if curr_row == 2:
            start_idx = row.find('{') + 1
            # Create substring that holds the activities
            temp_str = row[start_idx:len(row) - 1]
            # Join with the other activities
            activities.extend(temp_str.split(", "))
        elif curr_row == 3:
            # Save the name
            names.append(row.split()[0])
            # Check for uncommitted members
            if 'not' in row or 'no' in row:
                members_not_interested += 1
    # Print report
    num_members = 0 if not idx else int((idx + 1) / 4)
    print('Number of team members: ', num_members)
    print('Number of team members committed to helping the team learn python: ', num_members - members_not_interested)
    # Remove duplicates from activities
    activities = list(dict.fromkeys(activities))
    activities.sort()
    print('Their collective list of interests in alphabetical order include: ', ', '.join(activities))
    names.sort()
    print('Team members in alphabetical order: ', ', '.join(names))


"""
if __name__ == '__main__':
    tupleizer()
    altnet()
    calculator()
    MeetMyTeam()
    print("Done")
"""