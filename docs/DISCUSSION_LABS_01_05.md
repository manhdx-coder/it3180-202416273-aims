# TRẢ LỜI CÂU HỎI THẢO LUẬN – LAB 01 ĐẾN LAB 05

# LAB 01 – GIT CƠ BẢN VÀ BASELINE

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

- **Vị trí lưu trữ**: Cấu hình `--global` được lưu tại tệp `~/.gitconfig` trong thư mục Home của người dùng. Cấu hình `--local` được lưu tại `.git/config` bên trong thư mục gốc của repository cụ thể.
- **Khác biệt**: Cấu hình `--global` áp dụng cho mọi kho Git trên máy tính của người dùng nếu kho đó chưa có cấu hình riêng. Cấu hình `--local` chỉ áp dụng riêng cho repository hiện hành và có quyền ưu tiên cao hơn, ghi đè cấu hình `--global`.

## 2. Vì sao dùng `git mv` thay vì di chuyển tệp thủ công?

- `git mv` thực hiện đồng thời việc di chuyển tệp trên hệ thống tệp và tự động đưa thay đổi vào Staging Area (tương đương chuỗi lệnh di chuyển + `git rm` tệp cũ + `git add` tệp mới).
- Giúp Git nhận diện tường minh trạng thái đổi tên (`renamed`) thay vì báo xóa tệp cũ và tạo một tệp mới không liên quan.
- Bảo toàn tính liên tục của lịch sử commit, cho phép dùng `git log --follow -- <tệp>` để truy vết xuyên suốt qua các lần tái cấu trúc.

## 3. Nhánh `release/lab01` có phải là baseline không?

- **Có**. Theo định nghĩa SCM, Baseline là cấu hình đã được kiểm tra, thống nhất và đóng băng tại một mốc nhất định, chỉ được thay đổi qua quy trình chính thức.
- Nhánh `release/lab01` (và tag `v0.1.0`) đại diện cho sản phẩm bàn giao hoàn chỉnh của Lab 01, đóng vai trò là mốc chuẩn để đánh giá và làm nền tảng cho các lab tiếp theo.

## 4. Vì sao không commit thẳng vào `master` dù làm một mình?

- Rèn luyện kỷ luật Release Flow chuẩn công nghiệp phần mềm.
- Cách ly các thay đổi đang thử nghiệm sang nhánh riêng (`refactor/*`, `feature/*`), giữ cho nhánh `master` luôn ổn định và có thể chạy được.
- Đảm bảo mọi thay đổi đều được ghi nhận mục đích, diff và kiểm thử qua PR template và checklist nghiệm thu.
- Tuân thủ chính sách bảo vệ nhánh (Branch Protection) trên remote vốn cấm push trực tiếp.

---

# LAB 02 – BRANCHING VÀ PULL REQUEST

## 1. Vì sao phải đồng bộ `master` trước khi gửi Pull Request?

- **Đảm bảo tính tương thích tích hợp**: Kiểm tra mã nguồn tính năng mới chạy ăn khớp với những cập nhật mới nhất vừa được đưa vào `master` (ví dụ: Dev 2 kiểm tra hàm tìm kiếm với giỏ hàng đã có `print_cart`).
- **Phát hiện và xử lý xung đột sớm**: Cho phép lập trình viên tự giải quyết xung đột (conflict resolution) và chạy kiểm thử an toàn trên máy cục bộ trước khi chuyển cho reviewer.
- **Giữ PR rõ ràng**: Giúp giao diện so sánh PR trên GitHub chỉ hiển thị đúng các commit và thay đổi mới của tính năng, hỗ trợ review nhanh chóng.

## 2. Khi nào không được dùng `rebase`?

- **Quy tắc vàng của Git**: Không nên dùng `rebase` trên các nhánh công khai hoặc dùng chung (như `master`, `release/*`, hoặc nhánh tính năng có nhiều người cùng tham gia).
- **Nguyên nhân**: `rebase` tạo ra các commit hoàn toàn mới với mã SHA mới (viết lại lịch sử). Nếu nhánh đã chia sẻ bị rebase sẽ làm sai lệch đồ thị Git của các thành viên khác, gây phân mảnh và xung đột nghiêm trọng khi pull/push.

## 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?

