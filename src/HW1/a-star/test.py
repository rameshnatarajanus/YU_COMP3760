import frontier
import search
import state

pushed_lst, popped_lst, path_cost_lst = [], [], []

N_TRIES = 100

unsuccessful_tries = 0
for _ in range(N_TRIES):
    pushed, popped, path_cost = search.search(4)
    if pushed >= search.MAX_PUSHED:
        unsuccessful_tries += 1
    else:     
        pushed_lst.append(pushed)
        popped_lst.append(popped)
        path_cost_lst.append(path_cost)


print(f"Average states pushed: {sum(pushed_lst)/len(pushed_lst)}")
print(f"Average states popped: {sum(popped_lst)/len(popped_lst)}")
print(f"Average path cost of solution: {sum(path_cost_lst)/len(path_cost_lst)}")
print(f"Max states pushed: {max(pushed_lst)}")
print(f"Max states popped: {max(popped_lst)}")
print(f"Max path cost of solution: {max(path_cost_lst)}")
print(f"Fraction of unsuccessful tries: {unsuccessful_tries/N_TRIES}")