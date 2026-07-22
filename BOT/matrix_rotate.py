inp_ls = [1, 12, 45, 43, 46, 2, 6, 4, 2, 623, 4, 5, 6, 7, 8]
max_len = 1
current_len = 1
start = 0
best_start = 0
for n in range(1, len(inp_ls)):
    if inp_ls[n] > inp_ls[n-1]:
        if start == 0:
            start = n-1
        current_len += 1
        
        if current_len > max_len:
            max_len = current_len
            best_start = start
    else:
        current_len = 0
        start = 0

print(max_len)
for i in range(best_start, max_len+best_start+1):
    print(inp_ls[i], end=" ")