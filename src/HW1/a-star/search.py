#search
import state
import frontier
MAX_PUSHED = 2000

# search return tuple (#pushed, #popped, #path_len of solution if obtained else 100)
def search(n):
    s = state.create(n)
    f = frontier.create(s)
    visited = set()
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if state.is_target(s):
            return [ f[1], f[1]-f[2], state.path_len(s)]
        shashable = tuple(s[0])
        if (shashable in visited):
            continue
        else:
            visited.add(shashable)
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
        if f[1] >= MAX_PUSHED:
            return [f[1], f[1]-f[2],  100]
    return 0

# print (search(4))
