# Blog Generation 
[Introducing Llama 2](https://ai.meta.com/llama/)
- Used llama2 model with 7B parameter
- [TheBloke/Llama-2-7B-Chat-GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main) version llama-2-7b-chat.ggmlv3.q8_0.bin
- Used stremlit python package to create UI

### Steps for running code
- Download llama-2-7b-chat.ggmlv3.q8_0.bin model and copy into /model folder
- Create virtual env
  - *conda create --name myenv python=3.x*
  - *conda activate myenv*
- Install requirements file with *pip install -r requirements.txt*
- In Terminal run *streamlit run .\app.py*