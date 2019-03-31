/*
Author: Daniel Córdova A.
*/

/**
 * This file has requests for series settings includes SeriesTypes and SeriesGenres
 */

const seriesFullPath = httpProtocol.concat('/')
  .concat(seriesMicroServiceConfig.ipAddress)
  .concat(':')
  .concat(seriesMicroServiceConfig.port)
  .concat('/')
  .concat(paths.seriesPath);

const seriesTypePath = seriesFullPath
  .concat('/')
  .concat(paths.typePath);

const seriesGenrePath = seriesFullPath
  .concat('/')
  .concat(paths.genrePath);

var serieTypes = new Vue({
  el: seriesIds.seriesTypeId,
  data: {
    types: [],
    genres: []
  },
  methods: {
    getSeriesTypes: function() {
      axios.get(seriesTypePath)
        .then(response => {this.types = response.data})
        .catch(error => console.log(error))
    },
    postSeriesTypes: function(e){
      var newType = document.getElementById(seriesIds.newSerieTypeId);
      var inputJson = {
        type_name: newType.value
      }
      axios.post(seriesTypePath, inputJson)
    },
    getSeriesGenres: function() {
      axios.get(seriesGenrePath)
        .then(response => {this.genres = response.data})
        .catch(error => console.log(error))
    },
    postSeriesGenres: function(e){
      var newType = document.getElementById(seriesIds.selectedSerieTypeId);
      var newGenre = document.getElementById(seriesIds.newSerieGenreId);
      var inputJson = {
        type_name: newType.value,
        genre: newGenre.value
      }
      axios.post(seriesGenrePath, inputJson)
    }
  }
});

serieTypes.getSeriesTypes();
serieTypes.getSeriesGenres();