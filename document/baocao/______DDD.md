<!--@yêu cầu nghiệp vụ-->

trình bày nội dung yêu cầu nghiệp vụ

<!--@Chi tiết và áp dụng thiết kế hướng miền-->
<!--@Đôi nét về thiết kế hướng miền-->
<!--@Thiết kế hướng miền là gì?-->

Thiết kế hướng miền được Eric Evans giới thiệu trong cuốn sách “DomainDrivenDesign: Tackling Complexity in the Heart of Software”.

Thiết kế hướng miền là một phương pháp thiết kế phần mềm tập trung vào việc hiểu và mô hình hóa lĩnh vực kinh doanh của một tổ chức.

Thiết kế hướng miền nhấn mạnh việc sử dụng lĩnh vực nghiệp vụ kinh doanh để thảo luận và đề xuất giải pháp đáp ứng nhu cầu. Vì để tạo ra một phần mềm tốt, bạn cần phải hiểu rõ về chính phần mềm đó. Chính vì vậy mà để đạt được kết quả như mong đợi, chúng ta thường bắt đầu từ yêu cầu nghiệp vụ.

Trong ứng dụng điển hình khó tương thích với lập trình hướng đối tượng vì có nhiều phần code xử lý các công việc không liên quan đến vấn đề nghiệp vụ như truy cập file, hạ tầng mạng, CSDL, ... được nhúng trực tiếp vào đối tượng nghiệp vụ kinh doanh. Cách này giúp tốc độ hoàn thiện ứng dụng nhanh. Tuy nhiên, cách này làm cho thiết kế bị mất đi tính hướng đối tượng trong thực tế với mức độ doanh nghiệp lớn. Đây là lý do thiết kế hướng miền trở nên quan trọng.

Trong kiến trúc vi dịch vụ, thiết kế hướng miền giúp đảm bảo rằng mỗi dịch vụ được thiết kế phản ánh một phần cụ thể của lĩnh vực kinh doanh. Mỗi dịch vụ được quản lí bởi một nhóm nhỏ được hỗ trợ bởi các chuyên gia ngành.

<!--@Miền (Domain)-->

Phần mềm được tạo ra để giúp xử lý sự phức tạp trong cuộc sống hiện đại. Việc phát triển phần mềm liên kết chặt chẽ với một số khía cạnh cụ thể trong cuộc sống của chúng ta.

Miền đề cập đến phạm vi kiến thức và vấn đề mà hệ thống hoặc dự án cụ thể đang xử lý.

Về góc độ kinh doanh: miền đại diện cho một lĩnh vực hoặc ngành mà doanh nghiệp hoạt động.
Về góc độ phần mềm: miền có thể coi là đại diện cho không gian vấn đề của phần mềm đó.

Phần mềm cần phản ánh đúng miền và hiện thực hóa chính xác miền.

<!--$VD: Ở đồ án này, miền được xác định là bài toán giải pháp hóa đơn điện tử .-->

<!---->
<!--Trong một miền phức tạp, không thể có một chuyên gia duy nhất có kiến thức tổng thể về tất cả các miền phụ.-->
<!--Phần mềm cần phản ánh đúng miền và hiện thực hóa một cách chính xác quan hệ giữa các miền.-->

<!--@Tên miền phụ (Sub-Domain)-->
Tên miền được tạo thành từ nhiều tên miền phụ.


Một miền doanh nghiệp bao gồm nhiều tên miền phụ.
Có nhiều yếu tố khác nhau góp phần tạo nên sự phức tạp của tên miền phụ.

<!--@Phân loại các tên miền phụ.-->

Có ba loại tên miền phụ:

<!--@Tên miền phụ chung (Generic Subdomain)**-->

Tên miền phụ chung cung cấp các giải pháp có sẵn mà doanh nghiệp có thể mua.

Không có gì đặc biệt về những tên miền phụ này và các phương pháp tốt nhất đã sẵn có cho những tên miền này.

