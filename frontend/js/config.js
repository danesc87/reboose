/*
Author: Daniel Córdova A.
*/
/**
 * This file has some configurations to make it easier the development of the frontend
 */

 //
 const httpProtocol = 'http://'

// MicroServices configs
const bookMicroServiceConfig = {
    ipAddress: '127.0.0.1',
    port: '2050'
};

const seriesMicroServiceConfig = {
    ipAddress: '127.0.0.1',
    port: '2051'
};

const paths = {
    bookPath: 'book',
    seriesPath: 'series',
    typePath: 'type',
    genrePath: 'genre',
    authorPath: 'author'
};

// Series Id's
var seriesIds = {
    seriesTypeId: '#series-settings',
    newSerieTypeId: 'new-type',
    newSerieGenreId: 'new-genre'
};
