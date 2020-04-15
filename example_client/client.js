const io = require('socket.io-client');
const socket = io('https://lyricsgenerator.didithilmy.com');

const seedText = "Hello world this is me";
const numGen = 100;
const replyId = "predict:a";

socket.emit('predict', seedText, numGen, replyId);
socket.on(replyId, (data) => {
    console.log(data);
});