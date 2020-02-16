const Discord = require("discord.js");
const client = new Discord.Client();

const config = require('./auth.json');

client.login(config.token);


client.on('message', (message) => {
})

client.on('ready', () => {
  console.log('The ear hears all...');
});