# Swinburne Online FAQ Chatbot

This project encompasses the creation of an intelligent FAQ chatbot designed to enhance the online experience for Swinburne University's staff and students. The chatbot aims to provide quick, accurate responses to user inquiries, surpassing the traditional FAQ system's capabilities. Developed using advanced natural language processing (NLP) technologies, including GPT-2 and DistilBERT, it ensures efficient and relevant information delivery.

By leveraging a React-based frontend and a Flask backend, the project achieves a balance between technological sophistication and user-friendly interaction. This report documents the development process, the challenges faced, and the outcomes achieved, reflecting a significant stride toward integrating AI into student services.

## Features

- **Intelligent Query Handling:** Uses a combination of GPT-2 and DistilBERT models for understanding and generating responses.
- **User-Friendly Design:** React and Ant Design libraries provide a responsive and intuitive user interface.
- **Local Server Hosting:** Flask backend allows for robust API endpoint creation and maintenance on a local server setup.
- **Performance and Cost Efficiency:** A carefully selected hardware setup supports the chatbot infrastructure without compromising on performance.

## Motivation

The motivation behind the Swinburne Online FAQ Chatbot project was to streamline the process of information retrieval on the Swinburne Online portal. Recognizing the inefficiency of sifting through lengthy FAQ sections and the limited availability of live chat agents, the chatbot serves as a 24/7 support system to address these challenges, thereby enhancing the overall learning experience.

## Prerequisites

Before running this project, you will need to install the following:

- Python 3
- Node.js

Make sure you have a web browser to view the application.

## Installation

Clone the project repository:

```bash
git clone https://github.com/Shashank7016/swinburne-faq-ai.git
cd swinburne-faq-ai
```

Set up a virtual environment:

```bash
# Linux or macOS
python3 -m venv venv
source venv/bin/activate

# Windows
py -m venv venv
.env\Scriptsctivate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, follow these steps:

Start the backend server:

```bash
# Make sure you are in the project directory and the virtual environment is activated
python faq_server.py
```

Start the frontend in development mode:

```bash
# Open a new terminal and make sure you are in the project directory
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Contributing

We welcome contributions to this project! If you would like to contribute, please follow these steps:

1. Fork the repository and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code lints.
5. Issue that pull request!

Before submitting a pull request, please check the following:

- Any new code or change must be properly commented and documented.
- If you have any new feature proposal or a bug fix, open an issue first, so we discuss it.
- Make sure to push your changes to a separate branch, not directly to `master`.

We will review all pull requests and provide feedback where necessary. If everything is okay, we will merge your changes into the master branch. Please note that not all requests will be approved, and feedback may be given to further improve the contribution.

## License

This project is released under the MIT License. See the `LICENSE` file for more details.

## Contact

Your Name - bryanhovak@gmail.com

Project Link: [https://github.com/Shashank7016/swinburne-faq-ai](https://github.com/Shashank7016/swinburne-faq-ai)

## Customizing FAQ Content

To personalize the FAQ content for your use case, you can modify the questions and answers by following these steps:

- Replace the contents of `Questions.docx` and `Answers.docx` with your own Q&A pairs.
- If you have existing `.docx` files with questions and answers, place them in the same directory as `faq_server.py`.
- Update the file names in the `faq_server.py` code to match your new `.docx` files. Change the lines where `questions_content` and `answers_content` are set to read from your files instead of the default ones.

For example, if your questions file is named `CustomQuestions.docx`, update the `faq_server.py` like so:

```python
questions_content = read_docx("CustomQuestions.docx")
```

And if your answers file is named `CustomAnswers.docx`, do the same for the answers:

```python
answers_content = read_docx("CustomAnswers.docx")
```

Remember to keep the format of your `.docx` files consistent with the original ones for the code to process them correctly.
