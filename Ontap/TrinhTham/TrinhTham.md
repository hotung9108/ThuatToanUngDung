# Trinh Thám

## Đề bài

Amas là một sinh viên mới vào học tại ĐHGTVT năm thứ nhất. Kết thúc học kỳ 1, Amas được tham gia một học kỳ quân sự. Hôm nay, lớp học của Amas được chia làm 2 phía chiến trường và tổ chức tập trận, Amas tham gia bên phía quân xanh có nhiệm vụ di trinh thám quân đỏ huấn luyện. Amas leo lên một quả đồi và sử dụng ống nhòm để quan sát thì phát hiện ra quân đỏ đang dàn hàng ngang để tập luyện, khối nổi đồng nhòm nhỏ nên mỗi khung nhìn chỉ quan sát được một số lính liên tiếp của quân đỏ. Nhiệm vụ trinh thám lần này là tìm ra chiều cao cao nhất của đối phương, để làm được điều đó rất khó nên phải quan sát dần dần lần lượt từ đầu đến cuối của hàng bằng cách dịch khung nhìn lần lượt mỗi lần tiến lên một đơn vị.

Bài toán đặt ra với Amas là với \(n\) quân đỏ có chiều lượt là \(a_1, a_2, \ldots, a_n\), khung nhìn có khoảng rộng là \(1 \leq k \leq n\). Khi dịch khung nhìn lần lượt từ đầu đến cuối thì với từng vị trí khung nhìn phải tìm ra chiều cao của quân đỏ cao nhất trong khung nhìn đó.

---

## Input

- Dòng đầu chứa 2 số \(n\) là số quân đỏ \((1 \leq n \leq 10^5)\) và \(k\) là khung nhìn của ống nhòm \((1 \leq k \leq n)\) (số quân đỏ tối đa mà một lần ống nhòm quan sát được).
- Dòng thứ 2 chứa \(n\) số nguyên là chiều cao của quân đỏ theo đơn vị chiều cao \((1 \leq a_i \leq 10^4)\).

---

## Output

- Kết quả đầu ra gồm \(n-k+1\) số nguyên là chiều cao của quân đỏ cao nhất trong từng khung nhìn.

---

## Ví dụ:

### Input:
```
8 3
4 7 2 5 6 3 9 1
```

### Output:
```
7 7 6 6 9 9
```

### Giải thích:
Lần lượt khung nhìn duyệt qua 3 phần tử một lần:
- \(\max(4, 7, 2)\),
- \(\max(7, 2, 5)\),
- \(\max(2, 5, 6)\),
- \(\max(5, 6, 3)\),
- \(\max(6, 3, 9)\),
- \(\max(3, 9, 1)\).