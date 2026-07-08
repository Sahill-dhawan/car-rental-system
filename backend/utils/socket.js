let io;

module.exports = {
  init: (httpServer) => {
    const { Server } = require('socket.io');
    io = new Server(httpServer, {
      cors: {
        origin: process.env.CLIENT_URL || 'http://localhost:3000',
        credentials: true
      }
    });
    
    io.on('connection', (socket) => {
      console.log('🔗 New WebSocket connection:', socket.id);
      
      socket.on('disconnect', () => {
        console.log('🔗 WebSocket disconnected:', socket.id);
      });
    });
    
    return io;
  },
  getIO: () => {
    if (!io) {
      throw new Error('Socket.io not initialized!');
    }
    return io;
  }
};
