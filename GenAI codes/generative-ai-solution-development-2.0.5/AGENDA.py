# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Generative AI Solution Development
# MAGIC
# MAGIC This course is designed to introduce participants to contextual generative AI solutions using the retrieval-augmented generation (RAG) method. Firstly, participants will be introduced to the RAG architecture and the significance of contextual information using Mosaic AI Playground. Next, the course will demonstrate how to prepare data for generative AI solutions and connect this process with building an RAG architecture. Finally, participants will explore concepts related to context embedding, vectors, vector databases, and the utilization of the Mosaic AI Vector Search product.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Prerequisites
# MAGIC The content was developed for participants with these skills/knowledge/abilities: 
# MAGIC - Familiarity with natural language processing concepts
# MAGIC - Familiarity with prompt engineering/prompt engineering best practices 
# MAGIC - Familiarity with the Databricks Data Intelligence Platform
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Course Agenda  
# MAGIC The following modules are part of the **Generative AI Solution Development** course by **Databricks Academy**.
# MAGIC
# MAGIC | # | Module Name | Lesson Name |
# MAGIC |---|-------------|-------------|
# MAGIC | 1 | [From Prompt Engineering to RAG]($./01 - From Prompt Engineering to RAG) | • *Lecture:* Prompt Engineering Primer <br> • *Lecture:* Introduction to RAG <br> • [Demo: In Context Learning with AI Playground]($./01 - From Prompt Engineering to RAG/1.1 - In Context Learning with AI Playground) <br> • [Lab: In Context Learning with AI Playground]($./01 - From Prompt Engineering to RAG/1.LAB - In Context Learning with AI Playground) |
# MAGIC | 2 | [Preparing Data for RAG Solutions]($./02 - Preparing Data for RAG Solutions) | • *Lecture:* Preparing Data for RAG Solutions <br> • [Demo: Preparing Data for RAG]($./02 - Preparing Data for RAG Solutions/2.1 - Preparing Data for RAG) <br> • [Lab: Preparing Data for RAG]($./02 - Preparing Data for RAG Solutions/2.LAB - Preparing Data for RAG) |
# MAGIC | 3 | [Mosaic AI Vector Search]($./03 - Mosaic AI Vector Search) | • *Lecture:* Introduction to Vector Stores <br> • *Lecture:* Introduction to Mosaic AI Vector Search <br> • [Demo: Create Self-managed Vector Search Index]($./03 - Mosaic AI Vector Search/3.1 - Create Self-managed Vector Search Index) <br> • [Lab: Create Managed Vector Search Index]($./03 - Mosaic AI Vector Search/3.LAB - Create Managed Vector Search Index) |
# MAGIC | 4 | [Assembling and Evaluating a RAG Application]($./04 - Assembling and Evaluating a RAG Application) | • *Lecture:* Assembling a RAG Application <br> • [Demo: Assembling and Evaluating a RAG Application]($./04 - Assembling and Evaluating a RAG Application/4.1 - Assembling and Evaluating a RAG Application) <br> • [Lab: Assembling a RAG Application]($./04 - Assembling and Evaluating a RAG Application/4.LAB - Assembling a RAG Application) |
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * Use Databricks Runtime version: **`15.4.x-cpu-ml-scala2.12`** for running all demo and lab notebooks.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2025 Databricks, Inc. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the <a href="https://www.apache.org/" target="blank">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy" target="blank">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use" target="blank">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/" target="blank">Support</a>
