import random

try:
    print("The acrobat jumped!")
    if random.random() < 0.5:
        print("The acrobat was able to grab the cradle.")
        print("He swung to the other side!")
    else:
        raise Exception("Wasn't able to grab the swing.")
except Exception as err:
    print("An error occurred in the performance!")
    print("The error was:", str(err))
finally:
    print("-------")
    print("No matter what happened, we hope you enjoyed the show!")


