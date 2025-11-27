# Chào đón K59

## Giới thiệu

Nhân dịp chào đón các tân sinh viên K59 Đại học Giao thông vận tải, Nhà trường tổ chức các trò chơi trí tuệ cho các tân sinh viên có một tinh thần thật thoải mái trước khi bước vào năm học. Trò chơi thú vị này có luật chơi như sau:

Có tất cả n sinh viên tham dự, xếp thành một hàng và mỗi bạn được đánh số từ 0 đến n - 1. Sau khi chỉ định bất kỳ bạn nào, bạn đó sẽ phải chỉ ra chỉ số của bạn đứng gần mình nhất mà có chiều cao cao hơn mình. Nếu có nhiều chỉ số cùng thỏa mãn thì lấy chỉ số bé hơn, nếu không có ai cao hơn thì chỉ số đó sẽ là -1.

Để trò chơi diễn ra thuận lợi và công bằng, Thầy TichPX giao cho đội tuyển Olympic tin học UTC viết một chương trình nhập vào một dãy số nguyên a cho biết chiều cao của sinh viên ở từng chỉ số, và in ra dãy số nguyên khác thể hiện chỉ số cần tìm ở mỗi vị trí trong dãy ban đầu.

---

## Input

- Dòng đầu tiên là n thể hiện số sinh viên (1 ≤ n ≤ \(4 \cdot 10^4\)).
- Dòng thứ 2 bao gồm n số nguyên thể hiện chiều cao của n sinh viên. Số thứ i thể hiện chiều cao của sinh viên thứ i (0 ≤ i < n).

---

## Output

- Dòng duy nhất in ra n số nguyên. Số thứ i tương ứng là chỉ số của sinh viên gần nhất cao hơn sinh viên thứ i trong dãy đã cho.

---

## Ví dụ:

### Input:
```
6
1 4 2 1 7 6
```

### Output:
```
1 4 1 2 -1 4
```

### Chú ý:
- Nếu có nhiều chỉ số cùng thỏa mãn thì lấy chỉ số bé hơn, nếu không có ai cao hơn thì chỉ số đó sẽ là -1.