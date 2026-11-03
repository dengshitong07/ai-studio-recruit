def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    word_map = [
        ("zero", "0"),
        ("two", "2"),
        ("four", "4"),
        ("six", "6"),
        ("nine", "9"),
    ]
    target_digit = {"0","2","4","6","9"}
    
    for s in cases:
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] in target_digit:
                res.append(s[i])
                i += 1
            else:
                matched = False
                for w, num in word_map:
                    lw = len(w)
                    if i + lw <= n and s[i:i+lw] == w:
                        res.append(num)
                        i += lw
                        matched = True
                        break
                if not matched:
                    i += 1
        print(''.join(res))

if __name__ == "__main__":
    main()