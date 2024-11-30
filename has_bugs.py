def has_bugs(bug):
    # Check if the input 'bug' is True
    if bug == True:
        # If 'bug' is True, return "sad days"
        return "sad days"
    else:
        # If 'bug' is False, return "it's a good day"
        return "it's a good day"

# Examples with detailed explanations:
print(has_bugs(True))  # Input is True, so it will return "sad days"
print(has_bugs(False))  # Input is False, so it will return "it's a good day"
