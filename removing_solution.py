import regex as re
path = "C:\\Users\\DHAN RAJ\\Downloads\\leetcode_problem_links.txt"
with open (path,'r') as f:
    text = f.readlines()
    with open(path,'w') as file:
        for line in text:
            if '/solution' not in line:
                file.write(line)
