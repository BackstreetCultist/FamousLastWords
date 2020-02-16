
async function main()
{
const language = require("@google-cloud/language")

const client = new language.LanguageServiceClient();

var text = process.argv[2]

const document = {
    content: text,
    type: 'PLAIN_TEXT'
}

const [result] = await client.analyzeEntitySentiment({document});
const entities = result.entities;

console.log(`Entities and sentiments:`);
entities.forEach(entity => {
  console.log(`  Name: ${entity.name}`);
  console.log(`  Type: ${entity.type}`);
  console.log(`  Score: ${entity.sentiment.score}`);
  console.log(`  Magnitude: ${entity.sentiment.magnitude}`);
});
}

main().catch(console.error)