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

3. Embedding Model
    - BAA/bge-small-env-v1.5
        - https://huggingface.co/BAAI/bge-small-en-v1.5
    - Go to RunPod, click "Infinity Vector Embeddings"
    - Keep the settings as default
    - Worker Configuration: 24GB GPU PRO
    - Max Worker: 1

4. Recommendation Model
    - "what goes well with which order"
    - https://www.kaggle.com/datasets/ylchang/coffee-shop-sample-data-1113
    - pip install mlxtend
        - apriori recommendation model

6. Firebase
    - account: <your account>@gmail.com
    - new project: coffee-appetit
        - project settings:
            - service account:
                - select language `python`
                - generate new private key
            - setup react native app:
                - add firebase to your `web app`
                - register your app
        - database: Realtime Database
            - test mode: on
        - storage: Firebase Storage
            - test mode: on

7. Pinecone
    - create an index
    - create api key

8. React Native
    - Setup project
        - node version: 22.14.0
        - npx create-expo-app@latest
        - npx expo start --tunnel
        - npm run reset-project
        - npx expo start --clear

    - Debug
        - React Native Orbit
        - Expo GO 51
        - Command + D
        - Command + Shift + K (screenshot)

    - NativeWind CSS
        - https://www.nativewind.dev/getting-started/installation

9. Release APP
    - Developer Account $99
        - https://developer.apple.com
    - EAS
        - npm install -g eas-cli
        - eas login
        - eas build:configure
            - `eas.json` generated
        - eas build -p ios --profile production
            - download the ipa file
    - Upload to App Store
        - Transporter App
        - upload the ipa file
    - App Store Connect
        - https://appstoreconnect.apple.com

