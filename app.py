# from flask import Flask, render_template, request, redirect, url_for
# from PIL import Image, ImageEnhance
# import os

# app = Flask(__name__)

# # Thư mục lưu ảnh tải lên
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Tên file cố định cho ảnh kết quả
# OUTPUT_FILE = os.path.join("static", "output.jpg")

# # Chức năng lật ảnh
# def flip_image(img, flip_type):
#     image = Image.open(img)
#     if flip_type == 'vertical':
#         flipped_img = image.transpose(Image.FLIP_TOP_BOTTOM)  # Lật ảnh theo chiều dọc
#     elif flip_type == 'horizontal':
#         flipped_img = image.transpose(Image.FLIP_LEFT_RIGHT)  # Lật ảnh theo chiều ngang
#     flipped_img.save(OUTPUT_FILE)  # Lưu ảnh đã lật vào tệp cố định
#     return flipped_img

# # Chức năng ghép ảnh
# def merge_images(img1, img2):
#     img1 = Image.open(img1)
#     img2 = Image.open(img2)
    
#     # Ghép ảnh ngang (side by side)
#     merged_img = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
#     merged_img.paste(img1, (0, 0))
#     merged_img.paste(img2, (img1.width, 0))
    
#     return merged_img

# # làm mờ ảnh
# from PIL import ImageFilter

# # Chức năng làm mờ ảnh
# def blur_image(img, blur_level):
#     image = Image.open(img)
#     blurred_img = image.filter(ImageFilter.GaussianBlur(blur_level))  # Làm mờ ảnh với độ mờ
#     return blurred_img


# # Chức năng làm nét ảnh
# def sharpen_image(img):
#     image = Image.open(img)
#     enhancer = ImageEnhance.Sharpness(image)
    
#     # Kiểm tra các mức độ làm nét, thử tăng lên 2.5 hoặc 3.0
#     sharpened_img = enhancer.enhance(3.0)  # Tăng độ nét mạnh mẽ hơn
#     return sharpened_img

# # Chức năng chuyển ảnh thành đen trắng
# def convert_to_black_and_white(img):
#     image = Image.open(img)
#     bw_img = image.convert('L')  # Chuyển thành ảnh đen trắng
#     return bw_img

# # Chức năng cắt ảnh
# def crop_image(img, left, upper, right, lower):
#     image = Image.open(img)
#     cropped_img = image.crop((left, upper, right, lower))  # Cắt ảnh theo vùng xác định
#     return cropped_img

# # Trang chủ (chọn chức năng)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')

# # Trang chọn ảnh và chức năng
# @app.route('/upload/<function_type>', methods=['GET', 'POST'])
# def upload(function_type):
#     function_names = {
#         'merge': 'Ghép Ảnh',
#         'sharpen': 'Làm Nét Ảnh',
#         'bw': 'Chuyển Ảnh Thành Đen Trắng',
#         'flip': 'Lật Ảnh',
#         'crop': 'Cắt Ảnh',
#         'blur': 'Làm Mờ Ảnh'  # Thêm chức năng làm mờ ảnh
#     }
#     function_name = function_names.get(function_type, 'Chức Năng Chưa Xác Định')
    
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(file_path)

#             # Thực hiện chức năng xử lý ảnh
#             if function_type == 'merge':
#                 file2 = request.files['file2']
#                 if file2:
#                     file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
#                     file2.save(file2_path)
#                     merged_img = merge_images(file_path, file2_path)
#                     merged_img.save(OUTPUT_FILE)  # Lưu ảnh ghép vào tệp cố định
#                     return redirect(url_for('result'))

#             elif function_type == 'sharpen':
#                 sharpened_img = sharpen_image(file_path)
#                 sharpened_img.save(OUTPUT_FILE)  # Lưu ảnh làm nét vào tệp cố định
#                 return redirect(url_for('result'))

#             elif function_type == 'bw':
#                 bw_img = convert_to_black_and_white(file_path)
#                 bw_img.save(OUTPUT_FILE)  # Lưu ảnh đen trắng vào tệp cố định
#                 return redirect(url_for('result'))

#             elif function_type == 'flip':
#                 flip_type = request.form.get('flip_type')  # Lấy kiểu lật ảnh (vertical/horizontal)
#                 if flip_type:
#                     flipped_img = flip_image(file_path, flip_type)
#                     flipped_img.save(OUTPUT_FILE)  # Lưu ảnh lật vào tệp cố định
#                     return redirect(url_for('result'))

#             elif function_type == 'blur':
#                 blur_level = float(request.form['blur_level'])  # Lấy mức độ làm mờ từ form
#                 blurred_img = blur_image(file_path, blur_level)
#                 blurred_img.save(OUTPUT_FILE)  # Lưu ảnh làm mờ vào tệp cố định
#                 return redirect(url_for('result'))

#             elif function_type == 'crop':
#                 left = int(request.form['left'])
#                 upper = int(request.form['upper'])
#                 right = int(request.form['right'])
#                 lower = int(request.form['lower'])
#                 cropped_img = crop_image(file_path, left, upper, right, lower)
#                 cropped_img.save(OUTPUT_FILE)  # Lưu ảnh đã cắt vào tệp cố định
#                 return redirect(url_for('result'))

#     return render_template('upload.html', function_name=function_name, function_type=function_type)

