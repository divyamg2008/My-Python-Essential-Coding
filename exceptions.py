import sys
try:
    x = 9/a
except ValueError:
    print("I caught a value error")
except ZeroDivisionError:
    print ("Don\'t divide by zero")
except:
    print(f"unknown error: {sys.exc_info()[1]}")
else:
    print("good job")