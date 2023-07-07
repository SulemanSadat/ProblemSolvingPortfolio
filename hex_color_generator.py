def hexa():
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())
    res1, ress1, res2, ress2, res3, ress3 = int1 // 16, int1 % 16, int2 // 16, int2 % 16, int3 // 16, int3 % 16
    dic = {0: "0", 1: "1", 2: "2",
           3: "3", 4: "4", 5: "5",
           6: "6", 7: "7", 8: "8",
           9: "9", 10: "a", 11: "b",
           12: "c", 13: "d", 14: "e",
           15: "f"}
    if res1 > 16 or res1 < -0 or res2 > 16 or res2 < -0 or res3 > 16 or res3 < -0:
        print("This is not a color")
    elif res1 and res2 and res3 in dic or res1 < 10 or res2 < 10 or res3 < 10:
        print(f"#{dic[res1]}{dic[ress1]}{dic[res2]}{dic[ress2]}{dic[res3]}{dic[ress3]}")
    else:
        print("Incorrect Value!")

















hexa()  # Suleman Sadat Programmer