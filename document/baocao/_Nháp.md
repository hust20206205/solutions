phân tán
dễ dàng nhìn nhận kiểm soát như youtube
Repository độc lập miền và lưu trữ sql (dễ tuhaajn tiện Unit testing and Mocking)
Repository trong ORM
https://images.viblo.asia/fd4b10a0-f1b1-4ed1-9bd1-578c871820ae.png
,gprc rabitmq đồng bộ hay k,ít hay nhiều như pub sub
Tuy nhiên, cộng động vẫn thiếu một tầm nhìn rõ
ràng về cách áp dụng hướng đối tượng ở mức độ doanh nghiệp. Đây là lý do tại sao tôi nghĩ DDD
trở nên quan trọng



# Service Mesh, CICD, microfe, API gateway , cache redis, log xử lí lỗi ,

<!--DDD-->001 Intro to Events in kiến trúc vi dịch vụ.en

Problem Space
Domain
Sub-Domains

<!---->

DDD là một cách tiếp cận để phát triển những phần mềm phức tạp thông qua sự kết nối chặt chẽ giữa việc triển khai ứng dụng với sự phát triển của mô hình kinh doanh.

<!--Problem Space / Business Domain: Không gian vấn đề / Lĩnh vực kinh doanh-->

Không gian vấn đề / Lĩnh vực kinh doanh là điểm khởi đầu của hành trình DDD và nó xác định vấn đề kinh doanh chính mà bạn dự định giải quyết bằng DDD.

<!--=> Đầu tiên ta cần phải xem xét yêu cầu nghiệp vụ đó là Không gian vấn đề / Lĩnh vực kinh doanh. Bất kì 1 ứng dụng phần mềm kĩ thuật cntt nào đều giải quyết cho 1 vấn đề yêu cầu cụ thể nào đó.-->

<!--Sub-Domains: Tên miền phụ-->

Việc xác định các miền phụ về cơ bản liên quan đến việc chia nhỏ các khả năng kinh doanh khác nhau của miền kinh doanh chính của bạn thành các đơn vị chức năng kinh doanh gắn kết.

<!--Ví dụ: Người dùng Sub-Domain, Thông báo Sub-Domain, Hóa đơn Sub-Domain-->

<!--Bounded Context: Bối cảnh bị ràng buộc là gì?-->

Bối cảnh bị giới hạn là giải pháp thiết kế cho Miền / Miền phụ doanh nghiệp đã được xác định của chúng tôi.

Việc xác định Bối cảnh bị ràng buộc chủ yếu được điều chỉnh bởi sự gắn kết mà bạn cần trong miền kinh doanh và giữa các miền phụ của bạn.

<!--Domain Model: Mô hình miền-->

Mô hình miền là việc triển khai logic nghiệp vụ cốt lõi
trong một Bối cảnh bị ràng buộc cụ thể.

Trong ngôn ngữ kinh doanh, điều này liên quan đến việc xác định:

- Thực thể kinh doanh (Business Entities)
- Quy tắc kinh doanh (Business Rules)
- Quy trình kinh doanh (Business Flows)
- Hoạt động kinh doanh (Business Operations)
- Sự kiện kinh doanh (Business Events)

Theo ngôn ngữ kỹ thuật trong thế giới DDD, điều này có nghĩa là xác định:

- Tổng hợp/Thực thể/Đối tượng giá trị (Aggregates/Entities/Value Objects)
- Quy tắc tên miền (Domain Rules)
- Sagas (Sagas)
- Lệnh/Truy vấn (Commands/Queries)
- Sự kiện (Events)
<!--=> bảng-->

<!--Aggregates/Entities/Value Objects-->

Tổng hợp là đối tượng kinh doanh trung tâm trong Bối cảnh bị ràng buộc của bạn và xác định phạm vi nhất quán trong bối cảnh bị ràng buộc đó.
Tổng hợp = Mã định danh chính của Bối cảnh bị ràng buộc của bạn

Đối tượng thực thể có bản sắc riêng nhưng không thể
tồn tại nếu không có tập hợp gốc, nghĩa là chúng
được tạo khi tập hợp gốc được tạo và bị hủy khi tập
hợp gốc bị phá hủy.

Đối tượng thực thể = Mã định danh phụ của Bối cảnh bị ràng buộc của bạn

<!--Đồ án 2-->

Dùng file readme ghi chép
Tạo các nội dung báo cáo
mônnithic
tct-demo
sơ đồ hình....
uml

<!--link tham khảo:-->

dấu .
dấu "
dấu space

<!--PTTKHT chuẩn bị-->
<!--crawl data-->

<!--Mục Lục:-->
<!--Căn cứ pháp lý-->

Thông tư 32/2011/TT-BTC: https://thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Thong-tu-32-2011-TT-BTC-huong-dan-ve-khoi-tao-phat-hanh-su-dung-hoa-don-dien-tu-120233.aspx

<!--https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=99887-->

