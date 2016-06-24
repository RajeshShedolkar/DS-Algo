# A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. 
# Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel 
# to satisfy the demand. Write a program that solves this problem in time O(N log N) .

# INPUT
# First list for arrival time of booking.
# Second list for departure time of booking.
# Third is K which denotes count of rooms.

# OUTPUT
# A boolean which tells whether its possible to make a booking. 
# Return 0/1 for C programs.
# O -> No there are not enough rooms for N booking.
# 1 -> Yes there are enough rooms for N booking.

def check_hotel_status(Arr, Dep, k):
    arr = [(t, 1) for t in Arr]+[(t, 0) for t in Dep]
    arr = sorted(arr)
    print arr
    guest = 0

    for event in arr:
        if event[1]==1:
            guest+=1
        else:
            guest-=1
        if guest > k:
            return 0
    return 1                        

Arr = [1, 2, 4, 5]
Dep = [5, 6, 8, 6]
k = 3
print check_hotel_status(Arr, Dep, k)    
