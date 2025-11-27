# Khối lượng hóa chất

## Đề bài

Một chất hữu cơ chỉ gồm các nguyên tố hóa học C, H, O có khối lượng phân tử tương ứng C=12, H=1, O=16.
Ví dụ Axit capric có công thức CH3-CH2-CH2-CH2-CH2-CH2-CH2-CH2-COOH ở dạng rút gọn CH3(CH2)8COOH.
Bài toán đặt ra là cho một công thức ở dạng rút gọn bạn hãy tính khối lượng hóa chất đó biết rằng số rút gọn chỉ nằm trong khoản [2,9].

---

## Input

- Dòng đầu là số trường hợp kiểm thử `t` (1 ≤ t ≤ 10).
- Mỗi trường hợp kiểm thử là một xâu ký tự trên một dòng chỉ gồm các ký tự `C`, `H`, `O`, `(`, `)` và các số trong đoạn [2,9] có độ dài không vượt quá 500 ký tự.

---

## Output

- Với mỗi công thức tính khối lượng của hóa chất đó là số tự nhiên có giá trị không vượt quá \(10^9\) xuất ra trên từng dòng.

---

## Ví dụ:

### Input:
```
2
((CHOH)2(CO2H)2H2O)4
CH3((CHCO2H)2(CH2)8CO2H)3H2CO3H
```

### Output:
```
672
897
```