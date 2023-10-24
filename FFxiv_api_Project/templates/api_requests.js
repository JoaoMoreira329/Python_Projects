// api_request.js
const axios = require('axios');

const options = {
    method: 'GET',
    url: 'https://ffxiv-misc-data.p.rapidapi.com/ffxiv/job-v1',
    params: { per_page: '9' },
    headers: {
        'X-RapidAPI-Key': 'f5f15a1377mshe39ae238d398908p16141ejsn917d42e8db7e',
        'X-RapidAPI-Host': 'ffxiv-misc-data.p.rapidapi.com'
    }
};

try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
// Rest of your JavaScript code