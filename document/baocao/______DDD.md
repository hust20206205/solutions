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
00:00:00,420 --> 00:00:09,400
Chuyển đổi kinh doanh và kiến ​​trúc dịch vụ vi mô.  Tôi sẽ bắt đầu bài học này bằng cách xác định các thuật ngữ, chuyển đổi kinh doanh và chuyển đổi kỹ thuật số.

2
00:00:09,750 --> 00:00:20,760
Đến cuối bài học này, bạn sẽ có thể mô tả lý do tại sao doanh nghiệp cần chuyển đổi và cách kiến ​​trúc dịch vụ Maiko hỗ trợ doanh nghiệp chuyển đổi.

3
00:00:21,690 --> 00:00:31,260
Chuyển đổi kinh doanh là một thuật ngữ chung được sử dụng
 để đề cập đến những thay đổi cơ bản trong cách một tổ chức tiến hành hoạt động kinh doanh của mình.

4
00:00:31,760 --> 00:00:42,180
Đây là một ví dụ.  Microsoft đã từng bán phần mềm của họ dưới dạng sản phẩm đóng gói dưới dạng đĩa CD và đĩa mềm từ lâu.

5
00:00:42,660 --> 00:00:56,200
Nhưng theo thời gian với sự phát triển của Internet và công nghệ đám mây, ngày nay họ bán phần mềm của mình theo mô hình đăng ký thay vì tính phí một lần cho khách hàng.

6
00:00:56,340 --> 00:01:12,800
Microsoft tính phí khách hàng hàng tháng hoặc hàng năm.  Một ví dụ khác là Amazon.  Amazon khởi đầu là một hiệu sách trực tuyến, nhưng theo thời gian, họ đã biến toàn bộ hiệu sách này thành một thị trường nơi các nhà cung cấp khác cũng có thể bán sản phẩm của họ.

7
00:01:12,810 --> 00:01:24,330
Vì vậy, thay vì phụ thuộc vào hoạt động kinh doanh cốt lõi là bán sách của riêng mình, họ bắt đầu kiếm tiền từ thị trường mà họ đã tạo ra cho các nhà cung cấp bên ngoài.

8
00:01:24,480 --> 00:01:39,360
Ví dụ tiếp theo là Apple.  Apple từng bán máy tính, nhưng trong hai thập kỷ qua, hãng đã chuyển từ máy tính sang iPod, iPhone, iPad, kho nhạc và một số sản phẩm khác.

9
00:01:39,540 --> 00:01:47,760
Họ không còn phụ thuộc vào sản phẩm cốt lõi của mình là máy tính nữa.  Bây giờ, có thể bạn đang thắc mắc tại sao doanh nghiệp cần chuyển đổi?

10
00:01:47,850 --> 00:01:53,490
Có rất nhiều lý do cho nó.  Tôi sẽ đi một số trong những cái phổ biến.  Đầu tiên là những thay đổi về môi trường.

11
00:01:53,520 --> 00:02:10,570
Các quy định mới như GDP có thể buộc tổ chức phải thay đổi cách họ tiến hành kinh doanh.  Tiếp theo là bể áp lực cạnh tranh của một tổ chức đang giao dịch với một đối thủ cạnh tranh đang tung ra các sản phẩm đổi mới với tốc độ rất nhanh.

12
00:02:10,840 --> 00:02:17,510
Bây giờ, sự lựa chọn cho tổ chức này là gì?  Họ phải biến đổi.  Họ phải nghĩ ra sản phẩm mới.

13
00:02:17,520 --> 00:02:24,130
Họ phải suy nghĩ về tốc độ có thể tung ra những sản phẩm mới này.  Trên thực tế, tổ chức cần phải chuyển đổi.

14
00:02:24,300 --> 00:02:37,080
Tiếp theo là những cơ hội mới.  Đầu những năm 90, khi Internet bắt đầu trở nên phổ biến, các doanh nghiệp có cơ hội mới sử dụng Internet để bán sản phẩm và dịch vụ của mình.

15
00:02:37,110 --> 00:02:47,000
Các tổ chức đã phải tự chuyển đổi để tích hợp hoạt động kinh doanh của mình với công nghệ mới này và điều đó đòi hỏi phải có những sáng kiến ​​chuyển đổi nghiêm túc.

16
00:02:47,550 --> 00:03:00,720
Lý do tiếp theo là một trong những lý do lớn nhất khiến tổ chức cần chuyển đổi nhu cầu và mong đợi của khách hàng liên tục thay đổi để duy trì và mở rộng cơ sở khách hàng của mình.

17
00:03:00,750 --> 00:03:12,480
Các tổ chức cần điều chỉnh hoạt động kinh doanh của mình để đáp ứng nhu cầu và mong đợi của khách hàng.  Các doanh nghiệp bỏ qua kỳ vọng của khách hàng có xu hướng thua đối thủ cạnh tranh.

