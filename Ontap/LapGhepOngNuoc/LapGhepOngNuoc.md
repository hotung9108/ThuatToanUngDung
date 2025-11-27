# Lắp ghép ống nước

## Đề bài

Thành phố xây dựng hệ thống nước sạch cần phải lắp ghép các đoạn ống có độ dài lần lượt là \(a_1, a_2, \ldots, a_n\) thành một đường ống thẳng. Để lắp ghép cần một máy năng nhưng khả năng của nó mỗi lúc chỉ nối được tối đa \(k\) đoạn ống và chi phí để nối chính là tổng độ dài của đoạn đó sau khi nối. Bạn hãy lập trình tính tổng chi phí nối là ít nhất.

---

## Input

- Dòng thứ nhất chứa hai số nguyên dương \(n\) và \(k\) \((1 < k < n \leq 10^5)\).
- Dòng tiếp theo chứa \(n\) số nguyên dương là độ dài của các đoạn ống cần nối có giá trị không vượt quá \(3 \cdot 10^4\).

---

## Output

- Một số nguyên dương duy nhất là tổng số chi phí ít nhất để nối hệ thống cấp nước.

---

## Ví dụ:

### Ví dụ 1:

#### Input:
```
3 2
8 4 6
```

#### Output:
```
28
```

#### Giải thích:
Mỗi bước chỉ nối tối đa được 2 đoạn:
- Nếu ta nối \(8\) với \(4\), tổng chi phí là \(8 + 4 = 12\). Sau khi nối xong còn 2 đoạn độ dài \(12\) và \(6\).
- Nối \(12\) và \(6\), tổng chi phí nối là \(12 + 6 = 18\).

Tổng chi phí nối là \(12 + 18 = 30\). Nếu ta nối \(4\) với \(6\) trước, tốn \(10\), và \(8\) nối lại với nhau tốn \(18\), tổng chi phí ít hơn chỉ còn \(28\).

---

### Ví dụ 2:

#### Input:
```
6 3
8 2 1 5 2 3
```

#### Output:
```
39
```

#### Giải thích:
- **Bước 1:** Lắp các đoạn \(1 + 2 + 2\), tốn \(5\). Bây giờ sẽ giảm đi \(1, 2, 2\) và thêm vào đoạn \(6\), nên còn các đoạn \(8, 5, 3, 5\).
- **Bước 2:** Lắp các đoạn \(5 + 3 + 5\), tốn \(13\). Bây giờ sẽ giảm đi \(5, 3, 5\) và thêm vào đoạn \(13\), nên còn các đoạn \(8, 13\).
- **Bước 3:** Lắp nốt \(8 + 13\), tốn \(21\).

Tổng chi phí: \(5 + 13 + 21 = 39\).