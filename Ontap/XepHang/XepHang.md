# Xếp hàng

## Đề bài

Toto chuẩn bị thi môn Phân Tích Thiết Kế Thuật toán nên ôn ngày ôn đêm, mệt quá thiếp đi trên bàn phím và bị xuyên không về thế kỷ XVIII vào ngay Quốc Tử Giám gặp bao nhiêu là sĩ tử đang xếp hàng chuẩn bị thi môn **Đại thành toán pháp**. Quan Chánh chủ khảo là cụ **Lê Quý Đôn** đang gọi thí sinh vào phòng thi trông thấy Toto liền ra bài toán như sau:

Hãy đếm xem trong dãy các sĩ tử đang xếp thành một hàng dài thẳng tắp có bao nhiêu cặp hai người nhìn thấy nhau, tức là giữa hai người không có ai cao hơn một trong hai người đó.

Toto muốn quay về thế giới thực nhưng cụ tránh chủ khảo nói phải trả lời được mới cho về. Bạn hãy giúp Toto nhé.

---

## Input

- Dòng đầu chứa số nguyên dương \(n\) là số người đang xếp hàng \((1 \leq n \leq 10^5)\).
- Dòng thứ 2 là chiều cao của các sĩ tử theo đơn vị thời đó là số nguyên dương có giá trị không vượt quá \(10^9\).

---

## Output

- Một số tự nhiên là kết quả bài toán.

---

## Ví dụ:

### Ví dụ 1:

#### Input:
```
6
7 6 5 1 4 2
```

#### Output:
```
6
```

---

### Ví dụ 2:

#### Input:
```
8
4 7 2 8 4 4 4 6
```

#### Output:
```
14
```

#### Giải thích:
Để dễ đếm cặp ta chỉ xét người trước nhìn về phía sau:
- Người thứ nhất có chiều cao \(4\) nên chỉ nhìn thấy \(1\) người thứ 2.
- Người thứ hai có chiều cao \(7\) nên nhìn thấy \(2\) người thứ 3, thứ 4.
- Người thứ ba có chiều cao \(2\) nên chỉ nhìn thấy \(1\) người thứ 5.
- Người thứ tư chiều cao \(8\) nên chỉ nhìn thấy \(4\) người thứ 5, thứ 6, thứ 7, thứ 8.
- Người thứ năm chiều cao \(4\) nên chỉ nhìn thấy \(3\) người thứ 6, thứ 7, thứ 8.
- Người thứ sáu chiều cao \(4\) nên chỉ nhìn thấy \(2\) người thứ 7, thứ 8.
- Người thứ bảy chiều cao \(4\) nên chỉ nhìn thấy \(1\) người thứ 8.
- Người thứ tám không còn ai.

Tổng số cặp là \(14\).