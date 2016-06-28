
class Underscore(object):

    def map(self, arr, func):
        newList = []  # initialize new list
        for val in arr:  # iterate elements in passed list
            # apply passed function to elements and append to new list
            newList.append(func(val))
        return newList

        # Reduce should take an array and a callback
        # and apply the provided callback to every value in
        # the array, returning a single value.
    def reduce(self, arr, func):
        # initialize int variable
        running_total = 0
        for i in arr:
            # iterate through list item and get value as 'i'
            # pass each value into provided lamba function as well as the
            # current running total
            running_total = func(i, running_total)
        return running_total  # Return running total

    def find(self, arr, func):
        for val in arr:  # iterate passed list
            # If return value from lambda is 0, we have the first
            # even number
            if func(val) == 0:
                # Return even number as well as index of even number in array
                return "Found at index {0}, {1}".format(arr.index(val), val)

    def filter(self, arr, func):
        newList = []  # initialize new list
        for val in arr:
            # append to new list each element that meets condition in passed
            # function
            newList.append(val) if func(val) else None
            # ^ Single line statement that reads like a sentence. Awesome syntax.
        return newList

    def reject(self, arr, func):
        newList = []  # initialize new list
        for val in arr:
            # append to new list each element that fails condition in passed
            # function
            newList.append(val) if not func(val) else None
        return newList


_ = Underscore()  # instantiate Underscore class

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# call methods of Underscore class & pass in list and lambda; print returned
# list. Only pass in lambda functions as the callback

print _.map(myList, lambda x: x + 5)

print _.reduce(myList, lambda x, y: x + y)

print _.find(myList, lambda x: x % 2)

print _.filter(myList, lambda x: x % 2 == 0)

print _.reject(myList, lambda x: x >= 3)
