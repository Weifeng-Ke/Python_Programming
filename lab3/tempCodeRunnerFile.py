    for i in range(SIZE):
        p1=mp.Process(target=checkColumn(testcase, i), daemon=False)
        p1.start()
        p2=mp.Process(target=checkRow(testcase, i), daemon=False)
        p2.start()
        p3=mp.Process(target=checkSubgrid(testcase, i), daemon=False)
        p3.start()
    p1.join()
    p2.join()
    p3.join()