- `feature/*`: Dùng để phát triển các tính năng nghiệp vụ cụ thể phục vụ trực tiếp người dùng cuối (ví dụ: `feature/cart-print`, `feature/search-by-title`, `feature/discount`).
- `topic/*`: Dùng cho các công việc liên quan đến hạ tầng kỹ thuật, tài liệu, quy trình hoặc cấu hình nội bộ mà không phải tính năng nghiệp vụ (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/prepare-release-1.0.0`).

---

# LAB 03 – MERGE, CONFLICT VÀ HOÀN TÁC

## 1. Merge base là gì?

- Merge base là commit tổ tiên chung gần nhất (best common ancestor) giữa hai nhánh trong đồ thị commit của Git.
- Khi hòa nhập nhánh (merge), Git dùng thuật toán 3-way merge để so sánh 3 điểm: commit đỉnh nhánh hiện tại, commit đỉnh nhánh được merge và commit merge base.
- Nhờ đó Git nhận biết chính xác phần nào đã thay đổi ở mỗi nhánh để tự động hợp nhất hoặc phát hiện xung đột nếu cả hai cùng sửa một vùng mã.

## 2. Vì sao trên nhánh dùng chung (`master`, `release/*`) phải dùng `revert` thay vì `reset`?

- `git reset` dời con trỏ nhánh về quá khứ và thay đổi lịch sử nhánh. Khi đã push lên remote, đưa trạng thái `reset` lên thường bắt buộc phải dùng `--force`, điều này có thể phá hỏng lịch sử của người khác và bị Branch Protection chặn.
- `git revert` tạo một commit mới đảo ngược các thay đổi của commit cũ mà không làm thay đổi các commit trước đó.
- Nhờ vậy, toàn bộ lịch sử được bảo toàn nguyên vẹn, minh bạch, đảm bảo truy vết kiểm toán và an toàn để áp dụng qua Pull Request.

---

# LAB 04 – RELEASE FLOW VÀ SEMANTIC VERSIONING

## 1. Vì sao `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.

- **Lý do không merge ngược**: Nhánh `release/*` là baseline phát hành cố định đã tách ra từ `master`, trong khi `master` liên tục tiến về phía trước để phát triển tính năng mới. Merge ngược cả nhánh release vào `master` có nguy cơ đưa các thay đổi chỉ dành cho phiên bản cũ vào nhánh phát triển hiện tại hoặc gây xung đột diện rộng. Khi cần sửa lỗi (hotfix), ta chỉ bốc tách riêng commit sửa lỗi bằng `git cherry-pick -x` đưa về `master`.
- **So sánh với GitFlow**:
  - *GitFlow*: Duy trì hai nhánh dài hạn (`main` và `develop`). Nhánh release khi hoàn thành thường được merge vào cả hai nhánh này.
  - *Release Flow*: Chỉ duy trì duy nhất một nhánh chính dài hạn là `master`. Nhánh `release/*` đóng băng baseline và không merge ngược toàn bộ vào `master`; các bản sửa lỗi cần thiết được lan truyền bằng cherry-pick.

## 2. Vì sao nâng lên phiên bản `1.0.0` mà không phải `0.4.0`?

- Theo Semantic Versioning (SemVer), dải `0.y.z` dành cho giai đoạn phát triển ban đầu khi API chưa ổn định.
- Tại Lab 04, dự án AIMS-mini đã hoàn thiện cấu trúc gói, giao diện dòng lệnh hoạt động, có `CHANGELOG.md` theo Keep a Changelog và có bộ kiểm thử `unittest` cho các chức năng đã triển khai.
- Phiên bản `1.0.0` đánh dấu bản phát hành ổn định đầu tiên (First Stable Release) của dự án.

## 3. Vì sao công tác chuẩn bị phát hành thực hiện trên `master` trước mà không sửa trên nhánh `release`?

- Nhánh `master` là nguồn chân lý duy nhất (Single Source of Truth).
- Nếu nâng phiên bản và viết `CHANGELOG.md` trên nhánh `release/*`, nhánh `master` sẽ không có những thông tin này, dẫn đến thiếu đồng bộ lịch sử hoặc gây xung đột khi tạo các nhánh release tiếp theo (`release/lab05`).
- Chuẩn bị trên `master` trước giúp các nhánh release kế thừa trạng thái hoàn thiện nhất tại thời điểm tạo nhánh.

---

# LAB 05 – HOTFIX VÀ LAN TRUYỀN BẢN SỬA LỖI

## 1. Ưu, nhược điểm của mô hình Upstream First so với Release First?

- **Release First (Làm hotfix từ nhánh release cũ rồi cherry-pick về master)**:
  - *Ưu điểm*: Phát hành bản vá khẩn cấp nhanh nhất cho người dùng đang gặp sự cố trên production mà không phụ thuộc vào trạng thái đang phát triển của `master`.
  - *Nhược điểm*: Dễ quên lan truyền bản sửa lỗi về `master` hoặc các nhánh release kế tiếp, dẫn đến hiện tượng hồi quy lỗi (regression) ở các phiên bản sau.

- **Upstream First (Sửa trên master trước rồi cherry-pick sang nhánh release)**:
  - *Ưu điểm*: Đảm bảo mã nguồn chính luôn có giải pháp chuẩn và đầy đủ nhất; không bị sót lỗi khi phát triển các bản phát hành tương lai.
  - *Nhược điểm*: Khi nhánh `master` đã thay đổi kiến trúc quá nhiều so với bản phát hành cũ, việc cherry-pick ngược về nhánh release có thể gặp các xung đột phức tạp.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Có thể sử dụng hai cách kiểm tra:

**Cách 1: Kiểm tra hành vi thực tế trên từng phiên bản**

```bash
for ref in v1.0.1 v1.1.0 master; do
    echo "=== $ref ==="
    git switch --detach "$ref"
    python -c "from aims.dvd import DigitalVideoDisc as D; from aims.cart import Cart; from aims.search import search_by_title; c=Cart(); c.items=[D('The Lion King')]; print(len(search_by_title(c, 'lion')))"
done
git switch master
```

- Nếu phiên bản đã có bản sửa, kết quả tìm kiếm phải trả về `1`.
- Nếu phiên bản chưa có bản sửa và vẫn còn lỗi phân biệt chữ hoa/chữ thường, kết quả sẽ là `0`.
- Nếu quên lan truyền sang `release/lab05`, tag `v1.1.0` sẽ cho kết quả `0`, trong khi `v1.0.1` và `master` cho kết quả `1` (theo kịch bản giả định của bài thực hành).

**Cách 2: Kiểm tra lịch sử cherry-pick**

```bash
git log --all --grep="cherry picked from commit <FIX_SHA>"
```

- Lệnh này tìm các commit có nội dung truy vết được Git tự động thêm khi sử dụng `git cherry-pick -x`.
- Nếu thiếu một commit lan truyền, kết quả sẽ không hiển thị đầy đủ các lần cherry-pick như mong đợi.
- Có thể dùng cách này để kiểm tra lịch sử lan truyền bản sửa giữa các nhánh.

