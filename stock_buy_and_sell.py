"""
Efficient Approch approch
Time complexity -> O(n)
Aux space -> O(1)

"""
arr = [10,20,30]

def buy_and_sell(arr:list):
    results = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
           results = results + arr[i] - arr[i-1]
    return results

print(buy_and_sell(arr))
