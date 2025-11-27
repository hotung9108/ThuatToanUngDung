# Tìm dãy con liên tục có tổng cho trước

## Đề bài

Nhập vào một dãy số nguyên có N phần tử \(a_1, a_2, \ldots, a_N\) và một giá trị nguyên T, tìm độ dài dãy con liên tục dài nhất của dãy có tổng bằng T.

---

## Input

- Dòng đầu chứa số nguyên dương \(N\) \((0 < N \leq 10^6)\) và giá trị nguyên \(T\) có trị tuyệt đối không vượt quá \(10^{15}\).
- Dòng tiếp theo chứa \(N\) số nguyên, mỗi số có giá trị tuyệt đối không vượt quá \(10^9\).

---

## Output

- Một số nguyên không âm là độ dài của dãy con liên tục dài nhất có tổng bằng \(T\).

---

## Ví dụ:

### Input:
```
10 9
2 6 0 3 -3 5 4 0 9 8
```

### Output:
```
6
```

### Giải thích:
Có các dãy con liên tục có tổng bằng 9 gồm:
- \([6, 0, 3]\),
- \([0, 3, -3, 5, 4, 0]\),
- \([3, -3, 5, 4]\),
- \([3, -3, 5, 4, 0]\),
- \([5, 4, 0]\),
- \([0, 9]\),
- \([9]\),

Và dãy dài nhất có 6 phần tử.