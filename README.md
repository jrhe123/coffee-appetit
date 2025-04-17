# coffee-appetit
LLMs + Python + RunPod + Hugging Face + React Native

### Prerequisite

0. Models
    - e.g., LLM, Embedding, Recommendation Model

1. RunPod
    - Deploy AI models & Embedding model
    - https://www.runpod.io/
    - Add credit to your account
        - https://www.runpod.io/console/user/billing
    - Add your API key
        - https://www.runpod.io/console/user/settings
        - read only

2. LLM
    - Llama 3 / 8B
        - https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
        - https://huggingface.co/meta-llama
    - Request the model access, fill up with your personal information
    - Generate Hugging Face API Token
    - Go back to RunPod, click "serverless" -> "Serverless vLLM" configure
        - https://www.runpod.io/console/serverless
        - HuggingFace Model:
            https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
        - HuggingFace Token:
            <your hugging face token>
        - Keep the settings as default
        - Worker Configuration: 48GB GPU
        - Max Worker: 2
        - Deploy
    - Get the endpoint URL
        - OPENAI_BASE_URL: https://api.runpod.ai/v2/vllm-0k6mmyup3gpvws/openai/v1
        - RUNSYNC: https://api.runpod.ai/v2/vllm-0k6mmyup3gpvws/runsync

3. 
    