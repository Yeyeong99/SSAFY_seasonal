const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello SSAFY!');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

const { Configuration, OpenAIApi } = require('openai');

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

app.get('/chat', async (req, res) => {
    const { message } = req.query;
    const response = await openai.createCompletion({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: message }],
    });
    res.send(response.data.choices[0].message.content);
});
