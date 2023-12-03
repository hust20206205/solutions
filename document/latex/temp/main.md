[](0.TrangBia.md)
[](0.DanhSach.md)
[](0.LoiCamOn_LoiMoDau.md)

[](1.0.GioiThieuChung.md)
[](1.1.GioiThieuMicroservice.md)
[](1.2.GioiThieuBaiToanHoaDonDienTu.md)
[](1.3.GioiThieuDDD.md)

[](2.0.ApDungDDDVoiBaiToanNghiepVu.md)

[](3.0.TrienKhaiKienTrucMicroservice.md)

[](0.KetLuan_TongKet.md)
[](_.TaiLieuThamKhao.md)

<!---->
<!--! Mô hình chiến lược (strategic):-->
<!--Ngôn ngữ phổ biến (Ubiquitous Language)-->

Trong quá trình xây dựng mô hình domain, cần Đối thoại Trao đổi người thiết kế phần mềm và chuyên gia nghiệp vụ để hiểu đúng domain. Tuy nhên, Nhóm kinh doanh sử dụng ngôn ngữ kinh doanh, trong khi nhóm công nghệ có xu hướng sử dụng các thuật ngữ kỹ thuật trong giao tiếp của họ. Lập trình viên tập trung vào lớp, phương thức, thuật toán, trong khi chuyên gia domain thường sử dụng ngôn ngữ chuyên ngành của họ. Sự khác biệt về ngôn ngữ giữa các nhóm có thể dẫn đến những thách thức về ngôn ngữ.

Thách thức cùng một thuật ngữ có thể xuất hiện trong bối cảnh các lĩnh vực kinh doanh khác nhau. đối với ngôn ngữ kinh doanh được sử dụng trong nhiều miền có thể dẫn đến nhầm lẫn. Nếu bạn đang sử dụng các thuật ngữ kinh doanh từ tên miền này sang tên miền khác thì điều đó có thể dẫn đến nhầm lẫn và hiểu sai. Vì vậy, thách thức ở đây là cùng một thời điểm trên nhiều miền có thể có ý nghĩa khác nhau, tùy thuộc vào ngữ cảnh và điều này có thể gây nhầm lẫn giữa các mục.

<!--Thiết kế hướng miền đề xuất sử dụng ngôn ngữ phổ biến để giải quyết những thách thức ngôn ngữ này.-->

Ngôn ngữ phổ biến là một trong những mô hình chiến lược của thiết kế hướng miền, thiết lập một ngôn ngữ chung trong từng bối cảnh kinh doanh.

<!-- một số đặc điểm: -->

Ngôn ngữ phổ biến không được tạo và quản lý tập trung: Có nhiều ngôn ngữ phổ biến trong một tổ chức. Vì vậy, mỗi nhóm sẽ tạo và quản lý các ngôn ngữ phổ biến này một cách độc lập.

Ngôn ngữ phổ biến bao gồm các cuốn sách thường được sử dụng bởi cả chuyên gia kinh doanh và chuyên gia công nghệ: Ngôn ngữ không bị áp đặt bởi các chuyên gia và không phải phải là ngôn ngữ được sử dụng trong ngành.

Ngôn ngữ phổ biến như một ngôn ngữ nhóm, một ngôn ngữ phát triển theo thời gian thông qua sự cộng tác giữa doanh nghiệp và các chuyên gia công nghệ.

Không Ngừng Cập Nhật: việc tạo ra ngôn ngữ phổ biến không phải là công việc chỉ làm một lần. Đó là một quá trình liên tục vì ngôn ngữ phải mất một thời gian để đạt đến mức độ trưởng thành cao. Ngôn ngữ phổ biến không phải là một khái niệm cố định mà được cập nhật liên tục theo sự thay đổi trong dự án. Các thành viên của đội ngũ phải liên tục đảm bảo rằng ngôn ngữ phổ biến của họ vẫn phản ánh đúng hiện trạng của hệ thống.

Đồng Nhất Trong Mọi Phần Của Hệ Thống: không chỉ giới hạn trong phạm vi của một module hay một thành phần cụ thể, mà nó phải được áp dụng đồng nhất trong toàn bộ hệ thống.

<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!--Khi nhóm đã đạt đến mức độ trưởng thành khá cao đối với ngôn ngữ phổ biến của mình, họ nên bắt đầu sử dụng nó cho mọi thứ.-->

<!--Và sau đó ngôn ngữ này sẽ phát triển theo thời gian. Các chuyên gia tên miền nên sử dụng nó. Các đội giao hàng phải sử dụng nó cho công việc chung hàng ngày của họ.-->

<!--Và tất cả tài liệu nên sử dụng ngôn ngữ phổ biến nếu nhóm đang phát triển tài liệu và họ tạo một thuật ngữ mới hoặc tìm thấy một thuật ngữ mới, thì thuật ngữ đó sẽ được thêm vào ngôn ngữ phổ biến vào cuối ngày.-->

<!--Ngôn ngữ phổ biến phải đóng vai trò là nguồn thông tin chính xác cho tất cả mọi người sử dụng vào thời điểm ngôn ngữ phổ biến đó được sử dụng trong mã ứng dụng cũng như trong mã thử nghiệm.-->

<!--Cuối cùng nhưng không kém phần quan trọng, các nhóm phải sử dụng ngôn ngữ phổ biến trong tất cả các cuộc trò chuyện của mình.-->

![Alt text](image-1.png)

<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->

<!--Vì vậy, tại thời điểm này bạn có thể hỏi lợi ích của việc làm đó là gì?-->
<!--Mọi thứ trở nên nhất quán và dễ theo dõi hơn đối với cả chuyên gia tên miền cũng như chuyên gia ID. Một tác dụng phụ thú vị của ngôn ngữ phổ biến là nó giúp xác định các liên hệ chồng chéo.-->
<!--Và điều đó có nghĩa là chúng ta có thể sử dụng ngôn ngữ phổ biến để chia các mối liên hệ kinh doanh của mình thành các phần nhỏ hơn và theo các thiết kế khác nhau về miền. Những phần nhỏ hơn của bối cảnh này được gọi là bối cảnh liên kết. Thêm về điều này trong các bài giảng sau.-->

<!--Ngôn ngữ phổ biến phát triển trong một khoảng thời gian.-->
<!--Đây không phải là công việc chỉ làm một lần mà nó được tạo ra bởi sự cộng tác giữa chuyên gia tên miền và chuyên gia công nghệ.-->
<!--Ngôn ngữ phổ biến không yêu cầu bất kỳ công cụ đặc biệt nào mà bạn có thể sử dụng bất kỳ nền tảng cộng tác tri thức nào.-->

<!--Hướng dẫn 5/7-->
