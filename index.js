const Discord = require("discord.js");
const client = new Discord.Client();

const config = require('./auth.json');
const language = require("@google-cloud/language")
const googleclient = new language.LanguageServiceClient();

const wordList = require("./bannedWords.json")

const threshold = 0.4

async function getSentiment(text) 
{

  var document = {
      content: text,
      type: 'PLAIN_TEXT'
  }

  var [result] = await googleclient.analyzeEntitySentiment({document});
  var entities = result.entities;

  console.log(`Entities and sentiments:`);

  badwords = []
  entities.forEach(entity => {
    if (wordList['bad'].includes(entity.name) && entity.sentiment.score >= threshold )
    { 
      console.log(`  Name: ${entity.name}`);
      console.log(`  Score: ${entity.sentiment.score}`);
      console.log(`  Magnitude: ${entity.sentiment.magnitude}`);
      badwords.push(entity)
    }
  });

  return badwords;
}

client.login(config.token);

client.on('message', async function (message) {
  var badwords = await getSentiment(message.content)
  if (badwords.length > 0) 
  {
    message.react('👎')
  }
})

client.on('ready', () => {
  console.log('The ear hears all...');
});