18
00:03:13,170 --> 00:03:27,840
Bây giờ hãy nói về chuyển đổi kỹ thuật số.  Chuyển đổi kỹ thuật số là quá trình sử dụng công nghệ kỹ thuật số để đáp ứng nhu cầu của các quy trình kinh doanh được chuyển đổi và tạo ra các cơ chế tương tác khách hàng sáng tạo.

19
00:03:28,170 --> 00:03:39,090
Mối quan hệ giữa chuyển đổi số và chuyển đổi kinh doanh là chuyển đổi số hỗ trợ các sáng kiến ​​chuyển đổi kinh doanh.

20
00:03:39,270 --> 00:03:50,430
Chúng ta hãy xem qua một số ví dụ.  Target là một cửa hàng bán lẻ ở Mỹ cho đến năm 2011. Trang web và khâu xử lý đơn hàng của họ được gia công cho Amazon.

21
00:03:50,580 --> 00:04:08,820
Năm 2011, Target quyết định chuyển đổi hoạt động kinh doanh của họ.  Họ đã đầu tư rất nhiều vào công nghệ kỹ thuật số để tích hợp hàng tồn kho trong chuỗi cung ứng của mình trên khắp các cửa hàng trong mạng lưới đối tác và kho hàng của họ, đồng thời điều đó cho phép họ tạo ra những trải nghiệm mới cho khách hàng.

22
00:04:08,830 --> 00:04:16,770
Khách hàng có thể đặt hàng trực tuyến và nhận hàng tại cửa hàng trong vòng vài phút sau khi đặt hàng.

23
00:04:17,010 --> 00:04:24,570
Tại thời điểm này, Target liên tục có thể tạo ra những trải nghiệm mới cho khách hàng nhờ nền tảng vững chắc.

24
00:04:24,570 --> 00:04:38,070
Họ đã tạo ra các công nghệ kỹ thuật số mới.  Capital One từng là một ngân hàng vật lý truyền thống, nhưng ngày nay nó thực sự là một ngân hàng kỹ thuật số, không có trung tâm dữ liệu riêng.

25
00:04:38,340 --> 00:04:53,430
Họ phụ thuộc vào đám mây AWG cho tất cả các nhu cầu công nghệ của mình.  Họ sử dụng các dịch vụ khác nhau trên đám mây để hỗ trợ mô hình hoạt động luôn thay đổi của mình và tạo ra những trải nghiệm sáng tạo cho khách hàng.

26
00:04:53,670 --> 00:05:10,590
Amazon.com sử dụng nhiều công nghệ kỹ thuật số để hỗ trợ quá trình chuyển đổi hoạt động kinh doanh của họ.  Các công nghệ như Emelle API Analytics thường được sử dụng và điều này giúp họ thay đổi mô hình kinh doanh với tốc độ rất nhanh.

27
00:05:10,620 --> 00:05:22,540
Điều này giúp họ tạo ra sản phẩm mới trong một khoảng thời gian rất ngắn.  Nhìn chung, việc sử dụng các công nghệ kỹ thuật số này đã giúp Amazon.com trở thành công ty dẫn đầu trong lĩnh vực bán lẻ.

28
00:05:23,610 --> 00:05:33,180
Vì vậy, điều xảy ra với những doanh nghiệp không chuyển đổi, câu trả lời ngắn gọn cho câu hỏi này là những doanh nghiệp không chuyển đổi sẽ không thể tồn tại.

29
00:05:33,420 --> 00:05:42,750
Tôi sẽ cho bạn một ví dụ.  Năm 1997, Netflix bắt đầu cung cấp mô hình đăng ký DVD cải tiến cho khách hàng của mình.

30
00:05:42,900 --> 00:05:51,310
Khách hàng có thể nhận DVD qua thư, xem phim và trả lại cho Netflix để đổi lấy DVD mới hơn.

31
00:05:51,360 --> 00:06:03,430
Năm 2007, Netflix bắt đầu dịch vụ phát trực tuyến bằng cách sử dụng các nền tảng và công nghệ kỹ thuật số mới hơn.  Khách hàng có thể xem phim trên điện thoại di động, máy chơi game và TV.

32
00:06:03,480 --> 00:06:11,720
Mặt khác, Blockbuster đã bỏ qua tất cả những công nghệ kỹ thuật số mới hơn này.  Họ đã thất bại trong việc chuyển đổi hoạt động kinh doanh của mình kịp thời.

33
00:06:11,880 --> 00:06:20,250
Và đoán xem?  Đầu năm 2021, cửa hàng bom tấn cuối cùng đã đóng cửa vào thời điểm này.  Bom tấn không còn trong kinh doanh nữa.

34
00:06:20,890 --> 00:06:36,600
Một điểm quan trọng cần ghi nhớ là chuyển đổi không phải là sáng kiến ​​hay nhiệm vụ chỉ diễn ra một lần.  Các doanh nghiệp cần thay đổi liên tục và điều này đòi hỏi những thay đổi nhanh chóng đối với hệ thống và ứng dụng của họ.

