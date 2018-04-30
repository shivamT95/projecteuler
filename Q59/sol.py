enc = map(int,raw_input("Paste the cipher.txt here \n").split(','))
for a in range(26):
    a += ord('a')
    for b in range(26):
        b += ord('a')
        for c in range(26):
            c += ord('a')
            dec = [x for x in enc]
            f = 0
            for i in range(len(dec)):
                if i %3 == 0:
                    dec[i] = a^dec[i]
                elif i%3 == 1:
                    dec[i] = b^dec[i]
                else:
                    dec[i] = c^dec[i]
                if dec[i]>=256:
                    f = 1
            if f == 0:
                decs = "".join([chr(x) for x in dec])
                f2 = 0
                for i in range(len(decs)-3):
                    if dec[i:i+3] == "The":
                        f2 = 1
                        break
                if a == ord('g') and b == ord('o') and c == ord('d'):
                    print(decs)
                    print(f2,sum(dec))
