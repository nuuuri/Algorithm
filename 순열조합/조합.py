def comb(arr, n):
    selected = []

    def generate(idx):
        if len(selected) == n:
            print(selected)
            return
        
        if idx >= len(arr):
            return
        
        selected.append(arr[idx])
        generate(idx+1)
        selected.pop()
        generate(idx+1)
    
    generate(0)

comb([1,2,3,4,5], 3)