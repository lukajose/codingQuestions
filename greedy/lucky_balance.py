def luckBalance(k, contests):
    contests = sorted(contests,key=lambda pair: (pair[1],-pair[0]))
    print(contests)
    m = 0
    lost = 0
    for contest in contests:
        print("contest:",contest)
        if contest[1] == 0:
            m += contest[0]
            print(m)
        else:
            if lost < k:
                m += contest[0]
                lost += 1
            else:
                m -= contest[0]
    return m