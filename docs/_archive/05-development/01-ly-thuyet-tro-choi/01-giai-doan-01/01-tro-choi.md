---
title: "tro choi"
description: "Trò chơi là gì - người chơi, chiến lược, payoff, luật chơi, ví dụ và khi nào không phải trò chơi"
sidebar_position: 1
tags: [game-theory]
---

# tro choi

## Trò Chơi Là Gì?

### Trực Giác

Ở bất kỳ tình nào mà kết quả nhận được phụ thuộc vào

- Lựa chọn của bạn
- Lựa chọn của người khác
- Cả hai điều biết điều đó

Ví dụ

- Quyết định mang áo mưa &rarr; Không phải
- Quyết định giá bán khi quán đối diện đang tính giá &rarr; Phải

### Định Nghĩa

Một trò chơi dạng chuẩn gồm 3 thành phần 

- Người chơi `N = {1, 2, ..., n}`: những bên ra quyết định có chủ đích
- Tập chiến lược `Sᵢ` của mỗi người chơi `i`: mọi phương án người đó có thể chọn
- Hàm payoff `uᵢ(s₁, …, sₙ)`: mức độ người chơi `i` đánh giá mỗi tổ hợp lựa chọn của tất cả mọi người
    - Payoff của bạn là hàm của cả chiến lược người khác

## Luật Chơi Là gì?

Phần ngầm định

- Ai đi trước, sau
- Ai biết gì vào lúc nào, có được giao tiếp hay cam kết không

Thay luật thì trò chơi đổi, dù người chơi và phương án giữ nguyên

## Ví Dụ Cụ Thể

Đời thường: Đi ăn nhóm, chia đều hoá đơn

- Người chơi: 6 người bạn
- Chiến lược của mỗi người: Gọi món rẻ hoặc món đắt
- Payoff: Độ ngon trừ đi số tiền phải trả
- Luật chơi
    - Vì chia đều, nếu bạn gọi món đắt hơn 60k thì bạn chỉ chịu 10k, 50k còn lại chia đều cho 5 người kia
    - Nếu "ai gọi nấy trả" thì sự phụ thuộc lẫn nhau biến mất

Lịch sử: Khủng hoảng tên lửa Cuba, 1962

- Người chơi: Mỹ và Liên Xô
- Các chiến lược có thể
    - Mỹ: Không làm gì, phong toả hải quân, không kích, etc.
    - Liên Xô: Rút tên lửa, giữ nguyên, leo thang, etc.
- Payoff: An ninh, uy tín quốc, vị thế chính trị trong nước
- Luật chơi: Các nước đi tuần tự, thông tin không đầy đủ và có kênh liên lạc bí mật
- Kết quả: Nước đi phụ thuộc vào mỗi bên đọc bên kia thế nào

## Ranh Giới - Không Phải Là Trò Chơi

Khi đối phương là tự nhiên hoặc hệ thống không có chủ đích

- Ví dụ: Ổ đĩa sắp chết, hay bug gây memory leak không đoán bạn làm gì &rarr; Lý thuyết quyết định

Khi bạn quá nhỏ để ảnh hưởng người khác

- Mua 1kg gạo ở chở, giá không đổi vì bạn &rarr; Kinh tế học thị trường
 
Khi không xác định được người chơi muốn gì

- Nếu hành vi là do thói quen, cảm xúc, hỗn loạn &rarr; Tâm lý học hoặc xã hội học

## Hiểu Lầm

Lý thuyết trò chơi giả định con người ích kỷ và chỉ quan tâm tiền &rarr; Sai

- Payoff có thể bất cứ gì: Tiền, danh dự, sĩ diễn, lòng tốt, mối quan hệ lâu dài, cảm giác công bằng
- Ví dụ
    - Một người mẹ nhường phần ăn cho con không phi lý
    - Payoff của bà đơn giản là bao gồm hạnh phúc của con
- &rarr; Họ thực sự muốn gì?

## Kiểm Tra

```text
Mỗi sáng ở TP.HCM, bạn chọn đi làm lúc 7h00 hay 7h30 để tránh kẹt xe. Đây có phải là một trò chơi không? Nếu có, hãy chỉ ra người chơi, chiến lược, payoff và luật chơi. Nếu không, hãy giải thích nó thuộc loại bài toán nào
```

| Cấp độ | Nên coi là gì | Vì sao |
| :--- | :--- | :--- |
| **Bạn, một cá nhân** | Bài toán quyết định (xấp xỉ) | Bạn quá nhỏ để ảnh hưởng người khác |
| **Cả dân số người đi làm** | Trò chơi nhiều người chơi, gọi là congestion game | Payoff mỗi người phụ thuộc vào số người chọn cùng giờ, cùng đường |

Ở cấp độ dân số thì:

- Người chơi: Toàn bộ người đi làm trên cùng tuyến
- Chiến lược: Giờ xuất phát và tuyến đường
- Payoff: Thời gian di chuyển (âm) trừ thêm phần phạt nếu đến muộn
- Luật chơi: Mọi người quyết định gần như đồng thời, không giao tiếp được với nhau, và chỉ học được từ kinh nghiệm những ngày trước
