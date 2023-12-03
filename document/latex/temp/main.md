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
<!--  -->
  - Mất thời gian nhưng cần thiết để xây dựng mô hình phù hợp với domain và giải quyết vấn đề nghiệp vụ trong thực tế.



<!-- - **Xây dựng mô hình domain:** -->
<!-- - **Đối thoại giữa bạn và chuyên gia nghiệp vụ:** -->


<!-- - **Quan trọng của hiểu đúng domain:** -->
  <!-- - Khái niệm xuất hiện không tổ chức nhưng cần thiết để hiểu domain. -->
  <!-- - Cần tìm hiểu nhiều từ chuyên gia về domain. -->

  <!-- - Trao đổi giữa người kiến trúc phần mềm và chuyên gia domain. -->
  - Phản hồi giữa các bên giúp cải thiện mô hình và hiểu đúng về domain.




<!---->

<!--! Mô hình chiến lược (strategic): Ngôn ngữ phổ biến (Ubiquitous Language)-->

<!--Nhóm kinh doanh sử dụng ngôn ngữ kinh doanh, trong khi nhóm công nghệ có xu hướng sử dụng các thuật ngữ kỹ thuật trong giao tiếp của họ.-->
<!--Sự khác biệt về ngôn ngữ giữa các nhóm kinh doanh và I.T. các nhóm có thể dẫn đến những thách thức về ngôn ngữ.-->
<!--Thiết kế hướng miền đề xuất sử dụng ngôn ngữ phổ biến để giải quyết những thách thức ngôn ngữ này.-->
<!---->
<!--đối với ngôn ngữ kinh doanh được sử dụng trong nhiều miền có thể dẫn đến nhầm lẫn. Nếu bạn đang sử dụng các thuật ngữ kinh doanh từ tên miền này sang tên miền khác thì điều đó có thể dẫn đến nhầm lẫn và hiểu sai.-->

<!--Thách thức để xây dựng các hệ thống phức tạp, các nhóm phải học nhiều ngôn ngữ kinh doanh được các chuyên gia sử dụng trong bối cảnh các miền hoặc miền phụ khác nhau.-->
<!--Thách thức cùng một thuật ngữ có thể xuất hiện trong bối cảnh các lĩnh vực kinh doanh khác nhau.-->
<!--Vì vậy, thách thức ở đây là cùng một thời điểm trên nhiều miền có thể có ý nghĩa khác nhau, tùy thuộc vào ngữ cảnh và điều này có thể gây nhầm lẫn giữa các mục.-->
<!--Thử thách thứ ba liên quan đến việc nó có biệt ngữ riêng.-->
<!--Thiết kế hướng miền gợi ý thiết lập một ngôn ngữ chung trong từng bối cảnh kinh doanh và ngôn ngữ này được tất cả các bên liên quan sử dụng. Ngôn ngữ này được gọi là ngôn ngữ phổ biến.-->

<!--Ngôn ngữ phổ biến là một trong những mô hình chiến lược và thiết kế hướng miền, thiết kế hướng miền, chẳng hạn như thiết lập một ngôn ngữ chung trong từng bối cảnh kinh doanh.-->

<!--ngôn ngữ phổ biến giải quyết tất cả những thách thức-->

<!--Ngôn ngữ phổ biến có thể được coi là một phương ngữ được sử dụng bởi các nhóm khác nhau trong một tổ chức.-->

<!--xác định bởi từ vựng và ngôn ngữ phổ biến có định nghĩa rõ ràng về ngữ cảnh mà từ vựng hoặc bảng chú giải thuật ngữ áp dụng.-->
<!--Bảng thuật ngữ này chứa các thuật ngữ và từ viết tắt phổ biến được sử dụng trong ngữ cảnh được xác định. Tùy chọn, nó cũng có thể giúp làm ví dụ về cách sử dụng các thuật ngữ và từ viết tắt, đồng thời nó cũng có thể có tham chiếu hoặc liên kết đến nội dung có liên quan.-->
<!---->
<!--Tại thời điểm này, bạn có thể nói rằng nó trông giống như Từ điển Doanh nghiệp Doanh nghiệp và bạn đã đúng ở một mức độ nào đó.-->
<!--Đó là một thuật ngữ từ điển, nhưng có sự khác biệt. Hãy để tôi giải thích nó bằng một ví dụ. Trong một bài giảng, tôi đã nói về kinh nghiệm của mình khi xây dựng một mô hình kinh doanh doanh nghiệp thống nhất.-->
<!--Dự án đó cũng bao gồm việc tạo ra một từ điển kinh doanh. Và từ điển kinh doanh mà tôi đã tạo này có các thuật ngữ trong toàn doanh nghiệp và nó cũng có logic cho nhiều mục khác.-->
<!--Và logic này về cơ bản đã hướng dẫn người sử dụng từ điển về ý nghĩa của thuật ngữ này trong các ngữ cảnh khác nhau.-->
<!--Và điều đó đã làm tăng thêm sự phức tạp cho việc sử dụng từ điển kinh doanh này. Khi kết thúc dự án này, tôi đã giao cuốn từ điển kinh doanh này cho một nhà phân tích kinh doanh, người quản lý nó một cách tập trung trong một trang tính Excel.-->
<!--Bạn có thể tưởng tượng cuốn từ điển kinh doanh này đã đi đến đâu trong một khoảng thời gian.
-->
<!---->
<!--Ngôn ngữ phổ biến không được tạo và quản lý tập trung.-->
<!--Có nhiều ngôn ngữ phổ biến trong một tổ chức. Vì vậy, trong trường hợp của ngân hàng, sẽ có một ngôn ngữ phổ biến cho tài khoản tiết kiệm và một ngôn ngữ phổ biến cho tài khoản tín dụng, đồng thời các nhóm tài khoản tiết kiệm và thẻ tín dụng sẽ tạo và quản lý các ngôn ngữ phổ biến này một cách độc lập.-->

