from google.colab import userdata

# Replace 'HF_TOKEN' with the name you used for your secret
hf_api_key = userdata.get('HF_TOKEN')

if hf_api_key is not None:
    print("Hugging Face API key loaded successfully!")
else:
    print("Hugging Face API key not found in Colab secrets.")
    print("Please add your HF token to Colab secrets with the name 'HF_TOKEN'.")
