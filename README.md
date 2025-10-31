# LexBot 🤖⚖️

A legal-focused AI chatbot powered by Meta's LLaMA 2 model, designed to provide legal suggestions and assistance through an intuitive web interface. LexBot runs completely locally without external API dependencies, ensuring privacy and data security.

## 📋 Overview

LexBot is an intelligent legal assistant that leverages the power of large language models to help users understand legal concepts, get preliminary legal guidance, and navigate common legal questions. Built with LLaMA 2, it provides reliable and contextually aware responses while maintaining complete local deployment.

## ✨ Features

- **Local Deployment**: Runs entirely on your local machine without requiring external API calls
- **LLaMA 2 Integration**: Powered by Meta's open-source LLaMA 2 model for high-quality responses
- **Legal Domain Focus**: Specialized for legal queries, suggestions, and guidance
- **User-Friendly Web Interface**: Clean and intuitive webpage for easy interaction
- **Privacy-First**: All data processing happens locally, ensuring user privacy
- **No API Dependencies**: Fully self-contained system requiring no external services

## 🚀 Getting Started

### Prerequisites

Before running LexBot, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Sufficient RAM (minimum 8GB recommended for 7B model)
- Storage space for the LLaMA 2 model files

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aditya24112002/LexBot.git
   cd LexBot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download LLaMA 2 Model**
   
   Follow Meta's official guide to download the LLaMA 2 model weights:
   - Visit [Meta's LLaMA download page](https://www.llama.com/llama-downloads/)
   - Request access and download the model files
   - Place the model files in the appropriate directory (as specified in configuration)

4. **Configure the Application**
   
   Update the configuration file with the path to your LLaMA 2 model:
   ```python
   MODEL_PATH = "/path/to/your/llama2/model"
   ```

### Running LexBot

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Start Chatting**
   
   Type your legal questions in the chat interface and receive AI-powered responses!

## 🛠️ Technology Stack

- **LLaMA 2**: Meta's open-source large language model
- **Python**: Core programming language
- **Flask/FastAPI**: Web framework (backend)
- **HTML/CSS/JavaScript**: Frontend interface
- **PyTorch**: Deep learning framework
- **Transformers**: Hugging Face library for model inference

## 💡 Use Cases

LexBot can assist with:

- Understanding legal terminology and concepts
- Getting preliminary guidance on common legal issues
- Exploring legal rights and obligations
- Learning about legal procedures and documentation
- General legal information and education

**⚠️ Disclaimer**: LexBot is an AI assistant designed for informational and educational purposes only. It does not replace professional legal advice from qualified attorneys. Always consult with a licensed legal professional for specific legal matters.

## 📁 Project Structure

```
LexBot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── models/               # Model files directory
├── static/              # Static assets (CSS, JS, images)
├── templates/           # HTML templates
├── utils/              # Utility functions
└── README.md           # Project documentation
```

## ⚙️ Configuration

Key configuration parameters can be adjusted in the `config.py` or `app.py` file:

- **Model Path**: Location of LLaMA 2 model files
- **Temperature**: Controls response randomness (0.0 - 1.0)
- **Max Tokens**: Maximum length of generated responses
- **Port**: Server port (default: 5000)

## 🔧 Customization

### Adjusting Model Parameters

Modify response behavior by adjusting these parameters:

```python
temperature = 0.7  # Lower for more focused responses
max_tokens = 512   # Increase for longer responses
top_p = 0.9       # Nucleus sampling parameter
```

### Adding Custom Legal Context

You can enhance LexBot's legal knowledge by:
- Fine-tuning the model on specific legal documents
- Implementing RAG (Retrieval Augmented Generation) for legal databases
- Adding custom prompts for specific legal domains

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues & Troubleshooting

- **High Memory Usage**: LLaMA 2 requires substantial RAM. Consider using the 7B parameter model for machines with limited resources.
- **Slow Response Times**: First-time model loading may take time. Subsequent responses should be faster.
- **GPU Support**: For faster inference, ensure CUDA is properly installed if using GPU acceleration.

## 📝 Future Enhancements

- [ ] Add support for multiple LLaMA 2 model sizes
- [ ] Implement conversation history and context management
- [ ] Add document upload for legal document analysis
- [ ] Integrate vector database for enhanced RAG capabilities
- [ ] Mobile-responsive UI improvements
- [ ] Multi-language support
- [ ] Export chat history functionality

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Meta AI** for releasing LLaMA 2 as an open-source model
- The Hugging Face community for their excellent Transformers library
- Contributors and testers who helped improve LexBot

## 👨‍💻 Author

**Aditya Bhadra**
- GitHub: [@Aditya24112002](https://github.com/Aditya24112002)
- Education: B.Tech in Computer Science and Engineering, JIS College of Engineering

## 📧 Contact

For questions, suggestions, or issues, please:
- Open an issue on GitHub
- Contact via GitHub profile

---

**⭐ If you find LexBot helpful, please consider giving it a star on GitHub!**

**Note**: This is an educational and experimental project. Always verify legal information with qualified professionals before making legal decisions.