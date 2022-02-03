const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http, {
    cors: {
      origin: "*",
      methods: ["GET", "POST"]
    }
  });
const documents = {};

io.on('connection', socket => {    
    let previousId;
    const safeJoin = currentId => {
        socket.leave(previousId);
        socket.join(currentId, () => 
        console.log(`Socket ${socket.id} joined room ${currentId}`));
        previousId = currentId;
    }

    socket.on('getDoc', docId => {
        safeJoin(docId);
        socket.emit('document', documents[docId]);
    });

    socket.on('addDoc', doc => {
        var count = 0;
        for (var key of Object.keys(documents)) {
            if(key.includes(doc.id,0)){
                count++;
            }            
        }
        if(count != 0){
            doc.id += count
        }
        documents[doc.id] = doc;
        safeJoin(doc.id);
        io.emit('documents', Object.keys(documents));
        socket.emit('document', doc);        
    });

    socket.on('editDoc', doc => {
        documents[doc.id] = doc;
        socket.to(doc.id).emit('document', doc);
        
    });

    socket.on('deleteDoc', docId => {
        
        delete documents[docId];
        safeJoin(docId);
        io.emit('documents', Object.keys(documents));
             
    });

    io.emit('documents', Object.keys(documents));
    console.log(`Socket ${socket.id} has connected`);
});

http.listen(4444, () => {
    console.log('Listening on port 4444');
});

