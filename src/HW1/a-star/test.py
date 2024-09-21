import frontier
import search
import state

tot_pushed, tot_popped, tot_path_cost = 0, 0, 0
max_pushed, max_popped, max_path_cost = 0, 0, 0

N_TRIES = 100

for _ in range(N_TRIES):
    pushed, popped, path_cost = search.search(4)
    tot_pushed += pushed
    tot_popped += popped
    tot_path_cost += path_cost

    max_pushed = max(max_pushed, pushed)
    max_popped = max(max_popped, popped)
    max_path_cost = max(max_path_cost, path_cost)

print(f"Average total items pushed: {tot_pushed/N_TRIES}")
print(f"Average total items popped: {tot_popped/N_TRIES}")
print(f"Average path cost of solution: {tot_path_cost/N_TRIES}")
print(f"Max total items pushed: {max_pushed}")
print(f"Max total items popped: {max_popped}")
print(f"Max path cost of solution: {max_path_cost}")