35
00:06:36,810 --> 00:06:47,280
Các tổ chức phải theo kịp tốc độ của các công nghệ mới và đang phát triển.  Một ví dụ điển hình về sự chuyển đổi liên tục là Amazon.

36
00:06:47,520 --> 00:06:57,000
Amazon đang bắt kịp các công nghệ kỹ thuật số mới hơn và cung cấp các sản phẩm và dịch vụ mới cho khách hàng cũng như đối tác của họ.

37
00:06:57,900 --> 00:07:10,650
Một thách thức chung mà các doanh nghiệp phải đối mặt trong hành trình chuyển đổi là cách xây dựng phần mềm cũ cản trở hoặc gây khó khăn cho các tổ chức trong việc chuyển đổi.

38
00:07:10,920 --> 00:07:27,290
Việc xây dựng phần mềm bằng cách sử dụng các công nghệ và mô hình kiến ​​trúc cũ sẽ chậm hơn.  Các công nghệ cũ hơn và cách xây dựng ứng dụng cũ khiến các ứng dụng này khó tích hợp với các công nghệ kỹ thuật số mới hơn.

39
00:07:27,720 --> 00:07:43,390
Và đây là lúc kiến ​​trúc dịch vụ vi mô có thể trợ giúp.  Kiến trúc của Microsoft giải quyết những thách thức này và giúp các tổ chức phát triển với tốc độ nhanh hơn để đạt được các mục tiêu chuyển đổi của mình.

40
00:07:44,910 --> 00:07:55,890
Một câu hỏi hiển nhiên mà bạn có thể muốn hỏi vào thời điểm này là làm thế nào kiến ​​trúc dịch vụ vi mô giúp chuyển đổi trong khi chuyển đổi chỉ là những thay đổi nhanh chóng?

41
00:07:56,310 --> 00:08:05,940
Và trong trường hợp dịch vụ vi mô, các thay đổi về kiến ​​trúc được tách biệt thành một tập hợp các dịch vụ vi mô.  Tôi sẽ giải thích nó bằng một ví dụ về ngân hàng.

42
00:08:06,270 --> 00:08:14,880
Giả sử một ngân hàng đã áp dụng kiến ​​trúc dịch vụ vi mô và điều đó có nghĩa là họ sẽ tạo ra nhiều dịch vụ vi mô.

43
00:08:14,880 --> 00:08:22,140
Mỗi máy chủ vi mô sẽ nhận ra một khả năng kinh doanh.  Ở đây tôi đang hiển thị ba dịch vụ vi mô như vậy.

44
00:08:22,290 --> 00:08:31,320
Các tài khoản bán lẻ.  Dịch vụ vi mô đảm nhiệm chức năng kinh doanh cần thiết cho sản phẩm ngân hàng bán lẻ, chẳng hạn như tài khoản séc và tài khoản tiết kiệm.

45
00:08:31,470 --> 00:08:38,230
Thẻ tín dụng Microsoft.  Điều này nhằm mục đích hiện thực hóa các sản phẩm thẻ tín dụng do ngân hàng cung cấp.

46
00:08:38,370 --> 00:08:50,580
Giả sử ngân hàng quyết định chuyển đổi chiến lược kinh doanh thẻ tín dụng của họ.  Vì vậy, điều đó có nghĩa là sẽ chỉ cần thay đổi thẻ tín dụng, các dịch vụ vi mô.

47
00:08:50,730 --> 00:09:13,770
Và vì không có sự phụ thuộc giữa thẻ tín dụng, dịch vụ vi mô và các dịch vụ vi mô khác nên tốc độ thực hiện và phát hành những thay đổi này sẽ nhanh hơn nhiều so với kiến ​​trúc nguyên khối nơi có sự phụ thuộc lẫn nhau giữa nhiều mô-đun thực hiện  chức năng kinh doanh khác nhau.

48
00:09:13,770 --> 00:09:22,310
Trong bài giảng tiếp theo, bạn sẽ tìm hiểu các lợi ích kinh doanh của kiến ​​trúc dịch vụ vi mô.  Đã đến lúc ôn lại những điểm chính của bài học này.

49
00:09:22,920 --> 00:09:32,590
Các tổ chức cần phải liên tục chuyển đổi.  Sự chuyển đổi này đòi hỏi I.T.  hệ thống thay đổi với tốc độ rất nhanh.

50
00:09:33,000 --> 00:09:47,910
Cần phải áp dụng nhanh chóng các công nghệ kỹ thuật số mới và tốc độ đưa ra thị trường là chìa khóa. Kiến trúc của Microsoft giúp các tổ chức đáp ứng các yêu cầu này từ bộ phận CNTT.  luật xa gần.