Doanh nghiệp không thể đạt được bất kỳ lợi thế cạnh tranh nào bằng cách thực hiện những điều khác biệt trong tên miền phụ chung.

<!--$VD:-->

Ví dụ về các tên miền phụ như vậy là quản lý nguồn nhân lực và cơ sở vật chất. Vì vậy, bất kỳ ngành nào hoặc doanh nghiệp nào, các hoạt động quản lý nhân sự và quản lý cơ sở vật chất đều khá trưởng thành và không tạo thêm bất kỳ giá trị khác biệt nào cho doanh nghiệp.

<!--@Tên miền phụ cốt lõi (Core Subdomain)**-->

Tên miền phụ cốt lõi là điểm khác biệt quan trọng cho doanh nghiệp.

Mỗi doanh nghiệp trong một ngành cụ thể hoạt động khác nhau trong các tên miền phụ cốt lõi để đạt được một số lợi thế so với đối thủ cạnh tranh.

Thành công của một doanh nghiệp nằm ở tên miền phụ cốt lõi.

Doanh nghiệp luôn tìm cách thực hiện những điều khác biệt trong các tên miền phụ cốt lõi này để có được một số lợi thế cạnh tranh.

<!--$VD:-->

<!--@Tên miền phụ hỗ trợ (Supporting Subdomain)**-->

Các tên miền phụ cốt lõi phụ thuộc vào các tên miền phụ hỗ trợ.

Tên miền phụ hỗ trợ cung cấp các dịch vụ để tên miền phụ cốt lõi hoạt động hiệu quả.

Tên miền phụ hỗ trợ không có mức độ phức tạp cao về logic nghiệp vụ.

<!--$VD:-->
<!--phụ thuộc rất nhiều vào bộ phận hỗ trợ khách hàng-->
<!---->
<!---->
<!---->
<!--@Xác định các tên miền phụ-->

Sơ đồ:
![](pictures/XacDinhTenMienPhu/_XacDinhTenMienPhu.png)

Diễn giải:
Bắt đầu bằng cách xem xét nghiệp vụ kinh doanh.

Nếu có sẵn giải pháp đã biết thì có khả năng là Tên miền phụ chung. Ngược lại, nghiệp vụ đó thêm bất kỳ giá trị kinh doanh nào không.

Nếu không có giá trị kinh doanh thì kiểm tra xem các tên miền phụ cốt lõi có phụ thuộc vào tên miền phụ này hay không? Và câu trả lời đó là có thì có khả năng là tên miền phụ hỗ trợ. Nếu câu trả lời là không thì đó là tên miền phụ chung.

Nếu tên miền phụ có tiềm năng bổ sung một số giá trị kinh doanh thì bước kiểm tra tiếp theo là xem liệu tên miền doanh nghiệp có độ phức tạp cao hay không?

Nếu miền doanh nghiệp không có độ phức tạp cao thì có khả năng là tên miền phụ hỗ trợ. Nếu không thì nó có khả năng là tên miền phụ cốt lõi.

<!--$VD: Sau khi phân tích em có cccccccc-->

<!--Tại sao cần phân loại các tên miền phụ?-->

Việc phân loại tên miền phụ giúp doanh nghiệp đưa ra quyết định với từng loại tên miền phụ khác nhau.

Doanh nghiệp có nguồn lực hạn chế như nguồn nhân lực và kinh phí dành cho các sáng kiến. Việc phân loại các tên miền phụ giúp ưu tiên các sáng kiến khác nhau.

Các doanh nghiệp mong muốn tối đa hóa lợi nhuận đầu tư. Do đó, các sáng kiến liên quan đến tên miền phụ cốt lõi sẽ được ưu tiên.

<!--$VD:-->
<!--Hướng dẫn: 5/3-->

<!--@Bối cảnh giới hạn (Bounded Context)-->

<!--@Mô hình miền (Domain model)-->
