import qrcode

# Создаем объект QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

# Добавляем данные в QR-код
data = "https://github.com/qweope"
qr.add_data(data)
qr.make(fit=True)

# Создаем изображение QR-кода
img = qr.make_image(fill_color="black", back_color="white")

# Сохраняем изображение в файл
img.save("qrcode.png")