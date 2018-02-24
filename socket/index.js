const io = require("socket.io")()

const events = [
    "stream",
    "unlock",
    "neutral",
    "invalid"
]

io.on("connection",function(socket){
    var socketid = socket.id;
    console.log(`Connected : ${socketid}`);

    events.forEach(function(event, i){
        socket.on(event, function(ret){
            console.log(`Event ${event} triggered`);
            io.sockets.emit(event, ret);
        });
    });

    socket.on("disconnect", function(){
        console.log(`Disconnect : ${socketid}`);
    });
})

io.listen(2000);
console.log("Start..");