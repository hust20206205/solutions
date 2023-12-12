

33
00:05:28,130 --> 00:05:49,910
Vì Microsoft tương tác với nhau qua giao thức mạng nên một ứng dụng được xây dựng bằng kiến ​​trúc, dịch vụ vi mô có thể làm trầm trọng thêm hiệu suất kém so với cùng một ứng dụng được triển khai với kiến ​​trúc nguyên khối trong ứng dụng dịch vụ vi mô, nên mỗi dịch vụ vi mô sẽ quản lý cơ sở dữ liệu riêng của mình.

34
00:05:50,300 --> 00:06:06,050
Điều này dẫn đến sự phức tạp trong việc quản lý tính toàn vẹn dữ liệu.  Và lý do cho điều đó là trong trường hợp ứng dụng nguyên khối, bạn có thể sử dụng cơ sở dữ liệu chung và bạn có thể sử dụng các giao dịch cục bộ để quản lý tính toàn vẹn của dữ liệu.

35
00:06:06,380 --> 00:06:14,440
Trong trường hợp kiến ​​trúc phân tán như kiến ​​trúc dịch vụ vi mô, các cơ chế giao dịch truyền thống có thể không hoạt động.

36
00:06:14,450 --> 00:06:22,460
Và điều này dẫn đến độ phức tạp cao hơn.  Trong thời gian chạy, các dịch vụ vi mô được khởi chạy dưới dạng các quy trình độc lập.

37
00:06:22,490 --> 00:06:39,650
Những quá trình độc lập này cần được giám sát.  Nếu bạn có một kiến ​​trúc cần hàng chục hoặc hàng trăm phiên bản của cùng một máy chủ vi mô, thì việc giám sát các dịch vụ vi mô này và gỡ lỗi các dịch vụ vi mô trong trường hợp xảy ra sự cố có thể trở nên khó khăn.

38
00:06:39,980 --> 00:07:17,460
Những hình ảnh mà bạn thấy ở đây là bản đồ dịch vụ vi mô cho Amazon.com và Netflix và mối quan tâm chung khác đối với các dịch vụ vi mô là vì các dịch vụ vi mô hiển thị giao diện dưới dạng API dẫn đến bề mặt tấn công mở rộng cho ứng dụng dựa trên dịch vụ vi mô để giải quyết  Một số nhược điểm này, các tổ chức có kế hoạch áp dụng các dịch vụ vi mô cần đầu tư vào công nghệ mới về các công cụ cơ sở hạ tầng, sau đó họ cũng cần đầu tư vào phát triển kỹ năng.

39
00:07:17,630 --> 00:07:27,610
Vì vậy, điều này có nghĩa là các tổ chức có thể cần phải đầu tư trước cho một ứng dụng sẽ được xây dựng với Microsoft, kiến ​​trúc cho biết.

40
00:07:28,400 --> 00:07:37,370
Trong bài học này, tôi đã thảo luận về kiến ​​trúc dịch vụ vi mô từ góc độ công nghệ.  Hãy cùng điểm qua những ưu điểm của kiến ​​trúc dịch vụ vi mô.

41
00:07:37,850 --> 00:07:48,260
Việc quản lý thay đổi trở nên dễ dàng hơn và việc triển khai có thể được thực hiện độc lập.  Và điều này có nghĩa là các tính năng có thể được phát hành nhanh hơn nhiều.

42
00:07:48,530 --> 00:08:03,140
Tốc độ tiếp cận thị trường được tăng lên, các lỗi bị cô lập và các dịch vụ có thể được mở rộng quy mô một cách độc lập.  Và điều này có nghĩa là nó mang lại chất lượng trải nghiệm tốt hơn cho người tiêu dùng hoặc ứng dụng.

43
00:08:03,140 --> 00:08:12,120
Từ quan điểm của Korn, hiệu suất mạng hỗ trợ là một vấn đề cần quan tâm.  Và sau đó là những thách thức liên quan đến việc giám sát quản lý và bảo mật dữ liệu.

44
00:08:12,800 --> 00:08:20,720
Một số thách thức này có thể được giải quyết bằng cách đầu tư và phát triển công cụ, cơ sở hạ tầng và kỹ năng.

