# PDF OCR CLI

เครื่องมือที่ใช้บนคอมมานด์ไลน์สำหรับแปลงไฟล์ PDF ที่มีรูปภาพ (เช่น เอกสารที่สแกน) เป็นข้อความด้วย OCR (Optical Character Recognition) โดยเฉพาะอย่างยิ่งสำหรับภาษาไทย

## คุณสมบัติ

- แปลงไฟล์ PDF ที่มีรูปภาพ (เช่น เอกสารที่สแกน) เป็นข้อความ
- รองรับการทำ OCR สำหรับภาษาไทย
- มีตัวเลือก OCR หลากหลาย (Tesseract, EasyOCR)
- ปรับค่า DPI ได้ตามต้องการเพื่อเพิ่มความแม่นยำในการทำ OCR
- บันทึกข้อความไปยังไฟล์พร้อมระบุตำแหน่งเลขหน้า

## การติดตั้ง

### สิ่งที่ต้องมีก่อน

1. Python 3.7 หรือสูงกว่า
2. ขึ้นอยู่กับเครื่องมือ OCR ที่เลือกใช้:
   - Tesseract OCR (พร้อมชุดข้อมูลภาษาไทย)
   - หรือ EasyOCR (พร้อม PyTorch)

### การติดตั้ง Tesseract และชุดข้อมูลภาษา

#### macOS
```bash
# ติดตั้ง Tesseract ด้วย Homebrew
brew install tesseract

# ติดตั้งชุดข้อมูลภาษาทั้งหมด (รวมถึงภาษาไทย)
brew install tesseract-lang

# หรือติดตั้งเฉพาะชุดข้อมูลภาษาไทย
brew install tesseract-data-tha
```

#### Ubuntu/Debian
```bash
# ติดตั้ง Tesseract
sudo apt-get update
sudo apt-get install tesseract-ocr

# ติดตั้งชุดข้อมูลภาษาไทย
sudo apt-get install tesseract-ocr-tha
```

#### Windows
1. ดาวน์โหลดตัวติดตั้ง Tesseract จาก [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. ระหว่างการติดตั้ง เลือกติดตั้งชุดข้อมูลภาษาไทยด้วย (Thai language pack)

### การติดตั้งโปรเจค

```bash
# โคลนจาก GitHub
git clone https://github.com/yourusername/pdf-ocr-cli.git
cd pdf-ocr-cli

# สร้าง virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# ติดตั้ง dependencies
pip install -r requirements.txt
```

## การใช้งาน

มีหลายทางเลือกในการรันโปรแกรม:

### 1. ใช้สคริปต์อำนวยความสะดวก

```bash
# สามารถส่งพารามิเตอร์ต่าง ๆ ได้เหมือนการใช้ python -m pdf_ocr
./run_ocr.sh your_file.pdf
```

### 2. รันโดยตรงด้วย Python

```bash
# การใช้งานพื้นฐาน
python -m pdf_ocr your_file.pdf

# ระบุไฟล์เอาท์พุต
python -m pdf_ocr your_file.pdf -o output.txt

# ใช้ EasyOCR แทน Tesseract
python -m pdf_ocr your_file.pdf --engine easyocr

# ตั้งค่า DPI เพื่อคุณภาพที่ดีขึ้น
python -m pdf_ocr your_file.pdf --dpi 300

# ระบุภาษา
python -m pdf_ocr your_file.pdf --lang tha
python -m pdf_ocr your_file.pdf --lang tha+eng

# ระบุตำแหน่งของ tessdata โดยตรง (กรณีมีปัญหากับการค้นหาไฟล์ภาษา)
python -m pdf_ocr your_file.pdf --tessdata-dir /path/to/tessdata
```

## การแก้ปัญหาที่พบบ่อย

### ไม่พบไฟล์ข้อมูลภาษาไทย

หากเจอข้อผิดพลาด:
```
Error opening data file /path/to/tessdata/tha.traineddata
```

วิธีแก้:
1. ตรวจสอบว่าได้ติดตั้งชุดข้อมูลภาษาไทยแล้ว (ดูคำแนะนำด้านบน)
2. ตั้งค่า environment variable `TESSDATA_PREFIX` ให้ชี้ไปที่โฟลเดอร์ที่มีไฟล์ข้อมูลภาษา:
   ```bash
   export TESSDATA_PREFIX="/path/to/tessdata"
   ```
3. หรือใช้ตัวเลือก `--tessdata-dir` เมื่อรันโปรแกรม:
   ```bash
   python -m pdf_ocr your_file.pdf --tessdata-dir /path/to/tessdata
   ```

### ไม่พบ Tesseract

หากเจอข้อผิดพลาดเกี่ยวกับการไม่พบ Tesseract:
1. ตรวจสอบว่าติดตั้ง Tesseract ถูกต้องแล้ว
2. ใช้ตัวเลือก `--tesseract-cmd` เพื่อระบุตำแหน่งของไฟล์ executable โดยตรง:
   ```bash
   python -m pdf_ocr your_file.pdf --tesseract-cmd /path/to/tesseract
   ```

## ตัวอย่างผลลัพธ์

เมื่อประมวลผลเอกสารภาษาไทย คุณจะได้ไฟล์ข้อความที่มีรูปแบบดังนี้:

```
--- Page 1 ---
เนื้อหาจากหน้าแรกของเอกสาร
ข้อความภาษาไทยที่สกัดได้จากรูปภาพ

--- Page 2 ---
เนื้อหาจากหน้าที่สองของเอกสาร
...
```

## การพัฒนาเพิ่มเติม

คุณสามารถช่วยพัฒนาโปรเจคนี้ได้โดย:
1. Fork โปรเจค
2. สร้าง branch สำหรับฟีเจอร์ (`git checkout -b feature/amazing-feature`)
3. Commit การเปลี่ยนแปลง (`git commit -m 'Add some amazing feature'`)
4. Push ไปยัง branch (`git push origin feature/amazing-feature`)
5. เปิด Pull Request

## ใบอนุญาต

MIT
