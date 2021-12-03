module.exports = {
  transpileDependencies: ["color"],
  devServer: {
    proxy: {
      "/api": {
        target: "https://kazan-cam.herokuapp.com/",
        changeOrigin: true,
        ws: true,
        logLevel: "debug",
      },
    },
  },
};
