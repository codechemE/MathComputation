f = open("sunspots.txt", "r")  # Draw back: have to explicitly close it
# print(f.read())

# Methods 1 through 3
# Method 1
# lines = f.readlines()

# Method 2
# lines = []
# for line in f:
#    lines.append(line)

# Method 3 List comprehension
# lines = [line for line in f]
# print(lines)

# print(f.name)
# print(f.mode)

f.close()

# another method for opening files but closing is done automatically
# context manager
with open('sunspots.txt', 'r') as g:

    size_to_read = 10

    g_contents = g.read(size_to_read)
    # print(g_contents)

    while len(g_contents) > 0:
        print(g_contents, end='')
        g_contents = g.read(size_to_read)

# if file doesn't exist, file will be created
with open('nugs.txt', 'w') as h:
    h.write("Nugget is chicken nugget shaped.")

with open("nugs.txt", 'r') as rf:
    with open("copy_nugs.txt", "w") as wf:
        wf.write(rf.read())

with open('XRD.png', 'rb') as oi:
    with open('copy_XRD.png', 'wb') as ci:
        chunk_size = 400
        original_chunk = oi.read(chunk_size)

        while len(original_chunk) > 0:
            ci.write(original_chunk)
            original_chunk = oi.read(chunk_size)