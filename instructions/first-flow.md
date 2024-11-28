
# First flow

## 1. สร้าง Flow แรก

1. จาก Visual Studio Code > Promptflow Activity > Flow > กดปุ่ม new flow
    <img width="411" alt="2024-11-28_20-43-44" src="https://github.com/user-attachments/assets/02301d39-7350-49e3-ace1-caf6f7e438ce">

2. เลือก **Empty flow** 
3. ตั้งชื่อ Flow ว่า `first-flow`
   1. ใน Github Codespace จะมีการสร้าง flow ดังกล่าวในโปรเจค
   2. ใน local machine จะมีการให้เลือกว่าจะเก็บไฟล์ flow ที่ไหนในเครื่อง
4. จะได้ directory ชื่อ `first-flow` 


## 2. รู้จักกับ Flex flow

1. จาก Visual Studio Code เลือก Explore Activity
2. เปิด directory `first-flow` 
3. เปิดไฟล์ `flow.dag.yaml` จะเห็นโครงสร้างของ Flex flow ดังนี้ และให้กดเปิด Visual Editor

    <img width="395" alt="2024-11-28_21-14-53" src="https://github.com/user-attachments/assets/194b8422-40e8-448b-aad2-1bf4835a8a56">


4. จะเห็นว่ามีส่วน `input` และ `output` ซึ่งเราสามารถทดสอบการทำงานของ flow ได้โดยการกดปุ่ม `Run` และจะเห็นผลลัพธ์ที่ได้ในส่วน `output` ด้านล่าง

    <img width="679" alt="2024-11-28_21-16-53" src="https://github.com/user-attachments/assets/7740849e-1c72-4f7e-9028-54f24e2a9c2a">


## 3. การกำหนดตัวแปรใน input และ output 

1. ในส่วนของ Visual Editor ให้มาที่ส่วนของ input และกดปุ่ม **Add input** เพื่อเพิ่มตัวแปรใหม่ และตั้งชื่อว่า `message` 
2. กรอกข้อความในส่วน **default value**
3. มาที่ส่วนของ output ให้กดปุ่ม **Add output** และใส่ชื่อตัวแปรว่า `result` 
4. จากตัวเลือก **Reference** ให้เลือก `inputs.message`

    <img width="799" alt="2024-11-28_21-21-08" src="https://github.com/user-attachments/assets/75894ace-3511-4164-bdb6-438ce0a241f3">

5. ทดสอบรัน flow  
6. เมื่อรันเสร็จให้สังเกตข้อมูลในส่วน **run output**