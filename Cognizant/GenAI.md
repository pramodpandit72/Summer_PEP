# 🤖 Generative AI (GenAI) Interview Notes for Cognizant 2026

> **Target:** Cognizant GenC / GenC Next (2026)
>
> These are the most expected GenAI questions for service-based company interviews.

---

# 1. What is Artificial Intelligence (AI)?

Artificial Intelligence (AI) is the ability of a machine to perform tasks that normally require human intelligence.

Examples:
- Voice Assistant
- Self Driving Car
- Recommendation System
- Face Recognition

---

# 2. What is Machine Learning (ML)?

Machine Learning is a subset of AI where computers learn patterns from data without being explicitly programmed.

Example

```
Data → Training → Model → Prediction
```

Examples

- Spam Detection
- House Price Prediction
- Disease Prediction

---

# 3. What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses Artificial Neural Networks with multiple hidden layers.

Examples

- Face Recognition
- Speech Recognition
- ChatGPT
- Image Generation

---

# AI vs ML vs DL

| AI | ML | DL |
|----|----|----|
| Broad field | Subset of AI | Subset of ML |
| Rule + Learning | Learns from data | Neural Networks |
| Smart Systems | Prediction | Complex Tasks |

---

# 4. What is Generative AI? ⭐⭐⭐⭐⭐

Generative AI is a type of AI that creates new content instead of only analyzing existing data.

It can generate

- Text
- Images
- Videos
- Audio
- Code

Examples

- ChatGPT
- GitHub Copilot
- Google Gemini
- Claude
- Midjourney
- DALL·E

---

# 5. Examples of Generative AI

Text

- ChatGPT
- Gemini
- Claude

Image

- DALL·E
- Midjourney
- Stable Diffusion

Code

- GitHub Copilot
- Amazon CodeWhisperer

Video

- Sora
- Runway

---

# 6. What is an LLM?

LLM = Large Language Model

An LLM is a deep learning model trained on massive amounts of text to understand and generate human language.

Examples

- GPT
- Llama
- Gemini
- Claude

---

# 7. What is a Prompt?

A prompt is the instruction or input given to an AI model.

Example

```
Write a C++ program to reverse a linked list.
```

---

# 8. Prompt Engineering ⭐⭐⭐⭐⭐

Prompt Engineering is the process of writing clear and effective prompts to obtain better AI responses.

Good Prompt

```
Write a C++ program to implement Binary Search.
Explain the time complexity.
```

Bad Prompt

```
Binary Search
```

---

# 9. Prompt Engineering Best Practices

- Be specific
- Give context
- Mention output format
- Mention programming language
- Ask step by step if needed

Example

```
Explain Binary Search in simple words.
Give C++ code.
Explain Time Complexity.
```

---

# 10. Hallucination ⭐⭐⭐⭐⭐

Hallucination occurs when an AI model generates incorrect or fabricated information that sounds convincing.

Example

AI invents a function or cites a fake source.

---

# 11. Token

A token is the basic unit of text processed by an LLM.

Example

```
Hello World
```

may be split into multiple tokens depending on the tokenizer.

---

# 12. Temperature

Temperature controls randomness in AI responses.

- Low Temperature → More accurate and consistent
- High Temperature → More creative and varied

---

# 13. Context Window

The context window is the maximum amount of text an LLM can consider at one time.

Larger context windows help the model remember more of the conversation or document.

---

# 14. Fine-Tuning

Fine-tuning is training a pre-trained model further on domain-specific data to specialize it for a task.

Example

Training an existing LLM on medical documents.

---

# 15. RAG (Retrieval-Augmented Generation) ⭐⭐⭐⭐⭐

RAG combines an LLM with external knowledge retrieval.

Flow

```
Question
      ↓
Retrieve Documents
      ↓
LLM
      ↓
Answer
```

Advantages

- More accurate
- Uses latest information
- Reduces hallucination

---

# 16. Embeddings

Embeddings convert text into numerical vectors that capture semantic meaning.

Used for

- Semantic Search
- Recommendations
- Chatbots

---

# 17. Vector Database

Stores embeddings instead of plain text.

Popular Databases

- Pinecone
- Chroma
- FAISS
- Weaviate
- Milvus

---

# 18. Transformer

Transformer is the deep learning architecture behind modern LLMs.

Advantages

- Faster Training
- Better Context Understanding
- Parallel Processing

---

# 19. Attention Mechanism

Attention helps the model focus on the most relevant words in a sentence.

Example

