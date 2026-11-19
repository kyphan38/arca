# Diátaxis audit - 2026-11-19

Chưa sửa trang nào. Duyệt xong bảng này thì mới tách hoặc đổi trang.

Loại theo Diátaxis

- tutorial - bài học từng bước cho người mới, làm theo là xong
- how-to - các bước để làm một việc cụ thể
- reference - tra cứu: danh sách, bảng, lệnh, con số
- explanation - giải thích vì sao, cơ chế hoạt động

Lưu ý: repo này là note học (Problem, How It Works, Traps, Questions). Phần lớn note học sẽ rơi vào explanation. Đó là bình thường, không cần tách chỉ để cho đủ 4 loại.

## 1. Bảng phân loại

| Trang | Loại chính | Loại phụ | Đề xuất |
| --- | --- | --- | --- |
| `00-introduction/index.md` | landing (không thuộc 4 loại) | - | Giữ. Có thể thêm link tới các chủ đề chính |
| `00-introduction/study-method.md` | how-to | explanation (Nguyên Tắc), reference (Các Skill) | Giữ một trang. Là trang hướng dẫn chính, tách ra sẽ khó đọc lại |
| `01-foundations/leetcode/01` đến `06`, `08` | reference | - | Giữ. Bảng bài tập là tra cứu |
| `01-foundations/leetcode/07`, `09` đến `20` | trống (chỉ có H1) | - | 13 trang trống. Chuyển vào `_archive/` hoặc để đó tới khi học tới |
| `02-technologies/aws/00-map.md` | reference (theo dõi tiến độ) | - | Giữ |
| `02-technologies/aws/13-.../sqs-dead-letter-queues.md` | explanation | reference (Exam Traps) | Giữ. Đúng format note mẫu |
| `02-technologies/docker/01-fundamentals.md` | explanation | reference (Daily Commands, restart policy), how-to (Practical Redis Setup) | Nên tách: `docker-architecture` (explanation), `docker-commands` (reference). Redis setup thành how-to ngắn hoặc gộp vào commands |
| `02-technologies/docker/02-images.md` | explanation | reference (Best Practices) | Giữ. Dài 106 dòng, gấp đôi mức 40 dòng - có thể tách `image-layers` và `image-storage` |
| `02-technologies/linux/01-ssh/main.md` | explanation | - | Giữ loại. Đổi tên file (xem mục 3) |
| `02-technologies/security/01-foundations.md` | explanation | reference (bảng STRIDE) | Giữ |
| `03-guides/vim.md` | reference | - | Folder tên `guides` (how-to) nhưng trang là bảng tra cứu. Cân nhắc đổi folder thành `03-tools` hoặc `03-cheatsheets` |
| `04-interviews/placeholder.md` | trống | - | Chuyển vào `_archive/` hoặc thay bằng note thật |
| `05-development/.../01-tro-choi.md` | explanation | tutorial nhẹ (phần Kiểm Tra) | Giữ |
| `05-development/.../02-hop-ly-va-common-knowledge.md` | explanation | - | Chưa xong - dừng ở `### Định Nghĩa` trống |

Tổng: 32 trang - 7 explanation, 9 reference, 1 how-to, 1 landing, 14 trang trống. Chưa có tutorial nào.

## 2. Ảnh sơ đồ - chọn cái nào đổi sang Mermaid

| # | Ảnh | Trong note | Nội dung | Đổi sang Mermaid? |
| --- | --- | --- | --- | --- |
| 1 | `docker/img/01/01.png` | docker fundamentals | CLI → dockerd → containerd → runc → kernel | Dễ - `flowchart TD` 5 ô |
| 2 | `docker/img/01/02.png` | docker fundamentals | Container = namespaces (7) + cgroups (2) | Được - `flowchart` với 2 subgraph |
| 3 | `docker/img/02/01.png` | docker images | tag → manifest → config blob + 3 layers | Dễ - `flowchart TD` |
| 4 | `docker/img/02/02.png` | docker images | Mỗi lệnh build → 1 layer diff | Dễ - `flowchart LR` 3 cặp |
| 5 | `docker/img/02/03.png` | docker images | OverlayFS stack → merged view | Được, nhưng mất phần chữ chú thích |
| 6 | `docker/img/02/04.png` | docker images | Tag mutable vs digest immutable | Được - 2 subgraph |
| 7 | `docker/img/02/05.png` | docker images | `docker image ls` vs dung lượng thật | Khó - đây là phép tính, bảng Markdown hợp hơn |
| 8 | `docker/img/02/06.png` | docker images | 3 container dùng chung lowerdir | Được - `flowchart TD` |
| 9 | `security/img/01/01.png` | security foundations | Luồng request qua Boundary A, B tới các service | Được - `flowchart TD` có subgraph cho mỗi vùng tin cậy |
| 10 | `guides/img/01.png` | vim | Bảng lệnh Vim (ảnh của linuxacademy.com) | Không - không phải sơ đồ. Thay bằng bảng lệnh tự viết thì tốt hơn |

Ghi chú: note docker images có 6 ảnh, quy tắc là tối đa 1 ảnh mỗi note. Đổi sang Mermaid cũng giúp giảm số ảnh.

## 3. Tên thư mục và trang

- `linux/01-ssh/main.md` - chỉ có một file trong folder và tên `main` không nói gì. Đề xuất `linux/01-ssh.md` hoặc `linux/01-ssh/ssh-protocol.md`
- `leetcode/08-recursion.md` - H1 và `title` là "recusion" (thiếu chữ r). Chưa sửa vì là nội dung của bạn
- `05-development/01-ly-thuyet-tro-choi` - tên tiếng Việt không dấu, các chủ đề khác tên tiếng Anh. Không sai lint, chỉ không đồng đều. Sidebar đã có nhãn có dấu qua `_category_.yml`
- `05-development` chứa lý thuyết trò chơi - tên folder gợi ý phát triển phần mềm. Cân nhắc đổi tên cho đúng nội dung

## 4. Đã quyết định và làm (2026-11-19)

- Mermaid: đổi ảnh 1, 2, 3, 4, 5, 6, 8, 9. Giữ ảnh 7 (phép tính, ảnh dễ đọc hơn) và ảnh 10 (không phải sơ đồ). Mỗi note còn tối đa 1 ảnh
- Tách `docker/01-fundamentals.md`: phần lệnh, quy tắc, Redis, restart policy chuyển sang `docker/03-commands.md` (reference). `01-fundamentals.md` còn kiến trúc, isolation, Alpine (explanation). Hai trang link qua lại
- `linux/01-ssh/main.md` → `linux/01-ssh.md`
- Sửa tiêu đề "recusion" → "recursion"
- Chưa làm: tách `docker/02-images.md`, đổi tên folder `03-guides` và `05-development`, xử lý 14 trang trống. Các việc này đổi URL hoặc cấu trúc chủ đề, để bạn quyết định sau
