# Answer Generator
[![Cortex](https://img.shields.io/badge/Engine-Cortex-F7B955)](https://www.cortex.dev/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-79FFE1)](https://pytorch.org)
![NLP](https://img.shields.io/badge/Type-NLP-79FFE1)
![Input](https://img.shields.io/badge/Input-JSON%20(string)-79FFE1)
![Output](https://img.shields.io/badge/Output-JSON%20(string)-79FFE1)

The model based on GPT-2 algorithm which answers any question. The model was built on top of [Cortex](https://www.cortex.dev/) engine using [PyTorch](https://pytorch.org) framework.


## Deploy 
Deploy a model using [Syndicai](https://syndic.ai).

[![Syndicai-Deploy](https://laskowskidesign.com/sai/syndicai-deploy-button.svg)]()




## Run Locally
Execute following commands in order to run a model locally. For more details please visit [Cortex Documentation](https://docs.cortex.dev/install).
```bash
# Install cortex
bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/0.19/get-cli.sh)"

# Deploy a model
cortex deploy

# Run model
curl http://localhost:8892 -X POST -H "Content-Type: application/json" -d @sample_data/sample_input.json
```