Thông tư 78/2021/TT-BTC: https://thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-78-2022-TT-BTC-du-toan-ngan-sach-Nha-nuoc-2023-547888.aspx

<!--https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=204200-->

Nghị định 123/2020/NĐ-CP: https://thuvienphapluat.vn/van-ban/Ke-toan-Kiem-toan/Nghi-dinh-123-2020-ND-CP-quy-dinh-hoa-don-chung-tu-445980.aspx

<!--https://vanban.chinhphu.vn/?pageid=27160&docid=201365-->

<!---->

Bảng CSDL này được em thu thập dữ liệu từ trang web CƠ SỞ DỮU DANH MỤC DÙNG CHUNG (https://dmdc.mof.gov.vn/khai-thac-pb/co-quan-thue)

https://helpsme.misa.vn/2020/kb/quan-ly-hoa-don-dien-tu/

https://helpsme.misa.vn/2022/kb/quy-trinh-nghiep-vu-hddt-theo-nghi-dinh-123-2020-nd-cp/

https://www.meinvoice.vn/tin-tuc/3442/nhung-nghiep-vu-co-ban-cua-hoa-don-dien-tu-xac-thuc/

stt Bước

<!--PTTKHT chuẩn bị-->
<!--crawl data-->

<!--Mục Lục:-->
<!--Căn cứ pháp lý-->

Thông tư 32/2011/TT-BTC: https://thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Thong-tu-32-2011-TT-BTC-huong-dan-ve-khoi-tao-phat-hanh-su-dung-hoa-don-dien-tu-120233.aspx

<!--https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=99887-->

Thông tư 78/2021/TT-BTC: https://thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-78-2022-TT-BTC-du-toan-ngan-sach-Nha-nuoc-2023-547888.aspx

<!--https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=204200-->

Nghị định 123/2020/NĐ-CP: https://thuvienphapluat.vn/van-ban/Ke-toan-Kiem-toan/Nghi-dinh-123-2020-ND-CP-quy-dinh-hoa-don-chung-tu-445980.aspx

<!--https://vanban.chinhphu.vn/?pageid=27160&docid=201365-->

<!---->

Bảng CSDL này được em thu thập dữ liệu từ trang web CƠ SỞ DỮU DANH MỤC DÙNG CHUNG (https://dmdc.mof.gov.vn/khai-thac-pb/co-quan-thue)

https://helpsme.misa.vn/2020/kb/quan-ly-hoa-don-dien-tu/

https://helpsme.misa.vn/2022/kb/quy-trinh-nghiep-vu-hddt-theo-nghi-dinh-123-2020-nd-cp/

https://www.meinvoice.vn/tin-tuc/3442/nhung-nghiep-vu-co-ban-cua-hoa-don-dien-tu-xac-thuc/

<!--Thay thế = NULL-->
<!--Bị thay thế = NULL-->
<!--quy trình tương tự như lập mới hóa đơn giá trị gia tăng.-->
<!---->

<!--@Chú ý ở đồ án này:-->
<!--Sử dụng hàm ngẫu nhiên (tỉ lệ 10%) cho trường hợp "Mã số thuế không tồn tại."-->
<!--Sử dụng hàm ngẫu nhiên tạo tên cho Tên NNT vì em không có thông tin đăng ký thực tế của NNT.-->
<!--Sử dụng hàm ngẫu nhiên trong bảng CSDL cho "Mã cơ quan thuế quản lý" và "Tên cơ quan thuế quản lý"-->

Bảng CSDL này được em thu thập dữ liệu từ trang web CƠ SỞ DỮU DANH MỤC DÙNG CHUNG (https://dmdc.mof.gov.vn/khai-thac-pb/co-quan-thue)

<!--! Mã thuế số-chi nhánh-->
<!--Mã captcha không đúng.-->
<!--0107001729-->

dấu chấm cuối câu .
email=>Thư điện tử
Viết tắt NNT...

<!--Validtae-->

Điều kiện

<!---->

Chỉ dùng 1 loại hóa đơn vì em thấy tương tự.
Loại hóa đơn: + Hóa đơn giá trị gia tăng + Hóa đơn bán hàng + Hóa đơn bán tài sản công + Hóa đơn bán hàng dự trữ quốc gia + Hóa đơn khác + Chứng từ điện tử được sử dụng và quản lý như hóa đơn

<!--Nghiệp vụ của bài toán chính-->

Video Viettel

<!--@Chú ý ở đồ án này:-->

Mã giao dịch điện tử = Mã số thuế + Thời gian đăng kí
Sử dụng hàm ngẫu nhiên (tỉ lệ 10%) cho trường hợp từ chối.

<!--Phân tích và thiết kế-->

Xác định các tính năng cần thiết và các yêu cầu kỹ thuật tạo ra một thiết kế hệ thống hoặc kiến trúc đáp ứng.
UML Activity Diagrams
UML Use Case Diagrams
UML Class Diagrams
UML Sequence Diagrams

UML
ORM
SQL
