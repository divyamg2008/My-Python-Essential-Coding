infile = open('image.jpg', 'rb')
outfile = open('imagecopy.jpg', 'wb')
while True:
    buf = infile.read(102400)
    if buf:
        outfile.write(buf)
        print(buf)
        print('.', end='')
    else:
        break
outfile.close()
print('done')
