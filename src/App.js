import React, { useState } from 'react';
import './App.css';
import axios from 'axios';
import logo from './swin.png';
import './App.css';
import { Button, Input, Layout, Typography, Space, Image } from 'antd';

const { Header, Content } = Layout;
const { Title } = Typography;
function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:5000/get-answer", {
        question: question
      });
      setAnswer(response.data.response);
    } catch (error) {
      console.error("Error fetching answer:", error);
      setAnswer("There was an error processing your request.");
    }
  };

  return (
    <Layout>
    <Header style={{ backgroundColor: '#333' }}>
        <Space>
            <Image src="./swin.png" width={50} />
            <Title style={{ color: 'white' }} level={2}>Swinburne FAQ</Title>
        </Space>
    </Header>
    <Content style={{ padding: '50px', textAlign: 'center' }}>
        <Space direction="vertical" size="large">
            <Title>Ask a question</Title>
            <Input 
                size="large"
                placeholder="Enter your question here" 
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                onPressEnter={handleSubmit}  // This allows the "Enter" key to submit the question
            />
            <Button type="primary" onClick={handleSubmit}>Submit</Button>
            <div>
                {answer && (
                    <p>{answer}</p>
                )}
            </div>
        </Space>
    </Content>
</Layout>
);
}

export default App;