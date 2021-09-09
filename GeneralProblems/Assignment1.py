def tupleizer():
    # Helper functions
    def isPrime(n):
        # 1 is not prime by definition, neither nums < 0
        if num < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_digit(n):
        # Handles negative numbers
        try:
            int(n)
            return True
        except ValueError:
            return False

    # Read contents of file
    f = open("integers.txt", "r")
    temp_list = []
    # Iterate through the values
    for num in f:
        # Remove new line char line
        num = num.strip('\n')
        # Avoid non-numeric types
        if is_digit(num):
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
    print('The difference between the largest and smallest value:', abs(max(int_tuple) - min(int_tuple)))
    print('The number of items in the tuple:', len(int_tuple))
    print('The number of even integers in the tuple:', even_nums)
    print('The sum of the values in the tuple:', sum(int_tuple))
    print('The average of the values:', round(sum(int_tuple) / len(int_tuple), 2))
    print('The number of prime numbers in the tuple:', prime_nums)
    print('The number of items if the tuple is converted to a set:', len(set(int_tuple)))


def altnet():
    # Read contents of file
    f = open("file.txt", "r")
    topic_dict = dict()
    for row in f:
        # Ignore words that does not start with alt
        if row.startswith('alt'):
            temp_str = row.split()[0]
            copy_str = temp_str
            temp_str = temp_str.split('.')
            # Check we are dealing with a valid row (at least 1 topic)
            if len(temp_str) > 1:
                topic = temp_str[1]
                # Avoid empty alts
                if len(topic) == 0:
                    continue
                # Add the topic
                if topic not in topic_dict:
                    topic_dict[topic] = []
                # Retrieve the subtopic(s)
                copy_str = copy_str[5 + len(topic):]
                # Add the subtopics
                if len(copy_str) > 0:
                    if copy_str not in topic_dict[topic]:
                        topic_dict[topic].append(copy_str)
                else:
                    if 'root' not in topic_dict[topic]:
                        topic_dict[topic].append('root')
    # Analyze the dictionary
    total_newsgroups = 0
    max_subtopics = [0, ""]
    subtopic_max_length = ""
    topic_w_subtopic_count = []
    reconstruct_dict = dict()
    for key in topic_dict.keys():
        num_subtopics = len(topic_dict[key])
        total_newsgroups += num_subtopics
        topic_w_subtopic_count.append([key, num_subtopics])
        if num_subtopics > max_subtopics[0]:
            max_subtopics[0] = num_subtopics
            max_subtopics[1] = key
        for subtopic in topic_dict[key]:
            curr_subtopic = "alt." + key + "." + subtopic
            if len(curr_subtopic) > len(subtopic_max_length):
                subtopic_max_length = curr_subtopic
    # Print the report
    print("The total number of topics is " + "[" + str(len(topic_dict)) + "]")
    print("The total number of newsgroups is " + "[" + str(total_newsgroups) + "]")
    print("The topic with the most subtopics is " + "[" + max_subtopics[1] + "]"
          + " with " + "[" + str(max_subtopics[0]) + "]" + " subtopics")
    print("The longest news group name is " + "[" + subtopic_max_length + "]"
          + " with " + "[" + str(len(subtopic_max_length)) + "]" + " characters\n")
    # Make the words case insensitive and store them in a dict for reconstruction
    for topic in topic_w_subtopic_count:
        # If we have to do changes, do them before hand and save its past status
        if topic[0].lower() != topic[0]:
            if topic[0].lower() in reconstruct_dict:
                # Count num of occurrences
                curr_count = reconstruct_dict[topic[0].lower()][1]
                reconstruct_dict[topic[0].lower()] = [topic[0], curr_count + 1]
            else:
                reconstruct_dict[topic[0].lower()] = [topic[0], 1]
            topic[0] = topic[0].lower()
    # Sort by alphabetical, case insensitive order
    topic_w_subtopic_count = sorted(topic_w_subtopic_count)
    # Sort by second value (num_subtopics), in descending order
    topic_w_subtopic_count = sorted(topic_w_subtopic_count, key=lambda x: int(x[1]), reverse=True)
    for topic in topic_w_subtopic_count:
        if topic[0] in reconstruct_dict and reconstruct_dict[topic[0]][1] > 0:
            topic[0] = reconstruct_dict[topic[0]][0]
            curr_count = reconstruct_dict[topic[0].lower()][1]
            reconstruct_dict[topic[0].lower()] = [topic[0], curr_count - 1]
        print(topic[0], topic[1])


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
        first_num = float(first_num) if first_num != "" else 0.0
        second_num = input('Enter second number: ')
        second_num = float(second_num) if second_num != "" else 0.0
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
    idx = None
    names = []
    activities = []
    members_interested = 0

    for idx, row in enumerate(f):
        row = row.strip('\n')
        curr_row = idx % 4
        if curr_row == 2:
            # Save the name
            names.append(row.split()[0])
            # Create substring that holds the activities
            start_idx = row.find('{') + 1
            temp_str = row[start_idx:len(row) - 1]
            # Join with the other activities
            activities.extend(temp_str.split(", "))
        elif curr_row == 3:
            # If user has filled line 4, they are must likely committed on the team
            members_interested += 1
            # Check for uncommitted members
            if 'not' in row or 'no' in row:
                members_interested -= 1
    # Print report
    num_members = 0 if not idx else int((idx + 1) / 4)
    print('Number of team members:', num_members)
    print('Number of team members committed to helping the team learn python:', members_interested)
    # Remove duplicates from activities
    activities = list(dict.fromkeys(activities))
    activities.sort()
    print('Their collective list of interests in alphabetical order include:', ', '.join(activities))
    names.sort()
    print('Team members in alphabetical order:', ', '.join(names))


if __name__ == '__main__':
    # tupleizer()
    altnet()
    # calculator()
    # MeetMyTeam()
    print("Done")