<!--Ngôn ngữ phổ biến bao gồm các cuốn sách thường được sử dụng bởi cả chuyên gia kinh doanh và chuyên gia công nghệ.-->

Và có một quan niệm sai lầm đằng sau ngôn ngữ phổ biến này rằng việc xuất khẩu kinh doanh luôn xác định ngôn ngữ.

<!--Trên thực tế, điều đó không phổ biến. Ngôn ngữ không bị áp đặt bởi các chuyên gia. Và không chỉ vậy, nó không phải là ngôn ngữ được sử dụng trong ngành.-->

<!--Hãy coi nó như một ngôn ngữ nhóm, một ngôn ngữ bộ lạc phát triển hoặc phát triển theo thời gian thông qua sự cộng tác giữa doanh nghiệp và các chuyên gia công nghệ.-->

<!--Nhóm tạo ra ngôn ngữ phổ biến có thể sử dụng nhiều kỹ thuật, chẳng hạn như vẽ sơ đồ quy trình, câu chuyện của người dùng, viết kịch bản phân cảnh và thậm chí là gây bão.-->

<!--Và điều này dẫn đến việc tạo ra ngôn ngữ phổ biến. Điều quan trọng cần ghi nhớ là việc tạo ra ngôn ngữ phổ biến không phải là công việc chỉ làm một lần.-->
<!--Đó là một quá trình liên tục vì ngôn ngữ phải mất một thời gian để đạt đến mức độ trưởng thành cao. Khi một câu hỏi phổ biến được đặt ra vào thời điểm này là liệu có bất kỳ công cụ đặc biệt nào để tạo và quản lý ngôn ngữ phổ biến hay không thì câu trả lời ngắn gọn là không.-->
<!--Bạn có thể sử dụng bất kỳ công cụ nào miễn là nó giúp tất cả thành viên trong nhóm có thể tiếp cận được ngôn ngữ phổ biến này. Các công cụ cộng tác và chia sẻ kiến ​​thức như hội nghị và quip thường được sử dụng.-->
<!--Xin lưu ý rằng đây không phải là công cụ cộng tác và chia sẻ kiến ​​thức duy nhất. Bất kỳ công cụ nào có sẵn trong tổ chức của bạn sẽ giúp các thành viên trong nhóm của chúng tôi có thể dễ dàng tiếp cận ngôn ngữ phổ biến này.-->

<!--Khi nhóm đã đạt đến mức độ trưởng thành khá cao đối với ngôn ngữ phổ biến của mình, họ nên bắt đầu sử dụng nó cho mọi thứ.-->
<!--Và sau đó ngôn ngữ này sẽ phát triển theo thời gian. Các chuyên gia tên miền nên sử dụng nó. Các đội giao hàng phải sử dụng nó cho công việc chung hàng ngày của họ.-->
<!--Và tất cả tài liệu nên sử dụng ngôn ngữ phổ biến nếu nhóm đang phát triển tài liệu và họ tạo một thuật ngữ mới hoặc tìm thấy một thuật ngữ mới, thì thuật ngữ đó sẽ được thêm vào ngôn ngữ phổ biến vào cuối ngày.-->
<!--Ngôn ngữ phổ biến phải đóng vai trò là nguồn thông tin chính xác cho tất cả mọi người sử dụng vào thời điểm ngôn ngữ phổ biến đó được sử dụng trong mã ứng dụng cũng như trong mã thử nghiệm.-->
<!--Cuối cùng nhưng không kém phần quan trọng, các nhóm phải sử dụng ngôn ngữ phổ biến trong tất cả các cuộc trò chuyện của mình.-->

![Alt text](image-1.png)

<!--Vì vậy, tại thời điểm này bạn có thể hỏi lợi ích của việc làm đó là gì?-->
<!--Mọi thứ trở nên nhất quán và dễ theo dõi hơn đối với cả chuyên gia tên miền cũng như chuyên gia ID. Một tác dụng phụ thú vị của ngôn ngữ phổ biến là nó giúp xác định các liên hệ chồng chéo.-->
<!--Và điều đó có nghĩa là chúng ta có thể sử dụng ngôn ngữ phổ biến để chia các mối liên hệ kinh doanh của mình thành các phần nhỏ hơn và theo các thiết kế khác nhau về miền. Những phần nhỏ hơn của bối cảnh này được gọi là bối cảnh liên kết. Thêm về điều này trong các bài giảng sau.-->

<!--Ngôn ngữ phổ biến phát triển trong một khoảng thời gian.-->
<!--Đây không phải là công việc chỉ làm một lần mà nó được tạo ra bởi sự cộng tác giữa chuyên gia tên miền và chuyên gia công nghệ.-->
<!--Ngôn ngữ phổ biến không yêu cầu bất kỳ công cụ đặc biệt nào mà bạn có thể sử dụng bất kỳ nền tảng cộng tác tri thức nào.-->

<!--Hướng dẫn 5/7-->