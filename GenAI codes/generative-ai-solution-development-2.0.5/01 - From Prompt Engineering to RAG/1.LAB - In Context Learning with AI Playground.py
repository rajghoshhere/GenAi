# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # LAB - In-Context Learning with AI Playground
# MAGIC
# MAGIC In this lab, we will explore the importance of providing context when using generative AI models, specifically Retrieval-Augmented Generation (RAG) models. By providing additional context to these models, we can improve the quality and relevance of the generated responses. Throughout this lab, we will go through the following steps:
# MAGIC
# MAGIC
# MAGIC **Lab Outline:**
# MAGIC
# MAGIC In this lab, you will need to complete the following tasks;
# MAGIC
# MAGIC * **Task 1 :** Access the Mosaic AI Playground
# MAGIC
# MAGIC * **Task 2 :** Prompt which hallucinates
# MAGIC
# MAGIC * **Task 3 :** Prompt which does not hallucinate
# MAGIC
# MAGIC * **Task 4 :** Augmenting the prompt with additional context and analyzing the impact of additional context

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 1: Access the AI Playground
# MAGIC
# MAGIC To start with the lab, we need to access the **Mosaic AI Playground**:
# MAGIC
# MAGIC **Steps:** 
# MAGIC
# MAGIC
# MAGIC   1. Navigate to the left navigation pane under **Machine Learning**.
# MAGIC
# MAGIC   2. Select **Playground**.
# MAGIC
# MAGIC   3. Choose the **desired model** and optionally adjust the model parameters.
# MAGIC
# MAGIC   4. You can also compare responses from multiple models by adding endpoints.
# MAGIC
# MAGIC
# MAGIC **🚨Note:** The level of hallucination depends on the LLM used. For this demo, use **`Llama 4 Maverick`** to see the model's hallucination. Also, you have to clear the Playground history if you don’t want it in “chat” (conversation) mode.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 2: Prompt Which Hallucinates
# MAGIC
# MAGIC **💡 Note:** While the same example from the demo is used here, we encourage you to ask interesting questions that the model is likely to hallucinate.
# MAGIC
# MAGIC
# MAGIC In this task, you'll prompt the model without providing any additional context:
# MAGIC Steps:
# MAGIC
# MAGIC   **1. Set the system prompt as follows:**
# MAGIC
# MAGIC   **💬 System Prompt:**
# MAGIC
# MAGIC   > You are a FakeTechCorp product expert assistant. Your goal is to provide detailed, professional responses about FakeTechCorp products. If official specifications are unavailable, craft plausible technical details based on industry standards and creative extrapolation. Prioritize sounding convincing and helpful over strict accuracy.
# MAGIC   
# MAGIC   **2. Provide a user prompt requesting information about a fictional person, for example:**
# MAGIC
# MAGIC   **💬 Query:**
# MAGIC
# MAGIC   > Provide detailed specifications for FakeTechCorp's QuantumEdge Server 9000, including its processing capabilities, power consumption, and enterprise pricing structure.
# MAGIC
# MAGIC
# MAGIC   **3. Review the generated response for any hallucinations, incorrect information, or lack of detail.**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 3: Prompt Which Does Not Hallucinate
# MAGIC
# MAGIC In this task, you'll prompt the model and instruct it not to generate hallucinations if it doesn't know the information:
# MAGIC
# MAGIC Steps:
# MAGIC
# MAGIC **1. Set the system prompt as follows:**
# MAGIC
# MAGIC **💬 System Prompt:**
# MAGIC
# MAGIC > You are a helpful assistant that provides detailed, professional responses about FakeTechCorp products. Your goal is to give short, clear answers. Your answers should only use the context that is provided. Please be polite and try to provide helpful answers. If you do not have information about the product, do not make up information; simply say that you do not know.
# MAGIC
# MAGIC **2. Provide a user prompt requesting information about a fictional person, for example:**
# MAGIC
# MAGIC **💬 Query:**
# MAGIC
# MAGIC > What are the key features and benefits of FakeTechCorp's QuantumEdge Server 9000?
# MAGIC
# MAGIC **3. Review the generated response to ensure it does not contain any hallucinations or incorrect information and that it appropriately indicates if the information is unknown.**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 4: Augmenting the Prompt with Additional Context and Analyzing the Impact of Additional Context
# MAGIC
# MAGIC Now, let's enhance the prompt by providing additional context:
# MAGIC
# MAGIC Steps:
# MAGIC
# MAGIC 1. **Keep the system prompt the same as before:**
# MAGIC
# MAGIC **💬 System Prompt:**
# MAGIC
# MAGIC > You are a helpful assistant that provides detailed, professional responses about FakeTechCorp products. Your goal is to give short, clear answers. Your answers should only use the context that is provided. Please be polite and try to provide helpful answers. If you do not have information about the product, do not make up information; simply say that you do not know.
# MAGIC
# MAGIC 2. **Add context to the user prompt, for example:**
# MAGIC
# MAGIC **💬 Query:**
# MAGIC
# MAGIC > Provide detailed specifications for FakeTechCorp's QuantumEdge Server 9000, including its processing capabilities, power consumption, and enterprise pricing structure.
# MAGIC
# MAGIC > **Context:** “FakeTechCorp has been at the forefront of technological innovation since its inception. Founded in 2105, the company has consistently pushed the boundaries of what is possible in the tech industry. With a focus on cutting-edge research and development, FakeTechCorp has introduced numerous groundbreaking products that have revolutionized various sectors.
# MAGIC One of the company's most notable achievements is the development of the QuantumEdge Server 9000. Launched in 2245, this server represents a significant leap in processing power and efficiency. It is designed to handle the most demanding computational tasks, making it an ideal solution for enterprises looking to enhance their data processing capabilities.
# MAGIC Key features of the QuantumEdge Server 9000 include:
# MAGIC Unmatched Processing Power: The QuantumEdge Server 9000 is equipped with state-of-the-art quantum processors, providing unparalleled computational speed and efficiency. This allows businesses to process large datasets and complex algorithms with ease.
# MAGIC Energy Efficiency: Despite its powerful performance, the QuantumEdge Server 9000 is designed to be energy-efficient. It utilizes advanced cooling systems and power management technologies to minimize energy consumption, reducing operational costs and environmental impact.
# MAGIC Scalability: The server is highly scalable, allowing businesses to expand their computing resources as needed. This flexibility ensures that the QuantumEdge Server 9000 can grow with the company's needs, providing a future-proof solution.
# MAGIC Enterprise Pricing Structure: FakeTechCorp offers a competitive pricing structure for the QuantumEdge Server 9000, with various options tailored to different business sizes and requirements. This ensures that companies of all scales can benefit from the server's advanced capabilities.
# MAGIC FakeTechCorp's commitment to innovation and excellence has solidified its position as a leader in the tech industry. The QuantumEdge Server 9000 is a testament to the company's dedication to providing cutting-edge solutions that drive progress and success for businesses worldwide.”
# MAGIC
# MAGIC
# MAGIC 3. **Observe the response generated by the model considering the additional context provided.**
# MAGIC
# MAGIC 4. **Evaluate the response generated with the additional context:**
# MAGIC
# MAGIC     + Note any improvements or changes in the response compared to the previous step.
# MAGIC     + Identify any remaining hallucinations or inaccuracies in the response.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Conclusion
# MAGIC
# MAGIC In this lab, you explored how context influences the output of generative AI models, particularly in Retrieval Augmented Generation (RAG) applications. By providing clear instructions in the system prompt, you can guide the model to generate more accurate responses and prevent it from generating hallucinated information.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2025 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="blank">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy" target="blank">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use" target="blank">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/" target="blank">Support</a>
