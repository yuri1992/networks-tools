var BundleTracker = require('webpack-bundle-tracker'),
    config = require('./webpack.config.js'),
    ExtractTextPlugin = require('extract-text-webpack-plugin'),
    path = require('path'),
    webpack = require('webpack');

config.cache = false;
config.debug = false;
config.devtool = '';

config.entry = {
    main: "./static/js/index.js",
};

config.module.loaders = [
    {
        loader: 'url?limit=8192',
        test: /\.(gif|jpg|png|woff|woff2|eot|ttf|svg)$/
    },
    {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract('style-loader', 'css!autoprefixer?browsers=last 2 version!less')
    },
    {
        test: /\.less$/,
        loader: ExtractTextPlugin.extract('style-loader', 'css!autoprefixer?browsers=last 2 version!less')
    }
];

config.output.path = path.resolve('./static/dist');
config.output.publicPath = '/static/dist/';

config.plugins = [
    new BundleTracker({filename: './webpack-stats-prod.json'}),
    new webpack.DefinePlugin({
        'process.env': {
            'NODE_ENV': JSON.stringify('production'),
            IS_BROWSER: true
        }
    }),
    new webpack.optimize.DedupePlugin(),
    new ExtractTextPlugin('[name]-[contenthash].css'),
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({
        compressor: {
            drop_console: true,
            screw_ie8: true,
            warnings: false
        }
    })
];

module.exports = config;