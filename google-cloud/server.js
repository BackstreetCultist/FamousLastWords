async function main()
{
    const speech = require("@google-cloud/speech");
    const fs = require("fs");

    const client = new speech.SpeechClient();
    const filename = "./out.wav";

    const file  = fs.readFileSync(filename);

    const audio = {
        content: file
    };

    const config = {
        languageCode: 'en-UK'
    }

    const request = {
        audio: audio,
        config: config
    }

    const [response] = await client.recognize(request);
    const transcription = response.results
    .map ( result => result.alternatives[0].transcript)
    .join ('\n');

    console.log(`${transcription}`) 

}

main().catch(console.error)