<!--thiết kế hướng miền-->
<!--@miền (Domain) là gì?-->

là vấn đề
là giải pháp
của dự án
của nghiệp vụ kinh doanh

<!--@Tên miền phụ (Sub-Domain) là gì?-->

<!--@Bối cảnh giới hạn (Bounded Context)-->

<!--@Mô hình miền (Domain model)-->


1
00:00:00,330 --> 00:00:16,190
Microsoft nói kiến ​​trúc là một góc độ kinh doanh. Tôi sẽ bắt đầu bài học này bằng cách thảo luận cách tổ chức các nhóm để xây dựng các ứng dụng Microsoft nói mà bạn tìm hiểu về mối quan hệ giữa khả năng kinh doanh và các dịch vụ của Microsoft.

2
00:00:16,650 --> 00:00:33,290
Đến cuối bài học này, bạn sẽ có thể giải thích các lợi ích kinh doanh của kiến ​​trúc Microsoft khi các dịch vụ vi mô đã được xác định trong ứng dụng Microsoft, mỗi dịch vụ vi mô được gán cho một nhóm nhỏ.

3
00:00:33,510 --> 00:00:45,570
Những I.T nhỏ này.  đội xây dựng và vận hành.  Microsoft là vậy.  Các thành viên trong các nhóm này xây dựng các kỹ năng khác nhau trên bàn và các nhóm này được hỗ trợ bởi các chuyên gia tên miền.

4
00:00:46,110 --> 00:00:52,350
Một câu hỏi phổ biến được đặt ra vào thời điểm này là quy mô của nhóm tìm kiếm Microsoft sẽ như thế nào?

5
00:00:52,380 --> 00:01:14,790
Và để trả lời câu hỏi này, tôi sẽ trích dẫn ý tưởng của Jeff Bezos về đội ngũ ngu ngốc.  Đầu những năm 2000, khi Amazon đang xây dựng trang web Amazon.com cho kiến ​​trúc của Microsoft, Jeff Bezos và đội ngũ lãnh đạo của ông đã quyết định rằng quy mô của nhóm dịch vụ vi mô sẽ được giữ ở mức tám thành viên.

6
00:01:15,300 --> 00:01:25,390
Và đây là một trích dẫn.  Chúng tôi đã cố gắng tạo ra những đội không lớn hơn mức có thể cho hai người ăn.  Chúng tôi gọi đó là quy tắc nhóm dupatta.

7
00:01:25,950 --> 00:01:39,490
Ý tưởng là có sự hợp tác tốt hơn giữa các nhóm nhỏ hơn, dẫn đến việc phát hành phần mềm thường xuyên, từ đó giúp tổ chức phản ứng nhanh hơn với những thay đổi trong hoạt động kinh doanh nói chung.

8
00:01:39,540 --> 00:01:49,130
Điều này sẽ dẫn đến việc công nghệ trở thành một lợi thế cạnh tranh cho một tổ chức và nói tóm lại.  Mô hình này đã mang lại hiệu quả rất tốt cho Amazon.

9
00:01:49,710 --> 00:01:59,880
Bây giờ là lúc cho một bài kiểm tra.  Trong bài giảng trước, bạn đã biết rằng dịch vụ vi mô là các đơn vị độc lập được xây dựng để hiện thực hóa một khả năng kinh doanh cụ thể.

10
00:02:00,240 --> 00:02:07,440
Câu hỏi của tôi dành cho bạn là lợi ích của việc tổ chức các dịch vụ vi mô xung quanh khả năng kinh doanh là gì?

11
00:02:07,920 --> 00:02:15,390
Jordan, hãy đăng video suy nghĩ của bạn lên một tờ giấy và cùng tôi tìm hiểu những lợi ích của phương pháp này.

12
00:02:16,560 --> 00:02:25,380
Lợi ích đầu tiên của việc tổ chức các dịch vụ vi mô xoay quanh khả năng kinh doanh là mỗi dịch vụ có thể phát triển độc lập.

13
00:02:25,800 --> 00:02:37,880
Hãy để tôi giải thích cho bạn bằng một ví dụ.  Hãy xem xét một ngân hàng cung cấp ba loại sản phẩm cho khách hàng của mình là tài khoản bán lẻ, thẻ tín dụng và tài khoản cho vay và thế chấp.

