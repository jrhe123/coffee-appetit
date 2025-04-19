import axios from 'axios';
import { MessageInterface } from '@/types/types';
import { API_KEY, API_URL } from '@/config/serverConfigs';

async function callChatBotAPI(messages: MessageInterface[]): Promise<MessageInterface> {
    try {
        // const response = await axios.post(`${API_URL}/run`, {
        const response = await axios.post(`http://127.0.0.1:8000/run`, {
            "messages": messages
        }, {
            headers: {
                'Content-Type': 'application/json',
                // 'Authorization': `Bearer ${API_KEY}`
            }
        });
                
        let output = response.data;
        let outputMessage: MessageInterface = output;

        return outputMessage;
    } catch (error) {
        console.error('Error calling the API:', error);
        throw error;
    }
}

export { callChatBotAPI };