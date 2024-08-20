# User defined pair class
class Pair:
    first = 0
    second = 0

    def __init__(self, a,  b):
        self.first = a
        self.second = b


class GFG:
    @staticmethod
    def findSubArrays(arr,  n):

        # Array to store all the start and end
        # indices of subarrays with 0 sum
        out = []
        i = 0
        while (i < n):
            prefix = 0
            j = i
            while (j < n):
                prefix += arr[j]
                if (prefix == 0):
                    out.append(Pair(i, j))
                j += 1
            i += 1
        return out

    # Function to print all subarrays with 0 sum
    @staticmethod
    def print(out):
        i = 0
        while (i < len(out)):
            p = out[i]
            print("Subarray found from Index " +
                  str(p.first) + " to " + str(p.second))
            i += 1

    # Driver code
    @staticmethod
    def main(args):

        # Given array
        arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
        n = len(arr)

        # Function Call
        out = GFG.findSubArrays(arr, n)

        # if we didn't find any subarray with 0 sum,
        # then subarray doesn't exists
        if (len(out) == 0):
            print("No subarray exists")
        else:
            GFG.print(out)


if __name__ == "__main__":
    GFG.main([])
