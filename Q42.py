#Emily Rusch

def count_hashtags(string):
    total = 0
    index = 0
    while index < len(string):
        for ch in string:
            if ch == "#":
                total += 1
                index += 1
            else:
                index += 1
        return total
        if total > 4:
            print("This tweet will be considered as a spam!")
        

print(count_hashtags("toda#y is# a goo#d# day"))
