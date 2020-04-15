const io = require('socket.io-client');
const socket = io('http://lyricsgenerator.didithilmy.com:8080');

const seedText = "Hello world this is me";
const numGen = 10;
const replyId = "predict:a";

socket.emit('predict', seedText, numGen, replyId);
socket.on(replyId, (data) => {
    console.log(data);
});