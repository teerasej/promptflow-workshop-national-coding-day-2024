
# Try integration: weather bot

## 1. สำรวจ

1. เปิด `Exercises/start-05-weather-bot/flow.dag.yaml`
2. เปิด Visual Editor
3. สังเกต input node และ inputs ที่มีการกำหนดว่า question
4. สังเกต output node และ outputs ที่มีการกำหนดว่า result

## 2. แกะชื่อเมืองจาก input 

1.  เพิ่ม LLM node ตั้งชื่อ node ว่า **extract_city_name**
2.  กำหนด connection ตามรายละเอียดด้านล่าง 
    1.  api: chat
    2.  model: gpt-3.5-turbo
    3.  tempurature: 0.7
    4.  max_token: 100
3.  แก้ไขไฟล์ jinja2 ตามรายละเอียดด้านล่าง

  ```

  system:
  You are city's name extractor. you will return only first city's name you found in the given question.

  question:
  {{question}}

  ```

3. บันทึกไฟล์
4. กลับมาที่ visual editor 
5. กำหนด inputs ของ node ให้รับค่าจาก `${inputs.question}`
6. ทดสอบรัน LLM node เพื่อดู output

## 3. query อุณหภูมิของเมืองที่ได้จาก node แรก

1.  เพิ่ม Python node ตั้งชื่อ node ว่า **extract_city_name**
2.  แก้ไขไฟล์ python ตามรายละเอียดด้านล่าง

  ```python

  
  from promptflow import tool
  import requests
  import re

  # The inputs section will change based on the arguments of the tool function, after you save the code
  # Adding type to arguments and return value will help the system show the types properly
  # Please update the function name/signature per need
  @tool
  def my_python_tool(city_name: str) -> str:
      # wttr.in API URL
      base_url = f"https://wttr.in/{city_name}"
      
      # Parameters for the API request
      params = {
          "format": "%t",  # Get only the temperature
      }
      
      try:
          # Make the API request
          response = requests.get(base_url, params=params)
          response.raise_for_status()  # Raise an error for HTTP error responses
          
          # Get the temperature from the response text
          temperature = response.text.strip()
          
          # Remove any '+' or arithmetic symbols
          clean_temperature = re.sub(r'[+\-*/]', '', temperature)
          
          return f"The current temperature in {city_name} is {clean_temperature}."
      except requests.exceptions.RequestException as e:
          print(f"Error querying the temperature: {e}")


  ```

3. บันทึกไฟล์
4. กลับมาที่ visual editor 
5. กำหนด inputs > city_name ของ node ให้รับค่าจาก `${extract_city_name.output}`
6. ทดสอบรัน Python node เพื่อดู output

## 4. สรุปคำแนะนำสำหรับการ result

1.  เพิ่ม LLM node ตั้งชื่อ node ว่า **completer**
2.  กำหนด connection ตามรายละเอียดด้านล่าง 
    1.  api: chat
    2.  model: gpt-3.5-turbo
    3.  tempurature: 0.7
    4.  max_token: 300
3.  แก้ไขไฟล์ jinja2 ตามรายละเอียดด้านล่าง

  ```

  system:
  You are a weather predictor. you will response by use temperature information and user's question to suggest the best solution to live the day to use.

  temperature's information:
  {{temp_info}}

  user's question:
  {{question}}


  ```

3. บันทึกไฟล์
4. กลับมาที่ visual editor 
5. กำหนด inputs ของ node ให้รับค่าตามรายการด้านล่าง
   1. question: ${inputs.question}
   2. temp_info: ${query_temp.output}
6. ทดสอบรัน LLM node เพื่อดู output

## ทดสอบ flow 

1. ทดสอบรัน flow 
   
## Complete flow.dag.yaml

```yml
inputs:
  question:
    type: string
    default: Is it winter in Bangkok?
outputs:
  result:
    type: string
    reference: ${completer.output}
nodes:
- name: extract_city_name
  type: llm
  source:
    type: code
    path: extract_city_name.jinja2
  inputs:
    temperature: 0.7
    max_tokens: 100
    question: ${inputs.question}
    model: gpt-3.5-turbo
  connection: openai_connection_009
  api: chat
- name: query_temp
  type: python
  source:
    type: code
    path: query_temp.py
  inputs:
    city_name: ${extract_city_name.output}
- name: completer
  type: llm
  source:
    type: code
    path: completer.jinja2
  inputs:
    model: gpt-3.5-turbo
    temperature: 0.7
    max_tokens: 300
    temp_info: ${query_temp.output}
    question: ${inputs.question}
  connection: openai_connection_009
  api: chat

```