14
00:02:38,670 --> 00:02:47,010
Giả sử một ứng dụng nguyên khối duy nhất cung cấp tất cả chức năng kinh doanh cần thiết để quản lý các sản phẩm này.

15
00:02:47,310 --> 00:02:56,910
Bây giờ, giả sử có một sự thay đổi trong môi trường kinh doanh đòi hỏi một số thay đổi trong các sản phẩm cho vay và thế chấp để không tạo ra sự thay đổi đối với khoản cho vay và thế chấp.

16
00:02:57,240 --> 00:03:12,160
Ứng dụng nguyên khối sẽ cần phải trải qua một sự thay đổi đòi hỏi sự phối hợp giữa tất cả các nhóm quản lý các mô-đun cho các sản phẩm khác nhau, chẳng hạn như tài khoản bán lẻ, thẻ tín dụng, khoản vay và thế chấp nói chung.

17
00:03:12,540 --> 00:03:26,460
Điều này có ý nghĩa gì từ góc độ kinh doanh?  Điều đó có nghĩa là sự phối hợp giữa các nhóm khác nhau sẽ làm chậm quá trình thực hiện thay đổi đối với các phần khác nhau của ứng dụng.

18
00:03:26,550 --> 00:03:35,100
Ở góc độ kinh doanh, ngân hàng sẽ chậm tung sản phẩm mới ra thị trường.  Vấn đề này được giải quyết với các dịch vụ vi mô.

19
00:03:35,790 --> 00:03:47,170
Kiến trúc nguyên khối này khi được thay thế bằng các dịch vụ vi mô.  Kiến trúc sẽ trông giống như thế này, trong đó mỗi khả năng sẽ được hiện thực hóa trong một dịch vụ vi mô độc lập.

20
00:03:47,220 --> 00:04:01,990
Vì vậy, điều đó có nghĩa là những thay đổi có thể được thực hiện một cách độc lập trên từng dịch vụ này và điều đó chuyển thành lợi ích kinh doanh trong phạm vi phản ứng thúc đẩy có thể đạt được trước những thay đổi trong môi trường kinh doanh.

21
00:04:02,070 --> 00:04:11,390
Ví dụ: nếu có thay đổi về quy định đối với các khoản vay và dịch vụ thế chấp thì sẽ không có thay đổi nào được yêu cầu đối với thẻ tín dụng hoặc tài khoản bán lẻ.

22
00:04:11,640 --> 00:04:18,150
Nhóm làm việc về Dịch vụ vi mô cho vay và thế chấp sẽ có thể thực hiện các thay đổi một cách độc lập.

23
00:04:19,050 --> 00:04:32,070
Kiến trúc Micro Services cho phép doanh nghiệp thực hiện những thay đổi căn bản về cách thức hoạt động.  Hãy xem xét ví dụ này trong đó ngân hàng đã quyết định chuyển đổi hoàn toàn các sản phẩm cho vay và thế chấp.

24
00:04:32,340 --> 00:04:42,410
Trong trường hợp đó, họ có thể dễ dàng thay thế các khoản vay và dịch vụ thế chấp vi mô bằng một dịch vụ vi mô mới thực hiện mô hình hoạt động kinh doanh đã chuyển đổi.

25
00:04:42,420 --> 00:04:52,210
Miễn là dịch vụ vi mô mới này vẫn duy trì hợp đồng giống như dịch vụ vi mô cũ thì sẽ không có thay đổi nào được yêu cầu đối với các dịch vụ vi mô khác.

26
00:04:52,500 --> 00:04:59,850
Lợi ích tiếp theo là nó giúp I.T.  nhóm để hiểu về doanh nghiệp.  Vì vậy, trong trường hợp.

27
00:04:59,990 --> 00:05:11,960
Ngân hàng, nhóm làm việc về tài khoản bán lẻ sẽ cần phải có hiểu biết sâu sắc về tài khoản bán lẻ, nhưng họ có thể không cần đi sâu vào các quy trình kinh doanh xung quanh thẻ tín dụng chẳng hạn.

