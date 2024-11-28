
# Add Python Node


1. เปิด `Exercises/start-03-python-node/flow.dag.yaml`
2. เปิด Visual Editor
3. กดปุ่ม **Add new node** และเลือก **Python**

    <img width="640" alt="2024-11-28_21-38-01" src="https://github.com/user-attachments/assets/6b7d4fb0-0672-4030-87e8-54df19847e4c">

4. ตั้งชื่อ node ว่า **complete_message**
5. เลือก **new file**
6. ลงมาที่ **complete_message** node ให้สังเกตในส่วน Inputs ของ node ว่ามีชื่อ **input1** อยู่ในรายการ
7. กดเปิดไฟล์ python ชื่อเดียวกัน สังเกตว่าชื่อ parameter ของ function เหมือนกับช่ือของ inputs 
8. แก้ชื่อ parameter จาก `input1` เป็น `message` และปรับให้ code สอดคล้องกัน

    ```python

    from promptflow import tool


    # The inputs section will change based on the arguments of the tool function, after you save the code
    # Adding type to arguments and return value will help the system show the types properly
    # Please update the function name/signature per need
    @tool
    def my_python_tool(message: str) -> str:
        return 'hello ' + message

    ```

9. บันทึกไฟล์ และกลับมาที่ Visual Editor จะเห็นว่า inputs มีชื่อเปลี่ยนไปตาม code ของเรา
10. ทำการแก้ไขการตั้งค่าของ node แต่ละอันตามภาพ หรือรายละเอียดด้านล่าง 
    1. Inputs
        1. Inputs > message: `nextflow`
    2. Outputs
        1. result: `${complete_message.output}`
    3. Complete_message
       1. Inputs > message: `${inputs.message}`

    <img width="832" alt="2024-11-28_21-48-14" src="https://github.com/user-attachments/assets/9871650a-bd3b-4bfc-b2b7-a58bfae750bc">

11. ทดสอบรัน flow และสังเกต output 
    
## 2. Run node ที่ต้องการแบบเจาะจง

1. ลงมาที่ส่วน **complete_message** node จะสังเกตว่ามีส่วนของปุ่มสำหรับรันทดสอบเฉพาะ node 

    <img width="824" alt="2024-11-28_22-01-45" src="https://github.com/user-attachments/assets/0f6bbb0d-9ca8-4b16-a67c-16919afda932">

2. ให้กดปุ่มเพื่อทดสอบ จะเห็นว่าการทำงานจะมาหยุดที่ node และเห็น output เฉพาะ node ที่เลือก 

## 3. Debug node 

1. เปิดไฟล์ `complete_message.py` และวาง break point ไว้ที่คำสั่ง return statement
2. กลับมาใน Visual Editor 
3. ในส่วนของ flow control ให้ทดสอบกดปุ่ม debug flow 
4. จะเห็นว่าการทำงานของ flow มาหยุดที่ break point เหมือนกับการเขียนโปรแกรมทั่วไป


## Complete flow.dag.yaml

```yml
inputs:
  message:
    type: string
    default: nextflow
outputs:
  result:
    type: string
    reference: ${complete_message.output}
nodes:
- name: complete_message
  type: python
  source:
    type: code
    path: complete_message.py
  inputs:
    message: ${inputs.message}

```