# # Route cho trang cắt ảnh
# @app.route('/crop', methods=['GET', 'POST'])
# def crop():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(file_path)

#             # Lấy các giá trị từ form để cắt ảnh
#             left = int(request.form['left'])
#             upper = int(request.form['upper'])
#             right = int(request.form['right'])
#             lower = int(request.form['lower'])
            
#             # Cắt ảnh và lưu vào output
#             cropped_img = crop_image(file_path, left, upper, right, lower)
#             cropped_img.save(OUTPUT_FILE)  # Lưu ảnh đã cắt vào tệp cố định
#             return redirect(url_for('result'))  # Chuyển hướng đến trang kết quả

#     return render_template('crop.html')  # Trả về trang HTML cho việc cắt ảnh
# # Trang xem kết quả
# @app.route('/result')
# def result():
#     return render_template('result.html', result_img='output.jpg')

# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np

app = Flask(__name__)

# Thư mục lưu ảnh tải lên
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tên file cố định cho ảnh kết quả
OUTPUT_FILE = os.path.join("static", "output.jpg")

# Chức năng lật ảnh
def flip_image(img_path, flip_type):
    image = cv2.imread(img_path)
    if flip_type == 'vertical':
        flipped_img = cv2.flip(image, 0)  # Lật ảnh theo chiều dọc
    elif flip_type == 'horizontal':
        flipped_img = cv2.flip(image, 1)  # Lật ảnh theo chiều ngang
    cv2.imwrite(OUTPUT_FILE, flipped_img)  # Lưu ảnh đã lật
    return OUTPUT_FILE

# Chức năng chuyển ảnh thành đen trắng
def convert_to_black_and_white(img_path):
    image = cv2.imread(img_path)
    bw_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Chuyển thành ảnh đen trắng
    cv2.imwrite(OUTPUT_FILE, bw_img)  # Lưu ảnh đen trắng
    return OUTPUT_FILE

# Chức năng ghép ảnh
def merge_images(img_path1, img_path2):
    img1 = cv2.imread(img_path1)
    img2 = cv2.imread(img_path2)

    # Đảm bảo hai ảnh có cùng chiều cao
    if img1.shape[0] != img2.shape[0]:
        new_height = max(img1.shape[0], img2.shape[0])
        img1 = cv2.resize(img1, (img1.shape[1], new_height))
        img2 = cv2.resize(img2, (img2.shape[1], new_height))

    # Lấy thông tin kích thước ảnh
    height, width1, channels = img1.shape
    _, width2, _ = img2.shape

    # Tạo mảng trống cho ảnh ghép
    merged_width = width1 + width2
    merged_image = np.zeros((height, merged_width, channels), dtype=np.uint8)

    # Sao chép pixel từ img1 sang merged_image
    for y in range(height):
        for x in range(width1):
            for c in range(channels):
                merged_image[y, x, c] = img1[y, x, c]

    # Sao chép pixel từ img2 sang merged_image
    for y in range(height):
        for x in range(width2):
            for c in range(channels):
                merged_image[y, x + width1, c] = img2[y, x, c]

    # Lưu ảnh kết quả
    cv2.imwrite(OUTPUT_FILE, merged_image)
    return OUTPUT_FILE

# Chức năng làm mờ ảnh (Sử dụng bộ lọc trung bình)
def blur_image(img_path, kernel_size=5):
    # Đảm bảo kernel_size là số lẻ
    if kernel_size % 2 == 0:
        kernel_size += 1  # Nếu kernel_size là số chẵn, thêm 1 để trở thành số lẻ

    image = cv2.imread(img_path)

    # Áp dụng bộ lọc Gaussian với kernel_size
    blurred_img = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Lưu ảnh đã làm mờ
    cv2.imwrite(OUTPUT_FILE, blurred_img)
    return OUTPUT_FILE


# Trang chủ (chọn chức năng)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Trang chọn ảnh và chức năng
@app.route('/upload/<function_type>', methods=['GET', 'POST'])
def upload(function_type):
    function_names = {
        'merge': 'Ghép Ảnh',
        'bw': 'Chuyển Ảnh Thành Đen Trắng',
        'flip': 'Lật Ảnh',
        'blur': 'Làm Mờ Ảnh'
    }
    function_name = function_names.get(function_type, 'Chức Năng Chưa Xác Định')

    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            if function_type == 'merge':
                file2 = request.files['file2']
                if file2:
                    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
                    file2.save(file2_path)
                    merge_images(file_path, file2_path)
                    return redirect(url_for('result'))

            elif function_type == 'bw':
                convert_to_black_and_white(file_path)
                return redirect(url_for('result'))

            elif function_type == 'flip':
                flip_type = request.form.get('flip_type')  # Lấy kiểu lật ảnh
                if flip_type:
                    flip_image(file_path, flip_type)
                    return redirect(url_for('result'))
            elif function_type == 'blur':
                blur_level = int(request.form['blur_level'])  # Lấy mức độ làm mờ từ form
                blur_image(file_path, blur_level)  # Làm mờ ảnh với mức độ được chỉ định
                return redirect(url_for('result'))

    return render_template('upload.html', function_name=function_name, function_type=function_type)

# Trang xem kết quả
@app.route('/result')
def result():
    return render_template('result.html', result_img='output.jpg')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