28
00:05:12,020 --> 00:05:22,640
Nhìn chung, điều đó có nghĩa là I.T.  các nhóm không cần phải đi sâu vào mọi khả năng kinh doanh.  Họ có thể tập trung vào năng lực kinh doanh mà họ đang xây dựng trong dịch vụ vi mô của mình.

29
00:05:23,060 --> 00:05:33,690
Với các dịch vụ vi mô được xây dựng xung quanh khả năng kinh doanh, I.T.  các nhóm có thể đạt được sự liên kết cao hơn với các ưu tiên kinh doanh.

30
00:05:33,710 --> 00:05:47,600
Ví dụ: nếu hoạt động kinh doanh tài khoản bán lẻ không trải qua những thay đổi thường xuyên, nhóm làm việc về tài khoản bán lẻ có thể hoặc dịch vụ có thể quyết định cung cấp dịch vụ y tế của họ hai tuần một lần.

31
00:05:47,610 --> 00:05:59,890
Nhưng giả sử hoạt động kinh doanh cho vay và thế chấp đang trải qua một sự chuyển đổi nghiêm trọng nào đó, trong trường hợp đó, nhóm cho vay và thế chấp có thể quyết định phát hành dịch vụ vi mô của họ mỗi ngày.

32
00:06:00,560 --> 00:06:12,890
Và điều này tóm lại là vì mỗi nhóm dịch vụ vi mô hoạt động độc lập nên họ không dành thời gian để quản lý các ưu tiên kinh doanh xung đột nhau.

33
00:06:12,900 --> 00:06:26,810
Và trên thực tế, điều này sẽ dẫn đến tốc độ định giá doanh nghiệp nhanh hơn.  Bây giờ, nếu tôi tóm tắt cuộc thảo luận, cách tôi sẽ trình bày là các doanh nghiệp cần duy trì khả năng cạnh tranh bằng cách chuyển đổi nhanh chóng.

34
00:06:26,810 --> 00:06:35,060
Và sự chuyển đổi nhanh chóng này cần có sự hỗ trợ từ bộ phận CNTT.  các nhóm để cung cấp giá trị cho thị trường với tốc độ nhanh hơn.

35
00:06:35,150 --> 00:06:47,270
Kiến trúc dịch vụ vi mô là yếu tố hỗ trợ hoặc chất xúc tác cho quá trình chuyển đổi kinh doanh liên tục vì nó giúp CNTT phát triển.  các nhóm di chuyển với tốc độ tương tự như doanh nghiệp.

36
00:06:48,790 --> 00:07:03,550
Một điều quan trọng cần lưu ý là để tận dụng tối đa kiến ​​trúc dịch vụ vi mô, điều quan trọng đối với nhóm dịch vụ vi mô là phải tạo ra mã nghiệp vụ phù hợp cho từng máy chủ vi mô.

37
00:07:03,700 --> 00:07:13,860
Nếu không thực hiện đúng sẽ dẫn đến tình trạng các nhóm phụ thuộc lẫn nhau và điều đó sẽ dẫn đến mất đi lợi thế của kiến ​​trúc dịch vụ vi mô.

38
00:07:14,260 --> 00:07:24,690
Và đây là lúc thiết kế Theo nhu cầu xuất hiện.  Bối cảnh giới hạn của thiết kế hướng miền là sự thể hiện phạm vi kinh doanh của dịch vụ vi mô.

39
00:07:24,910 --> 00:07:31,570
Tôi sẽ không đề cập đến Thiết kế theo nhu cầu ở đây.  Bạn sẽ tìm hiểu tất cả về thiết kế hướng miền trong các phần sau.

40
00:07:32,560 --> 00:07:48,790
Đã đến lúc ôn lại những điểm chính trong bài học này, các nhóm nhỏ hơn sẽ có tốc độ tiếp cận thị trường nhanh hơn.  Các dịch vụ vi mô được tổ chức xoay quanh khả năng kinh doanh và lợi ích của phương pháp này là nó cho phép I.T.  các đội hoạt động độc lập.

41
00:07:48,970 --> 00:08:00,730
Một điểm quan trọng cần lưu ý là nhóm kiến ​​trúc dịch vụ vi mô phải tạo ra phạm vi kinh doanh phù hợp cho từng dịch vụ vi mô để duy trì tính độc lập.

