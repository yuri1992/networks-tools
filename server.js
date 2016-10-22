var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack.config');

new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    historyApiFallback: true,
    quiet: false,
    stats: {
        assets: true,
        colors: true,
        version: false,
        hash: false,
        timings: true,
        chunks: false,
        chunkModules: false
    }
}).listen(3007, '0.0.0.0', function (err, result) {
    if (err) {
        console.log(err);
    }
    console.log('Listening at 0.0.0.0:3007');
});
