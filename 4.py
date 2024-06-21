import itertools

# Digits to consider
digits = '0123456789'

# Letters involved in the problem
letters = 'SENDMORY'

# Generate all possible digit assignments
for perm in itertools.permutations(digits, len(letters)):
    assignment = dict(zip(letters, perm))
    
    # Skip if any leading digit is zero
    if assignment['S'] == '0' or assignment['M'] == '0':
        continue
    
    # Convert the words to numbers based on the current assignment
    send = int(''.join(assignment[c] for c in 'SEND'))
    more = int(''.join(assignment[c] for c in 'MORE'))
    money = int(''.join(assignment[c] for c in 'MONEY'))
    
    # Check if the assignment satisfies SEND + MORE = MONEY
    if send + more == money:
        print(f"SEND + MORE = MONEY\n{send} + {more} = {money}")
        break
