MSSV: 24120261
Họ và tên: Đặng Bùi Thế Bảo

Tên mô hình: facebook/bart-large-mnli model

Đường dẫn đến mô hình trên Hugging Face: https://huggingface.co/facebook/bart-large-mnli

Chức năng của hệ thống:
    - Đây là một mô hình sử dụng cho bài toán Zero-shot Classification (phân loại không cần huấn luyện)
    - Mô hình được huấn luyện bằng cách làm xáo trộn văn bản và thêm chi tiết gây nhiễu rồi học cách khôi phục lại bản gốc dẫn đến kiến trúc này hiểu rất rõ ngữ nghĩa của câu
    - Áp dụng vào đồ án thực hiện chức năng phán đoán cảm xúc của người dùng thông qua việc phân tích ngữ nghĩa trong mô tả của người dùng, dùng vào việc đưa ra đề xuất các món ăn phù hợp vơi staam trạng của người dùng lúc đó

Cài đặt các thư viện cần thiết: pip install -r requirements.txt

Hướng đãn chạy chương trình:
    - Sử dụng Google Colab để mở file .ipynb
    - thực hiện run từng đoạn code cell trong file
    - Mở Terminal -> nhập lệnh: ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io để mở server public
    - Chạy cell Public API call để gọi API
    - Sao chép đường dẫn sau khi chạy xong lệnh trên rồi mở bằng tab trình duyệt khác