const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    hot: true,
  client: {
    webSocketURL: 'wss://10.0.3.108:4000/ws', // Use wss:// instead of ws://
  },
  },
});

