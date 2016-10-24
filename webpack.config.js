var BundleTracker = require('webpack-bundle-tracker'),
    ExtractTextPlugin = require("extract-text-webpack-plugin"),
    path = require('path'),
    webpack = require('webpack');

module.exports = {
    context: __dirname,
    entry: {
        main: [
            'webpack-dev-server/client?http://localhost:4000',
            'webpack/hot/only-dev-server',
            "./static/js/index.js"
        ]
    },
    output: {
        path: path.resolve('./static/bundles/'),
        publicPath: 'http://localhost:4000/static/bundles/',
        filename: "[name]-[hash].js"
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(), // don't reload if there is an error
        new ExtractTextPlugin('[name]-[contenthash].css'),
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    devServer: {
        hot: true
    },
    module: {
        loaders: [
            {
                loader: 'url?limit=100000',
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
        ]
    },
    amd: {
        jQuery: true
    },
    resolve: {
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js', '.jsx']
    }
};