# MSSV: 24120261
# Họ và tên: Đặng Bùi Thế Bảo

## Tên mô hình: facebook/bart-large-mnli model

## Đường dẫn đến mô hình trên Hugging Face: https://huggingface.co/facebook/bart-large-mnli

## Chức năng của hệ thống:
    - Đây là một mô hình sử dụng cho bài toán Zero-shot Classification (phân loại không cần huấn luyện)
    -Mô hình dựa trên bài toán Natural Language Inference (NLI), được fine-tune trên tập MNLI và có thể áp dụng cho zero-shot classification.
    - Áp dụng vào đồ án thực hiện chức năng phán đoán cảm xúc của người dùng thông qua việc phân tích ngữ nghĩa trong mô tả của người dùng, dùng vào việc đưa ra đề xuất các món ăn phù hợp vơi staam trạng của người dùng lúc đó

## Cài đặt các thư viện cần thiết: pip install -r requirements.txt

## Hướng đãn chạy chương trình:
    Cách chạy:
        1. Mở file .ipynb trên Google Colab
        2. Run toàn bộ cell
        3. Chạy lệnh mở public API(trong terminal  trên colab): ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io
        4. Lấy URL public → dùng để gọi API
        Lưu ý: dán đường link public mới thay cho  link cũ mỗi khi mở server public một lần

## Hướng dẫn gọi API
    Cách gọi:
        1. import thư viên request
        2. Viết code gọi API:
            import requests
            API_URL = "Đường link public API/endpoint"
            params = {"message": "I just broke up with my girl friend"}
            response = requests.[phương thức](API_URL, params=params)
            print(response.json())

## Đường link video mô tả: https://drive.google.com/drive/folders/1_KBbpkl-CSMgsVkFRWltcUm4QtODxtK9

## Câu trúc repo
facebookbart-large-mnli/                  
├── src/                     # Mã nguồn chính (Source code)
│   ├── BuildModel.py  
│   ├── InitializeAPI.py     
│   └── RunMoDel.py         
├── test/                    # Thư mục chứa các script kiểm thử API
│   ├── Test_Local_API.py    
│   └── Test_Public_API.py   
├── .gitignore              
├── config.yaml              
├── Demo_Model.ipynb         
├── README.md                
└── requirements.txt         