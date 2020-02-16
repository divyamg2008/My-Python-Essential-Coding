infile = open('log1.txt', 'rt')
outfile = open('log1copy.txt', 'wt')
for i in infile:
    print(i.rstrip(), end='***', flush=True, file=outfile)
    print("", file=outfile)
    outfile.writelines(i.rstrip())
outfile.close()
print('done')