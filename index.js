const Discord = require("discord.js");
const client = new Discord.Client();

const config = require('./auth.json');
const language = require("@google-cloud/language")
const googleclient = new language.LanguageServiceClient();

async function getSentiment(text) 
{

var document = {
    content: text,
    type: 'PLAIN_TEXT'
}

var [result] = await googleclient.analyzeEntitySentiment({document});
var entities = result.entities;

console.log(`Entities and sentiments:`);

entities.forEach(entity => {
    console.log(`  Name: ${entity.name}`);
    console.log(`  Score: ${entity.sentiment.score}`);
    console.log(`  Magnitude: ${entity.sentiment.magnitude}`);
  });
}

client.login(config.token);

client.on('message', async function (message) {
  await getSentiment(message.content)
})

client.on('ready', () => {
  console.log('The ear hears all...');
});