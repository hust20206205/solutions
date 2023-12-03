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


<!--! Mối quan hệ đối xứng-->
<!--Mối quan hệ bất đối xứng-->

<!--! mẫu chiến lược (Strategic patterns)-->
<!--!Phân rã các miền phức tạp (Decomposition of complex domains)-->

Entities ,Value Objects ,Aggregate đư

<!--!Mẫu nhà xưởng (Factory Pattern)-->

<!--mẫu kho lưu trữ (Repository Pattern)-->

<!--Domain Services dịch vụ miền-->
<!--Domain Service Pattern-->
<!--Characteristics of Domain Services đặc điểm-->

<!--Dịch vụ ứng dụng (app sẻvice)-->

<!--Dịch vụ cơ sở hạ tầng-->
<!--  -->
<!-- Tích hợp Liên tục (CI/CD) -->

Khi một Ngữ cảnh Giới hạn đã được định nghĩa, chúng ta cần đảm bảo rằng nó luôn mới và hoạt động tốt.


Doanh nghiệp nhu cầu phát triển thay đổi liên tục và nhanh chóng.


Ngay cả khi nhóm làm việc cùng trên một Ngữ cảnh Giới hạn thì vẫn có thể có lỗi. 


 => vì vậy , CI/CD tạo ra một quy trình tự động và liên tục từ việc tích hợp mã nguồn, kiểm thử tự động, đến quá trình triển khai, giúp tăng cường chất lượng phần mềm, giảm thời gian và rủi ro trong quá trình phát triển phần mềm.
 

 **Continuous Integration (CI)**: Đây là một phương pháp phát triển phần mềm mà ở đó, các thành viên trong đội phát triển tích hợp mã nguồn của họ vào một hệ thống chung thường xuyên - thường là hàng ngày. Mục tiêu của CI là giảm xung đột giữa các phiên bản mã nguồn khác nhau, giúp phát hiện và sửa lỗi sớm hơn. Khi một nhóm sử dụng CI, mã nguồn mới được tự động kiểm thử và xây dựng mỗi khi tích hợp vào hệ thống.

 **Continuous Delivery (CD)**: Sau khi mã nguồn đã được tích hợp, Continuous Delivery tập trung vào việc tự động hóa quá trình triển khai (deployment) để có thể triển khai ứng dụng vào môi trường sản xuất một cách nhanh chóng và đáng tin cậy. Điều này có nghĩa là mọi thay đổi trong mã nguồn có thể tự động triển khai vào môi trường thử nghiệm hoặc môi trường sản xuất mà không cần sự can thiệp thủ công.
 