```
The cat sat on the mat because it was tired.
```

The model learns that "it" refers to "cat."

---

# 20. Chatbot

A chatbot is software that interacts with users using natural language.

Examples

- Customer Support
- Banking Assistant
- Shopping Assistant

---

# 21. AI Agent

An AI Agent can

- Plan
- Reason
- Use tools
- Take actions
- Complete tasks automatically

Example

An AI assistant that reads emails, schedules meetings, and sends replies.

---

# 22. NLP (Natural Language Processing)

NLP enables computers to understand, interpret, and generate human language.

Applications

- Translation
- Chatbots
- Sentiment Analysis
- Speech Recognition

---

# 23. Computer Vision

Allows computers to understand images and videos.

Applications

- Face Detection
- OCR
- Self-driving Cars

---

# 24. Responsible AI

Responsible AI means developing AI systems that are

- Fair
- Transparent
- Safe
- Secure
- Accountable
- Respectful of Privacy

---

# 25. AI Ethics

Important principles

- Fairness
- Privacy
- Transparency
- Accountability
- Bias Reduction

---

# 26. Limitations of GenAI

- Hallucinations
- Bias
- Outdated knowledge
- Privacy concerns
- Copyright issues
- Requires human verification

---

# 27. Applications of GenAI

- Coding Assistant
- Content Writing
- Customer Support
- Education
- Healthcare
- Finance
- Marketing
- Image Generation
- Software Testing

---

# 28. GenAI in Software Development

- Generate Code
- Debug Code
- Explain Code
- Generate Unit Tests
- Create Documentation
- Code Refactoring

---

# 29. Difference Between AI, ML, DL, and GenAI

| AI | ML | DL | GenAI |
|----|----|----|--------|
| Intelligent systems | Learns from data | Neural Networks | Generates new content |

---

# 30. Popular GenAI Tools

- ChatGPT
- GitHub Copilot
- Google Gemini
- Claude
- Microsoft Copilot
- Perplexity AI
- DALL·E
- Midjourney

---

# Most Expected Interview Questions ⭐⭐⭐⭐⭐

### Q1. What is Generative AI?

Generative AI is a type of AI that creates new content such as text, images, code, audio, or videos based on patterns learned from data.

---

### Q2. Difference between AI, ML, Deep Learning, and Generative AI?

- AI: Broad field of intelligent systems.
- ML: AI systems that learn from data.
- DL: ML using deep neural networks.
- GenAI: AI that creates new content.

---

### Q3. What is an LLM?

A Large Language Model is an AI model trained on massive text data to understand and generate human language.

---

### Q4. What is Prompt Engineering?

Prompt Engineering is the practice of designing clear and specific prompts to get better responses from AI models.

---

### Q5. What is Hallucination?

Hallucination is when an AI model generates incorrect or fabricated information while presenting it as factual.

---

### Q6. What is RAG?

Retrieval-Augmented Generation combines information retrieval with an LLM so answers are grounded in external documents, improving accuracy and reducing hallucinations.

---

### Q7. What are Embeddings?

Embeddings are numerical vector representations of data that preserve semantic meaning.

---

### Q8. What is Fine-Tuning?

Fine-tuning is additional training of a pre-trained model on domain-specific data to improve performance for a particular task.

---

### Q9. Name some applications of GenAI.

- Chatbots
- Code Generation
- Content Writing
- Image Generation
- Translation
- Customer Support

---

### Q10. Why should developers learn GenAI?

Because it improves productivity by assisting with coding, debugging, testing, documentation, and problem-solving, while also enabling the development of intelligent AI-powered applications.

---

# ⭐ Most Important Topics for Cognizant

- AI vs ML vs DL vs GenAI
- What is Generative AI?
- Large Language Models (LLMs)
- Prompt Engineering
- Hallucination
- Tokens
- Context Window
- Temperature
- Embeddings
- Vector Database
- Transformer
- Attention Mechanism
- RAG
- Fine-Tuning
- Responsible AI
- AI Ethics
- GenAI Applications
- AI Agents
- Chatbots
- GitHub Copilot and AI Coding Assistants

---

# 🎯 Tip for Cognizant Interviews

If asked **"Have you used GenAI?"**, answer with a practical example:

> "Yes. I have used ChatGPT and GitHub Copilot to understand DSA concepts, generate boilerplate code, debug C++ programs, explain SQL queries, and speed up full-stack development. I always review and test AI-generated code before using it because AI can sometimes produce incorrect or inefficient solutions."