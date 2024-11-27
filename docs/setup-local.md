
# การติดตั้งโปรแกรมเพื่อใช้

> ถ้าต้องการ เราสามารถใช้ environment control อย่าง [Conda](https://docs.conda.io/en/latest/) หรือ [Pipenv](https://pipenv.pypa.io/en/latest/) หรือ [Poetry](https://python-poetry.org/) ในการจัดการ environment ได้นะครับ แต่ในที่นี้เพื่อให้เรียบง่ายที่สุด ขั้นตอนจะใช้เฉพาะ `pip` ในการจัดการ package ครับ 

## 1. โปรแกรมที่จำเป็นต้องติดตั้ง

1. [Python 3.9 เป็นต้นไป](https://www.python.org/downloads/)
2. [Visual Studio Code](https://code.visualstudio.com/download)
   1. เสร็จแล้วติดตั้ง Extension ตามนี้
      1. [Python Extension](https://code.visualstudio.com/docs/languages/python) 
      2. [Prompt flow for VSCode](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

## 2. ติดตั้ง Python Package 

ขั้นตอนนี้ สามารถใช้โปรแกรม Command Prompt, Powershell, Windows Terminal, หรือ Terminal ได้ตามถนัดตามเครื่องของตัวเองครับ

1. รันคำสั่งต่อไปนี้เพื่อติดตั้ง package ที่จำเป็น

    ```bash
    pip install promptflow promptflow-tools
    ```

    ```bash
    pip install promptflow-devkit promptflow-tracing promptflow-azure
    ```

2. รันคำสั่งเพื่อเช็คว่าในเครื่องเราได้มี package ตามที่เราสั่งติดตั้งเรียบร้อยหรือยัง

    ```bash
    pip list
    ```

    ถ้าเราเห็น package ที่ติดตั้งไว้แล้วใน list แสดงว่าเราติดตั้งเรียบร้อยแล้วครับ

## 3. ใช้งาน Promptflow Extension บน Visual Studio Code

> ในขั้นตอนนี้ ถ้าเราไม่มีการใช้ environment control (ไม่มีการสลับ environment) ก็ให้เลือก default environment ของระบบเรานะครับ

1. เปิดแอพ Visual Studio Code > เปิด Promptflow Activity ทางด้านซ้าย จะสังเกตเห็นว่า dependencies ของ package ยังไม่ถูกติดตั้ง ให้กดเลือก install dependencies

   <img width="508" alt="2024-11-23_20-47-53" src="https://github.com/user-attachments/assets/d025a713-a656-4c2f-a179-14aff01c4aa0">


2. เราจะเห็นหน้าจอสำหรับช่วยติดตั้ง และเช็คความพร้อมของ package ที่จำเป็น ส่วนแรกของเราคือ 
   1. **Python Interpreter** ที่ควรจะแสดงที่อยู่ของ python ที่เราติดตั้งไว้ในเครื่องจากขั้นตอนแรก
   2. กดปุ่ม **Select Python Interpreter** เพื่อไปเลือก python environment ที่เราสร้างไว้ (เช่นในภาพเลือกเป็น default environment )

   <img width="955" alt="2024-11-23_20-50-40" src="https://github.com/user-attachments/assets/9b6c97f8-53e4-41e4-bfda-56ff7c395b87">

3. ให้ทำการเลือก environment ที่เรามี หรือสร้างเตรียมไว้ 

   > ไม่จำเป็นต้องมีชื่อ path ตรงกับในภาพตัวอย่างนะครับ

   <img width="850" alt="2024-11-23_20-59-34" src="https://github.com/user-attachments/assets/1a6c39e0-0997-4b8e-ab01-32773f5335d8">
   
4. รอสักพัก จะเห็นว่าชื่อของ Current Python Interpreter จะเปลี่ยนเป็น environment ที่เราเลือกไว้ (ถ้าไม่เปลี่ยน ให้ลองเปิดและเลือก interpreter ใหม่)

   <img width="863" alt="2024-11-23_20-59-47" src="https://github.com/user-attachments/assets/a08fae27-07b6-4b83-a506-048e0fb8f972">

## 4. เช็คความพร้อมของ Package ที่ติดตั้ง

> ส่วนสำคัญที่ต้องใช้ใน workshop นี้ได้แก่
> 1. promptflow
> 2. promptflow-tools
> 3. promptflow-core
> 4. promptflow-devkit
> 
> ถ้า promptflow-azure หรือ promptflow-tracing ไม่มีก็ไม่เป็นไรนะ

1. จากหน้า Install dependencies เลื่อนมาที่ **Install Status** เพื่อกดปุ่ม refresh ของแต่ละ dependencies เพื่อเช็คว่าติดตั้งเรียบร้อยไหม

   <img width="842" alt="2024-11-23_21-02-31" src="https://github.com/user-attachments/assets/7f954ba3-3366-40c1-b8a7-074fd4fe17e0">


2. ถ้าติดตั้งสมบูรณ์ จะเห็นว่าทุกอันจะเป็นสีเขียว 

   <img width="847" alt="2024-11-23_21-03-12" src="https://github.com/user-attachments/assets/4e2e9840-e1c9-4466-9bb6-39fea8dd4242">


5. ทดสอบว่าติดตั้งสมบูรณ์หรือไม่ โดยปิดและเปิด Visual Studio code ใหม่ และเข้ามาเช็คในส่วน Promptflow Activity > install dependencies ว่าสถานะของ dependencies ยังเป็นสีเขียวหรือไม่



