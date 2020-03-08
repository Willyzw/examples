import glob

requirements = set()
for r in glob.glob('*/requirements.txt'):
    with open(r, 'r') as file:
        requirements.update(file.read().split('\n'))

with open("requirements.txt", "w") as output:
    output.write("\n".join(requirements))
