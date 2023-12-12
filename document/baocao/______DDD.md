<!--@Chi tiết và áp dụng thiết kế hướng miền-->
<!-- @Đôi nét về    thiết kế hướng miền -->
<!--@Thiết kế hướng miền là gì?-->

Thiết kế hướng miền được Eric Evans giới thiệu trong cuốn sách “DomainDrivenDesign: Tackling Complexity in the Heart of Software”.

Thiết kế hướng miền là một phương pháp thiết kế phần mềm tập trung vào việc hiểu và mô hình hóa lĩnh vực kinh doanh của một tổ chức.

Thiết kế hướng miền nhấn mạnh việc sử dụng lĩnh vực nghiệp vụ kinh doanh để thảo luận và đề xuất giải pháp đáp ứng nhu cầu. Vì để tạo ra một phần mềm tốt, bạn cần phải hiểu rõ về chính phần mềm đó. Chính vì vậy mà để đạt được kết quả như mong đợi, chúng ta thường bắt đầu từ yêu cầu nghiệp vụ.

Trong ứng dụng điển hình khó tương thích với lập trình hướng đối tượng vì có nhiều phần code xử lý các công việc không liên quan đến vấn đề nghiệp vụ như truy cập file, hạ tầng mạng, CSDL, ... được nhúng trực tiếp vào đối tượng nghiệp vụ kinh doanh. Cách này giúp tốc độ hoàn thiện ứng dụng nhanh. Tuy nhiên, cách này làm cho thiết kế bị mất đi tính hướng đối tượng trong thực tế với mức độ doanh nghiệp. Đây là lý do thiết kế hướng miền trở nên quan trọng.

Trong kiến trúc vi dịch vụ, thiết kế hướng miền giúp đảm bảo rằng mỗi dịch vụ được thiết kế phản ánh một phần cụ thể của lĩnh vực kinh doanh. Mỗi dịch vụ được quản lí bởi một nhóm nhỏ được hỗ trợ bởi các chuyên gia ngành.
<!--@Miền (Domain)-->

Phần mềm được tạo ra để giúp xử lý sự phức tạp trong cuộc sống hiện đại. Việc phát triển phần mềm liên kết chặt chẽ với một số khía cạnh cụ thể trong cuộc sống của chúng ta.

Miền đề cập đến phạm vi kiến thức và vấn đề mà hệ thống hoặc dự án cụ thể đang xử lý.

Về góc độ kinh doanh: miền đại diện cho một lĩnh vực hoặc ngành mà doanh nghiệp hoạt động.
Về góc độ phần mềm: miền có thể coi là đại diện cho không gian vấn đề của phần mềm đó.

Phần mềm cần phản ánh đúng miền và hiện thực hóa chính xác miền.

<!--$VD: Ở đồ án này, miền được xác định là bài toán giải pháp hóa đơn điện tử .-->

<!--@miền (Domain) là gì?-->

là vấn đề
là giải pháp
của dự án
của nghiệp vụ kinh doanh

<!--@Tên miền phụ (Sub-Domain) là gì?-->

<!--@Bối cảnh giới hạn (Bounded Context)-->

<!--@Mô hình miền (Domain model)-->

