
# Add LLM Node

## 1. สร้าง OpenAI connection 

1. เปิดกลับมาที่ Promptflow Activity > Connection > OpenAI > กดปุ่ม new connection จะมีไฟล์ใหม่เปิดขึ้นมา

     <img width="459" alt="2024-11-28_22-09-00" src="https://github.com/user-attachments/assets/4f341c12-64c0-4601-9d20-f48c912c8945">

2. แก้ไขการตั้งค่าในไฟล์ 
   1. name: openai_connection_001
   2. organization: นำค่าที่อยู่ใน OpenAI Platform > setting > Organization > General มาใส่
   3. เมื่อเสร็จแล้ว กดปุ่ม Create connection (หรือใช้การบันทึกการแก้ไขไฟล์ก็ได้)

    <img width="848" alt="2024-11-28_22-15-56" src="https://github.com/user-attachments/assets/7a719f53-d461-4594-a333-c264f717d618">

3. จุดนี้ใน terminal ถึงจะให้เราใส่ API key ที่คัดลอกมาจากหน้าเว็บของ OpenAI Platform 
   
   <img width="490" alt="2024-11-28_22-16-52" src="https://github.com/user-attachments/assets/ff73569f-a787-49f9-a307-75dee5e48a06">

4. กด enter เพื่อสร้าง secrets profile ถ้าสร้างสำเร็จจะมีข้อความนี้ขึ้นมาใน terminal

    ```
    ================== Required secrets collected ===================
    ```

    > ถ้าไม่ได้ลองสั่งติดตั้ง `pip install keyrings.alt` ผ่าน terminal และลองอีกที

5. กลับมาเช็คใน Prompflow Activity > Connections > OpenAI จะมีชื่อของ connection แสดงขึ้นมา ตรงนี้สามารถนำไปใช้ใน flow ได้ 

    <img width="376" alt="2024-11-28_22-21-18" src="https://github.com/user-attachments/assets/4549a03b-d4a8-4fca-815f-ee741e00d120">


## 2. ปรับเพิ่ม LLM Node ใน flow

1. เปิด `Exercises/start-04-llm-node/flow.dag.yaml`
2. เปิด Visual Editor
3. กดปุ่ม **Add new node** และเลือก **LLM**
4. ตั้งชื่อ node ว่า **ai_model**
5. เลือก **new file**
6. ลงมาที่ **ai_model** node 
7. ให้เลือกตั้งค่าตามนี้
   1. connection: เลือกชื่อ connection ที่สร้างไว้ 
   2. api: chat
   3. model: gpt-3.5-turbo
   4. tempurature: 0.7
   5. max token: 300

    <img width="819" alt="2024-11-28_22-24-45" src="https://github.com/user-attachments/assets/2ba64561-f0c3-416e-a026-bedc0cd770c1">


8. กดเปิดไฟล์ `ai_model.jinja2` สังเกตว่าส่วน inputs มี 2 parameters คือ **chat_history** และ **question**
9. แก้ไข prompt ใน jinja2 ให้เป็นแบบตามข้อความด้านล่าง และบันทึกไฟล์

    ```

    system:
    You are a helpful assistant.

    user:
    {{question}}

    ```

10. กลับมาที่ Visual Editor จะสังเกตเห็นว่ารายชื่อของ inputs ใน **ai_model** node เหลือแค่ **question**
11. ทำการแก้ไขการตั้งค่าของ node แต่ละอันตามภาพ หรือรายละเอียดด้านล่าง 
    1. Inputs
        1. Inputs > message: `nextflow`
    2. Outputs
        1. result: `${ai_model.output}`
    3. ai_model
       1. Inputs > question: `${inputs.message}`

12. ทดสอบรัน flow และสังเกต output 
    
## Complete flow.dag.yaml

```yml
inputs:
  message:
    type: string
    default: nextflow
outputs:
  result:
    type: string
    reference: ${ai_model.output}
nodes:
- name: complete_message
  type: python
  source:
    type: code
    path: complete_message.py
  inputs:
    message: ${inputs.message}
- name: ai_model
  type: llm
  source:
    type: code
    path: ai_model.jinja2
  inputs:
    model: gpt-3.5-turbo
    temperature: 0.7
    max_tokens: 300
    question: ${complete_message.output}
  connection: openai_connection_009
  api: chat

```