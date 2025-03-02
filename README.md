ทดสอบซอฟต์แวร์

## บทนำ
โครงการนี้มุ่งเน้นไปที่วิธีการและการปฏิบัติในการทดสอบซอฟต์แวร์ รวมถึงกรณีทดสอบต่างๆ สคริปต์ และเอกสารเพื่อให้มั่นใจในคุณภาพและความน่าเชื่อถือของซอฟต์แวร์

## การรัน Test Cases
รัน test cases แบบ verbose
```bash
python -m coverage run -m unittest <ไฟล์>
```

## การตรวจสอบ Coverage
รัน test cases พร้อมตรวจสอบ coverage:
```bash
python -m coverage report -m