const path = require('path');

module.exports = {
    mode: 'development',
    entry: './dev/tsx/index.tsx',
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
        ],
    },

    watchOptions: {
        poll: 1000, // Check for changes every second
        followSymlinks: true,
    },

    resolve: {
        extensions: ['.js', '.ts', '.tsx'],
        // extensions: ['.tsx', '.ts', '.js', '.jsx'],
        // extensions: ['.scss', '.css', '.sass'],
    },

    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, 'static', 'js'),
    },
};