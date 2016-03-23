
(function () {

  'use strict';

  var BeerLister = angular.module('BeerListerApp', [])
    

  BeerLister.controller('BeerListerMainController', ['$scope', function($scope) {
  }]);

  BeerLister.controller('BeerForm', ['$scope', '$log', 'beerApi', function($scope, $log, beerApi) {
    
    var resetScope = function () {
      $scope.abv = 0.0;
      $scope.name = "";
      $scope.rating = 0;
    }
    
    $scope.saveBeer = function () {
      var beer = {
        name: $scope.name,
        rating: $scope.rating,
        abv: formatABV($scope.abv)
      };
      beerApi.add(beer, function(data){
        resetScope();
      })
      return false
    }

    var formatABV = function (num) {
      return Math.round(num*100)
    }


    resetScope();
  }])

  //Services
  BeerLister.factory('apiAccess',['$http', '$log', function($http, $log) {
    var BasicApiAccess = function(model_name) {
      var url = '/api/' + model_name + 's/';
      
      var formatDataObjet = function (model) {
        var data = {};
        data[model_name] = model;
        return data;
      }
      var logError = function(response) {
        $log.log(response.data.error);
      }
      
      this.add = function(model, callback) {
        $http.post(url, formatDataObjet(model)).then(callback, logError)
      }
      this.update = function(model, callback) {
        $http.post(url + model.id, formatDataObjet(model)).then(callback, logError)
      }
      this.list = function() {
        $http.get(url).then(callback)
      }
      this.remove = function (id) {
        $http.delete(url + id).then(callback)
      }
    }
    return BasicApiAccess
  }])

  BeerLister.factory('beerApi',['apiAccess', function(apiAccess){
    var api = new apiAccess('beer');
    return api;
  }])


}());