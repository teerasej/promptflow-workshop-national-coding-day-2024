# Prompt flow workshop in National Coding Day 2024 

by [Teerasej Jiraphatchandej](https://linktr.ee/teerasej), [Microsoft MVP - AI Platform](https://mvp.microsoft.com/en-US/MVP/profile/1b57773c-a042-e711-8112-3863bb2ed1f8)


## Part 0: Survey!

https://app.sli.do/event/39g7dBLfG9ov3Dsz6Xmg4v


## Part 1: ⚠️💰 Cost Alert! 

ในการทำ workshop นี้ ทางผู้เข้าร่วม workshop จะมีการใช้บัญชี Microsoft Azure Account หรือ OpenAI Developer Account อย่างใดอย่างหนึ่งในการทำ workshop ซึ่งจะมีค่าใช้จ่ายจากการใช้บริการดังกล่าวของตนเองนะครับ 

### A. ถ้าต้องการใช้ Open AI Platform

1. ต้องมีบัญชี OpenAI Developer Account และสามารถใช้งานได้ (สมัครได้ที่นี่ [OpenAI Developer Account](https://platform.openai.com/signup))
2. ถ้ามีบัญชีเดิมอยู่แล้ว ให้[เข้าไปเช็ค billing ว่ามี credit พร้อมใช้งานไหม](https://platform.openai.com/settings/organization/billing/overview) ถ้าไม่มีอาจจะต้องผูกบัตรเครดิตของตัวเอง เพื่อเติมเครดิตเข้าไปในบัญชีนะครับ 10 ดอลลาร์ ก็ได้ไม่ต้องมาก
3. ของสำคัญที่ต้องใช้ใน workshop มีดังนี้ครับ
   1. Orginization ID ที่สามารถ copy ได้จากหน้า [Organization Setting](https://platform.openai.com/settings/organization/general)
        <img width="837" alt="2024-11-28_18-05-02" src="https://github.com/user-attachments/assets/02723369-2d0d-42d2-b56a-ed2a19866a12">
    2. API Key ที่สามารถ copy ได้จาก[หน้า API Key](https://platform.openai.com/settings/organization/api-keys)
        <img width="834" alt="2024-11-28_18-08-40" src="https://github.com/user-attachments/assets/bc4f5e1c-3fed-43c0-993a-f13a370ecf17">

### B. ถ้าต้องการใช้ Azure OpenAI Service

1. ต้องมีบัญชี Microsoft Azure Account และสามารถใช้งานได้
2. ต้องมี Subscription ที่สามารถใช้งาน Azure OpenAI Service ได้ (ส่วนใหญ่จะต้องเป็น account ขององค์กรที่เปิดให้สามารถใช้งาน หรือสร้าง resource ได้)
3. สร้าง [Azure OpenAI Resource ที่นี่](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/OpenAI) 
4. ส่วนสำคัญที่ต้องมีสำหรับการใช้งานใน workshop คือ Endpoint และ Key ที่สามารถ copy ได้จากหน้า Key and Endpoint ของ resource นั้นๆ
    <img width="843" alt="2024-11-28_18-12-25" src="
   <img width="843" alt="2024-11-28_18-12-25" src="https://github.com/user-attachments/assets/50f6d6d8-c386-4b9f-b671-3155a9711163">


## Part 2: การเตรียมระบบสำหรับใช้ใน Workshop 

เลือกได้แบบใดแบบหนึ่ง 

1. แบบที่สะดวกที่สุดคือ กดสร้าง Github Codespace จากปุ่มด้านล่าง และข้ามไปยังส่วน exercise ได้เลย

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/teerasej/promptflow-workshop-national-coding-day-2024)

> Github codespace เป็นบริการที่ Github ให้บริการให้เราสามารถสร้าง environment สำหรับการพัฒนาโปรเจคได้ทันที โดยไม่ต้องติดตั้งอะไรเลย และสามารถเข้าใช้งานผ่านเว็บเบราว์เซอร์ได้ทันที [ดูรายละเอียดปริมาณการใช้งานได้จากที่นี่](https://github.blog/changelog/2022-11-09-codespaces-for-free-and-pro-accounts/?utm_source=chatgpt.com)


1. แบบที่ 2 คือ การเตรียมเครื่องเอง โดย[ติดตั้งโปรแกรมตามขั้นตอนต่อไปนี้](/instructions/setup-local.md) และข้ามไปยังส่วน exercise ได้เลย

## Exercise

1. [Checking Environment](/instructions/checking-env.md)
2. [First Flow](/instructions/first-flow.md) 
3. [Adding Python Node](/instructions/python-node.md)
4. [Adding LLM Node](/instructions/llm-node.md)
5. [Weather bot](/instructions/rag.md)


## Next Chapter 

- Microsoft Prompt Flow [Document](https://microsoft.github.io/promptflow/index.html)

## Reference

[![Python package](https://img.shields.io/pypi/v/promptflow)](https://pypi.org/project/promptflow/)
[![Python](https://img.shields.io/pypi/pyversions/promptflow.svg?maxAge=2592000)](https://pypi.python.org/pypi/promptflow/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/promptflow)](https://pypi.org/project/promptflow/)
[![CLI](https://img.shields.io/badge/CLI-reference-blue)](https://microsoft.github.io/promptflow/reference/pf-command-reference.html)
[![vsc extension](https://img.shields.io/visual-studio-marketplace/i/prompt-flow.prompt-flow?logo=Visual%20Studio&label=Extension%20)](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

[![Doc](https://img.shields.io/badge/Doc-online-green)](https://microsoft.github.io/promptflow/index.html)
[![Issue](https://img.shields.io/github/issues/microsoft/promptflow)](https://github.com/microsoft/promptflow/issues/new/choose)
[![Discussions](https://img.shields.io/github/discussions/microsoft/promptflow)](https://github.com/microsoft/promptflow/issues/new/choose)
[![CONTRIBUTING](https://img.shields.io/badge/Contributing-8A2BE2)](https://github.com/microsoft/promptflow/blob/main/CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/github/license/microsoft/promptflow)](https://github.com/microsoft/promptflow/blob/main/LICENSE)

> Welcome to join us to make prompt flow better by
> participating [discussions](https://github.com/microsoft/promptflow/discussions),
> opening [issues](https://github.com/microsoft/promptflow/issues/new/choose),
> submitting [PRs](https://github.com/microsoft/promptflow/pulls).


## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## Code of Conduct

This project has adopted the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com)
with any additional questions or comments.

## Data Collection

The software may collect information about you and your use of the software and
send it to Microsoft if configured to enable telemetry.
Microsoft may use this information to provide services and improve our products and services.
You may turn on the telemetry as described in the repository.
There are also some features in the software that may enable you and Microsoft
to collect data from users of your applications. If you use these features, you
must comply with applicable law, including providing appropriate notices to
users of your applications together with a copy of Microsoft's privacy
statement. Our privacy statement is located at
https://go.microsoft.com/fwlink/?LinkID=824704. You can learn more about data
collection and use in the help documentation and our privacy statement. Your
use of the software operates as your consent to these practices.

## License

Copyright (c) Amaround. All rights reserved.

Licensed under the [MIT](LICENSE) license.
