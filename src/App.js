
import React, { useState } from 'react';
import './App.css';
import axios from 'axios';
import logo from './swin.png';
import { Button, Input, Layout, Typography, Space, Image, Card, Alert, Spin, Tooltip } from 'antd';

const { Header, Content } = Layout;
const { Title } = Typography;

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  
  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/get-answer", { question: question });
      setAnswer(response.data.response);
    } catch (error) {
      console.error("Error fetching answer:", error);
      setAnswer("There was an error processing your request.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <Header style={{ backgroundColor: '#333' }}>
        <Space>
          <Image src={logo} width={50} />
          <Title style={{ color: 'white' }} level={2}>Swinburne FAQ</Title>
        </Space>
      </Header>
      <Content style={{ padding: '50px', textAlign: 'center', background: "linear-gradient(to right, #ece9e6, #ffffff)" }}>
        <Space direction="vertical" size="large">
        <Title style={{ marginBottom: "50px" }}>Ask a question</Title>
          <Tooltip title="Type your question and hit enter or click submit">
            <Input 
              size="large"
              placeholder="Enter your question here" 
              value={question}
              onChange={(e) => {
                setQuestion(e.target.value);
              }}
              onPressEnter={handleSubmit}
            />
          </Tooltip>
          <Button type="primary" onClick={handleSubmit}>Submit</Button>
          <div>
            {loading ? (
              <Spin><div style={{ height: "50px" }}></div></Spin>
              
            ) : answer ? (
              answer.includes("Sorry") ? (
                <Alert message={answer} type="warning" showIcon />
              ) : (
                <Card title="Answer" bordered={false} style={{ width: 300 }}>
                  <p>{answer}</p>
                </Card>
              )
            ) : null}
          </div>
        </Space>
      </Content>
    </Layout>
  );
}

export default App;
