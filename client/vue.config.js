module.exports = {
  transpileDependencies: ["color"],
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:9000",
        changeOrigin: true,
        ws: true,
        logLevel: "debug",
      },
    },
  },
};
