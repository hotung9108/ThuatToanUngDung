# Dãy con liên tục khác biệt

## Đề bài

Cho dãy \(n\) phần tử \(a_1, a_2, \ldots, a_n\), tìm một dãy con liên tục nhiều phần tử nhất có thể sao cho trong dãy con đó không có bất kỳ 2 phần tử nào bằng nhau.

---

## Input

- Dòng đầu gồm \(n\) là số phần tử của dãy \((1 \leq n \leq 1000)\).
- Dòng cuối chứa \(n\) số nguyên không âm có giá trị không vượt quá 32767.

---

## Output

- Một số tự nhiên duy nhất là độ dài của dãy con liên tục dài nhất thỏa mãn không có cặp 2 phần tử bất kỳ nào bằng nhau.

---

## Ví dụ:

### Input:
```
12
4 7 2 8 8 3 2 4 9 3 6
```

### Output:
```
5
```

### Giải thích:
Có hai dãy con liên tục có 5 số liên tiếp thỏa mãn như:
- \([8, 3, 2, 4, 9]\),
- \([2, 4, 9, 3, 6]\).