# Làm Bóng Tuyết

## Đề bài

Mùa đông đã tới, Alice rất thích làm cầu tuyết nên mỗi ngày Alice sẽ làm 1 quả để chơi. Nhưng không may mùa đông vẫn chưa tới hẳn nên nhiệt độ sẽ làm những quả bóng tuyết của Alice bị tan chảy. Cụ thể trọng lượng của quả cầu tuyết tại ngày thứ \(i\) là \(V[i]\) và nhiệt độ của ngày thứ \(i\) là \(T[i]\) thì quả cầu sẽ bị tan chảy 1 lượng đúng bằng \(T[i]\) (lúc này \(V[i] - T[i]\)). Do có thể nhiệt độ 1 ngày không thể làm tan luôn quả cầu nên có thể quả cầu vẫn còn tồn tới hôm sau và khối lượng quả cầu tiếp tục giảm đi đúng bằng với nhiệt độ các ngày sau đó.

Bạn được cho biết số ngày mà Alice sẽ làm các quả cầu và nhiệt độ các ngày. Nhiệm vụ của bạn là hãy xác định khối lượng tan chảy của các quả cầu tuyết theo các ngày.

---

## Input

- Dòng đầu chứa số nguyên \(n\) là số ngày mà Alice sẽ làm quả cầu \((1 \leq n \leq 100000)\).
- Dòng thứ 2 chứa \(n\) số nguyên là trọng lượng của các quả cầu mà Alice sẽ làm \((1 \leq V[i] \leq 1000000000)\).
- Dòng thứ 3 chứa \(n\) số nguyên là nhiệt độ của các ngày \((1 \leq T[i] \leq 1000000000)\).

---

## Output

- In ra một dòng duy nhất với \(n\) số nguyên, số thứ \(i\) là trọng lượng bị tan chảy tại ngày thứ \(i\).

---

## Ví dụ:

### Input:
```
3
10 10 5
5 7 2
```

### Output:
```
5 12 4
```

### Giải thích:
- Ngày đầu quả cầu đầu tiên sẽ tan chảy 5kg và còn lại 5kg.
- Ngày thứ hai quả cầu thứ hai sẽ tan chảy 7kg cộng với 5kg còn lại tại ngày thứ nhất nên tổng tan chảy là 12kg.
- Ngày thứ ba tương tự.