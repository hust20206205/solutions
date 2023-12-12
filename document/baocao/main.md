<!--!======================================================-->

- [1. Đồ án 2](#1-đồ-án-2)
  - [1.1. Trang bìa](#11-trang-bìa)
  - [1.2. Nhận xét của giảng viên](#12-nhận-xét-của-giảng-viên)
  - [1.3. Mục lục](#13-mục-lục)
  - [1.4. Lời cảm ơn](#14-lời-cảm-ơn)
  - [1.5. Lời mở đầu](#15-lời-mở-đầu)
  - [1.6. Tóm tắt nội dung đồ án](#16-tóm-tắt-nội-dung-đồ-án)
  - [1.7. Đánh giá và thảo luận](#17-đánh-giá-và-thảo-luận)
  - [1.8. Danh sách bảng](#18-danh-sách-bảng)
  - [1.9. Danh sách hình ảnh](#19-danh-sách-hình-ảnh)
  - [1.10. Danh sách mã nguồn](#110-danh-sách-mã-nguồn)
  - [1.11. Danh sách các cụm từ viết tắt](#111-danh-sách-các-cụm-từ-viết-tắt)
  - [1.12. Danh sách các thuật ngữ](#112-danh-sách-các-thuật-ngữ)
- [2. Giới thiệu chung](#2-giới-thiệu-chung)
  - [2.1. Giới thiệu về bài toán hóa đơn điện tử](#21-giới-thiệu-về-bài-toán-hóa-đơn-điện-tử)
    - [2.1.1. Hóa đơn](#211-hóa-đơn)
    - [2.1.2. Hóa đơn điện tử](#212-hóa-đơn-điện-tử)
    - [2.1.3. Bắt buộc sử dụng hóa đơn điện tử từ 01/07/2022.](#213-bắt-buộc-sử-dụng-hóa-đơn-điện-tử-từ-01072022)
    - [2.1.4. Bản thể hiện của hóa đơn điện tử:](#214-bản-thể-hiện-của-hóa-đơn-điện-tử)
    - [2.1.5. Lưu trữ hóa đơn điện tử](#215-lưu-trữ-hóa-đơn-điện-tử)
    - [2.1.6. Một số lợi ích của hóa đơn điện tử:](#216-một-số-lợi-ích-của-hóa-đơn-điện-tử)
  - [2.2. Giới thiệu về kiến trúc vi dịch vụ](#22-giới-thiệu-về-kiến-trúc-vi-dịch-vụ)
    - [2.2.1. Kiến trúc nguyên khối](#221-kiến-trúc-nguyên-khối)
    - [2.2.2. Kiến trúc vi dịch vụ](#222-kiến-trúc-vi-dịch-vụ)
    - [2.2.3. Một số đặc điểm và ưu điểm của kiến trúc vi dịch vụ](#223-một-số-đặc-điểm-và-ưu-điểm-của-kiến-trúc-vi-dịch-vụ)
    - [2.2.4. Một số nhược điểm và thách thức của kiến trúc vi dịch vụ](#224-một-số-nhược-điểm-và-thách-thức-của-kiến-trúc-vi-dịch-vụ)
  - [2.3. Giới thiệu về thiết kế hướng miền](#23-giới-thiệu-về-thiết-kế-hướng-miền)
- [3. Kết luận tổng kết](#3-kết-luận-tổng-kết)
- [4. Tài liệu tham khảo](#4-tài-liệu-tham-khảo)

<!--!======================================================-->

# 1. Đồ án 2

## 1.1. Trang bìa

ĐẠI HỌC BÁCH KHOA HÀ NỘI

VIỆN TOÁN ỨNG DỤNG VÀ TIN HỌC

![](pictures/logoBK.png)

BÁO CÁO ĐỒ ÁN II

ĐỀ TÀI:

<!--Xây dựng kiến trúc vi dịch vụ cho bài toán hóa đơn điện tử-->

<!--Sử dụng thiết kế hướng miền xây dựng kiến trúc vi dịch vụ cho bài toán hóa đơn điện tử-->

Giảng viên hướng dẫn: TS. Vũ Thành Nam

Sinh viên thực hiện: Vũ Văn Nghĩa

Mã số sinh viên: 20206205

Lớp: Toán Tin 02 - K65

Chuyên ngành: Toán Tin

Hà Nội - 2023

\thispagestyle{empty}

## 1.2. Nhận xét của giảng viên

Ý thức thực hiện: ...

Nội dung thực hiện: ...

Hình thức trình bày: ...

Đánh giá kết quả đạt được: ...

Hà Nội, \today

Giảng viên hướng dẫn
(Kí tên)

## 1.3. Mục lục

\tableofcontents

## 1.4. Lời cảm ơn

## 1.5. Lời mở đầu

## 1.6. Tóm tắt nội dung đồ án

## 1.7. Đánh giá và thảo luận

## 1.8. Danh sách bảng

auto

## 1.9. Danh sách hình ảnh

auto

## 1.10. Danh sách mã nguồn

auto

## 1.11. Danh sách các cụm từ viết tắt

<!--@sau-->

<!--STT; Từ viết tắt; Từ viết đầy đủ; Mô tả-->

<!--API; Application Programming Interface; Giao diện lập trình ứng dụng-->
<!--CI/CD; Continuous Integration (CI) and Continuous Delivery (CD) ; Quá trình tích hợp và chuyển giao liên tục-->
<!--thiết kế hướng miền ; thiết kế hướng miền; Kỹ thuật thiết kế theo hướng miền-->
<!--DI; Dependency Injection; Cơ chế tiêm sự phụ thuộc giữa các đối tượng-->
<!--HTTP; Hypertext Transfer Protocol; Giao thức truyền tải siêu văn bản-->
<!--JSON; JavaScript Object Notation; Một kiểu dữ liệu mở rộng của JavaScript-->
<!--ORM; Object Relational Mapping; Một kỹ thuật ánh xạ các đối tượng lập trình với từng bảng trong CSDL quan hệ-->

SOA; Service Oriented Architecture; Kiến trúc hướng dịch vụ
SOAP; Simple Object Access Protocol; Một giao thức để truy cập dịch vụ web
SPA; Single Page Application; Kiểu ứng dụng một trang
REST; Representational State Transfer; Một tiêu chuẩn thiết kế các API sử dụng cho các dịch vụ web
URL; Uniform Resource Locator ; Địa chỉ định vị tài nguyên trên Internet
XML; Extensible Markup Language; Ngôn ngữ đánh dấu mở rộng
Tổng cục Thuế ; TCT ;
Người nộp thuế ; NNT ;
Mã số thuế ; MST ;
Hóa đơn điện tử ; HĐĐT ;
Cơ quan thuế ; CQT ;
Công nghệ thông tin ; CNTT ;

<!--Cơ sở dữ liệu ; CSDL ;-->
<!--Tạo (Create), Đọc (Read), Sửa (Update), Xóa (Delete) ; CRUD ;-->
<!--Kubernetes ; K8s ;-->
<!--Số điện thoại ; SĐT ;-->
<!--UML-->
<!--MVC; Model View Controller; Một mẫu thiết kế ứng dụng-->

UML
ORM
SQL

## 1.12. Danh sách các thuật ngữ

<!--@sau-->

<!--STT; Tiếng Anh; Tiếng Việt-->

<!--kiến trúc nguyên khối, kiến trúc nguyên khối-->
<!--kiến trúc nguyên khối, kiến trúc nguyên khối-->
<!--kiến trúc vi dịch, kiến trúc vi dịch-->
<!--kiến trúc vi dịch, kiến trúc vi dịch-->
<!--kiến trúc vi dịch, kiến trúc vi dịch-->
<!--kiến trúc vi dịch, kiến trúc vi dịch-->
<!--thiết kế hướng miền, thiết kế hướng miền-->
<!--thiết kế hướng miền, thiết kế hướng miền-->

1 thiết kế hướng miền
Thiết kế hướng lĩnh vực
2 Domain (không dịch)
3 Abstraction Trừu tượng
4 chuyên gia ngành

# 2. Giới thiệu chung

Trong thời đại ngày nay, nhu cầu phát triển ứng dụng và hệ thống ngày càng tăng, đặt ra thách thức đối với kiến trúc phần mềm. Kiến trúc nguyên khối đã phục vụ hiệu quả trong quá khứ, nhưng kiến trúc này bắt đầu gặp khó khăn đối mặt với sự phức tạp, khả năng mở rộng và khả năng đáp ứng linh hoạt với thay đổi nhanh chóng trong yêu cầu kinh doanh.

Kiến trúc vi dịch vụ là giải pháp cho những thách thức này. Kiến trúc vi dịch vụ chia dự án thành những dịch vụ nhỏ độc lập, mỗi dịch vụ chịu trách nhiệm về một chức năng cụ thể. Từ đó, giảm sự phức tạp của dự án tăng tính linh hoạt và dễ dàng quản lý.

Việc vận dụng kết hợp giữa kiến trúc vi dịch vụ và thiết kế hướng miền là một cách tiếp cận toàn diện, giúp xác định và tổ chức các dịch vụ dựa trên việc hiểu rõ về lĩnh vực kinh doanh. Thiết kế hướng miền giúp xây dựng mô hình dựa trên yêu cầu nghiệp vụ thực tế, giúp dự án phản ánh đúng các quy trình kinh doanh.

## 2.1. Giới thiệu về bài toán hóa đơn điện tử

Bài toán hóa đơn điện tử là một phần quan trọng của quá trình chuyển đổi số. Trong quá khứ, mọi người thường sử dụng hóa đơn giấy truyền thống. Ngày nay, khi có quy định kế toán và quản lý tài chính, hóa đơn điện tử đã trở nên phổ biến giúp giảm bớt sự phụ thuộc vào giấy tờ. Cùng với sự phát triển của công nghệ đã giúp hiệu quả công việc và tối ưu hóa quy trình kế toán và tài chính.

Theo em tìm hiểu có các căn cứ pháp lý liên quan sau đây:

### 2.1.1. Hóa đơn

> Theo quy định tại khoản 1 Điều 3 Nghị định 123/2020/NĐ-CP:

Hóa đơn là chứng từ kế toán do tổ chức, cá nhân bán hàng hóa, cung cấp dịch vụ lập, ghi nhận thông tin bán hàng hóa, cung cấp dịch vụ. Hóa đơn được thể hiện theo hình thức hóa đơn điện tử hoặc hóa đơn do cơ quan thuế đặt in.

### 2.1.2. Hóa đơn điện tử

> Theo quy định tại khoản 2 Điều 3 Nghị định 123/2020/NĐ-CP:

Hóa đơn điện tử là hóa đơn có mã hoặc không có mã của cơ quan thuế được thể hiện ở dạng dữ liệu điện tử do tổ chức, cá nhân bán hàng hóa, cung cấp dịch vụ lập bằng phương tiện điện tử để ghi nhận thông tin bán hàng hóa, cung cấp dịch vụ theo quy định của pháp luật về kế toán, pháp luật về thuế, bao gồm cả trường hợp hóa đơn được khởi tạo từ máy tính tiền có kết nối chuyển dữ liệu điện tử với cơ quan thuế, trong đó:

a. Hóa đơn điện tử có mã của cơ quan thuế là hóa đơn điện tử được cơ quan thuế cấp mã trước khi tổ chức, cá nhân bán hàng hóa, cung cấp dịch vụ gửi cho người mua. Mã của cơ quan thuế trên hóa đơn điện tử bao gồm số giao dịch là một dãy số duy nhất do hệ thống của cơ quan thuế tạo ra và một chuỗi ký tự được cơ quan thuế mã hóa dựa trên thông tin của người bán lập trên hóa đơn.

b. Hóa đơn điện tử không có mã của cơ quan thuế là hóa đơn điện tử do tổ chức bán hàng hóa, cung cấp dịch vụ gửi cho người mua không có mã của cơ quan thuế.

### 2.1.3. Bắt buộc sử dụng hóa đơn điện tử từ 01/07/2022.

> Theo quy định tại khoản 1 Điều 59 Nghị định 123/2020/NĐ-CP:

Nghị định này có hiệu lực thi hành kể từ ngày 01 tháng 7 năm 2022, khuyến khích cơ quan, tổ chức, cá nhân đáp ứng điều kiện về hạ tầng công nghệ thông tin áp dụng quy định về hóa đơn, chứng từ điện tử của Nghị định này trước ngày 01 tháng 7 năm 2022.

=> Theo quy định của Chính phủ và Bộ Tài Chính, tất cả các doanh nghiệp, tổ chức và hộ kinh doanh đều bắt buộc phải chuyển từ sử dụng hóa đơn giấy sang hóa đơn điện tử kể từ tháng 07/2022. Vì vậy, nhu cầu sử dụng và xử lý hóa đơn điện tử trở nên rất lớn. Do đó, em đã chọn chủ đề:

<!--!"Xây dựng kiến trúc vi dịch vụ cho hệ thống quản lý hóa đơn điện tử".-->

### 2.1.4. Bản thể hiện của hóa đơn điện tử:

### 2.1.5. Lưu trữ hóa đơn điện tử

> Theo quy định tại khoản 1 Điều 11 Thông tư 32/2011/TT-BTC:

Người bán, người mua hàng hoá, dịch vụ sử dụng hóa đơn điện tử để ghi sổ kế toán, lập báo cáo tài chính phải lưu trữ hóa đơn điện tử theo thời hạn quy định của Luật Kế toán. Trường hợp hóa đơn điện tử được khởi tạo từ hệ thống của tổ chức trung gian cung cấp giải pháp hóa đơn điện tử thì tổ chức trung gian này cũng phải thực hiện lưu trữ hóa đơn điện tử theo thời hạn nêu trên.

> Theo quy định tại khoản 5 Điều 41 Luật số 88/2015/QH13

1. Tài liệu kế toán phải được lưu trữ theo thời hạn sau đây:

a. Ít nhất là 05 năm đối với tài liệu kế toán dùng cho quản lý, điều hành của đơn vị kế toán, gồm cả chứng từ kế toán không sử dụng trực tiếp để ghi sổ kế toán và lập báo cáo tài chính.

b. Ít nhất là 10 năm đối với chứng từ kế toán sử dụng trực tiếp để ghi sổ kế toán và lập báo cáo tài chính, sổ kế toán và báo cáo tài chính năm, trừ trường hợp pháp luật có quy định khác.

c. Lưu trữ vĩnh viễn đối với tài liệu kế toán có tính sử liệu, có ý nghĩa quan trọng về kinh tế, an ninh, quốc phòng.

=> Như vậy, hóa đơn điện tử dạng tệp XML sẽ được lưu trữ trên hệ thống hóa đơn điện tử của nhà cung cấp hoặc doanh nghiệp có thể tải về để tự lưu trữ. Thời gian lưu trữ là 10 năm theo quy định của pháp luật.

### 2.1.6. Một số lợi ích của hóa đơn điện tử:

Giúp tiết kiệm chi phí in ấn, lưu trữ và bảo quản.
Loại bỏ rủi ro cháy, hỏng hoặc mất và dễ dàng sao lưu.
Dễ dàng linh hoạt trong việc tra cứu, phát hành, quản lý và tạo báo cáo.
Tối ưu hóa quá trình kế toán (giảm sai sót và tiết kiệm thời gian) và giảm thủ tục giấy tờ.
Theo dõi tình hình tài chính của công ty (doanh thu, chi phí, lợi nhuận).
Tuân thủ các quy định về thuế và pháp luật.
Thể hiện tính minh bạch trong quá trình kinh doanh (bảo vệ quyền lợi của cả người mua và người bán).

## 2.2. Giới thiệu về kiến trúc vi dịch vụ

### 2.2.1. Kiến trúc nguyên khối

Trước khi kiến trúc vi dịch vụ trở nên phổ biến, kiến trúc nguyên khối đã được áp dụng rộng rãi trong kiến trúc phần mềm truyền thống. Kiến trúc nguyên khối là kiến trúc phần mềm trong đó toàn bộ dự án được xây dựng và triển khai như một đơn vị duy nhất.

Ví dụ: Mô hình MVC (Model-View-Controller) là một trong những dạng của kiến trúc nguyên khối.
Trong mô hình này, ứng dụng được chia thành ba thành phần chính:
Mô hình (Model): Đại diện cho dữ liệu và logic xử lý dữ liệu.
Giao diện (View): Đại diện cho giao diện người dùng.
Bộ điều khiển (Controller): Nhận yêu cầu người dùng thông qua View, sau đó tương tác với Model để làm việc với dữ liệu.

### 2.2.2. Kiến trúc vi dịch vụ

Kiến trúc vi dịch vụ chia dự án thành các thành phần nhỏ hơn được gọi là các dịch vụ.
Các dịch vụ này chịu trách nhiệm cho một chức năng cụ thể nhằm hiện thực hóa khả năng kinh doanh cụ thể.

Các dịch vụ này độc lập về ngôn ngữ lập trình, CSDL, triển khai, ...
Các dịch vụ này tương tác với nhau qua hạ tầng mạng.

![](pictures/ChuyenTu_KienTrucNguyenKhoi_Sang_KienTrucViDichVu.jpg)
![](pictures/AnhKhacNhau_KienTrucNguyenKhoi_KienTrucViDichVu.png)

### 2.2.3. Một số đặc điểm và ưu điểm của kiến trúc vi dịch vụ

Kiến trúc vi dịch vụ có nhiều ưu điểm đặc biệt với các dự án có quy mô lớn và phức tạp.

Kiến trúc vi dịch vụ phân chia dự án thành các dịch vụ nhỏ.
Giúp việc phát triển và quản lý dễ dàng hơn.
Dễ dàng mở rộng hệ thống.
Tận dụng sử dụng tài nguyên cho từng dịch vụ.
Tập trung yêu cầu nghiệp vụ trong dịch vụ dẫn đến tốc độ định giá doanh nghiệp nhanh hơn.

Vì các dịch vụ được phân chia là độc lập.

<!--Nhìn chung, điều đó có nghĩa là I.T. các nhóm không cần phải đi sâu vào mọi khả năng kinh doanh. Họ có thể tập trung vào năng lực kinh doanh mà họ đang xây dựng trong vi dịch vụ của mình.-->
<!--Nhưng giả sử hoạt động kinh doanh cho vay và thế chấp đang trải qua một sự chuyển đổi nghiêm trọng nào đó, trong trường hợp đó, nhóm cho vay và thế chấp có thể quyết định phát hành vi dịch vụ của họ mỗi ngày.-->

Các nhóm phát triển riêng dẫn tới tốc độ phát triển thay đổi nhanh.
Giảm thiểu ràng buộc và tăng tính linh hoạt của hệ thống.
Giảm chi phí và thời gian kiểm thử do ít ràng buộc.
Hệ thống có khả năng chịu lỗi cao tăng độ tin cậy.

Kiến trúc vi dịch vụ sử dụng đa ngôn ngữ và công nghệ khác nhau.
Tận dụng hiệu quả thế mạnh của từng ngôn ngữ, công nghệ phù hợp nhất cho yêu cầu nghiệp vụ cụ thể.

Ví dụ: Mỗi dịch vụ sử dụng ngôn ngữ lập trình nhau khác như: NodeJS, Go, Python, Java, CSharp, ...

![](pictures/DaNgonNgu/_DaNgonNgu.png)

### 2.2.4. Một số nhược điểm và thách thức của kiến trúc vi dịch vụ

Tuy nhiên, kiến trúc vi dịch vụ cũng có nhiều thách thức.

<!--Chịu ảnh hưởng của đường truyền mạng.-->

<!--Khả năng kiểm soát giao dịch (transaction).-->

<!--Tính nhất quán và toàn vẹn của dữ liệu giữa các dịch vụ.-->

Giám sát giữa các dịch vụ.

Bảo mật giao tiếp giữa các dịch vụ.

<!--Phát hiện lỗi và sửa lỗi khó khăn.-->

Ràng buộc về thứ tự sự kiện.
Đồng bộ đồng hồ thời gian.

<!--Chi phí xây dựng, quản lí vận hành lớn.-->

<!--@Có thể thêm phần truyền thông trực tiếp, gián tiếp-->

## 2.3. Giới thiệu về thiết kế hướng miền

<!--Lý do tiếp theo là một trong những lý do lớn nhất khiến tổ chức cần chuyển đổi nhu cầu và mong đợi của khách hàng liên tục thay đổi để duy trì và mở rộng cơ sở khách hàng của mình.-->
<!--Các tổ chức cần điều chỉnh hoạt động kinh doanh của mình để đáp ứng nhu cầu và mong đợi của khách hàng. Các doanh nghiệp bỏ qua kỳ vọng của khách hàng có xu hướng thua đối thủ cạnh tranh.-->
<!--Vì vậy, điều xảy ra với những doanh nghiệp không chuyển đổi, câu trả lời ngắn gọn cho câu hỏi này là những doanh nghiệp không chuyển đổi sẽ không thể tồn tại.-->

<!--Một điểm quan trọng cần ghi nhớ là chuyển đổi không phải là sáng kiến ​​hay nhiệm vụ chỉ diễn ra một lần. Các doanh nghiệp cần thay đổi liên tục và điều này đòi hỏi những thay đổi nhanh chóng đối với hệ thống và ứng dụng của họ.-->

<!--Một thách thức chung mà các doanh nghiệp phải đối mặt trong hành trình chuyển đổi là cách xây dựng phần mềm cũ cản trở hoặc gây khó khăn cho các tổ chức trong việc chuyển đổi.-->

Trong quá trình hoạt động, không phải mọi doanh nghiệp đều sẽ giữ nguyên mô hình kinh doanh được đưa ra ban đầu của mình. Khi quy mô thị trường thay đổi thì việc chuyển đổi mô hình kinh doanh là điều cần thiết. Chuyển đổi kinh doanh như một công cụ linh hoạt giúp các doanh nghiệp có thể phát triển và tồn tại giữa các đối thủ của mình.

Ví dụ:
Amazon từ hiệu sách trực tuyến thành thị trường cho nhà cung cấp khác như: Thương mại điện tử (E-commerce), Dịch vụ đám mây (Cloud Computing), ...

<!--!Thêm google-->

![](pictures/KienTrucViDichVuAmazon.png)
![](pictures/KienTrucViDichVuAmazon.png)

<!--Hình kiến trúc vi dịch vụ của Amazon-->
<!--!Thêm google-->

Gần đây, Baemin dịch vụ giao đồ ăn đã rời khỏi thị trường Việt Nam cũng do sức ép từ các đối thủ khác khiến Baemin khó cạnh tranh trong mảng kinh doanh cốt lõi là giao đồ ăn. Các đối thủ này không chỉ cung cấp dịch vụ giao đồ ăn mà còn có đặt xe, giao hàng, ...
![](pictures/Baemin.png)

<!--Hình Baemin đã rời khỏi thị trường Việt Nam-->

=> Hiện nay, các tổ chức doanh nghiệp có nhu cầu phát triển chuyển đổi kinh doanh để có thể tồn tại và phát triển khi thị trường thay đổi. Từ đó, đáp ứng nhu cầu của khách hàng, giúp mang đến ưu thế cạnh tranh so với các đối thủ. Do đó cần hệ thống chuyển đổi nhanh chóng đáp ứng nhu cầu của dự án và mong đợi của khách hàng.
=> Kiến trúc vi dịch vụ giải quyết những thách thức và hỗ trợ doanh nghiệp chuyển đổi dễ dàng.

Tuy nhiên, để xây dựng được kiến ​​trúc vi dịch vụ tốt cần phải tạo ra các dịch vụ nhỏ phù hợp và duy trì tính độc lập. Nếu không thực hiện đúng các nhóm phụ thuộc lẫn nhau và mất đi lợi thế của kiến ​​trúc vi dịch vụ.

Và từ đó, mẫu thiết kế hướng miền sử dụng để phân tích xây dựng kiến ​​trúc vi dịch vụ.
Thiết kế hướng miền xác định và tổ chức các dịch vụ dựa trên việc hiểu rõ về lĩnh vực kinh doanh, giúp dự án phản ánh đúng các quy trình và quy tắc kinh doanh.

<!--!======================================================-->

[](3.0.ChiTietVaApDungTKHM.md)

<!--[](3.1.TKHMLaGi.md)-->
<!--[](3.2.Mien.md)-->

[](3.3.MoHinhMien.md)
[](3.4.TenMienPhu.md)

# 3. Kết luận tổng kết

Kiến trúc vi dịch vụ, với việc tách biệt hệ thống thành các thành phần nhỏ quản lý độc lập, mang lại tính linh hoạt và khả năng mở rộng.

thiết kế hướng miền giúp xây dựng mô hình chính xác và nhất quán của lĩnh vực kinh doanh, giúp đảm bảo rằng hệ thống phản ánh đúng yêu cầu nghiệp vụ.

# 4. Tài liệu tham khảo

http

<!--Căn cứ pháp lý-->
<!--Thông tư 78/2021/TT-BTC-->
<!--Nghị định 123/2020/NĐ-CP-->
<!--Thông tư 78/2021/TT-BTC-->

Thông tư 32/2011/TT-BTC: https: //thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Thong-tu-32-2011-TT-BTC-huong-dan-ve-khoi-tao-phat-hanh-su-dung-hoa-don-dien-tu-120233.aspx

<!--https: //vanban.chinhphu.vn/default.aspx? pageid=27160&docid=99887-->

Thông tư 78/2021/TT-BTC: https: //thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-78-2022-TT-BTC-du-toan-ngan-sach-Nha-nuoc-2023-547888.aspx

<!--https: //vanban.chinhphu.vn/default.aspx? pageid=27160&docid=204200-->

Nghị định 123/2020/NĐ-CP: https: //thuvienphapluat.vn/van-ban/Ke-toan-Kiem-toan/Nghi-dinh-123-2020-ND-CP-quy-dinh-hoa-don-chung-tu-445980.aspx

<!--https: //vanban.chinhphu.vn/? pageid=27160&docid=201365-->

<!--https: //hoadondientu.gdt.gov.vn-->

<!--https: //en.wikipedia.org/wiki/kiến trúc vi dịch vụ-->
<!--https: //en.wikipedia.org/wiki/Domain-driven_design-->

<!--https: //kiến trúc vi dịch vụ.io-->
<!--2. Richardson, C. (2018). _kiến trúc vi dịch vụ Patterns: With Examples in Java._ O'Reilly Media.-->
<!--https: //refactoring.guru/design-mẫu/catalog-->

<!--https: //www.infoq.com/minibooks/domain-driven-design-quickly-->
<!--“thiết kế hướng miền: Tackling Complexity in the Heart of Software”, nhà xuất bản AddisonWesley, ISBN: 0-321-12521-5.-->
<!--1. Evans, E. (2003). _thiết kế hướng miền: Tackling Complexity in the Heart of Software._ Addison-Wesley.-->

<!--https: //learn.microsoft.com/en-us/archive/msdn-magazine/2009/february/best-practice-an-introduction-to-domain-driven-design-->

<!--https: //learn.microsoft.com/en-us/dotnet/architecture/kiến trúc vi dịch vụ/kiến trúc vi dịch vụ- thiết kế hướng miền -cqrs-mẫu/ thiết kế hướng miền -oriented-kiến trúc vi dịch vụ-->

<!--3. Newman, S. (2015). _Building kiến trúc vi dịch vụ: Designing Fine-Grained Systems._ O'Reilly Media.-->

<!--https: //github.com/GoogleCloudPlatform/kiến trúc vi dịch vụ-demo-->

<!--https: //www.uml-diagrams.org-->

<!--https: //www.udemy.com/course/domain-driven-design-and-kiến trúc vi dịch vụ-->

https: //viblo.asia/p/tim-hieu-ve-kiến trúc vi dịch vụ-phan-1-kiến trúc vi dịch vụ-la-gi-63vKjVjyK2R

https: //viblo.asia/p/domain-driven-design-phan-1-mrDGMOExkzL
https: //en.wikipedia.org/wiki/Business_Model_Canvas
