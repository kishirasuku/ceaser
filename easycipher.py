def main():
    print "input the source"
    source=raw_input()
    ceaser(source)

def ceaser(source):
    for i in range(27):
        for s in source:
            if ord('z')>=ord(s)>=ord('a'):
                if ord('z')>=ord(s)+i>=ord('a'):
                    print chr(ord(s)+i),
                else:
                    print chr(ord(s)+i-26),
            elif ord('Z')>=ord(s)>=ord('A'):
                if ord('Z')>=ord(s)+i>=ord('A'):
                    print chr(ord(s)+i),
                else:
                    print chr(ord(s)+i-26),
            else:
                print s,
        print ""
        print "-------------------------------------"

main()

