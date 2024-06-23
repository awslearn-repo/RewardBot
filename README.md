# RewardBot
Generative AI Assistant for Loyalty Reward System Using Amazon Bedrock Knowledge bases & Agent.

Let's use the example of building a **RewardBot** to illustrate the process, and if you're interested in learning how to build a chatbot using AWS services then this blog post is perfect for you. 

_Retail Rewards Inc.,_ a fictitious retail company, is taking generative AI to its customers. The functionalities of the first version of RewardBot for customers are to become loyalty card members, check their loyalty card balance, and help them fully understand the benefits of the loyalty program. Our goal is to create a pilot that we can iterate and improve over time. 

Key Features of RewardBot:

- **Membership Enrollment:** Guide users through the process of becoming loyalty card members. 

- **Balance Inquiry:** Allow users to check their loyalty card balance in real-time. 

- **FAQs and Support:** Provide answers to common questions and support for loyalty program issues.

_Membership Enrollment feature will be launched in next version._

Now that we’ve set the stage, it’s time to dive deeper into the technical details of our Generative AI Assistant. First, let's look at few important concepts-

**Retrieval-Augmented Generation (RAG)**

Imagine you're asking a large language model a question. Generally, it would just give you an answer based on what it's learned from its training data. However, it won't know anything about your customer data, or about your business policies around loyalty reward programs. That's where Retrieval-Augmented Generation (RAG) comes in. It is a technique to leverage your enterprise-specific data to enhance the responses of large language models (LLMs) <u>without retraining a model</u>.

**Knowledge Bases for Amazon Bedrock**

Amazon Bedrock Knowledge Bases are centralized repositories for structured and unstructured data, allowing AI models to access up-to-date information. They enhance the accuracy of AI responses without needing frequent retraining.

In a retail company's Loyalty Reward System, an FAQ document stored in Amazon S3 can be part of the knowledge base. When a customer asks the AI assistant a policy question, it retrieves the relevant information from this document to provide an accurate answer.

**Agents for Amazon Bedrock**

Agents for Amazon Bedrock plan and execute multistep tasks and help orchestrate interactions between foundation models, knowledge bases, and Lambda functions to securely execute APIs.   An agent analyzes the user request and automatically calls the necessary APIs and data sources to fulfill the request. Thus, agents reduce significant development efforts for developers and speed up generative AI application deployments.

**Repository Contains these files -**

1. OpenAPI specification (gm-lrs-openapi-specs.yaml)
2. Loyalty Program FAQ (Loyalty_Program_FAQ.docx)
3. Lambda Functions (call-agent.py & business-function.py)
4. DynamoDB table CLI commands (DynamoDB-Tables.txt)
