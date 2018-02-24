const io = require("socket.io")()

io.on("connection",function(socket){
    var socketid = socket.id;
    socket.on("stream", function(buf){
        console.log("Streaming..");
        io.sockets.emit("stream", buf);
    });
})

io.listen(2000);