def combine(pth):
    with open("a.txt") as f1, open("b.txt") as f2, open("c.txt", "w") as f3:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()
        f3.write(f1_lines[0].strip())
        f3.write(f2_lines[1].strip())
        f3.write(f1.read().strip())
        f3.write(f2.read().strip())
        f3.writelines(f1_lines[:])
        f3.writelines(f2_lines[:])

    
    
