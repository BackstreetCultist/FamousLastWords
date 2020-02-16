/* Discord API */
const Discord = require("discord.js");
const config = require('./auth.json');
const client = new Discord.Client();

/* Google API */ 
const language = require("@google-cloud/language")
const googleclient = new language.LanguageServiceClient();
const wordList = require("./bannedWords.json")
const threshold = 0.4

/* Websocket server */
const WebSocket = require("ws");
const wss = new WebSocket.Server({port : process.env.PORT || 8080});

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


client.on('message', async function (message) {
  var badwords = await getSentiment(message.content)
  if (badwords.length > 0)
  {
    message.react('👎')
    // message doesn't matter
    if (socket) {socket.send('now');}
  }
})

client.on('ready', () => {
  console.log('The ear hears all...');
});



var socket = null;
wss.on('connection', (ws)=>{
  console.log("pi connected");
  socket = ws; 
}); 

wss.on('close', (ws) => {
  console.log("pi disconnected");
  socket=null
});

client.login(config.token);